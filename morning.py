
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

