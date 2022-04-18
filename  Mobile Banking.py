print("""------Welcome------
--------------------
------Mobile BANK------
--------------------""")
def main():
    print("""
    Enter your choice
    1. Create account
    2. Login to your account
    """)
    choice = input("Choice:..")
    if choice == "1":
        print("Enter your account number:")
        accono = input(" ")
        print("create password")
        pwd = input(" ")
        print("Enter your phone number for verification")
        phoneno = input("+2547")
    elif choice =="2":
        print("Enter your password:")
        password = input (" ")
        if "12345" in password:
            print("Correct password")
        elif choice=="2":
            print("incorrect password")
    else:
        exit(1)

main() 

print("""
Mobile Banking
Select your option:
1. Balance Enquiry
2. Payments
3. Send Money
4. Withdraw Cash
5. Buy airtime
6. My account
""")
print("Enter your option:")
choice = input(" ")
if choice =="1":
    print("Your account Balance is")
    print("1200")
elif choice =="2":
    print("""
    Payments
    1. Pay Bills
    2. Buy Goods
    """)
    print("Enter your option")
    choice = input(" ")
    if choice =="1":
        print("Pay Bill")
        print("Enter paybill number")
        paybillno = input (" ")
        print("Amount")
        amount=input(" ")
    elif choice=="2":
        print("Buy Goods")
        print("Enter Till Number")
        tillno = input(" ")
        print("Enter Amount")
        amount = input(" ")
    else:
        exit(1)
elif choice =="3":
    print("Send Money")
    print("Enter phone Number:")
    phoneno = input("+2547")
    print("Enter Amount")
    amount = input(" ")
elif choice=="4":
    print("""
    Withdraw cash
    1. FROM AGENT
    2. FROM ATM
    """)
    print("Enter your option")
    choice = input(" ")
    if choice=="1":
        print("Enter Agent Number:")
        agentno= input(" ")
        print("Enter Amount")
        amount=input(" ")
    elif choice=="2":
        print("Enter ATM Number")
        atmno=input(" ")
    else:
        exit(1)
elif choice=="5":
    print("""
    Buy airtime
    1. My number
    2. Other Number
    """)
    print("Enter your option:")
    choice = input(" ")
    if choice=="1":
        print("Enter Amount")
        amount=input(" ")
    elif choice=="2":
        print("Enter phone number")
        pn=input(" ")
        print("Enter Amount")
        amount=input(" ")
    else:
        exit(1)
elif choice=="6":
    print("""
    My Account
    1. Mini Statement
    2. Account Management
    """)
    choice=input(" ")
    if choice == "1":
        print("""

        """)
    elif choice =="2":
        print("""
        Account Management
        1. Forgot pin
        2. Change pin
        """)
        choice=input(" ")
        if choice == "1":
            print("Enter your ID")
            id= input(" ")
        elif choice =="2":
            print("Enter your new pin")
            np=input(" ")
            print("Confirm your new pin")
            cpin=input(" ")
        else:
            exit(1)
    else:
        exit(1)
else:
    exit(1)
    I

        





     







      
