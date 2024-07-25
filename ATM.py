import time

def atm_machine():
    # Initial welcome message
    print('Welcome to the Future Bank ATM!')
    print('Please Insert Your Card...')
    time.sleep(3)
    
    # Initialize account details and transaction history
    password = 828776
    balance = 900000
    transaction_history = []
    
    # Set the maximum number of PIN attempts
    attempts = 0
    max_attempts = 3
    
    # PIN verification process
    while attempts < max_attempts:
        pin = int(input("Enter Your Pin: "))
        if pin == password:
            print('PIN Verified. Welcome!')
            break
        else:
            attempts += 1
            remaining_attempts = max_attempts - attempts
            print(f'Invalid Pin. You have {remaining_attempts} attempts left.')
            if remaining_attempts == 0:
                print('Too many failed attempts. Card blocked.')
                return
    
    # Main menu loop
    while True:
        # Display menu options
        print("""
            ********************************
            * 1 == Account Balance Inquiry *
            * 2 == Withdraw                *
            * 3 == Deposit                 *
            * 4 == Change PIN              *
            * 5 == Transaction History     *
            * 6 == Exit                    *
            ********************************
            """)
        
        try:
            # Get user's choice
            option = int(input("Please enter your choice: "))
        except ValueError:
            print('Please Enter a Valid Value')
            continue
        
        # Option 1: Display balance
        if option == 1:
            print(f'Your Balance is Rs.{balance}')
            transaction_history.append("Balance Inquiry")
        
        # Option 2: Withdraw money
        elif option == 2:
            withdraw_amount = int(input('Please Enter withdrawal amount: '))
            if withdraw_amount > balance:
                print('Insufficient Balance')
            else:
                balance -= withdraw_amount
                print(f'Rs.{withdraw_amount} has been debited from your account')
                print(f'Your Updated Balance is Rs.{balance}')
                transaction_history.append(f'Withdrawal: {withdraw_amount}')
        
        # Option 3: Deposit money
        elif option == 3:
            deposit_amount = int(input('Please Enter deposit amount: '))
            balance += deposit_amount
            print(f'Rs.{deposit_amount} has been credited to your account')
            print(f'Your Updated Balance is Rs.{balance}')
            transaction_history.append(f'Deposit: {deposit_amount}')
        
        # Option 4: Change PIN
        elif option == 4:
            old_pin = int(input("Enter Your Old Pin: "))
            if old_pin == password:
                new_pin = int(input("Enter Your New Pin: "))
                confirm_new_pin = int(input("Confirm Your New Pin: "))
                if new_pin == confirm_new_pin:
                    password = new_pin
                    print('Your PIN has been successfully changed.')
                    transaction_history.append("PIN Change")
                else:
                    print('New PIN and Confirm PIN do not match. Please try again.')
            else:
                print('Invalid Old Pin, Please Try Again')
        
        # Option 5: Display transaction history
        elif option == 5:
            print('Transaction History:')
            for transaction in transaction_history:
                print(transaction)
        
        # Option 6: Exit the program
        elif option == 6:
            print('Thank you for using Future Bank ATM. Have a great day!')
            break
        
        # Handle invalid menu option
        else:
            print('Invalid Option. Please try again.')

# Run the ATM machine program
atm_machine()