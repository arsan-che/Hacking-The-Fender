# Hacking-The-Fender
compromised_user_report.py
# Compromised User Report

This Python script processes a CSV file of usernames and passwords to identify compromised accounts. It outputs:

- A list of compromised users to `compromised_users.txt`
- A mission success message to `boss_message.json`
- A fake password file (`new_passwords.csv`) containing an ASCII "signature" banner to potentially distract attackers

## 📁 Files

- `passwords.csv`: Input file with at least a `Username` column
- `compromised_users.txt`: Output file listing compromised usernames
- `boss_message.json`: Output file with a success message
- `new_passwords.csv`: Output file with an ASCII art signature

## 🛠️ How to Use

1. Place your `passwords.csv` file in the same directory.
2. Run the script:

```bash
python compromised_user_report.py
