#Let's create touring app.
print("Welcome to Jeet's tours.")
name = input("What is your name? ")
print("Yes " + name + ",")
age = int(input("What is your age? "))
if age <= 10 :
    print("Sorry, you can not go to a tour because of your age.")
    exit()

print("We can give you a tour to Himalayas or to Goa.")
to = input("Where do you want to go?")

if to == "Himalayas" or "himalayas" :
    price = "5000"

if to == "Goa" or "goa" :
   price = "2500"
   
print("To go to " + to + ", your total will be $" + price + " including hotels, transport tickets and taxes.")
print("Here is your ticket, have a nice trip.")
print("Bye")


    
