# functions in dictionary

a = {
    'name': 'Talha Tariq',
    'class': 'intermediate',
    'language': 'python',
    'session number': '28'
}
b = a.get('name')  # this will show the result of key name = Talha Tariq
c = a.keys()  # this will only return keys
print(c)
d = a.values()  # this will shows the result of keys values
print(d)
for e in a.values():  # this will shows the result of statements
    print(e)
