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