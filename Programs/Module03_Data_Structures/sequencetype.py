# String
s = "Hello, World!"
print("String:", s)
print("First character of string:", s[0])
# String methods
print(s.replace("World", "Python"))
print(s)

# List
lst = [1, 2, 3, "Python", 4.5]
print(lst[3]) # Python
print(lst[3][2]) # t
# Positive indexing
print(lst[2]) # 3
print(lst[3]) # Python
# Negative indexing
print(lst[-3]) # 3
print(lst[-2]) # Python
print("List:", lst)
# List Methods
print(len(lst))
lst.append("Java")  # Adding an element at the end
print("Updated List:", lst)
print(len(lst))
lst.insert(2, "C++")
print("Modified List:", lst)
print(len(lst))
lst[0] = 9;
print("Modified List:", lst)
print(len(lst))

# Tuple
tpl = (10, 20, "Tuple", 30.5)
print("Tuple:", tpl)
# tpl[0] = 99  # Error: Tuples are immutable
