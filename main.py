'''
Gas Station Pricing Calculator
Group Members: Ben Hunt, Christopher Miller, Noah Germann, William Day, Hussain Alshawi
Date: 2026-10-08

This program will be used to calculate the prices of Oil or Gas at a gas station when it is being purchased.
A user will enter input the type of purchase which is either O for Oil, or G for gas.
Then the user will be prompted to input the amount of Gas or Oil they need in the form of litres or cases respectively. This information will be stored in variables.
Defined constants for the price of Gas, Oil, and the litres per case of oil.
The user will also recieve a discount off of their total if they purchase more than a certain amount.
Using these inputs we will calculate the total price, price before tax, price before and after discount, and the gst that the customer will pay.
An output is made to display nicely the selection and the calculations to end the program.
'''



print("---------------------------------------------")
print("*** Welcome to gas station program! ***")
print("---------------------------------------------")
print("Please select the type of purchase:")
print("G: Gas")
print("O: Oil")
selection = input(">>> ").upper()

# Define constants
GAS_LITRE_PRICE = 1.05
OIL_LITRE_PRICE = 1.25
LITRES_PER_CASE = 12

# Selection for Oil and Gas
match selection:
    case "O":
        # Oil option
        OIL_CASES = int(input("Enter # of cases of Oil: "))
        # Error Check
        if OIL_CASES <= 0:
            print("Number of oil cases should be > 0")
            exit()
        province_code = input("Please enter the 2 letters of province abbreviation: ")

        # Calculate oil price 
        if OIL_CASES < 7:
            price_final = (OIL_CASES * LITRES_PER_CASE) * OIL_LITRE_PRICE
        else:
            price_final = ((OIL_CASES * LITRES_PER_CASE) * OIL_LITRE_PRICE) * 0.90

    case "G":
        # Gas option
        GAS_LITRES = int(input("Enter the number of litres of gas: "))
        # Error Check
        if GAS_LITRES <= 0:
            print("Number of gas litres should be > 0")
            exit()
        province_code = input("Please enter the 2 letters of province abbreviation: ")
       
        # Calculate Gas Price
        if GAS_LITRES <= 2000:
            price_final = GAS_LITRE_PRICE * GAS_LITRES
        else:
            price_final = (GAS_LITRE_PRICE * GAS_LITRES) * 0.90
    case _:
        print("Invalid input, you should enter g/G or o/O")
        exit()

# Taxes and gst based on province
gst_percent = 0.0

match province_code.lower():
    case 'ab':  # Alberta
        gst_percent = 0.05
    case 'bc':  # British Columbia
        gst_percent = 0.05
    case 'on':  # Ontario
        gst_percent = 0.13
    case _:     # Everywhere else
        gst_percent = 0.15

# Apply GST to final price
price_before_tax = price_final
price_final += price_final * gst_percent

# Output
price_before_discount = price_before_tax

# Match case contains the entire output
match selection:
    # Checks if cases need to be multiplied by 12
    case "O":
        # In case there was a price before the discount, otherwise outputs price_final
        if OIL_CASES > 6:
            price_before_discount /= .90
        print('----------------------------------------------------------------------------------------------------')
        print(' Product    # Of Litres    Price Before Discount    Price After Discount      GST      Total Price')
        print(f'   {'Oil':<13}{(OIL_CASES*12):<19}{price_before_discount:<25}{price_before_tax:<18}{price_before_tax * gst_percent:<12}{price_final}')
        print('----------------------------------------------------------------------------------------------------')

    case "G":
        # In case there was a price before the discount, otherwise outputs price_final
        if GAS_LITRES > 2000:
            price_before_discount /= .90
        print('----------------------------------------------------------------------------------------------------')
        print(' Product    # Of Litres    Price Before Discount    Price After Discount      GST      Total Price')
        print(f'   {'Gas':<12}{(GAS_LITRES):<19}{price_before_discount:<25}{price_before_tax:<18}{(price_before_tax * gst_percent):<12}{price_final}')
        print('----------------------------------------------------------------------------------------------------')

# Program end
print('Thanks for your business, Good Bye')