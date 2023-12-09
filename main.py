# from colored import fg, attr, bg
# from todo_functions import add_todo, remove_todo, mark_todo, view_todo

file_name = "list.csv"

try:
  # open the file in read mode
  todo_file = open(file_name, "r")
  todo_file.close()
  print("Storage file active")
  # if it throws error, it means the file doesn't exist
  # if no error, it means the file exists
except FileNotFoundError:
  # Now, we know the file doesn't exist
  # Create the file
  todo_file = open(file_name, "w")
  # We can also insert the first line into the file
  todo_file.write("Information Storage File\n")
  todo_file.close()
  print("In except block")

print(f"{fg('white')}{bg('blue')}Welcome to Information Storage file!{attr('reset')}")

def create_menu():
  print("1. Enter your First Name")
  print("2. Enter your State & Suburb")
  print("3. Enter 3 to Remove Name or State/Suburb")
  print("4. Enter 4 to view Information List")
  print("5. Enter 5 to exit ")
  choice = input("Enter your selection: ")
  return choice

users_choice = ""

while users_choice != "5":
  users_choice = create_menu()
  if (users_choice == "1"):
    add_todo(file_name)
  elif (users_choice == "2"):
    remove_todo(file_name)
  elif (users_choice == "3"):
    mark_todo(file_name)
  elif (users_choice == "4"):
    view_todo(file_name)
  elif (users_choice == "5"):
    continue
  else:
    print("Invalid Input")
    

print("Thank you for using todo list")