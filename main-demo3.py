from module import  emailprocess, printMsg

def main():
    emails = ['thangquangloi21@gmail.com', 'vianhthuy@gmail.com', 'thangquangthang@dev.com']
    for email in emails:
        email_username, email_domain = emailprocess(email)
        printMsg(email_username, email_domain)
if __name__ == "__main__":
    main()