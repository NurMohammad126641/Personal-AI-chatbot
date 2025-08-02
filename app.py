import streamlit as strlt
from chat_bot import load_content_from_txt, get_chatbot_response

strlt.set_page_config(
    page_title="Rabbi's AI Assistant",
    page_icon= "🤖"
)


with strlt.sidebar:
    strlt.title("About the ChatBot")
    strlt.info(
        "This Chatbot is powered by Google's Gemini Pro Model."
        "It is designed to answer questions"
        "Feel free to ask what you want to know"
    )
    strlt.markdown("---")
    strlt.markdown("### Links")
    strlt.markdown("[LinkedIn](http.linkedin.com/in/nur-mohammad-rabbi-9a73931b6)")
    strlt.markdown("[GitHub](https://github.com/NurMohammad126641)")


strlt.title("🤖 Nur Mohammad Rabbi's AI Assistant")
strlt.markdown("Welcome! I am a personal AI assistant. Ask me anything about Nur Mohammad Rabbi.")


# Load the personal data (context) for the chatbot
personal_data = load_content_from_txt("data.txt")

# Check if data was loaded successfully
if "Error" in personal_data:
    strlt.error(personal_data) # Display an error message if the file is not found
else:
    # Get user input from a text box
    user_question = strlt.text_input("Ask your question here:", placeholder="e.g., What are his key skills?")


# "Get Answer" button
    if strlt.button("Get Answer"):
        if user_question:
            # Show a "thinking" message while the response is being generated
            with strlt.spinner("Finding the best answer..."):
                response = get_chatbot_response(user_question, personal_data)
                strlt.markdown("---")
                strlt.write("### My Answer:")
                strlt.markdown(response)
        else:
            # Show a warning if the user clicks the button without asking a question
            strlt.warning("Please enter a question first.")