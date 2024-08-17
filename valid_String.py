# cook your dish here
def validString(s):
    if s.count('*') == s.count('#'):
        return 0
    else:
        return s.count('*') - s.count('#')
            
s= input()
print(validString(s))