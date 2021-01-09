import sqlite3

def welcome():
	entry = int(input('''
	Welcome to your ContactBook.
	Your commands are:1 ,2, 3, 4, 5
	What would u like to do?
	1. Display your exciting contacts
	2. Create a New contact
	3. Check an entry
	4. Delete an entry 
	5. Exit
	Enter your entry here(1, 2, 3, 4, 5): '''))
	return entry

def phonebook():
	contact = {}

	while True:
		entry = welcome()
		if entry == 1:
			if bool(contact) != False:
				for i, j in contact.items():
					print(i, '->', j)
				else:
					print('Phonebook is empty! Go back to the Welcome-menu to add a new contact')

		elif entry == 2:
			phoneNumber = input('Enter a number: ')
			contactName = input('Enter the name in the format "First name,LastName".: ')
			if phoneNumber not in contact.items():
				contact.update({contactName:phoneNumber})
				print('Contact successfully saved')
				print('Your updated phonebook is Shown below: ')
				for i, j in contact.items():
					print(i, '->', j)
			else:
				print('That contact already exits in your Phonebook')

		elif entry == 3:
			name = input('Enter the name of the contact details you wish to view: ')
			if name in contact:
				print('The contact is', name, ':', contact[name])
			else:
				print('That contact does not exist! Return to the main menu to enter the contact')

		elif entry == 4:
			name = input('Enter the name of the contact you wish to delete: ')
			if name in contact:
				print('The contact is',name,':',contact[name])
			else:
				print('That contact does not exist! Return to the main menu to enter the contact')
        
			confirm = input('Are you sure you wish to delete this contact? Yes/No: ')
			if confirm.capitalize() == 'Yes':
			#If yes, delete contact from Phonebook
				contact.pop(name,None)
				#Loop through Phonebook and print updated contact list
				for k, v in contact.items():
					print('Your Updated Phonebook is shown below:')
					print(k, '-->', v)
				else:
					print('Return to Main Menu')

		elif entry == 5:
			print('Thanks for using the Phonebook')
			break
		else:
			print('Incorrect Entry!')

phonebook()