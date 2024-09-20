# cook your dish here
def NextCharacter(a, b):
    if ord(a)< ord(b):
        return chr(ord(b)+ abs(ord(b)-ord(a)))
    else:
        return chr(ord(b)- abs(ord(b)-ord(a)))

a= input()
b= input()
print(NextCharacter(a, b))