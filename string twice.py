# In Python, the loop "for i in range(len(str)):" loops i through each index in the string, 0, 1, 2, .. len-1.
def double_char(str):
    lisp = list(str)
    out = []
    string = ''
    for i in range(len(lisp)):
        out. append(lisp[i])
        out. append(lisp[i])
    for i in range(len(out)):
        string += out[i]
    return string

print(double_char("the"))

