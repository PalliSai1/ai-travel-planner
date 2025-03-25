import google.generativeai as genai

#  Set your Gemini API key here
genai.configure(api_key="AIzaSyCOD3atGvGFPguA-ILO1T768k_AxqRjS88")

def generate_itinerary(user_inputs):
    system_prompt = "You are an AI travel assistant. Create a personalized, day-wise travel itinerary."

    user_prompt = f"""
    Create a {user_inputs['Duration']}-day itinerary for a traveler going from {user_inputs['From']} to {user_inputs['To']}.
    The traveler has a {user_inputs['Budget']} budget and prefers {user_inputs['Preferences']}. 
    The trip purpose is {user_inputs['Purpose']}, and they have dietary preferences: {user_inputs['Dietary']}.
    Include top attractions, restaurants, and accommodations.
    """

    model = genai.GenerativeModel("gemini-1.5-pro-latest")  
    response = model.generate_content([system_prompt, user_prompt])

    return response.text  

# Example user input data
user_inputs = {
    "From": "Delhi",
    "To": "Manali",
    "Duration": "5",
    "Budget": "Medium",
    "Purpose": "Adventure",
    "Preferences": "Trekking, Paragliding, Local Food",
    "Dietary": "No restrictions"
}

# Generate and print itinerary
itinerary = generate_itinerary(user_inputs)
print("\n Generated Travel Itinerary:\n")
print(itinerary)

