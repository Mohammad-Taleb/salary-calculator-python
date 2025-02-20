def deposit_saving():
  pass


def monthly_rent():
  pass


def monthly_electricity():
  pass


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