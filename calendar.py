from time import sleep, strftime
user_first_name = "idil"
calendar = {
  "06/12/2023":"Meeting",
  "08/12/2023":"Family Meeting",
  "09/12/2023":"Road Trip",
  "21/12/2023":"Concert"
  }
def welcome():
  print ("Welcome " + user_first_name)
  print ("Calendar starting...")
  sleep(1)
  print ("Today is " + strftime("%A %B %d, %Y"))
  print ("Time is: " + strftime("%H:%M:%S"))
  sleep(1)
  print ("What would you like to do?")

def start_calendar():
  welcome()
  start = True
  while start:
    user_choice = input("A to Add, U to Update, V to View, D to Delete, X to Exit: ")
    user_choice = user_choice.upper()
    if user_choice == "V":
      if len(calendar.keys()) < 1:
        print ("Calendar is empty.")
      else:
        print (calendar)
    elif user_choice == "U":
      date = input("What date? ")
      update = input("Enter update: ")
      calendar[date] = update
      print ("Update is successful")
      print (calendar)
    elif user_choice == "A":
      event = input("Enter event: ")
      date = input("Enter date (MM/DD/YYYY): ")
      if (len(date) > 10 or int(date[6:]) < int(strftime("%Y"))):
        print ("You entered invalid date.")
        try_again = input("Try Again? Y for Yes, N for No: ")
        try_again = try_again.upper()
        if try_again == "Y":
          continue
        else:
          start = False
      else:
        calendar[date] = event
        print ("Event is added.")
        print (calendar)
    elif user_choice == "D":
      if len(calendar.keys()) <1:
        print ("Calendar is empty.")
      else:
        event = input("What event? ")
        for date in calendar.keys():
          if event == calendar[date]:
            del calendar[date]
            print ("Event deleted")
            print (calendar)
          else:
            print ("You entered invalid event")
  
    elif user_choice == "X":
      start = False

    else:
      print ("You entered invalid command")
      start = False
start_calendar()
