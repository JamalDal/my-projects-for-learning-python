
name = input("Please type your name: ").title()
print("Welcome", name, "to the adventure!")
answer = input("You are on a dirt road, it has come to an end. You can go left to right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You have come to a river. You can walk around it or swim across. Type walk to walk around or swim to swim across: ").lower()
    if answer == "walk":
        print("You walked over 50 miles and ran out of drinking water.")
        print("Sorry, you lost the game.")
        
    elif answer == "swim":
        print("While you were swimming, an alligator came and eaten you.")
        print("Sorry, you lost the game.")
    else:
        print("not a valid option. You lose.")

elif answer == "right":
    answer = input("You have come to a highway. You can ride or drive. Type ride to ride Royal Enfield or drive to drive Tesla: ").lower()
    if answer == "ride":
        print("You were rode over 100 miles and ran out of gas.")
        print("Sorry, you lost the game.")  
    elif answer == "drive":
        print("Thanks to solar panel on Tesla, you driven the highway sucessfully without running out of gas.")
        print("Conrats, you won the game.")
    else:
        print("not a valid option. You lose.")

else:
    print("not a valid option. Game ended.")

print("Thank you for trying,",name + "." + " Good luck for the next adventure.")