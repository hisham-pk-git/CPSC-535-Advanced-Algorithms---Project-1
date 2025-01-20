def shipping_two_items_optimized(products):
    seen_prices = {}  # Dictionary to store prices and corresponding product names

    # Iterate over each product in the list
    for price, name in products:
        required_price = 2500 - price  # Calculate the price needed to reach 2500

        # Check if the required_price is already in the seen_prices dictionary
        if required_price in seen_prices:
            # If required_price exists, we have a valid pair
            return ((required_price, seen_prices[required_price]), (price, name))

        # Add the current product to the seen_prices dictionary if not already present
        if price not in seen_prices:
            seen_prices[price] = name

    # Return 'NIL' if no valid pair is found
    return 'NIL'

"""
Authors: 
  
- Hisham Panamthodi Kajahussain (hisham.pk@csu.fullerton.edu)
- Kenny Le (lekenny43@csu.fullerton.edu)

"""    
def main():
    products = []  # List to store products

    # Get input from the user
    user_input = input("Enter products in the format '(price, name)' separated by spaces: ")

    # Split the input by spaces and process each product
    product_entries = user_input.split(') ')
    #print(product_entries)
    
    for entry in product_entries:
        entry = entry.strip()  # Trim any surrounding whitespace
        if not entry:  # Skip empty entries
            continue

        try:
            # Remove parentheses and split the input
            entry = entry.strip('()')
            price, name = entry.split(',', 1)
            price = price.strip()
            name = name.strip()

            # Check if price is an integer and name is a valid string
            if not price.isdigit() or not name.isalpha():
                print(f"Invalid input for '{entry}'. Price should be an integer and name should be a string.")
                return  # Exit if input format is incorrect

            price = int(price)  # Convert price to integer
            products.append((price, name))  # Append the product tuple to the list

        except ValueError:
            print(f"Invalid input for '{entry}'. Please enter in the format '(price, name)'.")
            return  # Exit if any input is invalid

    # Find and display all pairs
    result = shipping_two_items_optimized(products)
    print("Result:", result)

if __name__ == "__main__":
    main()
