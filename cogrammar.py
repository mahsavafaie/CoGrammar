# docstrings """ are more commonly used for describing the code
"""An SMS Simulation"""

class SMSMessage(object):
  # you don't need class attributes here, use them in the __init__ function (below)
  hasBeenRead = False
  messageText = text
  fromNumber = number

  # for init to actually be called when class is instantiated,
  # it needs to be called __init__
  # better to keep your variables lowercase with underscores for python
  # has_been_read instead of hasBeenRead
  def init(self,hasBeenRead,messageText,fromNumber):
    # right now, the arguments aren't getting set as attributes. you set them when you make instances.
    # also, text and number are undefined. I fixed the first attribute for you
    self.hasBeenRead = hasBeenRead
    self.messageText = text
    self.fromNumber = number

  def MarkASRead(self):
    # userChoice/read has not been defined here
    # define this method with userChoice as an argument
    # and make sure that "read" is a string, right now it is a variable
    if userChoice == read:
      self.hasBeenRead = True
  # these methods will all need self as first argument since it represents the instance
  # you might want to add 'pass' to each of your work in progress or comment them out,
  # so that you can at least test the code you're working on
  def add_sms():

  def get_count():

  def get_message():

  def get_unread_messages():

  def remove():

no_1 = SMSMessage(False, "Hello", "0798653452")
no_2 = SMSMessage(False, "WYD", "0845673864")
no_3 = SMSMessage(False, "How are you?", "0631873298")

SMSStore = []
userChoice = ""

# nice while loop! good way to run a program until the user wants to exit!
# for completeness, add instructions for them on how to quit. (i.e. type quit to exit.)
while userChoice != "quit":
    # to run this code in python3 use input instead of raw_input
    userChoice = raw_input("What would you like to do - read/send/quit?")
    if userChoice == "read":
    # here you could call a method on your instance, e.g. no_1.markASRead
    # Place your logic here
    elif userChoice == "send":
    # Place your logic here
    elif userChoice == "quit":
        print("Goodbye")
    else:
        print("Oops - incorrect input")

# in python, the most normal pattern is to instantiate an instance of the class with the needed data:
# instance = SMSMessage(false, "text", "01234")
# after you have instantiated objects, you can call class methods on them:
# instance.MarkASRead()
# if you need to pass arguments, you can. the first, self, is provided automatically,
# and needs to be included in your method definition.
