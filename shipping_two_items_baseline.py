def shipping_two_items_baseline(products):

    # Iterate over all pairs of products
    for i in range(len(products)):
        for j in range(i + 1, len(products)):
            # Check if the sum of their prices equals 2500
            if products[i][0] + products[j][0] == 2500:
                # Return the first valid pair found
                return (int(products[i][0]), products[i][1]), (int(products[j][0]), products[j][1])

    # Return 'NIL' if no pairs are found
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
    result = shipping_two_items_baseline(products)
    print("Result:", result)

if __name__ == "__main__":
    main()
