# Welcome in Nova's Bank.



#This block is for creating new accounts and saving data into files...
def account():
    print("So you come here to open an account. Cool..")
    name = input("Enter your name :")
    credit = input("And now enter a 4 digits code :")
    print("\n< ! WARNING | NEVER FORGET THAT CODE OTHERWISE YOU CAN'T ACCESS YOUR ACCOUNT THEN ! > \n")
    print("I would suggest you to write it somewhere because human brain is not for remembering stupid things\n.")
    with open("info.txt","a+") as t:
        t.write(str(name)+" "+str(credit)+"\n")
    with open("amount.txt","a+") as a:
        a.write(str(name)+" "+str(1000000)+"\n")
    print("Account created Successfully !\n")


#This is the block of code which is responsible for paying your i dont know what.
def payment(total):

    #Checking if there are any account in bank or not
    with open("info.txt","r") as r:
        if len(r.read()) < 1:
            print("There is no accounts opened in this bank yet..\nYou can be the first.\n")
            account()

    #Opening a txt file and converting it to dictionary. Btw that file contains username and credit card code
    with open("info.txt","r") as r:
        code_num = {}
        for line in r:
            name,code = line.split(" ")
            code_num[name] = int(code)

    #Doing same with the txt file which contains username and their available cash
    with open("amount.txt","r") as r:
        cash = {}
        for line in r:
            name,amount = line.split(" ")
            cash[name] = int(amount)
    t40 = list(code_num.keys()) #Thats a list containing all users name of my bank.    
    name = input("Enter your name to detect your account :")

    def act(cash,total,name):
        cash[name] = int(cash[name]) - int(total)  #Total money - items cost user bought
        print("Done.")
        print("Now your account have $"+str(cash[name])+" left.")
        print("And no thank you or something for using our service because you are using it for your convenience. - Noah")
        nameC = list(cash.keys()) #List of all user names
        cashC = list(cash.values()) #List of their money
        #Now editing the txt file which stores user's available money data because why not ;)
        with open("amount.txt","w") as w:
            counter = 0
            for i in nameC:
                w.write(str(i)+" "+str(cashC[counter])+"\n")
                counter += 1

    if name in t40:  #Checking if the has an account or not
        print("Access Granted !\nWelcome",name)
        cre_code = input("Can you please enter your four digit code :")

        if int(cre_code) == int(code_num[name]): #Now checking if the code is correct or not
            if int(cash[name]) < total:
                print("\nYou are broke. You can't afford these items. You need more MONEY $$$\n") 
            else:
                act(cash,total,name)
        else:
            print("You entered wrong code so now you are done.\nGoodbye :) ")
    else:
        print("You don't have an account.")
        would = input("<C | Create an account > <Any other key | EXIT > :")
        if would in ['c','C']:
            account()
            print("Now you can pay for your items...\n")
            payment(total)

payment(0)