def joining_databases_improved(L, R):
    # Create a hash map for R that maps each key to its associated value
    hash_map_R = {}
    for k, s in R:
        hash_map_R[k] = s  # Directly assign the value since keys are distinct

    # Create the joined list by iterating over elements in L
    joined_list = []
    for k, x in L:
        if k in hash_map_R:
           joined_list.append((k, x, hash_map_R[k]))
                

    return joined_list

def parse_input(user_input, is_L):
    # Remove extra spaces and split by parentheses to handle spaces inside tuples
    cleaned_input = ' '.join(user_input.split())
    # Extract tuples
    tuples = []
    
    # Split based on ')' and filter out empty parts
    parts = [part.strip() for part in cleaned_input.split(')') if part.strip()]
    for part in parts:
        part = part.strip() + ')'  # Add the closing parenthesis back
        if part.startswith('('):
            try:
                # Extract and clean k and value
                k_value = part[1:-1].split(',')
                k = k_value[0].strip()  # First element
                value = k_value[1].strip()  # Second element

                # Validate the input based on whether it's L or R
                if is_L:
                    # Both elements must be natural numbers (positive integers)
                    if not k.isdigit() or not value.isdigit() or int(k) <= 0 or int(value) <= 0:
                        print(f"Invalid tuple for L: {part}. Both elements must be natural numbers.")
                        return None
                    tuples.append((int(k), int(value)))
                else:
                    # First element must be a natural number, second must be a string
                    if not k.isdigit() or int(k) <= 0:
                        print(f"Invalid tuple for R: {part}. First element must be a natural number.")
                        return None
                    # Ensure the second element is a string (non-empty and alphabetic)
                    if not value.isalpha() or not value:  # check if string is non-empty and contains only letters
                        print(f"Invalid tuple for R: {part}. Second element must be a non-empty string.")
                        return None
                    tuples.append((int(k), value))
            except ValueError:
                print(f"Invalid tuple format: {part}")
                return None
        else:
            print(f"Invalid format: {part}. Tuples must be enclosed in parentheses.")
            return None
    return tuples

"""
Authors: 
  
- Hisham Panamthodi Kajahussain (hisham.pk@csu.fullerton.edu)
- Kenny Le (lekenny43@csu.fullerton.edu)

"""
def main():
    
    L_input = input("Enter elements for list L in the format L=(k,x) separated by space (e.g., L=(1,10) (2,20)): ")
    R_input = input("Enter elements for list R in the format R=(k,s) separated by space (e.g., R=(1,'a') (2,'b')): ")

    # Parse the input with validation
    L = parse_input(L_input, is_L=True)
    if L is None:
        print("Error in input for list L. Program terminated.")
        return
    R = parse_input(R_input, is_L=False)
    if R is None:
        print("Error in input for list R. Program terminated.")
        return

    # Assuming join_databases_improved function exists and works
    # Perform the join operation
    joined_list = joining_databases_improved(L, R)

    # Print the result
    print("\nJoined List J:")
    for item in joined_list:
        print(item)

if __name__ == "__main__":
    main()
