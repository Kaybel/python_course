#this is the first task but i do it in collab, need to do some changes for make some test.

def create_user(data):
  user_data = {
      'user': input('please digit your username: '),
      'password': input('please digit your password: ')
  }
  existing_usernames = [user['user'] for user in data]
  if user_data['user'] in existing_usernames:
    print(f"The username '{user_data['user']}' already exists. Please choose a different username.")
  else:
    data.append(user_data)
    print(f"User '{user_data['user']}' registered successfully.")


def read_data(data):
  if not data:
    print("you dont have any data to show")
  else:
    print("those are all the users and passwords saved until now:")
    for user_data in data:
      print(f"this user: << {user_data['user']} >> use this password: << {user_data['password']} >>")


def validate_user(data):
  if not data:
    print("you dont have any data to validate, please, use the function create_user first.")
  else:
    user_name = input('please digit your username: ')
    for user_data in data:
            if user_data['user'] == user_name:
                user_password = input('please digit your password: ')
                if user_data['password'] == user_password:
                    print("you are logged in")
                    return
                else:
                    print("The password does not match.")
                    return
    print("the username does not exists.")


def export_data(data):
  if not data:
    print("you dont have any data to export, please, use the function create_user first.")
  else:
    filename = input('you can export your data now. please give a name to your file without the extension: ')
    filename = filename.strip()
    filename= filename.replace(' ', '_')
    if '.txt' not in filename:
      filename = filename + '.txt'
    with open(filename, 'w') as file:
      file.write("those are all the users and passwords saved until now: \n \n")
      for user_data in data:
        file.write(f"this user: << {user_data['user']} >> use this password: << {user_data['password']} >> \n")
    print(f"all the data was saved in the file named: << '{filename}' >>")

user_data_list = []
