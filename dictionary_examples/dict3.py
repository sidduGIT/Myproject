# Dictionaries are sometimes as ``associative memories'' or ``associative arrays''

tel = {'jack': 4098, 'sape': 4139}
print tel
tel['guido'] = 4127
print tel

print tel['jack']

del tel['sape']
tel['irv'] = 4127
print tel

print tel.keys()

x=tel.has_key('guido')
print x

# The dict() constructor builds dictionaries directly from lists
# of key-value pairs stored as tuples. When the pairs form a pattern,
# list comprehensions can compactly specify the key-value list.

d=dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print d