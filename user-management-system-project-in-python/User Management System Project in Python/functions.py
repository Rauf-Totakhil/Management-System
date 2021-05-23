import random
import user_class


def getUniqueNumber():

    unique = False 
    while(not unique): 
        num = random.randrange(1,user_class.User.maxUsers)
           
        if(user_class.User.checkId_num(num) == True):
            unique = True   
    return num



def grabDate():
    while(True):
        date = input("Please enter a user's DOB: [mm/dd/yy] ")
        if( len(date) == 8 and date[2] == "/"):
            return date
        else:
            print("Incorrect date format!\nEnter date as: [mm/dd/yy] ")


def deleteUser():
    print("\nDeleting user...")
    selector = input("Please enter a name, ID number, or date: ")

    user_class.User.delUser(selector) 
        
def num_there(s):
    return any(i.isdigit() for i in s)



def loadDatabase():
 
    user_class.User.loadUsers()
    
#save database to csv file
def save_database():
    print("\nSaving Database....\n")
    user_class.User.saveUsers()
    return 1



def determineState():

    save=input("\nWould you like to save the database before closing? [Y/N]\n")

    if( save.lower() == "y" ):
        print("\nSaving database and exiting....\n")
        save_database()
    else:
        print("\nQutting program without saving....\n")
        
    return 1

def display_home_message():

    print("\nWelcome to User Management System")
    s = input("""Would you like to __
          1 - See Current Users
          2 - Add User
          3 - Delete User
          4 - Show a User
          5 - Save Database
          6 - More Options
          7 - Quit\n""")

    return s


