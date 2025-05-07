
#All quality attributes (1-3)
from logging import NullHandler
import random

rand_temp = random.randint(30,100)
rand_co = random.randint(0,50)
rand_IP = f"{random.randint(1,200)}.{random.randint(1,200)}.1. {random.randint(1,200)}"

#HOME
class BusMonitorApp:
	def __init__(self):
		self.menu_stack = []

	def run(self):
		self.show_welcome()
		while True:
			self.show_main_menu()

	def show_welcome(self):
		#Inclusivity heuristic #1: Explain benefits
		print("Welcome to the Bus Monitor App \n"
			  "Current Features: \n"
			  "Connect to your local Raspberry Pi network (no Internet required) \n"
			"Get real time data from inside and outside the bus \n"
			"Control all remotely connected functionality \n"
			"Press ENTER to begin \n")
		user_input = input()
		if user_input == "":
			return
		else:
			print("Try again")
			self.show_welcome()


	def show_main_menu(self):

		print("MAIN MENU \n"
			  "Type the option number and press ENTER: \n"
	  			"#1 INSIDE BUS \n"
	  			"#2 OUTSIDE BUS \n"
			  	"#3 CONNECT \n"
	  			"#4 EXIT \n"
			  	"#5 HELP - WHAT DO THESE OPTIONS MEAN? \n "
			  	"#6 LIST ALL OPTIONS\n"
			  #IH #2 included in note
			  "Note: All features for Inside and Outside bus require a connection to the Raspberry Pi. \n"
			  "If you are unsure if you are connected, please select #3 CONNECT \n")
		user_input = input()
		if user_input == "1":
			self.menu_stack.append(self.show_main_menu)
			self.inside_bus_menu()

		elif user_input == "2":
			self.menu_stack.append(self.show_main_menu)
			self.outside_menu()

		elif user_input == "3":
			self.menu_stack.append(self.show_main_menu)
			self.connect_menu()

		elif user_input == "4":
			print("Now exiting the program! Goodbye!")
			exit()

		elif user_input == "5":
			#IH 3
			self.menu_stack.append(self.show_main_menu)
			print("#1 INSIDE BUS: Contains all controls and readings from within the bus. \n"
				  "This includes temperature monitoring, CO monitoring, and temperature adjustments\n"
	  			"#2 OUTSIDE BUS: Contains all readings outside of the bus, such as temperature. \n"
			  	"#3 CONNECT: Provides functionality to connect to the bus LAN/Raspberry Pi, which is required to gather data or utilize controls  \n"
	  			"#4 EXIT: Exits ths program"
				  #IH 7 - Another way to see the options if you cant find them
				"#6 LIST ALL OPTIONS - provides a full list for all options in the program\n")
		elif user_input == "6":
			self.show_all_menu_options()
		else:
			print("Try again - not a valid option")


	def inside_bus_menu(self):
		#IH 4 - Consistent numbering throughout
		#IH 5 - go back option always available
		print("INSIDE BUS MENU \n"
			  "Type an option number and press ENTER: \n"
			  "#1 TEMPERATURE \n"
			  "#2 CARBON MONOXIDE \n"
			  "#3 GO BACK \n"
			  "#4 EXIT PROGRAM \n"
			  "#5 HELP \n"
			  "#0 MAIN MENU \n")
		user_input = input()
		if user_input == "1":
			self.menu_stack.append(self.inside_bus_menu)
			self.inside_temperature_menu()
		elif user_input == "2":
			self.menu_stack.append(self.inside_bus_menu)
			self.co_menu()
		elif user_input == "3":
			self.go_back()
		elif user_input == "4":
			print("Now exiting the program! Goodbye!")
			exit()

		elif user_input == "5":
			#IH 3
			self.menu_stack.append(self.inside_bus_menu)
			print("#1 TEMPERATURE - contains options to see what the current bus air temperature is \n"
				  "OR options to adjust the AC/Heat \n"
			  "#2 CARBON MONOXIDE -check the current CO readings to ensure they are within limits. \n"
			  "#3 GO BACK - go back to the previous menu \n"
			  "#4 EXIT PROGRAM - exit the program \n")

		elif user_input =="0":
			self.show_main_menu()

		else:
			print("Try again - not a valid option")


	def inside_temperature_menu(self):
		print("TEMPERATURE MENU \n"
					  "Select and option and press ENTER: \n"
					  "#1 READINGS \n"
					  "#2 SET \n"
					  "#3 GO BACK \n"
					  "#4 EXIT PROGRAM \n"
					  "#5 HELP \n"
			  		"#0 MAIN MENU \n")
		next_input = input()
		if next_input == "1":
			self.menu_stack.append(self.inside_temperature_menu)
			print(f"Current ACTUAL temperature reading is {rand_temp} degrees F\n"
				  f"Current temperature SETTING is {rand_temp} degrees F\n"
				  f"Please note: Temp setting will not necessarily align with current reading - this is what temp is set to\n ")
			self.inside_temperature_menu()
		elif next_input == "2":
			self.menu_stack.append(self.inside_temperature_menu)
			print("ARE YOU SURE YOU WANT TO CHANGE THE TEMP SETTING? 1 = YES 2 = NO (return to menu) \n")
			next_input = input()
			if next_input == "1":
				print("Set new temp value (range 58-75 degrees F) and press ENTER\n")
				new_temp = input()

				try:
					new_temp = int(new_temp)
					if 58 <= new_temp <= 75:
						print(f"New temperature set to {new_temp} degrees F \n"
						 	 #IH #2 also included here
						  	f"Please allow up to 1 hour for temperature to adjust to new set temperature \n"
						  	f"If you are not satisified with this temp setting, enter 1 and ENTER to go back to temp menu \n"
						  	f"If you want to go back to the main menu, enter 0 and ENTER")
						next_input = input()
						if next_input == "1":
							self.inside_temperature_menu()
						elif next_input == "0":
							self.show_main_menu()
						else:
							print("Invalid option, please try again")
					else:
						print("Try again. Invalid temp value")
						self.inside_temperature_menu()
				except ValueError:
					print("Please enter a valid number.")
					self.inside_temperature_menu()
			elif next_input == "0":
				self.inside_temperature_menu()
			self.inside_temperature_menu()
		elif user_input == "3":
			self.go_back()
		elif user_input == "4":
			print("Now exiting the program! Goodbye!")
			exit()
		elif user_input == "5":
			self.menu_stack.append(self.inside_temperature_menu)
			print("#1 READINGS - Gather temperature data (current temp setting AND actual reading) \n"
				"#2 SET -Adjust the current temperature \n"
				"#3 GO BACK - Go back to the previous menu \n"
				"#4 EXIT PROGRAM - Exit the program \n")
		elif user_input =="0":
			self.show_main_menu()
		else:
			print("Try again - not a valid option")

	def co_menu(self):
		#IH 5 - main menu option always the same
		print("CO MENU \n"
			  "Select and option and press ENTER: \n"
			  "#1 READINGS \n"
			  "#2 GO BACK \n"
			  "#3 EXIT PROGRAM \n"
			  "#4 HELP \n"
			  "#0 MAIN MENU \n")
		user_input = input()
		if user_input == "1":
			self.menu_stack.append(self.co_menu)
			print(f"Current CO is {rand_co} PPM")
			self.co_menu()
		elif user_input == "2":
			self.go_back()
		elif user_input == "3":
			print("Now exiting the program! Goodbye!")
			exit()
		elif user_input == "4":
			self.menu_stack.append(self.co_menu)
			print("#1 READINGS - Current carbon monoxide readings in PPM \n"
			  "#2 GO BACK - Go back to the previous menu \n"
			  "#3 EXIT PROGRAM - Exit the program \n")
		elif user_input == "0":
			self.show_main_menu()
		else:
			print("Try again - not a valid option")

	def outside_menu(self):
		print("OUTSIDE BUS MENU \n"
			  "Type an option number and press ENTER: \n\n"
			  "#1 TEMPERATURE \n"
			  "#2 GO BACK \n"
			  "#3 EXIT PROGRAM \n"
			  "#4 HELP \n"
			  "#0 MAIN MENU \n")
		user_input = input()
		if user_input == "1":
			self.menu_stack.append(self.outside_menu)
			self.outside_temp_menu()
		elif user_input == "2":
			self.go_back()
		elif user_input == "3":
			print("Now exiting the program! Goodbye!")
			exit()
		elif user_input == "4":
			#IH3
			self.menu_stack.append(self.outside_menu)
			print("#1 TEMPERATURE - Options related to outside temperature/weather \n"
			  "#2 GO BACK - go to the previous menu \n"
			  "#3 EXIT PROGRAM - exit the program \n")

		elif user_input =="0":
			self.show_main_menu()

		else:
			print("Try again - not a valid option")


	def go_back(self):
		if self.menu_stack:
			previous_menu = self.menu_stack.pop()
			previous_menu()
		else:
			print("No previous menu. Returning to main menu")
			self.show_main_menu()

	def outside_temp_menu(self):
		print("OUTSIDE TEMPERATURE MENU \n"
			  "Select and option and press ENTER: \n"
			  "#1 READINGS \n"
			  "#2 GO BACK \n"
			  "#3 EXIT PROGRAM \n"
			  "#4 HELP \n"
			  "#0 MAIN MENU \n")
		user_input = input()
		if user_input == "1":
			self.menu_stack.append(self.outside_temp_menu)
			print(f"Current temperature is {rand_temp} degrees F")

		elif user_input == "2":
			self.go_back()
		elif user_input == "3":
			print("Now exiting the program! Goodbye!")
			exit()

		elif user_input == "4":
			self.menu_stack.append(self.outside_temp_menu)
			#IH3
			print("#1 READINGS - Outside temp current readings \n"
			  "#2 GO BACK - go to the previous menu \n"
			  "#3 EXIT PROGRAM -exit the program \n")

		elif user_input =="0":
			self.show_main_menu()

		else:
			print("Try again - not a valid option")

	def connect_menu(self):
		print("CONNECTION MENU \n"
			  "Select and option and press ENTER: \n"
			  "#1 Wireless Connect to Raspberry Pi Network \n"
			  "#2 Check network connection \n"
			  "#3 Disconnect from Network \n"
			  "#4 GO BACK \n"
			  "#5 EXIT PROGRAM \n"
			  "#0 MAIN MENU \n"
			  "#6 HELP \n")

		user_input = input()
		#IH6
		if user_input == "1":
			self.menu_stack.append(self.connect_menu)
			print("Welcome to the Raspberry Pi connection Wizard"
				  "Make sure your Raspberry Pi is powered on\n"
				  "Once confirmed, enter the Raspberry Pi's IP address and press ENTER")
			user_input = input()
			if user_input == "":
				print(f"Attempting to connect to {rand_IP}\n"
				  "You're now connected tot the Raspberry Pi Bus Network!\n"
				  "Press ENTER to return to MAIN menu \n"
				  "Press 1 to go back\n")

			if user_input == "1":
				self.go_back()


			else:
				self.show_main_menu()

		elif user_input == "2":
			self.menu_stack.append(self.connect_menu)
			print("You are currently CONNECTED to the Raspberry Pi network!\n"
				  f"Raspberry pi IP is {rand_IP}\n")
		elif user_input =="3":
			self.menu_stack.append(self.connect_menu)
			#IH 8
			print("WARNING: PROCEEDING WILL DISCONNECT YOU FROM THE RASPBERRY PI LAN.\n"
				  "ARE YOU SURE YOU WANT TO DO THIS (Y=1/N=2)?\n")
			user_input = input()
			if user_input == "1":
				print("You have confirmed that you want to disconnect from the Raspberry Pi LAN \n"
					  "Press 1 to disconnect \n"
					  "Press 0 to go back to the Connect menu \n")
				user_input = input()
				if user_input == "1":
					print("You are now DISCONNECTED from the Raspberry Pi network.")
				elif user_input == "0":
					self.connect_menu()
			if user_input == "2":
				self.connect_menu()

		elif user_input == "4":
			self.go_back()
		elif user_input == "5":
			print("Now exiting the program! Goodbye!")
			exit()

		elif user_input == "6":
			#IH 3
			#IH 6
			print("#1 Connect to Raspberry Pi Network - This wizard will guide you through setting up your wireless connection \n"
				  " with the Raspberry PI. This connection is REQUIRED to pull all data readings and perform any controls, such as temp adjustments \n"
			  "#2 Check network connection - Check if you are currently connected to the Raspberry Pi LAN \n"
			  "#3 GO BACK - Go to the previous menu \n"
			  "#4 EXIT PROGRAM - Exit the program \n"
				  "DISCONNECT - Only use as needed- will disconnect from the Raspberry Pi LAN and will require reconnection")
		elif user_input =="0":
			self.show_main_menu()
		else:
			print("Try again - not a valid option")

	def show_all_menu_options(self):
		print("ALL MENU OPTIONS \n"
			  "#1 -INSIDE BUS TEMPERATURE (SET AND READ) \n"
			  "#2 -OUTSIDE BUS TEMPERATURE (READ) \n"
			  "#3 -INSIDE BUS CARBON MONOXIDE \n"
			  "#4 -WIRELESS CONNECTION \n"
			  "#5 - MAIN MENU \n"
			  "#6 - EXIT PROGRAM \n")

		user_input = input()
		if user_input == "1":
			self.inside_temperature_menu()
		elif user_input == "2":
			self.outside_temp_menu()
		elif user_input == "3":
			self.co_menu()
		elif user_input == "4":
			self.connect_menu()
		elif user_input == "5":
			self.show_main_menu()
		elif user_input == "6":
			exit()






if __name__ == "__main__":
	app = BusMonitorApp()
	app.run()


# ●	Given a temperature_inside file exists with temperature values,
# when a request is received to return the values,
# then the service returns all the temperature_inside values as float



# ●	Given a temperature_inside file exists with temperature values,
# when a temperature value changes > 5 degrees,
# then the service returns the updated temperature_inside values as float

# ●	Given a temperature_inside file exists with temperature values,
# when a value goes out of range,
# then the service returns the temperature inside out of range alert.
