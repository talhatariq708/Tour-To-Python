# nested dictionary

a = {
    'name1': {'details': 'Talha', 'class': 'intermediate', 'age': 22},
    'name2': {'details': 'Azmat', 'class': 'masters', 'age': 28},
    'name3': {'details': 'amanat', 'class': 'matric', 'age': 19},
}

print(a)  # this will print the whole a

print("")

print(a['name1']['age'])  # this will only print age
print(a['name2']['class'])  # this will only print class
print(a['name3']['details'])  # this will only print details

print("")

for n1 in a.keys():
    print(n1)  # will print only keys in a

print("")  # will do 1 line gap

for n in a.values():  # will print the whole dictionary
    print(n)

print("")
