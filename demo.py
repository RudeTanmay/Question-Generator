import os
import google.generativeai as genai
import streamlit as st

# Hardcode the Google API key directly
GOOGLE_API_KEY = "AIzaSyACvCC-icCESWi9VL8gCLaAAE-iNUsNqmQ"  # Replace with your actual API key

# Configure the Gemini Pro model with the API key
genai.configure(api_key=GOOGLE_API_KEY)

# Function to load the Gemini Pro model
def load_gemini_pro_model():
    return genai.GenerativeModel("gemini-pro")

# Function to generate questions using the Gemini Pro model
def generate_questions(topic, question_type, num_questions, marks_per_question):
    # Load the Gemini Pro model
    model = load_gemini_pro_model()

    # Create a prompt for the Gemini Pro model
    prompt = f"Generate {num_questions} {question_type} questions on the topic '{topic}', each worth {marks_per_question} marks."

    # Use generate_content() method
    response = model.generate_content(prompt)

    # Process the response
    questions = response.text.strip().split("\n")

    return questions

# Streamlit UI
st.title("Question Paper Generator")

# Input fields for topic, question type, number of questions, and marks per question
topic = st.text_input("Enter Topic:", "Artificial Intelligence")
question_type = st.selectbox("Select Question Type:", ["MCQ", "Short Answer", "Long Answer"])
num_questions = st.number_input("Number of Questions:", min_value=1, max_value=50, value=5)
marks_per_question = st.number_input("Marks per Question:", min_value=1, max_value=50, value=10)

# Generate button
if st.button("Generate Questions"):
    with st.spinner("Generating questions..."):
        questions = generate_questions(topic, question_type, num_questions, marks_per_question)
    
    # Display generated questions
    if questions:
        st.success("Questions Generated Successfully!")
        for question in questions:
            st.write(question)
    else:
        st.error("No questions were generated.")