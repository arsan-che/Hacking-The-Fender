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
