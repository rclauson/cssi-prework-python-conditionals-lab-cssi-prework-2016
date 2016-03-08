def isfloat(value):
  try:
    float(value)
    return True
  except:
    return False


#1. Waking Up
def wake_up(day_of_week):
    #write your conditional statement here
    if (day_of_week.lower() == "saturday" or day_of_week.lower() == "sunday"):
        message = "Go back to bed"
    else:
        message = "Stop hitting snooze"
    return message


#2. The Commute
def commute(climate, mins_until_work):
    #write your conditional statement here
    if climate.lower()=="rainy" or mins_until_work<=10:
        transport_type = "Better take the car"
    elif climate.lower()=="sunny" and mins_until_work >30:
        transport_type = "Enjoy a bike ride!"
    else:
        transport_type= "Hop on the bus"
    return transport_type


#3. Coffee Buzz
def coffee(number_of_emails):
    #write your conditional statement here
    if (number_of_emails>=100):
        response = "Time for a triple shot espresso"
    elif (number_of_emails>=50):
        response = "Go for a large black coffee"
    elif (number_of_emails>0):
        response = "A latte will serve you well"
    elif (number_of_emails==0):
        response = "You have reached the Nirvana of 21st century communication!"
    else:
       response = "Is this a new Gmail feature?"
    return response


#Asks user what day it is, calls wake_up() with that answer as an argument
day_of_week = raw_input("What day is it?")
print wake_up(day_of_week)

#Calls commute() with two arguments
weather = raw_input("What is the weather outside? (Rainy, Sunny or Windy?)")
mins = raw_input("How many minutes do you have before you're late?")
print commute(weather,float(mins))

#Checks if the user's input can be converted to a float, otherwise asks user to reenter their number
emails = raw_input("You made it to work on time. How many unread emails are in your inbox?")
if(isfloat(emails)):
    #convert to an integer
    email_num=float(emails)
    #call the coffee function
    print coffee(email_num)
else:
    emails = raw_input("Please enter a number!")
