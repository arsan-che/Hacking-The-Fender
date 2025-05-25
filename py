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
