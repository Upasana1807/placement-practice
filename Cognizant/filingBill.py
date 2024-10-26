# cook your dish here
def bill(pizza, puff, drink):
    
    return f"""No. of pizzas:{pizza}
No. of puffs:{puff}
No. of drinks:{drink}
Total price:{(pizza*100)+(puff*20)+(drink*10)}
    """

pizza = int(input("Enter the number of pizza: "))
puff= int(input())
drink= int(input())
print(bill(pizza, puff, drink))