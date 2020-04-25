import math
import argparse
import sys

# Creating arguments that are to be passed in command line.
parser = argparse.ArgumentParser()
parser.add_argument("--type")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")
parser.add_argument("--payment")
args = vars(parser.parse_args())

type_of_operation = args["type"]

if type_of_operation == "diff":
	"""
		If the operation is based on differentiate payment,
		this branch takes care of that
		"""

	# Allow operation only if the input arguments are present,
	# and are valid i.e not -ve value
	if args["principal"] and args["periods"] and args["interest"]:

		# Just creating some variable to work with
		principal = int(args["principal"])
		periods = int(args["periods"])
		interest = float(args["interest"])

		if principal < 0 or periods < 0 or interest < 0:  # Values cannot be negative
			print("Incorrect parameters!")
			sys.exit()
		else:
			i = interest / (12 * 100)
			total_payment = 0
			for m in range(1, periods + 1):
				D = round(principal / periods + i * (principal - principal * (m - 1) / periods), 2)
				total_payment += math.ceil(D)
				print(f"Month {m}: paid out {math.ceil(D)}")

			overpay = total_payment - principal
			print()
			print(f"Overpayment = {overpay}")
	else:
		print("Incorrect parameters")
		sys.exit()

elif type_of_operation == "annuity":
	"""
	If the operation is based on annuity payment,
	this branch takes care of that
	"""

	# Allow operation only if the input arguments are present,
	# and are valid i.e not -ve value
	if args["principal"] and args["payment"] and args["interest"] and not args["periods"]:
		"""
		If the certain arguments are present, they indicate a certain action.
		So these conditions differentiate the cases
		"""

		# Just creating some variable to work with
		principal = int(args["principal"])
		interest = float(args["interest"])
		payment = int(args["payment"])
		if principal < 0 or payment < 0 or interest < 0:
			print("Incorrect parameters!")
			sys.exit()
		else:
			i = (interest / (12 * 100))
			n = math.ceil(math.log(payment / (payment - i * principal), 1 + i))
			total_payment = n * payment

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
					print(
						f"You need {months} {month_plural if months > 1 else month_singular} to repay this credit!")
			print(f"Overpayment = {total_payment - principal}")

	elif args["periods"] and args["interest"] and args["payment"] and not args["principal"]:
		periods = int(args["periods"])
		interest = float(args["interest"])
		payment = int(args["payment"])
		if periods <= 0 or payment <= 0 or interest <= 0:
			print("Incorrect parameters!")
			sys.exit()
		else:
			i = (interest / (12 * 100))
			annuity = payment
			n = periods
			total_payment = payment * n
			principal = math.floor((annuity / ((i * math.pow((1 + i), n)) / (math.pow(1 + i, n) - 1))))
			print(f"Your credit principal = {principal}!")
			print(f"Overpayment = {total_payment - principal}")

	elif args["periods"] and args["interest"] and args["principal"] and not args["payment"]:
		periods = int(args["periods"])
		interest = float(args["interest"])
		principal = int(args["principal"])
		if periods <= 0 or principal <= 0 or interest <= 0:
			print("Incorrect parameters!")
			sys.exit()
		else:
			i = (interest / (12 * 100))
			n = periods
			annuity = math.ceil(principal * (i * math.pow(1 + i, n)) / (math.pow(1 + i, n) - 1))
			total_payment = n * annuity

			print(f"The payment = {annuity}!")
			print(f"Overpayment = {total_payment - principal}")
	else:
		print("Incorrect parameters")
		sys.exit()

else:
	print("Incorrect parameters")
	sys.exit()