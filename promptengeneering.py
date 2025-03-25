def get_user_preferences():
    print("Welcome to AI Travel Planner!")
    
    from_location = input("Where are you traveling from? ")
    to_location = input("Where do you want to go? ")
    duration = input("How many days will your trip be? ")
    budget = input("Select your budget (Low/Medium/Luxury): ")
    purpose = input("What’s the purpose of your trip? (Adventure/Relaxation/Culture/Food) ")
    preferences = input("Any specific preferences? (e.g., history, shopping, nature) ")
    dietary = input("Any dietary restrictions? ")
    mobility = input("Do you have any mobility concerns (e.g., prefer short walks)? ")

    user_data = {
        "From": from_location,
        "To": to_location,
        "Duration": duration,
        "Budget": budget,
        "Purpose": purpose,
        "Preferences": preferences,
        "Dietary": dietary,
        "Mobility": mobility
    }
    
    print("\n Collected User Preferences:")
    for key, value in user_data.items():
        print(f"{key}: {value}")

    return user_data

# Run the function
user_inputs = get_user_preferences()
