import sys
import user_class
import functions


functions.loadDatabase()



while( True ):

    s=functions.display_home_message()

    print("**The value chosen is: ",s)
    if(s == "1"):
        user_class.User.showUsers()    
    elif(s == "2"):
        user_class.User.addUser()
    elif(s == "3"):
        functions.deleteUser()  
    elif(s == "4"):    
        print("'Show a User' selected")
        user_class.User.showUserByNameDate(input("Please enter a name or date identifier: "))
    elif(s == "5"):
        functions.save_database()      
    elif(s == "6"):
        print("\n\nYou have selected more option.\nThere are none at the moment \n;)\n")
    elif(s == "7"):
        print("Quitting Program....")
       
        functions.determineState()
        sys.exit(0)
    else:
        print("Please enter a valid key...")
    print("\n\n")


