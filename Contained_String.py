# cook your dish here
def ContainedString(x, y):
    if x in y:
        return ("yes")
    else:
        return("no")
x= input()
y= input()
print(ContainedString(x, y))