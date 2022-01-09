import imaplib
import time

server = input("server: ")
username = input("username: ")
password = input("password: ")

################ IMAP SSL ##############################
start = time.time()
try:
    imap_ssl = imaplib.IMAP4_SSL(host=server, port=imaplib.IMAP4_SSL_PORT)
except Exception as e:
    print("ErrorType : {}, Error : {}".format(type(e).__name__, e))
    imap_ssl = None

print("Connection Object : {}".format(imap_ssl))
print("Total Time Taken  : {:,.2f} Seconds\n".format(time.time() - start))

############### Login to Mailbox ######################
print("Logging into mailbox...")
try:
    resp_code, response = imap_ssl.login(username, password)
except Exception as e:
    print("ErrorType : {}, Error : {}".format(type(e).__name__, e))
    resp_code, response = None, None

print("Response Code : {}".format(resp_code))
print("Response      : {}\n".format(response[0].decode()))

############### Logout of Mailbox ######################
print("\nLogging Out....")
try:
    resp_code, response = imap_ssl.logout()
except Exception as e:
    print("ErrorType : {}, Error : {}".format(type(e).__name__, e))
    resp_code, response = None, None

print("Response Code : {}".format(resp_code))
print("Response      : {}".format(response[0].decode()))