# define a function named calculate_discount that takes 2 parameters
def calculate_discount(price, discount_percent):
    # Check if the discount percentage is 20% or higher.
    if discount_percent >= 20:
        # Calculate the discount amount
        discount_amount = price * (discount_percent / 100)
        # calculate final price after applying discount
        final_price = price - discount_amount
        # return final price
        return final_price
    else:
        # If the discount is less than 20%, return the origianl price
        return price
    
# Prompt the user to enter the original price fo the item
original_price = float(input("Enter the original price of the item: "))
# prompt the user to enter the discount percenteage
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price after applying the discount by calling
final_price = calculate_discount(original_price, discount_percent)

# check if discount was applied, print the original price
if final_price == original_price:
    print("No discount applied. Fianl price:", final_price)
else:
    print("Fianl price ater discount:", final_price)