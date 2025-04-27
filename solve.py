string = "Was it a car or a cat I saw?"
a = "".join(filter(str.isalnum, string))
a = a.lower()
print(a[::] == a[::-1])
print(a)
print(a[::-1])
