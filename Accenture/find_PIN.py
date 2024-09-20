def FindPIN (inp1, inp2, inp3, inp4):
    inp1= str(inp1)
    inp2= str(inp2)
    inp3= str(inp3)
    inp1= sorted(inp1)
    inp2= sorted(inp2)
    inp3= sorted(inp3)
    return ((int(inp1[0])*int(inp2[-1])*int(inp3[-1]))+inp4)

inp1= int(input())
inp2= int(input())
inp3= int(input())
inp4= int(input())
print(FindPIN (inp1, inp2, inp3, inp4))
