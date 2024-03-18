def calculate_discount(price, discount_percent):
    if discount_percent >= 20: 
        discounted_price = price - (price * discount_percent / 100)#calciulates the price after discount is done
        return discounted_price
    else:
        return price #return the original price if discount isn't performed

def main():
    original_price = float(input("Enter the original price of the item: "))#prompts the user to enter the original price
    discount_percent = float(input("Enter the discount percentage: "))#prompts user to enter the discount percentage

    final_price = calculate_discount(original_price, discount_percent)

    if final_price != original_price:
        print(f"The final price after applying a {discount_percent}% discount is: ${final_price:.2f}")
    else:
        print("No discount applied. The original price is: ${:.2f}".format(original_price))

if __name__ == "__main__":
    main()
