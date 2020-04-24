import math
import sys

args = sys.argv

# print("""What do you want to calculate?
# type "n" - for count of months,
# type "a" - for annuity monthly payment,
# type "p" - for credit principal:
# """)

if len(args) == 5:
	
# choice = input()
if choice == "n":

	principal = int(input("Enter credit principal:\n"))
	monthly_payment = float(input("Enter monthly payment:\n"))
	credit_interest = float(input("Enter credit interest:\n"))

	i = (credit_interest / (12 * 100))
	n = math.ceil(math.log(monthly_payment / (monthly_payment - i * principal), 1 + i))

	months = n
	years = math.floor(months / 12)
	months = months % 12

	month_singular = "month"
	month_plural = "months"
	year_singular = "year"
	year_plural = "years"

	if years > 0:
		if months > 0:
			print(f"You need {years} {year_plural if years > 1 else year_singular} "
				  + f"and {months} {month_plural if months > 1 else month_singular} to repay this credit!")
		else:
			print(f"You need {years} {year_plural if years > 1 else year_singular} to repay this credit!")
	else:
		if months > 0:
			print(f"You need {months} {month_plural if months > 1 else month_singular} to repay this credit!")

elif choice == "a":
	principal = int(input("Enter credit principal:\n"))
	n = int(input("Enter count of periods:\n"))
	credit_interest = float(input("Enter credit interest:\n"))

	i = (credit_interest / (12 * 100))
	# n = math.ceil(math.log(monthly_payment / (monthly_payment - i * principal), 1 + i))

	annuity = math.ceil(principal * (i * math.pow(1+i, n)) / (math.pow(1+i, n) - 1))

	print(f"Your annuity payment = {annuity}!")
elif choice == "p":
	monthly_payment = float(input("Enter monthly payment:\n"))
	n = int(input("Enter count of periods:\n"))
	credit_interest = float(input("Enter credit interest:\n"))

	i = (credit_interest / (12 * 100))
	annuity = monthly_payment

	principal = round((annuity / ((i * math.pow((1+i), n)) / (math.pow(1+i, n) - 1 ))))

	print(f"Your credit principal = {principal}!")
