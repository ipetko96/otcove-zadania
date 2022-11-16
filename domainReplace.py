import csv
import re

base_path = "./data"
regex_pattern = r"@abc\.edu"

with open(f"{base_path}/user_emails.csv") as read_file:
    csv_reader = csv.reader(read_file)
    for email in csv_reader:
        email[1] = re.sub(regex_pattern, "@xyz.com", email[1])
        with open(f"{base_path}/output.csv", "a", newline="") as write_file:
            csv_writer = csv.writer(write_file, delimiter=",")
            csv_writer.writerow(email)
