//the following line of the code will import the current date and time of the system
import datetime
print("Hello world!")
now = datetime.datetime.now()

//this will display the date and the time
print ("Current date and time is ")
print (now.strftime("%A, %d-%m-%Y : %H:%M"))	
