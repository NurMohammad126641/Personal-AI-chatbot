
import streamlit as st
import google.generativeai as gen_ai
from PIL import Image  # ছবি যোগ করার জন্য নতুন লাইব্রেরি
from chat_bot import get_chatbot_response  # আপনার ফাইলের নাম chat_bot.py হলে

# --- পেজ কনফিগারেশন (সবসময় প্রথমে থাকবে) ---
st.set_page_config(
    page_title="Nur Mohammad Rabbi | AI Assistant",
    page_icon="🤖",
    layout="wide"  # পেজটিকে চওড়া করার জন্য
)

# --- API এবং ডেটা লোডিং ---
try:
    api_key = st.secrets["google_api_key"]
    personal_data = st.secrets["personal_data"]
    gen_ai.configure(api_key=api_key)
except KeyError as e:
    st.error(f"A required secret is missing! Please check your Streamlit Cloud settings. Missing key: {e}", icon="🚨")
    st.stop()
except Exception as e:
    st.error(f"An error occurred during API configuration: {e}", icon="🚨")
    st.stop()

# --- সাইডবার ---
with st.sidebar:
    # আপনার প্রোফাইল ছবিটি এখানে লোড করুন
    try:
        profile_image = Image.open('profile.jpg')
        st.image(profile_image, width=150)
    except FileNotFoundError:
        st.error("Profile image not found. Please add 'profile.jpg' to the root folder.")

    st.title("🤖")

    st.markdown("---")
    st.markdown("### 🔗 Links")
    st.markdown("[LinkedIn](https://www.linkedin.com/in/nur-mohammad-rabbi-9a73931b6)")
    st.markdown("[GitHub](https://github.com/NurMohammad126641)")

    st.markdown("---")
    st.success("This app is live and fully functional!", icon="✅")

# --- প্রধান ইন্টারফেস ---
st.title("🤖 AI Assistant")
st.markdown(
    "Welcome! I am a personal AI assistant trained on Nur Mohammad Rabbi's professional data. Feel free to ask me anything Rabbi.")
st.markdown("---")

# চ্যাট ইন্টারফেস
user_question = st.text_input("💬 Ask your question here...", placeholder="e.g., What was his role at TallyKhata?")

if st.button("Get Answer", type="primary"):
    if user_question:
        with st.spinner("🧠 Thinking..."):
            response = get_chatbot_response(user_question, personal_data)

            st.chat_message("user").write(user_question)
            st.chat_message("assistant").markdown(response)
    else:
        # প্রশ্ন না লিখলে ওয়ার্নিং দেখানো
        st.warning("Please enter a question first.", icon="⚠️")