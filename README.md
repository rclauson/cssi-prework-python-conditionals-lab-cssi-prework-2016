# Conditionals Lab
In this lab you will write a program that gets your user ready for their day at the office.
The functions are already written for you since we haven't quite covered Python functions yet. The general concepts should be familiar from JavaScript. Note that the raw_input() function returns whatever the user types and has a data type of string.

##1. Waking Up
The wake_up() function is written for you. You need to add a conditional statement that checks the day of the week. If it's Saturday or Sunday, tell the user "Go back to bed", otherwise, tell them to "Stop hitting snooze".

##2. The Commute
Help the user navigate their commute. They can choose between biking, public transportation or driving. The function has two parameters, weather and mins_until_work. In this magical climate, the weather is either rainy or sunny. The framework of the commute() function has already been written for you.

If  the weather is "rainy" or if they only have 10 minutes or less before work starts, the user should always drive, tell them by returning "Better take the car". If mins_until_work is greater than 30 and the weather is sunny, they should "Enjoy a bike ride". If mins_until_work is greater than 10 but less than or equal to 30 and it's not raining they should "Hop on the bus".

##3. Coffee Buzz
You first conditional statement will determine the type of coffee your user should equip themselves with before tackling their inbox.

The shell of the coffee() function is written for you. First, the user is prompted to enter the amount of emails in their inbox using the raw_input() function.  If the user's input is not a number, then "Please enter a number!" is returned. If the user's input is a number, then the coffee function is called with the user's response as an argument.

Your job is to write the code inside of the coffee() function that prints a recommendation for the type of coffee the user should grab. If the number of emails is greater than or equal to 100, print: "Time for a triple shot espresso". If the number of emails is between 50 and 99 inclusive, recommend: "Go for a large black coffee". If the user has more than 0 emails but less than 50 , you should print: "A latte will serve you well".  If the user enters that they have 0 unread emails, celebrate by printing: "You have reached the Nirvana of 21st century communication!".

Like all great programs that accept user input, your function should validate the user's input. If the number is less than 0, in this case, print "Is this a new Gmail feature?".
