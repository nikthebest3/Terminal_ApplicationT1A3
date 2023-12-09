import csv

def add_name(file_name):
  print("Enter Name: ")
  # Ask the user to Enter their First Name
  add_name = input("Enter your First Name: ")
    # Open file - list.csv
  with open(file_name, "a") as f:
      writer = csv.writer(f)
      # Insert values - title = user entered
      writer.writerow([add_name])

def add_suburb(file_name):
  print("Enter Suburb & Town")
  # Ask user to enter Suburb & Town where they are from.
  add_suburb = input("Enter your Suburb & Town: ")
    # Open file - list.csv
  with open(file_name, "a") as f:
      writer = csv.writer(f)
      # Insert values - title = user entered
      writer.writerow([add_suburb])

def remove_info(file_name):
  print("Remove Info")
  remove_info = input("Enter the Name/Suburb you want to remove: ")
  info_lists = []
  with open(file_name, "r") as f:
    reader = csv.reader(f)
    for row in reader:
      if (add_suburb != row[0]):
        info_lists.append(row)
  with open(file_name, "w") as f:
    writer = csv.writer(f)
    writer.writerows(info_lists)

def view_info(file_name):
  print("View Info")
  with open(file_name, "r") as f:
    reader = csv.reader(f)
    reader.__next__()
    for row in reader:
      # # row = ["Todo 1", "False"]
      # if (row[1] == "True"):
        print({row[0]})
      # else:
      #   print(f"Todo: {row[0]} is not complete")