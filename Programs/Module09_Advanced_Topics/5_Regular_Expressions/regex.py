import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

x = re.search(r"\s", txt)
print(x)
print("The first white-space character is located in position:", x.start())

x = re.split("\s", txt)
print(x)

x = re.split("\s", txt, 1)
print(x)

x = re.sub("\s", "9", txt)
print(x)

x = re.sub("\s", "9", txt, 2)
print(x)

x = re.search(r"\bS\w+", txt)
print(x.span())

x = re.search(r"\bS\w+", txt)
print(x.string)

x = re.search(r"\bS\w+", txt)
print(x.group())
