import os
import json
from imap_tools import MailBox, AND
import keyring
import getpass

application_id = "mailfilter"

access_data = keyring.get_password(application_id, "configuration")

if access_data == None:
    server = input("Server: ")
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    combined = server + "|" + username + "|" + password
    keyring.set_password(application_id, "configuration", combined)
    print("Configuration data saved in keyring. Restart to run.")
    exit()

splitted_configuration = access_data.split("|")
server = splitted_configuration[0]
username = splitted_configuration[1]
password = splitted_configuration[2]

print(f"  - Accessing {server} / {username}...")

# server = data["server"]
# username = data["username"]
# password = getpass.getpass("password: ")


# get list of email subjects from INBOX folder - equivalent verbose version
# mailbox = MailBox(server)
# mailbox.login(username, password, initial_folder='INBOX')  # or mailbox.folder.set instead 3d arg

# messages = mailbox.fetch(AND(all=True))

# for message in messages:
#     print(f"- {message.from_} : {message.subject}")

#     if not message.from_:
#         print("   -> this is spam, moving it")
#         mailbox.move([message.uid], "INBOX/MySpam")

# mailbox.logout()

