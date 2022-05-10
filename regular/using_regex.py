# regex is 'regular expressions' - ways to find stuff within other stuff
# often we may need to parse content looking for patterns
import re # re is the regular expression library built in to Python

source = 'Young Frankenstein Franky is ugly'
# search from start or ^ (caret) to search from start
# .* searches UNTIL it finds all matches
# .*? searches for the FIRST occurance
m = re.match('.*?Frank', source)
# .search will search for a term
m = re.search('Frank', source)
#  .findAll - return a list of all matches
m = re.findall('n.', source) # a list of all matches
print(m)

if m:
    print( m.group() )