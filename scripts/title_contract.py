"""House title and diagram readability guards; meaning still needs reader review."""
import re

MAX_TITLE_CHARACTERS = 96
MAX_TITLE_WORDS = 12
MAX_SUBTITLE_CHARACTERS = 160
MAX_SUBTITLE_WORDS = 24
COMMANDS = {'add', 'build', 'change', 'choose', 'click', 'configure', 'create', 'delete', 'deploy',
            'enable', 'disable', 'fix', 'generate', 'implement', 'install', 'move', 'open', 'close',
            'recover', 'remove', 'review', 'run', 'save', 'select', 'send', 'set', 'submit', 'update',
            'validate', 'verify', 'write', 'rewrite'}
TOPIC_QUALIFIERS = {'access', 'api', 'behavior', 'behaviour', 'command', 'commands', 'configuration',
                    'design', 'errors', 'failures', 'flow', 'format', 'handling', 'history', 'limits',
                    'of', 'operation', 'operations', 'performance', 'policy', 'process', 'request',
                    'requests', 'response', 'responses', 'results', 'rules', 'semantics', 'settings',
                    'status', 'validation', 'verification', 'workflow'}
VIEWS = {'overview': ('Overview', 8, 1), 'detail': ('Technical detail', 32, 3),
         'reference': ('Reference', 64, 3)}


def title_errors(title, task=False):
    if not isinstance(title, str) or not title.strip():
        return ['Use a nonempty title naming the subject.']
    visible = re.sub(r'`[^`]*`', 'Literal', title).strip()
    words = re.findall(r"[\w'-]+", visible)
    errors = []
    if len(title) > MAX_TITLE_CHARACTERS or len(words) > MAX_TITLE_WORDS:
        errors.append('Shorten the title to its subject; move scope and explanation into a subtitle or body.')
    if visible.casefold() in {'diagram', 'draft', 'introduction', 'overview', 'process', 'untitled', 'workflow'}:
        errors.append('Name the actual subject rather than using a generic title.')
    if not task and len(words) > 1 and words[0].casefold() in COMMANDS and words[1].casefold() not in TOPIC_QUALIFIERS:
        errors.append('Use a topic title such as Website review workflow; keep commands in task or step labels.')
    return errors


def subtitle_errors(subtitle):
    if not isinstance(subtitle, str) or not subtitle.strip():
        return ['Use a brief subtitle stating what the view covers.']
    if len(subtitle) > MAX_SUBTITLE_CHARACTERS or len(subtitle.split()) > MAX_SUBTITLE_WORDS:
        return ['Shorten the visible subtitle to the view scope; explain internal steps in the document.']
    return []


def readability_errors(source, context, manifest=None):
    view = context.get('view', 'overview')
    if view not in VIEWS:
        return ['Use an overview, detail or reference view.']
    _, maximum, depth_limit = VIEWS[view]
    errors = []
    if manifest is not None and len(manifest['elements']) > maximum:
        errors.append(f'The {view} view has too many components ({len(manifest["elements"])} > {maximum}); collapse detail or split the view.')
    if context.get('family') == 'sequence':
        depth = maximum_depth = 0
        for line in source.splitlines():
            line = line.strip()
            if re.match(r'(?:alt|opt|loop|par|critical|break|rect)\b', line):
                depth += 1
                maximum_depth = max(maximum_depth, depth)
            elif line == 'end':
                depth = max(0, depth - 1)
        if maximum_depth > depth_limit:
            errors.append(f'The {view} view nests too many alternatives; show the main path and separate the exceptions.')
    return errors
