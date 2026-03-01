class Atm:
  def __init__(self):
    self.pin = ''
    self.balance = 0
    self.menu()

  def menu(self):
    choice = input('''
    How can I help you ?
    1. Press 1 to create pin
    2. Press 2 to change pin
    3. Balance Inquiry
    4. Exit    
   ''')  
    
    if choice == '1': # create pin
      self.create_pin()
    
    if choice == '2':  # change pin
      pass
    
    if choice == '3':  # Balance Inquiry
      pass
    
    if choice == '4':  # Exit
      exit()
    
    else:
      print('Invalid choic')
      exit()
  def create_pin(self):
    user_pin = input("Enter your pin: ")
    self.pin += user_pin    

obj1 = Atm()   