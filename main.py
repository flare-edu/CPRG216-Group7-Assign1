# code go here
print("--------------------------------------")
print("*** Welcome to gas station program ***")
print("--------------------------------------")
print("Please select the type of purchase:")
print("G: Gas")
print("O: Oil")
selection = input(">>>").upper()

# Define constants
GAS_LITRE_PRICE = 1.05
OIL_LITRE_PRICE = 1.25
LITRES_PER_CASE = 12

match selection:
    case "O":
        # Oil option
        OIL_CASES = int(input("Enter # of cases of Oil: "))
        province_code = input("Please enter the 2 letters of province abbreviation: ")

        # Calculate oil price 
        if OIL_CASES <= 0:
            print("Number of oil cases should be > 0.")
            exit()
        elif OIL_CASES < 7:
            price_final = (OIL_CASES * LITRES_PER_CASE) * OIL_LITRE_PRICE
        else:
            price_final = ((OIL_CASES * LITRES_PER_CASE) * OIL_LITRE_PRICE) * 0.90

    case "G":
        # Gas option
        GAS_LITRES = float(input("Enter the number of litres of gas: "))
        province_code = input("Please enter the 2 letters of province abbreviation: ")
       
        #Calculate Gas Price
        if GAS_LITRES <= 0:
            print("Number of gas litres should be > 0.")
            exit()
        elif GAS_LITRES <= 2000:
            price_final = GAS_LITRE_PRICE * GAS_LITRES
        else:
            price_final = (GAS_LITRE_PRICE * GAS_LITRES) * 0.90
    case _:
        print("Invalid input, you should enter g/G or o/O")
        exit()

#taxes and output

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
price_final += price_final * gst_percent

# To final output handling: 'price_final' is the variable you want to print for the price