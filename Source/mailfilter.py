from datetime import datetime
from imap_tools import MailBox, AND
import keyring
import getpass
import my_rules
import pydoc
import sys
import time

"""
    We want to have an interactive mode and a mode in which the filter
    continuously runs without human interaction.

    - Use the interactive mode to be certain that you configure the filter correctly to handle all mails.
    - Use the non-interactive mode as a service on the raspberry pi of your choice to keep your emails clean.
"""
interactive_session = False
if len(sys.argv) > 1:
    if sys.argv[1] == "--interactive":
        interactive_session = True
        print("Interactive session activated!")


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

while (True):
    print(f"  - {datetime.now()} Accessing {server} / {username}...")

    mailbox = MailBox(server)
    mailbox.login(username, password, initial_folder='INBOX') 

    messages = mailbox.fetch(AND(all=True))

    for message in messages:
        print(f"  - {message.from_} : {message.subject} ...")
        
        targetFolder = my_rules.get_target_folder_for(message)

        if (not interactive_session) and (targetFolder == None):
            text  = "\n"
            text += "I could not find a target folder for this message.:\n"
            text += "\n"
            text += "==================================================================================================\n"
            text += f"From    : {message.from_}\n"
            text += f"Subject : {message.subject}\n"
            text += f"Body    :\n"
            text += "==================================================================================================\n"
            text += message.text
            pydoc.pager(text)
            break
        
        if targetFolder != None:
            print(f"    -=> moving to {targetFolder}...")
            mailbox.move([message.uid], targetFolder)

    mailbox.logout()

    if not interactive_session:
        break

    print(f"Waiting 60 seconds before applying the filter again.")
    time.sleep(60)
