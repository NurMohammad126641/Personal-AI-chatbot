import streamlit as strlt
from chat_bot import get_chatbot_response
import google.generativeai as gen_ai

strlt.set_page_config(
    page_title="Rabbi's AI Assistant",
    page_icon= "🤖"
)



try:
    api_key = strlt.secrets["google_api_key"]
    personal_data = strlt.secrets["personal_data"]
except KeyError as e:
    strlt.error(f"A required secret is missing! Please check your Streamlit Cloud settings. Missing key: {e}")
    strlt.stop()

# Google Generative AI কনফিগার করা
gen_ai.configure(api_key=api_key)




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


# ইউজারের ইনপুট নেওয়ার জন্য টেক্সট বক্স
user_question = strlt.text_input("Ask your question here:", placeholder="e.g., What are his key skills?")

# "Get Answer" বাটনে ক্লিক করলে
if strlt.button("Get Answer"):
    if user_question:
        # "thinking" মেসেজ দেখানো
        with strlt.spinner("Finding the best answer..."):
            response = get_chatbot_response(user_question, personal_data)
            strlt.markdown("---")
            strlt.write("### My Answer:")
            strlt.markdown(response)
    else:
        # প্রশ্ন না লিখলে ওয়ার্নিং দেখানো
        strlt.warning("Please enter a question first.")