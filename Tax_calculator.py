user_name = input("Enter your name : \n")
user_age = int(input("Enter your age : \n"))
user_income = int(input("Enter your total taxable income : \n"))
tax_regime = input("Enter 'New' for new tax regime u/s 115BAC /"
                   "Enter 'Old' for old tax regime \n")

def tax_calculator():
    tax_liability = 0
    if tax_regime == "Old":
        if user_age in range(0,61):
            if user_income <= 250000:
                tax_liability = 0
                return tax_liability

            elif user_income in range(250001, 500001):
                tax_liability = (user_income - 250000)* 0.05
                return tax_liability

            elif user_income in range(500001,1000001):
                tax_liability = 12500 + (user_income - 500000)*0.20
                return tax_liability

            else:
                tax_liability = 112500 + (user_income - 1000000)*0.30
                return tax_liability

        elif user_age in range(61,81):
                if user_income <= 300000:
                    tax_liability = 0
                    return tax_liability

                elif user_income in range(300001, 500001):
                    tax_liability = (user_income - 300000) * 0.05
                    return tax_liability

                elif user_income in range(500001, 1000001):
                    tax_liability = 12500 + (user_income - 500000) * 0.20
                    return tax_liability

                else:
                    tax_liability = 112500 + (user_income - 1000000) * 0.30
                    return tax_liability

        else:
           if user_income <= 500000:
                tax_liability = 0
                return tax_liability

           elif user_income in range(500001, 1000001):
                tax_liability = (user_income - 500000) * 0.20
                return tax_liability

           else:
               tax_liability = 100000 + (user_income - 1000000) * 0.30
               return tax_liability

    if tax_regime == "New":
        if user_income <= 250000:
            tax_liability = 0
            return tax_liability

        elif user_income in range(250001, 500001):
            tax_liability = (user_income - 250000)* 0.05
            return tax_liability

        elif user_income in range(500001,750001):
            tax_liability = 12500 + (user_income - 500000)*0.10
            return tax_liability

        elif user_income in range(750001,1000001):
            tax_liability = 37500 + (user_income - 750000)*0.15
            return tax_liability

        elif user_income in range(1000001,1250001):
            tax_liability = 75000 + (user_income - 1000000)*0.20
            return tax_liability

        elif user_income in range(1250001,1500001):
            tax_liability = 125000 + (user_income - 500000)*0.25
            return tax_liability
        else:
            tax_liability = 187500 + (user_income - 1500000)*0.30
            return tax_liability


print(f"{user_name} chose {tax_regime} tax regime. \nTax liability of {user_name} is Rupees {tax_calculator()}")

