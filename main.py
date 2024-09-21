name = input("What is your name? ")
print("Hey there, " + name  + ". My name is Ben, it's nice to meet you!")
age = int(input("How old are you? "))
print("Awesome, " + str(age) + " is a cool age! I'm 17 myself.")

def response(answer):
    if answer == 1:
        print("Placeholder")
    elif answer == 2:
        print("Placeholder")
    elif answer == 3: 
        print("Placeholder")
    elif answer == 4:
        print("Goodbye " + name + ", have a great day!")

print("\nPlease choose from the following options:\n1. Placeholder Option 1\n2. Placeholder Option 2\n3. Placeholder Option 3\n4. Exit the conversation.")
answer = int(input("Enter the number of your choice: "))
response(answer)