# Conditionals Lab
In this lab you will write a program that gets your user ready for their day at the office. The starter code is inside the file called `morning.py`.


## Running Python Tests
To run the tests at any point as you work through your lab, make sure you are in the lab directory and then run the `learn` command (you can also run `python morning_test.py`). If any test fails, try to understand what the test was checking for by reading the failure messages. Notice that we don't **call** the functions in `morning.py` - instead, we import the functions into `morning_test.py` and call them there in our tests. Make sure to look at `morning_test.py` before you get started!


##1. Waking Up
The first - and often hardest- part of the workday is waking up. Your first function, called wake_up() should accept one argument (`day_of_week`). Based on the day of the week, the function should either tell the user to go back to bed or to get up.  To do this, add a conditional statement that checks contents of the `day_of_week` argument. If it's Saturday or Sunday, tell the user to "Go back to bed". Otherwise, tell them to "Stop hitting snooze". You should use the Python string methods .upper() or .lower() to make sure that both `Saturday` and `saturday` get handled appropriately.

For example, if we were making a function called make_breakfast, we would want to use one of those methods to modify the user input string so that the strings on both side of the operator `==` will always be equal, regardless of how the user chooses to capitalize their answer.

```python
def make_breakfast(type_of_food):
    if (type_of_food.lower() == "eggs" ): #or type_of_food.upper()=="EGGS"
        instructions = "Get our pan"
    else:
        instructions = "Get out bowl"
    return message

bfast_request = raw_input("Are we doing eggs, cereal or yogurt?")
print make_breakfast(bfast_request)
```

## User Input
Note that the example above used raw_input(). When this function is called, the argument `Are we doing eggs, cereal, or yogurt?` is printed on the console and the user can respond with their answer by pressing enter. Whatever the user enters is stored as a string in the `bfast_request` variable. If you are using a Python version that is higher than 2.X, you should use `input()` instead of `raw_input`. To check your Python version, just type `python -V` into the console.


##2. The Commute
Help the user navigate their commute. They can choose between biking, public transportation or driving. The function, `commute()` should have two parameters, weather and mins_until_work. In this magical climate, the weather is either rainy or sunny.

If the weather is "rainy" or if they only have 10 minutes or less before work starts, the user should always drive. Tell them by returning "Better take the car". If mins_until_work is greater than 30 and the weather is sunny, they should "Enjoy a bike ride". If mins_until_work is greater than 10 but less than or equal to 30 and it's not raining they should "Hop on the bus".

##3. Coffee Buzz
The last function you will write is `coffee()` and will determine the type of coffee your user should equip themselves with before tackling their inbox.

First, the user is prompted to enter the amount of emails in their inbox by using the raw_input() function.  If the user's input is not a number, then "Please enter a number!" is returned. If the user's input is a number, then the coffee function is called with the user's response as an argument.

Your job is to write the coffee() function that prints a recommendation for the type of coffee the user should grab. If the number of emails is greater than or equal to 100, print: "Time for a triple shot espresso". If the number of emails is between 50 and 99 inclusive, recommend: "Go for a large black coffee". If the user has more than 0 emails but less than 50 , you should print: "A latte will serve you well".  If the user enters that they have 0 unread emails, celebrate by printing: "You have reached the Nirvana of 21st century communication!".

Like all great programs that accept user input, your function should validate the user's input. If the number is less than 0, in this case, print "Is this a new Gmail feature?".
