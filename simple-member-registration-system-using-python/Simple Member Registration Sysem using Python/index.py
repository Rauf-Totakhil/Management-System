import os
import platform

global listStd 
listStd = ["John Smith", "Claire Temple", "Steve Roger"] 

def manageMember(): 

	print(""" 

  ---------------------------------------------------------
 |========================================================| 
 |======== Welcome To Member Registration System =========|
 |========================================================|
  ---------------------------------------------------------

Enter 1 : To View Member List 
Enter 2 : To Register New Member 
Enter 3 : To Search Member 
Enter 4 : To Remove Member 
		
		""")

	try: 
		userInput = int(input("Please Select An Above Option: ")) 
	except ValueError:
		exit("\nHy! That's Not A Number") 
	else:
		print("\n") 

	
	if(userInput == 1): 
		print("List of Members\n")  
		for members in listStd:
			print("=> {}".format(members))

	elif(userInput == 2): 
		newStd = input("Enter New Member: ")
		if(newStd in listStd):
			print("\nThis Member {} Already In The Database".format(newStd))  #Error Message
		else:	
			listStd.append(newStd)
			print("\n=> New Member {} Successfully Add \n".format(newStd))
			for members in listStd:
				print("=> {}".format(members))	

	elif(userInput == 3): 
		srcStd = input("Enter Member Name To Search: ")
		if(srcStd in listStd): 
			print("\n=> Record Found Of Member {}".format(srcStd))
		else:
			print("\n=> No Record Found Of Member {}".format(srcStd)) 

	elif(userInput == 4): 
		rmStd = input("Enter Member Name To Remove: ")
		if(rmStd in listStd): 
			listStd.remove(rmStd)
			print("\n=> Member {} Successfully Deleted \n".format(rmStd))
			for members in listStd:
				print("=> {}".format(members))
		else:
			print("\n=> No Record Found of This Member {}".format(rmStd)) 
	 
	elif(userInput < 1 or userInput > 4): 
		print("Please Enter Valid Option")
						

manageMember()

def runAgain(): 
	runAgn = input("\nContinue Transaction? y/n: ")
	if(runAgn.lower() == 'y'):
		
		manageMember()
		runAgain()
	else:
		quit() 

runAgain()		
