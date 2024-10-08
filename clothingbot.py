print("Welcome to Ben's Clothing Store, how may we help you? \n1. Return an item\n2. Exhange and item.")
answer = int(input("Please enter the number of your choice: "))

def response(answer):
    if answer == 1:
        print("Return an item")
    elif answer == 2:
        print("Exhange an item")    
response(answer)