import json
import sqlite3
import re


# download backup of oc_customer
# rename it to oc_cusomter.txt
# have this file and oc_customer.txt in the same folder
# run 'python3 customer_csv.py'
# emails will be be in emails.csv in the folder the script was ran in
emails = []
w = open("emails.csv", "a+")
w.write("email\n")
with open('oc_customer.txt') as f:
  for row in f:
    split = re.split(r"(^[']+[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+[']$)", row)
    # split = row.split('@')
    email = re.findall(r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", row)
    # print(len(split))
    emails.append(email)

    if len(email) != 0:
      print(email[0])
      w.write(email[0]+"\n")
