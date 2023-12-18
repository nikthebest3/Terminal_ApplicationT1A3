from colored import fg, attr, bg
from info_functions import add_name, add_suburb, remove_info, view_info

file_name = "list.csv"

try:
  # open the file in read mode
  info_file = open(file_name, "r")
  info_file.close()
  print("Storage file active")
  # If the csv file doesn't exist, it will create one
except FileNotFoundError:
  # Now, we know the file doesn't exist
  # Create the file
  info_file = open(file_name, "w")
  # We can also insert the first line into the file
  info_file.write("Information Storage File\n")
  info_file.close()
  print("Storage File Active")
print(f"{fg('white')}{bg('blue')}Welcome to Information Storage file!{attr('reset')}")
print(f"{fg('white')}{bg('red')}Do NOT share this Information with the public!{attr('reset')}")

def create_menu():
  print("1. Enter your First Name ")
  print("2. Enter your State & Suburb ")
  print("3. Enter 3 to confirm to Delete all information ")
  print("4. Enter 4 to view Information List ")
  print("5. Enter 5 to exit the Program ")
  choice = input("Enter your selection: ")
  return choice

users_choice = ""

while users_choice != "5":
  users_choice = create_menu()
  if (users_choice == "1"):
    add_name(file_name)
  elif (users_choice == "2"):
    add_suburb(file_name)
  elif (users_choice == "3"):
    remove_info(file_name)
  elif (users_choice == "4"):
    view_info(file_name)
  elif (users_choice == "5"):
    continue
  else:
    print(f"{fg('white')}{bg('blue')}Not a valid Input, Please try again!{attr('reset')}")
    

print(f"{fg('white')}{bg('red')}Do NOT share this Information with the public!{attr('reset')}")
print(f"{fg('white')}{bg('sky_blue_3')}Thank you for using Info Storage, Have a nice day!{attr('reset')}")