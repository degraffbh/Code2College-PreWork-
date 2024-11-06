print("Welcome to Ben's Clothing Store, how may we help you? \n1. Return an item\n2. Exhange and item.")
validAnswer = False
while validAnswer == False:
    validAnswer = True
    try:
        answer = int(input("Please enter the number of your choice: "))
        if answer != 1 and answer != 2:
            validAnswer = False
    except:
        validAnswer = False
    
def response(answer):
    if answer == 1:
        item = input("What item would you like to return? ")
        print(f"{item} has been returned. Thank you for shopping with us.")

    elif answer == 2:
        oldItem = input("What item would you like to exchange? ")
        newItem = input("What item would you like to recieve? ") 
        print(f"{oldItem} has been returned and you have recieved {newItem} instead. Thank you for shopping with us.")

response(answer)