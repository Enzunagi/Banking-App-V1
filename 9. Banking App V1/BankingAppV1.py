#Python Banking Program
# 3 Key sections: Show Balance, Deposit and Withdraw

#Full requirements:
    #Project requirements:
    #Taking user input for banking options.
    #Handle invalid input with else statements
    #functions to handle balance display and deposit.
    #Updating the deposit function to handle negative deposits and returning a valid amount
    #Validate user input and handle withdrawal process
    #Enclosing the main portion of code within a function for better readability and maintainability.
    #Pass balance to withdraw and show functions

#defining the global functions and their corresponding local variables
def show_balance(balance):
    print("************")
    print(f"Your balance is £{balance: .2f}")
    print("************")

def deposit():
    print("************")
    amount = float(input("Enter an amount to be deposited: "))
    print("************")
    if amount < 0:
        print("************")
        print("that's not a valid amount")
        print("************")
        return 0
    else:
        return amount

def withdraw(balance):
    print("************")
    amount = float(input("Enter an amount to be withdrawn: "))
    print("************")

    if amount > balance:
        print("************")
        print("Insufficient funds")
        print("************")
        return 0
    elif amount < 0:
        print("************")
        print("Amount must be greater than 0")
        print("************")
        return 0
    else:
        return amount

#setting the variables under the main function

def main():
    balance = 0
    is_running = True

    #While loop to keep the program running
    while is_running:

       print("************")
       print("   Welcome to Enzu's Bank   ")
       print("************")
       print("1.Show Balance")
       print("2.Deposit")
       print("3.Withdraw")
       print("4.Exit")
       print("************")
       choice = input("Enter your choice (1-4):")

       if choice == '1':
           show_balance(balance)
       elif choice == '2':
           balance += deposit()
       elif choice == '3':
           balance -= withdraw(balance)
       elif choice == '4':
           is_running = False

     #handling invalid input
       else:
           print("************")
           print("That is not a valid choice")
           print("************")
    # message for exiting the while loop/ program
    print("************")
    print("Thank you! Have a nice day")
    print("************")

if __name__=='__main__':
    main()