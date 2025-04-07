def smart_home_automation():
    print("Welcome to the Smart Home Automation System!")
    
    while True:
        # Get sensor inputs from the user
        try:
            temperature = float(input("Enter the current temperature (in °C): "))
            humidity = float(input("Enter the current humidity (percentage): "))
            motion_detected = input("Is motion detected? (yes/no): ").strip().lower()
        except ValueError:
            print("Invalid input. Please enter valid numbers for temperature and humidity.")
            continue

        # Check if temperature exceeds threshold for fan control
        if temperature > 25:
            print("The temperature is too high! Turning on the fan.")
        else:
            print("The temperature is fine. The fan is off.")
        
        # Check if humidity exceeds threshold for fan control
        if humidity > 60:
            print("The humidity is high! Turning on the fan.")
        else:
            print("The humidity is comfortable. The fan is off.")
        
        # Check if motion is detected to turn on the lights
        if motion_detected == 'yes':
            print("Motion detected! Turning on the lights.")
        else:
            print("No motion detected. The lights are off.")
        
        # Ask the user if they want to continue simulating
        continue_simulation = input("\nWould you like to continue the simulation? (yes/no): ").strip().lower()
        if continue_simulation != 'yes':
            print("Exiting Smart Home Automation System. Goodbye!")
            break

# Start the smart home automation
smart_home_automation()
