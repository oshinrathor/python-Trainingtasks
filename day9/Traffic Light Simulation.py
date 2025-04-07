def traffic_light_simulation():
    while True:
        # Prompt the user for the next step
        print("\nTraffic Light Simulation")
        print("1. Red Light")
        print("2. Yellow Light")
        print("3. Green Light")
        print("4. Exit")
        
        # Get user input
        user_choice = input("Enter the number corresponding to the traffic light you want to simulate: ").strip()
        
        # Red Light Condition
        if user_choice == "1":
            print("\nRed Light: Stop! Cars must halt.")
        
        # Yellow Light Condition
        elif user_choice == "2":
            print("\nYellow Light: Prepare to stop or go.")
        
        # Green Light Condition
        elif user_choice == "3":
            print("\nGreen Light: Go! Cars can move.")
        
        # Exit Condition
        elif user_choice == "4":
            print("\nExiting Traffic Light Simulation. Goodbye!")
            break  # Exit the loop and end the simulation
        
        # Invalid input handling
        else:
            print("\nInvalid input. Please choose a valid option (1, 2, 3, or 4).")

# Start the traffic light simulation
traffic_light_simulation()
