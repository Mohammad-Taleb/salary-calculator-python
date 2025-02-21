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
    total_electricity = 0
    if pay_electricity < 0:
        print("Payment must be greater than zero")
        return 0
    elif pay_electricity > salary:
        print("Insufficient funds")
        return 0
    else:
        total_electricity += (pay_electricity * salary)/100
    return total_electricity



months = ['january', 'february', 'march', 'april', 'may',
          'june', 'july', 'august', 'september', 'october', 'november', 'december']

total_expenses = 0
total_savings = 0
yearly_expenses = 0
spendings = 0

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
            total_savings += deposit_saving()
            spendings += total_savings

        elif user_choice == '2':
            pay_rent = float(input("Enter a percentage to pay your rent: "))
            total_expenses += monthly_rent()
            spendings += total_expenses

        elif user_choice == '3':
            pay_electricity = float(input("Enter a percentage to pay your bill: "))
            total_expenses += monthly_electricity()
            spendings += total_expenses

        elif user_choice == '4':
            print(f"Your total savings for {month_name} is ${total_savings:.2f}")
            
        elif user_choice == '5':
          remainder = (salary) - spendings
          print(f"Your remaining salary for {month_name} is ${remainder:.2f}")
        elif user_choice == '6':
          print(f"Your yearly estimation is ${yearly_expenses + (monthly_rent() + monthly_electricity())*12:.2f}")
        elif user_choice == '7':
            print(f"Your total expenses for {month_name} is ${total_expenses:.2f}") 
        elif user_choice == '0':
            print()
            print("HAVE A NICE DAY <3")
            print(f"Your salary would look like this {salary**2:.2f}")
            print("if you worked TWO times harder 😉")
            break
        else:
            print()
            print("Enter a valid choice")
            print(f"Your salary would look like this {salary**2:.2f}")
            print("if you worked TWO times harder 😉")
        continue