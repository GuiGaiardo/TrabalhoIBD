import re

def parse(query):
    parser = re.compile(r'^select\s+(\*|\w+(\s*\,\s*\w+)*)\s+' \
                        'from\s+(\w+|\w+(\s+join\s+\w+)+\s+on\s+\w+\s*={1}\s*\w+)' \
                        '(\s+where\s+\w+\s*(=|<|>|<=|>=|<>){1}\s*\w+)?\s*$',flags=re.IGNORECASE)
    match = parser.match(query)
    if match:
        return 'ok'
    return 'error'
