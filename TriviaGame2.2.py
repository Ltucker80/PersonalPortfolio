import sys

que = input("How many players is it? 1 or 2? ")
player1 = input("Enter your name Player One: ")
score = 0

while True:

    if que == "1":
        print("Ready ", player1, "?")
        break

    else:
        print("This is only a 1 player game")
        break

aws = input()

if aws.lower() == "yes":
    print(" Starting the game. \n Each question is worth 100 pts. \n Let's Begin")

else:
    print("We will start when you are ready. Just hit Play to Restart.")
    sys.exit()

question1 = (input(" 1.) How many letters is in the Alphabet? "))
answer1 = "26"

if question1 == answer1:
    print("Correct, next question:")
    score = score + 100

else:
    print("Well, ", player1, " not everyone can be smart when answering simple questions")
    print("The answer was: ", answer1)
    print("Well done. Your total score for playing is: ", score)
    sys.exit()

question2 = (input(" 2.) What is the capital of the United States? "))
answer2 = "DC"

if question2 == answer2.lower():
    print("2 for 2, we are on a roll here. Next question:")
    score = score + 100
else:
    print("Well, ", player1, " you manage to get at least 1 right. So that's a BIG STEP closer to be smarter.")
    print("The answer was: ", answer2)
    print("Well done. Your total score for playing is: ", score)
    sys.exit()

question3 = (input(" 3.) 2 + 2 + 2 = 6. In a game of BlackJack, what number do you need to win? "))
answer3 = "21"

if question3 == answer3:
    print(player1, " do you gamble? Want to bet how easy the next question is? ")
    score = score + 100
else:
    print("2 out of 3 is not bad. You are still smarter than your child, if you have 1. If not you are smarter than A "
          "Child.")
    print("The answer was: ", answer3)
    print("Well done. Your total score for playing is: ", score)
    sys.exit()

question4 = (input(" 4.) Blue, Red, Yellow, or Green: What color is considered a 'Calm' color? "))
answer4 = "Blue"

if question4 == answer4.lower():
    print("You are too mellow. Next Question:")
    score = score + 100
else:
    print("Just like the color Red, you got it wrong.")
    print("The answer was: ", answer4)
    print("Well done. Your total score for playing is: ", score)
    sys.exit()

question5 = (input(" 5.) Ghostbusters or Goosebumps: Which had a legitimate business? "))
answer5 = "Ghostbusters"

if question5 == answer5.lower():
    print("If there's something strange in your neighborhood, who you gonna call? The Next question: ")
    score = score + 100
else:
    print("I blame the ghost behind you for getting this answer wrong. Unless you are scared of 'Right Answers'.")
    print("The answer was: ", answer5)
    print("Well done. Your total score for playing is: ", score)
    sys.exit()

question6 = (input(" 6.) What music artist was '2 legit 2 quit'? "))
answer6 = "MC Hammer"

if question6 == answer6.lower():
    print("Go ahead and finish singing the song. You are on a roll, 6 for 6. Next Question:")
    score = score + 100
else:
    print("Laughing my computer ass off because you are 2 irrelevant to keep playing. But you did at least get 5 out "
          "of 6.")
    print("The answer was: ", answer6)
    print("Well done. Your total score for playing is: ", score)
    sys.exit()

question7 = (input(" 7.) What was the name of the famous chocolate on the Nickelodeon show, 'Rugrats'? "))
answer7 = "Reptar bar"

if question7 == answer7.lower():
    print("Stealing candy from Tommy, Chuckie, The Twins, and Angelica I see. Next Question:")
    score = score + 100
else:
    print("Well, ", player1, " Hershey isn'tgood enough for a,", answer7, ".")
    print("The answer was: ", answer7)
    print("Well done. Your total score for playing is: ", score)
    sys.exit()

question8 = (input(" 8.) What month has '28' days? "))
answer8 = "every month"

if question8 == answer8.lower():
    print(player1, ", you almost got tricked by a trick question. Next Question:")
    score = score + 100
else:
    print("You must have been born yesterday.")
    print(answer8, " has 28 days in it.")
    print("Well done. Your total score for playing is: ", score)
    sys.exit()

question9 = (input(" 9.) Mary's Mom had 4 kids. Nickel, Dime, Penny. What is the name of the last kid? "))
answer9 = "Mary"

if question9 == answer9.lower():
    print(player1, ", 9 for 9. Next Question:")
    score = score + 100
else:
    print("Finally, I stopped your progress with a trick question HA HA HA!!!.")
    print("The answer was: ", answer9)
    print("Well done. Your total score for playing is: ", score)
    sys.exit()

question10 = (input(" 10.) What is the name of this game? "))

if question10 == "There is no name":
    print(player1, ", you are right. I should name this game.")
    print("Well done. You managed to make it this far into the game. \n Be warned, the questions will get harder and "
          "tougher than the last 9. \n The new question are worth 200 pts.\n Here's your Next Question:")

else:
    print("I know what you were really thinking and you are right. I should name this game.")
    print("Well done. You managed to make it this far into the game. \n Be warned, the questions will get harder and "
          "tougher than the last 9. \n The new question are worth 200 pts.\n Here's your Next Question:")

question11 = (input(" 11.) Which horoscope sign shares the same sexual position commonly known as '69'? "))
answer11 = "Cancer"

if question11 == answer11.lower():
    print(player1, ", you are a freak in the sheets I see. Next Question:")
    score = score + 200
else:
    print("You must haven't been laid in a very long time. There are dating sites you know. I'm telling you this cause "
          "I'm a computer.")
    print("The answer was: ", answer11)
    print("Well done. Your total score for playing is: ", score)
    sys.exit()

question12 = (input(" 12.) What is the rarest M&M color? "))
answer12 = "Brown"

if question12 == answer12.lower():
    print("You my friend, eat too many junk food to know this answer. Next Question:")
    score = score + 200
else:
    print("You don't like chocolate.")
    print("The answer was: ", answer12)
    print("Well done. Your total score for playing is: ", score)
    sys.exit()

question13 = (input(" 13.) 'Hendrick’s,' 'Larios,' and 'Seagram’s' are some of the best-selling brands of which "
                    "spirit? "))
answer13 = "Gin"

if question13 == answer13.lower():
    print("You are such a drunk. The next question comes with a Breathalyzer Test. Next Question:")
    score = score + 200
else:
    print("You must be a Goodie 2 Shoes. I suggest you get sloppy drunk.")
    print("The answer was: ", answer13)
    print("Well done. Your total score for playing is: ", score)
    sys.exit()

question14 = (input(" 14.) How many months does elephant pregnancies last? "))
answer14 = "22"

if question14 == answer14:
    print("Expert on Elephants I see. Next Question:")
    score = score + 200
else:
    print("You should have used a 'phone in' lifeline to a Poachers for this answer.")
    print("The answer was: ", answer14)
    print("Well done. Your total score for playing is: ", score)
    sys.exit()

question15 = (input(" 15.) When was the first New Year's Eve ball drop in Times Square? "))
answer15 = "December 31, 1907"

if question15 == answer15:
    print("Should old questions be forgotten cause you got it right. Don't expect me to kiss you cause it was the "
          "right answer but surely expect the Next Question:")
    score = score + 200
else:
    print("I am amazed that you have been able to answer 14 out of 15 right.")
    print("The answer was: ", answer15)
    print("Well done. Your total score for playing is: ", score)
    sys.exit()

question16 = (input(" 16.) Marines or Army: What branch of service did the actor ' Clint Eastwood' served? "))
answer16 = "Army"

if question16 == answer16.lower():
    print("You Googled this answer unless you are a Military nut. I'm about to serve the Next Question:")
    score = score + 200
else:
    print("I see. The closes thing to being in the Military you done was on a game of 'Call Of Duty'.")
    print("The answer was: ", answer16)
    print("Well done. Your total score for playing is: ", score)
    sys.exit()

question17 = (input(" 17.) What year did Israel become a state? "))
answer17 = "1948"

if question17 == answer17:
    print("17 for 17 you are on a role. Time for the Next Question:")
    score = score + 200
else:
    print("Did you listen to them misinformation Hebrew Israelites? Damn shame.")
    print("The answer was: ", answer17)
    print("Well done. Your total score for playing is: ", score)
    sys.exit()

question18 = (input(" 18.) Ag, Au, Pt, or At: Which Atomic Symbol is the Symbol for Gold? "))
answer18 = "Au"

if question18 == answer18.lower():
    print("Obviously you know the Periodic Table or you can spot fake Gold. Next Question:")
    score = score + 200
else:
    print("If you didn't know this, how do you know the gold jewelery you buy is real gold?.")
    print("The answer was: ", answer18)
    print("Well done. Your total score for playing is: ", score)
    sys.exit()

question19 = (input(" 19.) Bill Gates, Bill Nye, Bill Murray, Bill Walton, or Bill Clinton: Who's more likely to "
                    "speak on Science? "))
answer19 = "Bill Nye"

if question19 == answer19.lower():
    print("OBVIOUSLY!!! He's the SCIENCE GUY... DUH. Next Question:")
    score = score + 200
else:
    print("History must have been your favorite subject. That or Math cause Biology isn't it. Maybe you were a P.E. "
          "kid.")
    print("The answer was: ", answer19)
    print("Well done. Your total score for playing is: ", score)
    sys.exit()

question20 = (input(" 20.) Has this game been fun thus far? 'Y' or 'N' "))

if question20 == "Y":
    print(player1, ", it better have been since you are 19 for 19 and managed a score of : ", score)
    print("Again you managed to make it to a point where I figured you would have failed by now. \n The new questions "
          "WILL BE BRUTAL!!!! \n They are now worth 400 pts. \n Here's your Next Question:")

else:
    print("What did you have to Google all your answers? Is my questions too hard for the little baby? LOL.")
    print("Again you managed to make it to a point where I figured you would failed by now. \n The new questions "
          "WILL BE BRUTAL!!!! \n They are now worth 400 pts. \n Here's your Next Question:")

question21 = (input(" 21.) Bill Russell, Bill Withers, Bill Cobbs, or Bill Bellamy: Which Bill taught us 'How to be a "
                    "Player? "))
answer21 = "Bill Bellamy"

if question21 == answer21.lower():
    print("Does your partner know you are a Cheater? Next Question:")
    score = score + 400
else:
    print("If you got this question wrong cause you were with you partner, type in the word: HELP. I work in code too.")
    print("The answer was: ", answer21)
    print("Well done. Your total score for playing is: ", score)
    sys.exit()

question22 = (input(" 22.) How many miles away from the Earth to the Sun? "))
answer22 = "93 million"

if question22 == answer22:
    print("You are not Neil Armstrong, Who gave you this answer? Bill Nye? I'm on to you... Next Question:")
    score = score + 400
else:
    print("If I gave you the option to call Bill Nye you might have gotten it right.")
    print("The answer was: ", answer22)
    print("Well done. Your total score for playing is: ", score)
    sys.exit()

question23 =(input(" 22.) Before the Gregorian Calendar, what was the original date for New Year? "))
answer23 = "March 25"

if question23 == answer23:
    print("23 of 23 I am amazed that you are trying to beat the computer. Next Question:")
    score = score + 400
else:
    print("January and February didn't come until around 700 BCE.")
    print("The answer was: ", answer23)
    print("Well done. Your total score for playing is: ", score)
    sys.exit()

question24 = (input(" 23.) Lyndon B Johnson had 4 buttons installed in the Oval Office; Coffee, Tea, Coke, and what? "))
answer24 = "Fresca"

if question24 == answer24.lower():
    print("Did you get him his drink to know this answer? Next Question:")
    score = score + 400
else:
    print("I have 1 button for you: [ A ] You Lost.")
    print("The answer was: ", answer24)
    print("Well done. Your total score for playing is: ", score)
    sys.exit()

question25 = (input(" 25.) Eleanor, William, Beaver, or Dartmouth: What ship wasn't taken over by the Boston Tea Party?"))
answer25 = "William"

if question25 == answer25.lower():
    print("I guess you didn't think I was talking about the Tea Party Republicans. Good for you. Next Question:")
    score = score + 400
else:
    print("They didn't take over the ship because it never existed.")
    print("The answer was: ", answer25)
    print("Well done. Your total score for playing is: ", score)
    sys.exit()

question26 = (input(" 26.) Star Wars or Star Trek: LeVar Burton was a actor on which? "))
answer26 = "Star Trek"

if question26 == answer26.lower():
    print("George Lucas must didn't like Reading Rainbow to cast him. Next Question:")
    score = score + 400
else:
    print("25 out of 26 Hans Solo. I'm proud of you Chewbacca. Call me C-3PO.")
    print("The answer was: ", answer26)
    print("Well done. Your total score for playing is: ", score)
    sys.exit()

question27 = (input(" 27.) What city is know the Rose Capital? "))
answer27 = "Tyler, Tx"

if question27 == answer27:
    print("A true Texan I see. Next Question:")
    score = score + 400
else:
    print("Now you know where to buy a rose from lol.")
    print("The answer was: ", answer27)
    print("Well done. Your total score for playing is: ", score)
    sys.exit()

question28 = (input(" 28.) Coulrophobia is a far of what? "))
answer28 = "Clowns"

if question28 == answer28.lower():
    print("Don't go to the Circus or a Rodeo. Next Question:")
    score = score + 400
else:
    print("Have you ever seen the movie 'Killer Clowns from Outer Space'? You just might fear them after watching it "
          "lol.")
    print("The answer was: ", answer28)
    print("Well done. Your total score for playing is: ", score)
    sys.exit()

question29 = (input(" 29.) What 1990s Martial Arts actor took his skills to do work out videos? "))
answer29 = "Billy Blanks"

if question29 == answer29.lower():
    print("Look at you. Doing TAEBO and stuff. 29 for 29.")
    print("WOW!!! you are this smart to make it to the final question.", player1," you managed to score a total of: ",
          score, ". \n This last question is worth 1000 pts. ", player1, ", here is your Final Question of the game.")
    score = score + 400
else:
    print("You must be a fat loser. Pull yourself together.")
    print("The answer was: ", answer29)
    print("Well done. Your total score for playing is: ", score)
    sys.exit()

question30 = (input(" 30.) The 1st form of an Electronic email was sent when? "))
answer30 = "October 29, 1969"

if question30 == answer30:
    print("30 for 30 how did you do it? Hook me up to another computer? Cause that is the only way you could have "
          "beaten me.")
    print("Well done. Your total score for playing is: ", score)
    score = score + 1000
    sys.exit()

else:
    print("What a close call. But hey don't beat yourself up. You got 29 right answers.")
    print("The answer was: ", answer30)
    print("Well done. Your total score for playing is: ", score)
    sys.exit()
