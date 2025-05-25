import csv
import json

# List to store usernames of compromised accounts
compromised_users = []

# Read the CSV file containing usernames and passwords
with open('passwords.csv') as password_file:
    password_csv = csv.DictReader(password_file)  # Use DictReader to access by column name

    for row in password_csv:
        # Extract username and add to compromised list
        compromised_users.append(row['Username'])
# Write the list of compromised users to a text file
with open('compromised_users.txt', 'w') as compromised_user_file:
    for user in compromised_users:
        compromised_user_file.write(user + '\n')

# Write a JSON file to report mission success
with open('boss_message.json', 'w') as boss_message:
    boss_message_dict = {
        'recipient': 'The Boss',
        'message': 'Mission Success'
    }
    json.dump(boss_message_dict, boss_message)
# Write a fake signature banner to a new passwords file (possibly to confuse attackers)
with open('new_passwords.csv', 'w') as new_passwords_obj:
    slash_null_sig = '''
   _  _     ___   __  ____             
  / )( \   / __) /  \(_  _)            
  ) \/ (  ( (_ \(  O ) )(              
  \____/   \___/ \__/ (__)             
   _  _   __    ___  __ _  ____  ____  
  / )( \ / _\  / __)(  / )(  __)(    \ 
  ) __ (/    \( (__  )  (  ) _)  ) D ( 
  \_)(_/\_/\_/ \___)(__\_)(____)(____/ 
          ____  __     __   ____  _  _ 
   ___   / ___)(  )   / _\ / ___)/ )( \\
  (___)  \___ \/ (_/\/    \\___ \) __ (
         (____/\____/\_/\_/(____/\_)(_/
   __ _  _  _  __    __                
  (  ( \/ )( \(  )  (  )               
  /    /) \/ (/ (_/\/ (_/\             
  \_)__)\____/\____/\____/
    '''
    new_passwords_obj.write(slash_null_sig)
