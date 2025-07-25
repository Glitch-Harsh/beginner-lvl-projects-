#code tip calculator
def calculate_tip():
    #bill amount in dollars
    bill_amount = float(input("Enter the bill: $ "))
    #tip percent entered by user minimum 15%
    tip_percent = float(input("Enter the percent(minimum 15%): %"))
    #tip amount can be find by this
    tip_amount = float(( bill_amount  * tip_percent)/100 )

    print(f"tip_amount: ${tip_amount:.2f}")
# for recall the function by this we can run this function
calculate_tip()
                         