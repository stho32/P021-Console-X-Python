import os
import json
from imap_tools import MailBox, AND
import keyring
import argh

application_id = "mailfilter"

access_data = keyring.get_password(application_id, "configuration")


print(access_data)

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