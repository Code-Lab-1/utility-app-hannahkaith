#VENDING MACHINE!

#GREETINGS
#print method is used to show greetings, options and responses
print("⋆﹥━━━━━━━━━━━━━━━﹤⋆")
print("Hey there! ♥")
print("Can we offer you a beverage that would surely satiate your thirst? \n(Choose one of the options to answer!)\n")
print("1. Yes! / 2. No thanks")
print("⋆﹥━━━━━━━━━━━━━━━﹤⋆\n")



#if-else method determines whether a drink will be purchased by the user or not
ans1 = input() #a variable to store the answer to whether the user wants a drink or not
if ans1 == '1': #if '1' is chosen, this would be printed ↓
    print("That's great, then! \n")
elif ans1 == '2': #if '2' is chosen, this would be printed ↓
    print("Alright! Have a nice day.")
    quit() #this immediately terminates the program
else: #should any option not be chosen, this would be printed ↓
    print("Oh no! Please try again. This time, choose one of the options!")
    quit() #this immediately terminates the program


#DRINK CHOICES
drinks = [" a. Coldwater      $2", " b. Iced Tea       $2", " c. Iced Coffee    $2\n",
" d. Cola           $3", " e. Melon Soda     $3", " f. Banana Milk    $4"] #a list was used to store the items
print("Pick your drink of choice!\n (Choose one of the letters to answer!)")
for drink in drinks: #'for loop' is used to print each item on a new line
     print (drink)



#SUGGESTIONS MADE FOR THE CHOSEN DRINK 
#if-else method is used to print out suggestions and questions
drink = input() #a variable to store the chosen drink
if drink == 'a': #if 'a' is chosen, this would be printed ↓
        print("Great choice! this would pair nicely with a yanyan!")
        print("Would you like to buy a snack?\n\n 1. Yes! / 2. No thanks")
        drink = 'Coldwater' #its value will then be replaced with 'Coldwater'
elif drink == 'b':  #if 'b' is chosen, this would be printed ↓
        print("Great choice! You could pair this with a pocky nicely!")
        print("Would you like to buy a snack?\n\n 1. Yes! / 2. No thanks")
        drink = 'Iced Tea' #its value will then be replaced with 'Iced Tea'
elif drink == 'c':  #if 'c' is chosen, this would be printed ↓
        print("Great choice! this would pair nicely with milk bread!")
        print("Would you like to buy a snack?\n\n 1. Yes! / 2. No thanks")
        drink = 'Iced Coffee' #its value will then be replaced with 'Iced Coffee'        
elif drink == 'd':  #if 'd' is chosen, this would be printed ↓
        print("Great choice! You could pair this with hazelnut wafers nicely!")
        print("Would you like to buy a snack?\n\n 1. Yes! / 2. No thanks")
        drink = 'Cola' #its value will then be replaced with 'Cola'
elif drink == 'e':  #if 'e' is chosen, this would be printed ↓
        print("Great choice! this would pair nicely with a choco pie!")
        print("Would you like to buy a snack?\n\n 1. Yes! / 2. No thanks")
        drink = 'Melon Soda' #its value will then be replaced with 'Melon Soda'
elif drink == 'f':  #if 'f' is chosen, this would be printed ↓
        print("Great choice! You could pair this with a matcha flavoured kitkat nicely!")
        print("Would you like to buy a snack?\n\n 1. Yes! / 2. No thanks")
        drink = 'Banana Milk' #its value will then be replaced with 'Banana Milk'
else: #should any option not be chosen, this would be printed ↓
    print("Oh no! Please try again. This time, choose one of the options!")
    quit() #this immediately terminates the program 


#snack choices
ans3 = input() #a variable to store the answer to whether the user wants a snack
if ans3 == '1':
    snacks = [" i. Matcha KitKat           $2", " ii. Choco Pie              $2",
    " iii. Yan Yan               $3", " iv. Cookies n Cream Pocky  $3", " v. Hazelnut Wafers         $3 ", 
    " vi. Milk Bread             $4"] #a list was used to store the items
    for snack in snacks: #'for loop' is used to print each item on a new line
        print (snack)

    snack = input("\nPick your snack of choice!\n(Choose one of the numbers to answer!)\n") #a variable to store the chosen snack
    if snack == 'i': #if 'i' is chosen, it will be replaced with 'Matcha KitKat'
        snack = 'Matcha KitKat'
    elif snack == 'ii': #if 'ii' is chosen, it will be replaced with 'Choco pie'
        snack = 'Choco Pie'
    elif snack == 'iii': #if 'iii' is chosen, it will be replaced with 'Yan Yan'
        snack = 'Yan Yan'        
    elif snack == 'iv': #if 'iv' is chosen, it will be replaced with 'Cookies n Cream Pocky'
        snack = 'Cookies n Cream Pocky'
    elif snack == 'v': #if 'v' is chosen, it will be replaced with 'Hazelnut Wafers'
        snack = 'Hazelnut Wafers'
    elif snack == 'vi': #if 'vi' is chosen, it will be replaced with 'Milk Bread'
        snack = 'Milk Bread'
    else: #should any option not be chosen, this would be printed ↓
        print("Oh no! Please try again. This time, choose one of the options!")
        quit() #this immediately terminates the program 
    print("Great!")
    
    drinkchoice = int(input("Enter the price of the drink chosen here -> ")) #the drinks' price is stored in this variable
    snackchoice = int(input("Enter the price of the snack chosen here -> ")) #the snacks' price is stored in this variable
    total = int(drinkchoice) + int(snackchoice) #the total price is stored in this variable
    print(f"Your total is {total}")
    money = int(input("Enter the amount of money: ")) #this variable stores the money of the user
    change = int(money) - int(total) #this variable stores the change

    #if-else determines if there is change from the given amount
    if money == total: #if 'money' is equals to the 'total', this would be printed ↓
        print("⋆﹥━━━━━━━━━━━━━━━﹤⋆")
        print("Enjoy your food and have a splendid day!\n")
    elif money >= total: #if 'money' is greater than the 'total', this would be printed ↓
        print("⋆﹥━━━━━━━━━━━━━━━﹤⋆")
        print(f"Your change is {change}")
        print(f"Enjoy your {drink} and {snack}. Have a wondrous day!\n")
        print("⋆﹥━━━━━━━━━━━━━━━﹤\n⋆")
    elif money <= total: #if 'money' is less than the 'total', this would be printed ↓
        print("⋆﹥━━━━━━━━━━━━━━━﹤⋆")
        print("Oopsies! that's not enough money :<\n")



elif ans3 == '2':
    print("Alright! Let's get to paying!")
    drinkchoice = int(input("Enter the price of the drink chosen here -> ")) #the drinks' price is stored in this variable
    money = int(input("Enter the amount of money: ")) #this variable stores the money of the user
    change = int(money) - int(drinkchoice) #this variable stores the change
    if money == drinkchoice: #if 'money' is equals to the drinks' price, this would be printed ↓
        print("⋆﹥━━━━━━━━━━━━━━━﹤⋆")
        print("Enjoy your food and have a splendid day!\n")
    elif money >= drinkchoice: #if 'money' is greater than the drinks' price, this would be printed ↓
        print("⋆﹥━━━━━━━━━━━━━━━﹤⋆")
        print(f"Your change is {change}")
        print(f"Enjoy your {drink} and have a wondrous day!\n")
        print("⋆﹥━━━━━━━━━━━━━━━﹤⋆\n")
    elif money <= drinkchoice: #if 'money' is less than the drinks' price, this would be printed ↓
        print("⋆﹥━━━━━━━━━━━━━━━﹤⋆") 
        print("Oopsies! that's not enough money :<\n")
else: #should any option not be chosen, this would be printed ↓
    print("Oh no! Please try again. This time, choose one of the options!")
    quit() #this immediately terminates the program 

#END OF PROGRAM :)