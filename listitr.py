a = [10, 20, 30, 40, 50]
b = len(a)
for n in range(b):
    print(n)  # will only shows the index number

print("")

a = [10, 20, 30, 40, 50]
b = len(a)
for n in range(b):
    print(a)  # will shows the whole list excluded indexing

print("")

a = [10, 20, 30, 40, 50]
b = len(a)
for n in range(b):
    print(a[n])  # will show the real output of the list

print("")

l_1 = [10, 30, "Hello", "Talha", 29.99]
l_2 = len(l_1)
for l in range(l_2 - 1, -1, -1):
    print(l_1[l])  # will reverse the output
