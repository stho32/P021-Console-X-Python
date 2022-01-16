from email.header import decode_header
import os
import json
from imap_tools import MailBox, AND
import getpass

config_file = "./Source/config.json"

if os.path.isfile("./Source/config.json"):
    with open('./Source/config.json') as f:
        data = json.load(f)
        server = data["server"]
        username = data["username"]
        password = getpass.getpass("password: ")
else :
    server = input("server: ")
    username = input("username: ")
    password = getpass.getpass("password: ")

# get list of email subjects from INBOX folder
with MailBox(server).login(username, password) as mailbox:
    subjects = [msg.subject for msg in mailbox.fetch()]

# get list of email subjects from INBOX folder - equivalent verbose version
mailbox = MailBox(server)
mailbox.login(username, password, initial_folder='INBOX')  # or mailbox.folder.set instead 3d arg
subjects = [msg.subject for msg in mailbox.fetch(AND(all=True))]
print(subjects)
mailbox.logout()