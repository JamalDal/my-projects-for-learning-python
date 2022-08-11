

print("Hello, wlecome to the fun quiz")
print("Here, we will ask you some fun questions and will show your score as well")
name = str.title(input(str("Please enter your name ")))
print("Dear "+ str(name)+ " for each correct answer you will get one mark and for each incorrect answer you will lose 0.25 mark")

playing = str.lower(input(str("Are you ready to have some fun? ")))
if playing == "yes":    
    print("We are all set. Let's play")
elif playing == "no":
    print("you chose not to play. See you soon. Bye Bye!")
    quit()
else:
    print("Please enter a valid input: Yes or No")
    print("please start over")
    quit()
#     if playing == "yes":    
#         print("We are all set. Let's play")
#     elif playing == "no":
#         print("you chose not to play. See you soon. Bye Bye!")
#         quit()

score = 0
positive_score = 0
negative_score = 0

answer = str.lower(input(str("The maple leaf exists in the flag of Canada has how many corners/ points? ")))
if answer.strip() == str.lower(("11")) or str.lower(("Eleven")):
    print("congrats! Correct answer")
    positive_score += 1
else:
    print("Incorrect answer, Sorry!")
    print("The correct answe is 11")
    negative_score += 1
    #here giving an potion to know the correct answer/definition # need to think about it 

answer = str.lower(input(str("What are the 2 official languages used in Canada? ")))
if answer.strip() == str.lower(("English and French")) or str.lower(("English, French")) or str.lower(("French, Englsih")) or str.lower(("French and English")) or str.lower(("French, Englsih")): 
    print("congrats! Correct answer")
    positive_score += 1
else:
    print("Incorrect answer, Sorry!")
    print("The correct answe is English and french")
    negative_score += 1
    
answer = str.lower(input(str("What is the capital city of Canada? ")))
if answer.strip() == str.lower("Ottawa"):
    print("congrats! Correct answer")
    positive_score += 1
else:
    print("Incorrect answer, Sorry!")
    print("The correct answe is Ottawa")
    negative_score += 1

answer = str.lower(input(str("What is the largest city in Canada? ")))
if answer.strip() == str.lower("Toronto"):
    print("congrats! Correct answer")
    positive_score += 1
else:
    print("Incorrect answer, Sorry!")
    print("The correct answe is Toronto")
    negative_score += 1

answer = str.lower(input(str("Traffic flow on which side of the road in Canada? ")))
if answer.strip() == str.lower("Right side") or str.lower("Right"):
    print("congrats! Correct answer")
    positive_score += 1
else:
    print("Incorrect answer, Sorry!")
    print("The correct answe is Right side")
    negative_score += 1

answer = str.lower(input(str("“From sea to sea” is the official motto of which country? ")))
if answer.strip() == str.lower("Canada"):
    print("congrats! Correct answer")
    positive_score += 1
else:
    print("Incorrect answer, Sorry!")
    print("The correct answe is Canada")
    negative_score += 1

answer = str.lower(input(str("“O Canada” is the national anthem of Canada in which year it was officially announced? ")))
if answer.strip() == str.lower("1980"):
    print("congrats! Correct answer")
    positive_score += 1
else:
    print("Incorrect answer, Sorry!")
    print("The correct answe is 1980")
    negative_score += 1


answer = str.lower(input(str("In which province Jasper National Park Of Canada exist? ")))
if answer.strip() == str.lower("Alberta"):
    print("congrats! Correct answer")
    positive_score += 1
else:
    print("Incorrect answer, Sorry!")
    print("The correct answe is Alberta")
    negative_score += 1

answer = str.lower(input(str("What is the total height (in ft) of Niagara Fall? ")))
if answer.strip() == str.lower("167"):
    print("congrats! Correct answer")
    positive_score += 1
else:
    print("Incorrect answer, Sorry!")
    print("The correct answe is 167")
    negative_score += 1

answer = str.lower(input(str("Who was the first female prime minister of Canada? ")))
if answer.strip() == str.lower("Kim Campbell"):
    print("congrats! Correct answer")
    positive_score += 1
else:
    print("Incorrect answer, Sorry!")
    print("The correct answe is Kim Campbell")
    negative_score += 1



print ("you got: " + str(positive_score) + " correct answer(s)")
print ("you got: " + str(negative_score) + " incorrect answer(s)")
score= (positive_score*1 -negative_score*0.25)
print ("Dear " + str(name) + " your final score was : " + str(score))

#need to work on the following things
#giving a chance to play again
#multi "" in string
#multiple options like 11 or eleven, or skipping comma and 'and' like in english and french >> here looking for keywords: english and french
# or like Right side or right
#jiggling questions >> random quesions form the bank/db/already defined
# there will be xxxxx number of questions
# can we set the timer as well (total time)
