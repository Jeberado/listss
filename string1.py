import keyword
checking_str = input("")
def checking_char(s):
    if s[0].isdigit():
        return False
    elif not s.isidentifier():
        return False
    elif s in keyword.kwlist:
        return False
    else:
        return True

if checking_char(checking_str):
        print('True')
else: print('You wrote wrong string')

