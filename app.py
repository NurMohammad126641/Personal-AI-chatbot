# app.py-এর জন্য নতুন ডিজাইনের কোড
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

    st.title("Nur Mohammad Rabbi")
    st.info("Analytics Engineer | Python & Automation Enthusiast")

    st.markdown("---")
    st.markdown("### 🔗 Links")
    st.markdown("[LinkedIn](https://www.linkedin.com/in/nur-mohammad-rabbi-9a73931b6)")
    st.markdown("[GitHub](https://github.com/NurMohammad126641)")

    st.markdown("---")
    st.success("This app is live and fully functional!", icon="✅")

# --- প্রধান ইন্টারফেস ---
st.title("🤖 AI Assistant")
st.markdown(
    "Welcome! I am a personal AI assistant trained on Nur Mohammad Rabbi's professional data. Feel free to ask me anything about his Rabbi.")
st.markdown("---")

# একটি এক্সপ্যান্ডারের ভেতরে চ্যাটবটের তথ্য
with st.expander("Click here to see what I know about"):
    st.json({
        "Experience": "Progoti Systems (TallyKhata)",
        "Key Skills": ["Python", "SQL", "Django", "Data Analysis", "Automation"],
        "Education": "B.Sc. in EEE, Bangladesh University",
        "Projects": ["Advance Monitoring Dashboard", "Redmine API Automation"]
    })

# চ্যাট ইন্টারফেস
user_question = st.text_input("💬 Ask your question here...", placeholder="e.g., What was his role at TallyKhata?")

if user_question:
    with st.spinner("🧠 Thinking..."):
        response = get_chatbot_response(user_question, personal_data)

        # ইউজারের প্রশ্নটি দেখানো
        st.chat_message("user").write(user_question)

        # AI-এর উত্তর দেখানো
        st.chat_message("assistant").markdown(response)