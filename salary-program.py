def deposit_saving():
    amount_deposited = 0
    if deposit < 0:
        print("Deposited amount must be greater than zero")
        return 0
    elif deposit > salary:
        print("Insufficient funds")
        return 0
    else:
        amount_deposited += (deposit * salary)/100
    return amount_deposited


def monthly_rent():
    total_rent = 0
    if pay_rent < 0:
        print("Payment must be greater be than zero")
        return 0
    elif pay_rent > salary:
        print("Insufficient funds")
        return 0
    else:
        total_rent += (pay_rent * salary)/100
    return total_rent



def monthly_electricity():
    total_rent = 0
    if pay_rent < 0:
        print("Payment must be greater be than zero")
        return 0
    elif pay_rent > salary:
        print("Insufficient funds")
        return 0
    else:
        total_rent += (pay_rent * salary)/100
    return total_rent



months = ['january', 'february', 'march', 'april', 'may',
          'june', 'july', 'august', 'september', 'october', 'november', 'december']


salary = float(input("Enter your salary in $: "))
month_name = input("Enter the name of the month: ").lower()

if salary <= 0:
    print("Enter a valid salary")
elif month_name not in months:
    print("Enter a valid month name")
else:
   while True:
        print()
        print("********************************************************************")
        print("CHOOSE A NUMBER TO EXECUTE ONE OF THE CHOICES")
        print("1- TO DEPOSIT TO YOUR SAVINGS")
        print("2- TO PAY THE RENT")
        print("3- TO PAY THE ELECTRICITY BILL")
        print("4- TO CHECK YOUR TOTAL SAVINGS")
        print("5- TO CHECK THE REMAINDER OF THE SALARY (WALLET)")
        print("6- TO CHECK THE YEARLY ESTIMATION COST FOR THE RENT AND ELECTRICITY")
        print("7- T0 CHECK YOUR TOTAL EXPENSES")
        print("0- TO STOP THE PROGRAM")
        print("*********************************************************************")
        print()

        user_choice = input("Enter a number: ")

        if user_choice == '1':
            deposit = float(input("Enter a percentage to add to your savings: "))
        elif user_choice == '2':
            pay_rent = float(input("Enter a percentage to pay your rent: "))
        elif user_choice == '3':
            pay_electricity = float(input("Enter a percentage to pay your bill: "))
        