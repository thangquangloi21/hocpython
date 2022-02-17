def emailprocess(email):
    #cat den chu @
    email_username = email[0:email.index("@")]
    email_domain = email[email.index("@")+1:]
    #print(f"User name is {email_username}")
    return [email_username, email_domain]
def printMsg(email_username, email_domain):
    print(f"User name is {email_username}")
    print(f"domain name is {email_domain}")
def main():
    email = input("Please enter your email address: ").strip()
    email_username, email_domain = emailprocess(email)
    printMsg(email_username, email_domain)
if __name__ == "__main__":
    main()