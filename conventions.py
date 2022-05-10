# typical conventions found in all programming languages
ALL_CAPS = ('used', 'for', 'constants', 'eg', 'tuples')

lower_snake_case = 'identifiers, functions etc.'
camelCase = 'also for identifiers, functions etc.'

something_d = {'purpose':'indicate a dictionary'}
something_l = ['for', 'lists']
something_t = ('tuple',)

# there are also rules for module names, package names, identifier names, flenames ...
identifier_names = 'must start with a non-digit. Can include digits, alpha, underscore'
# 1thingy = 'nope'
# be careful not to accidentally override built-ins
print = 1 # we now no longer have the original 'print' capabilites

print('oops')

__internal__ = 'careful - dunders tend to belong to python internals'