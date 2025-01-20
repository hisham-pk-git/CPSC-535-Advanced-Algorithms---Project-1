def identify_start_city(road_lengths, gas_stations, efficiency):
    """
    Finds the optimal starting city index so that the car can complete the circular journey.

    Args:
    road_lengths (list): Distances between each pair of neighboring cities.
    gas_stations (list): Fuel available at each city.
    efficiency (int): Miles per gallon (efficiency of the car).

    Returns:
    int: Index of the optimal starting city.
    """
    net_balance = 0  # Tracks overall surplus or deficit of fuel for the entire journey
    current_balance = 0  # Tracks surplus of fuel from the current starting point
    start_city = 0  # Index of the potential starting city

    # Iterate through all the cities to determine the starting point
    for idx in range(len(road_lengths)):
        # Calculate available fuel in miles
        fuel_in_miles = gas_stations[idx] * efficiency
        # Distance to the next city
        distance_to_next = road_lengths[idx]

        # Update net and current balance
        net_balance += fuel_in_miles - distance_to_next
        current_balance += fuel_in_miles - distance_to_next

        # If the current balance becomes negative, reset to the next city
        if current_balance < 0:
            # Update the starting city to the next index
            start_city = idx + 1
            # Reset current balance to start fresh from the new city
            current_balance = 0

    # If net balance is non-negative, the last recorded start_city is valid
    return start_city if net_balance >= 0 else -1

"""
Authors: 
  
- Hisham Panamthodi Kajahussain (hisham.pk@csu.fullerton.edu)
- Kenny Le (lekenny43@csu.fullerton.edu)

"""
def main():
    
    # Get user input for road lengths between cities
    road_lengths = list(map(int, input("Enter road lengths between cities (space-separated): ").split()))

    # Get user input for fuel available at each gas station
    gas_stations = list(map(int, input("Enter fuel available at each gas station (space-separated): ").split()))

    # Get user input for car efficiency (MPG)
    efficiency = int(input("Enter car efficiency (MPG): "))

    # Identify the optimal starting city
    start_city = identify_start_city(road_lengths, gas_stations, efficiency)

    # Display the result
    if start_city != -1:
        print(f"The optimal starting city is at index: {start_city}")
    else:
        print("No valid starting city found.")


# Run the main function
if __name__ == "__main__":
    main()
