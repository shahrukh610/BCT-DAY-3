from prettytable import PrettyTable

l = []

def signIn():
    email=input("Enter your email: ")
    password=input("Enter your password: ")
    n=len(l)
    for i in range(n):
        if l[i]['email']!=email:
            print(l[i])
            print(f"{email} is not registered, please signUp first.")
            return
        else:
            if(l[i]['password']!=password):
                print("Incorrect password.")
                return
            else:
                print("Login successfull.")
                return
            

def signUp():
    database = {}
    email=input("Enter your email: ")
    password=input("Enter your password: ")
    if email.endswith(".com"):
        database["email"] = email
        database["password"] = password
        l.append(database)
        print("Signup successfull.")
        return
    else:
        print("Enter a valid email.")
    

def showAIData():

    myTable = PrettyTable(["Email", "Password"])
    for user in l:
        myTable.add_row([user["email"] , user["password"]])
    print(myTable)

def main():
    while True:
        key=int(input('''\nEnter 1 for signup...
                      \nEnter 2 for signin...
                      \nEnter 3 to exit...
                      \nEnter 4 to show all data '''))
        if(key==3):
            break
        elif(key==1):
            signUp()
        elif(key==2):
            signIn()
        elif(key==4):
            showAIData()
        else:
            print("Please enter a valid parameter.")

if __name__== "__main__":
    main()