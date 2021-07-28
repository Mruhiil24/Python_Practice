def isbalanced(string):
    s = []
    for char in string:
        if char in '({[':
            s.append(char)# add in the empty list
        elif char == ')':
            if (not s or s[-1] != '('):
                return False
            s.pop()
        elif char == '}':
            if (not s or s[-1] != '{'):
                return False
            s.pop()
        elif char == ']':
            if (not s or s[-1] != '['):
                return False
            s.pop()
    if (not s):
        return True
    return False



print ("----Enter input here---")
string = input()
ans= isbalanced(string)
print(ans)