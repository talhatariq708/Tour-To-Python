# We can do:
# "list , multiple listing, finding indexing, reversing elements"

l_1 = [1, 2, 3, 4]
print(l_1[1])  # will output 2
l_2 = [1, 3, 5, ["Hi", 9, 11.45]]
print(l_2[3])  # will output whole 2nd option
l_3 = [11, 20.99, ["Hello", "Talha", 9]]
print(l_3[2][0])  # will output only "Hello"
l_3 = [11, 91.90, "Hello", 0, ["Tariq", "Infinite", 11]]
print(l_3[4][1])  # will output "Infinite"
l_4 = [22, 50, 11, 19.79]
print(l_4[-1::-1])  # will reverse the output
l_5 = ["Hello World", 12, 22, ["Talha", "intermediate", 22]]
print(l_5[-1::-1])  # will also reverse the nested list
l_6 = ["Talha", "Python", [10, 22, 23]]
print(l_6[2][-1::-1])  # will reverse the nested list
