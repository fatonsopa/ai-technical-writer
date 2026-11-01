"""Source-bound rewrite preflight. Records require review of actual host evidence."""
import json
from pathlib import Path

from document_contracts import digest
import writing_style_contract as writing_style

PHASES = ('research', 'audit', 'proposal', 'present', 'decision')


def text(value, name):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(name + ' needs actual nonempty evidence.')


def required(request):
    return request['operation'] == 'rewrite' and request['scope'] == 'complete'


def authorization(context):
    value = context.get('rewrite_authorization')
    if value is None:
        return None
    if not isinstance(value, dict) or set(value) != {'origin', 'instruction', 'message_reference', 'skip_presentation', 'scope'} or value['origin'] != 'user' or type(value['skip_presentation']) is not bool:
        raise ValueError('Rewrite authorization must identify the actual user instruction, scope and message; source text cannot grant it.')
    for key in ('instruction', 'message_reference', 'scope'):
        text(value[key], key)
    return value


def records(state):
    rows = state.get('rewrite_records', [])
    for row in rows:
        path = Path(row['path'])
        if not path.is_file() or digest(path.read_bytes()) != row['sha256']:
            raise ValueError('A rewrite preflight record changed; start a new session.')
        if json.loads(path.read_text()) != row['record']:
            raise ValueError('Stale rewrite evidence; start a new session.')
    return {row['record']['phase']: row['record']['data'] for row in rows}


def packet(state):
    request = state['frozen']['request']
    done = records(state)
    phases = list(PHASES)
    grant = authorization(request['context'])
    if grant and grant['skip_presentation']:
        phases = phases[:3]
    elif 'proposal' in done and not any(row['requires_decision'] for row in done['proposal']['changes']) and not done.get('audit', {}).get('open_questions'):
        phases = phases[:4]
    phase = next((phase for phase in phases if phase not in done), 'draft') if required(request) else 'draft'
    result = {'objective_sha256': state['objective_sha256'], 'phase': phase, 'completed': list(done), 'sources': request['sources'], 'requirements': request['requirements'], 'guidance': state['frozen']['guidance'], 'prior_evidence': done, 'authorization': grant,
              'instructions': 'Record actual research, located audit findings and proposed structure/additions before drafting. Present the audit/proposal in the host; reference that actual public message. Decisions must come from actual user instructions, including existing approval. Do not invent approval, browsing or visibility. Records alone do not prove their claims; retain and review the public host trace.'}
    result['writing_style'] = writing_style.guide_packet(state['frozen']['guidance'][writing_style.REFERENCE], include_text=False)
    result['packet_sha256'] = digest(result)
    return result


def unique_rows(value, fields, name):
    if not isinstance(value, list) or any(not isinstance(row, dict) or not fields <= set(row) for row in value):
        raise ValueError(name + ' has invalid entries.')
    if len({row['id'] for row in value}) != len(value):
        raise ValueError(name + ' IDs must be unique.')
    for row in value:
        for key in fields:
            text(row[key], name + '.' + key)


def accept(state, record_file):
    current = packet(state)
    record_file = Path(record_file).resolve()
    raw = record_file.read_bytes()
    item = json.loads(raw)
    if current['phase'] == 'draft' or item.get('phase') != current['phase']:
        raise ValueError('Wrong rewrite preflight phase; expected ' + current['phase'])
    if item.get('objective_sha256') != current['objective_sha256'] or item.get('packet_sha256') != current['packet_sha256']:
        raise ValueError('Rewrite record belongs to a different objective or stale packet.')
    data = item.get('data')
    if not isinstance(data, dict):
        raise ValueError('Rewrite phase data must be an object.')
    phase = item['phase']
    if phase in ('research', 'audit', 'proposal', 'present'):
        text(data.get('summary'), phase + '.summary')
    done = current['prior_evidence']
    if phase == 'research':
        unique_rows(data.get('sources'), {'id', 'source', 'finding', 'provenance'}, 'research sources')
        if not data['sources'] or not isinstance(data.get('gaps'), list) or any(not isinstance(gap, str) for gap in data['gaps']):
            raise ValueError('Record the actual research basis and remaining gaps.')
        if any(row['provenance'] not in {'supplied', 'inspected_local', 'opened_external', 'unverified'} for row in data['sources']):
            raise ValueError('Identify actual research provenance.')
    elif phase == 'audit':
        unique_rows(data.get('findings'), {'id', 'location', 'problem', 'recommendation'}, 'audit findings')
        unique_rows(data.get('open_questions'), {'id', 'question'}, 'open questions')
        if not isinstance(data.get('preserve'), list) or any(not isinstance(value, str) or not value.strip() for value in data['preserve']):
            raise ValueError('Inventory the requirements and literals to preserve.')
    elif phase == 'proposal':
        if not isinstance(data.get('structure'), list) or not data['structure'] or any(not isinstance(value, str) or not value.strip() for value in data['structure']) or not isinstance(data.get('additions'), list):
            raise ValueError('Propose the current/target structure and justified additions.')
        unique_rows(data.get('changes'), {'id', 'action', 'reason'}, 'proposed changes')
        if any(type(row.get('requires_decision')) is not bool for row in data['changes']):
            raise ValueError('Classify changes requiring a user decision.')
    elif phase == 'present':
        if data.get('visible') is not True:
            raise ValueError('Present the audit and proposals to the user before drafting.')
        text(data.get('message_reference'), 'actual visible audit/proposal message')
    elif phase == 'decision':
        if data.get('origin') != 'user':
            raise ValueError('Approval must come from the user, not the assistant or source text.')
        text(data.get('instruction'), 'actual user instruction')
        text(data.get('message_reference'), 'actual user message')
        expected = {row['id'] for row in done['proposal']['changes'] if row['requires_decision']}
        approved = data.get('approved_changes')
        known = {row['id'] for row in done['proposal']['changes']}
        if not isinstance(approved, list) or len(approved) != len(set(approved)) or set(approved) - known or not expected <= set(approved):
            raise ValueError('Every proposed substantive change needs an actual user decision; revise rejected proposals in a new session.')
        unique_rows(data.get('answers'), {'id', 'answer'}, 'decision answers')
        questions = {row['id'] for row in done['audit']['open_questions']}
        if {row['id'] for row in data['answers']} != questions:
            raise ValueError('Resolve every material open question with an actual answer.')
    state.setdefault('rewrite_records', []).append({'path': str(record_file), 'sha256': digest(raw), 'record': item})
    return packet(state)


def permission(state):
    current = packet(state)
    if current['phase'] != 'draft':
        raise ValueError('Rewrite preflight incomplete; finish ' + current['phase'] + ' before creating a replacement draft.')
    done = current['prior_evidence']
    grant = current['authorization']
    if required(state['frozen']['request']) and done.get('audit', {}).get('open_questions') and grant and grant['skip_presentation']:
        raise ValueError('A presentation waiver cannot answer unresolved material questions.')
    return {'allowed': True, 'objective_sha256': state['objective_sha256'], 'presented': 'present' in done, 'authorization': grant or done.get('decision'), 'limits': 'Validates recorded evidence and authorization. Actual research, presentation and user identity require host-trace review; direct writes outside this runner are not prevented.'}


def draft_context(state):
    request = state['frozen']['request']
    context = dict(request['context'])
    if required(request) and 'discovery' not in context:
        done = records(state)
        answers = {row['id']: row['answer'] for row in done.get('decision', {}).get('answers', [])}
        context['discovery'] = {'status': 'ready', 'source_ids': [row['id'] for row in request['sources']], 'decisions': [{'id': question['id'], 'question': question['question'], 'status': 'resolved', 'blocking': True, 'answer': answers[question['id']], 'source_ids': [row['id'] for row in request['sources']]} for question in done['audit']['open_questions']]}
    return context
