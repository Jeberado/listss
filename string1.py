import keyword
s = input("")
if s[0].isdigit():
    print(False)
elif not s.isidentifier():
    print(False)
elif s in keyword.kwlist:
    print(False)
else:
    print(True)



