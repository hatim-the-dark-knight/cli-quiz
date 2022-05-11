from server import add_question, quiz

def User ():
    print ("Logged in as User")
    name = input ("\nEnter your Name-> ")
    while (1):
        ans = input ("\nDo you want to take the quiz? (Y/N) -> ")
        if (ans == 'Y' or ans == 'y'):
            quiz (name)
        else:
            return


def Admin ():
    passwd = "admin"
    pwd = input ("\nPassword-> ")
    if (pwd != passwd):
        print ("Invalid Password")
        return
    else: 
        print ("Logged in as Admin")
    while (1):
        ans = input ("\nDo you want to add a question? (Y/N) -> ")
        if (ans == 'Y' or ans == 'y'):
            add_question ()
        else:
            return


def main ():
    print ("A CLI quiz!\n\nLogin as \n(1) Admin\n(2) User")
    choice = input ("\nEnter your choice-> ")
    if (choice == str (1)):
        Admin ()
    elif (choice == str (2)):
        User ()
    else:
        print ("Invalid Choice!")


if __name__ =="__main__":
    main ()