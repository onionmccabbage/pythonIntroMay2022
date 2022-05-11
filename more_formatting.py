# we can use modern Python formatting
n = 1.2493
s = 'rainy'
w = 'NE'
#                           we can format decimal places
print('It is {0} (yes {0}) at {1:.2f} wind is {2}'.format(s, n, w))

# you may also come across older formatting syntax
print( '%s' % 42 ) # outputs '42' as a string
print( '%d' % 42 ) # output 42 as a decimal value
print( '%x' % 42 ) # output 42 as hex (2a)

# The old way of formatting strings in Python
# %s string
# %d decimal integer
# %x hex integer
# %o octal integer
# %f decimal float
# %e exponential float
# %g decimal or exponential float
##  %% a literal %