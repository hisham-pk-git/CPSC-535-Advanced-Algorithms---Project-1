# Function to read input from user
def read_matrix():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    matrix = []

    print("Enter the matrix row by row (0 or 1 only) separated by spaces. After each row, press Enter to proceed to the next one:")
    for _ in range(rows):
        row = list(map(int, input().split()))
        if len(row) != cols:
            raise ValueError("Each row must have exactly {} columns.".format(cols))
        matrix.append(row)

    return matrix

# Main function to calculate the largest possible land mass
def largest_land_mass(area):
    # Helper function to perform Depth First Search (DFS) to calculate the size of a land mass
    def depth_first_search(row, col, visited_cells):
        # Base condition to stop DFS if out of bounds or at water (1) or already visited
        if row < 0 or row >= len(area) or col < 0 or col >= len(area[0]) or (row, col) in visited_cells or area[row][col] == 1:
            return 0
        visited_cells.add((row, col))  # Mark the current cell as visited
        land_size = 1

        # Explore all four possible directions: up, down, left, right
        land_size += depth_first_search(row - 1, col, visited_cells)  # Up
        land_size += depth_first_search(row + 1, col, visited_cells)  # Down
        land_size += depth_first_search(row, col - 1, visited_cells)  # Left
        land_size += depth_first_search(row, col + 1, visited_cells)  # Right

        return land_size

    # Variable to keep track of the maximum land mass found
    largest_mass = 0
    num_rows, num_cols = len(area), len(area[0])

    # Iterate over each cell in the matrix
    for row in range(num_rows):
        for col in range(num_cols):
            # If the current cell is "1", try flipping it to "0"
            if area[row][col] == 1:
                # Flip the "1" to "0"
                area[row][col] = 0
                visited_cells = set()

                # Calculate the size of the new land mass formed
                current_mass = 0
                for r in range(num_rows):
                    for c in range(num_cols):
                        # If the cell is "0" and not visited, calculate the size of the land mass
                        if area[r][c] == 0 and (r, c) not in visited_cells:
                            current_mass = max(current_mass, depth_first_search(r, c, visited_cells))

                # Update the maximum land mass size if we found a bigger one
                largest_mass = max(largest_mass, current_mass)

                # Restore the cell back to "1" for further calculations
                area[row][col] = 1

    return largest_mass

"""
Authors: 
  
- Hisham Panamthodi Kajahussain (hisham.pk@csu.fullerton.edu)
- Kenny Le (lekenny43@csu.fullerton.edu)

"""
# Main part of the script
if __name__ == "__main__":
    # Step 1: Read the matrix from the user
    matrix = read_matrix()

    # Step 2: Calculate the largest possible land mass after flipping one "1" to "0"
    result = largest_land_mass(matrix)

    # Step 3: Print the result
    print("Largest possible land mass size after flipping one '1' to '0':", result)
