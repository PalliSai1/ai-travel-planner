import streamlit as st
import google.generativeai as genai


genai.configure(api_key="AIzaSyCOD3atGvGFPguA-ILO1T768k_AxqRjS88")

def generate_itinerary(user_inputs):
    system_prompt = "You are an AI travel assistant. Create a personalized, day-wise travel itinerary."

    user_prompt = f"""
    Create a {user_inputs['Duration']}-day itinerary for a traveler going from {user_inputs['From']} to {user_inputs['To']}.
    The traveler has a {user_inputs['Budget']} budget and prefers {user_inputs['Preferences']}. 
    The trip purpose is {user_inputs['Purpose']}, and they have dietary preferences: {user_inputs['Dietary']}.
    Include top attractions, restaurants, and accommodations.
    """

    model = genai.GenerativeModel("gemini-1.5-pro-latest")  #  Using the latest Gemini model
    response = model.generate_content([system_prompt, user_prompt])

    return response.text

st.title(" AI-Powered Travel Planner")

from_location = st.text_input("Where are you traveling from?")
to_location = st.text_input("Where do you want to go?")
duration = st.number_input("Trip Duration (Days)", min_value=1, max_value=30, value=5)
budget = st.selectbox("Select Budget:", ["Low", "Medium", "Luxury"])
purpose = st.selectbox("Trip Purpose:", ["Adventure", "Relaxation", "Cultural", "Food", "Business"])
preferences = st.text_area("Enter your travel preferences (e.g., trekking, food, shopping):")
dietary = st.text_input("Any dietary restrictions?")

if st.button("Generate Itinerary"):
    if from_location and to_location:
        user_inputs = {
            "From": from_location,
            "To": to_location,
            "Duration": duration,
            "Budget": budget,
            "Purpose": purpose,
            "Preferences": preferences,
            "Dietary": dietary
        }
        
        itinerary = generate_itinerary(user_inputs)
        st.subheader(" Your Personalized Travel Itinerary:")
        st.write(itinerary)
    else:
        st.warning("Please enter both your starting location and destination.")

