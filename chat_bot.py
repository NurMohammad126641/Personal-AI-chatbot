import os
import google.generativeai as gen_ai
from dotenv import load_dotenv

load_dotenv()


try:
    api_key=os.getenv('google_api_key')
    if not api_key:
        raise ValueError ('api key not found. please recheck .env')
    gen_ai.configure(api_key=api_key)
except Exception as error:
    print(f'error configure api key{error}')
    exit()


# নতুন, দ্রুত এবং আধুনিক মডেল
model = gen_ai.GenerativeModel('gemini-1.5-flash-latest')

def load_content_from_txt(filepath="data.txt"):

    try:
        with open(filepath,'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return 'Error- txt file not found'
    except Exception as error:
        return (f"An error occurred while reading the data file: {error}")


def get_chatbot_response(user_question, context):
    """Generates a response from the chatbot based on the user's question and context."""

    # Create a prompt that instructs the AI
    prompt = f"""
    You are Nur Mohammad Rabbi's personal AI assistant. Your role is to answer questions based ONLY on the information provided below.
    Be friendly, professional, and concise.
    If the answer is not found in the provided information, politely say, "I do not have that information at the moment."
    Do not answer any questions that are not related to Nur Mohammad Rabbi's professional life.

    Provided Information:
    ---
    {context}
    ---

    User's Question: {user_question}
    Your Answer:
    """

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Sorry, I encountered an error: {e}"


# This block is for testing the logic directly
if __name__ == '__main__':
    # Load the data
    personal_data = load_content_from_txt()

    if "Error" not in personal_data:
        # Test question 1
        test_question_1 = "What are Nur Mohammad Rabbi's main skills?"
        answer_1 = get_chatbot_response(test_question_1, personal_data)
        print("Test Question 1:", test_question_1)
        print("Chatbot's Answer 1:", answer_1)

        print("-" * 20)

        # Test question 2
        test_question_2 = "Tell me about his project on Redmine API."
        answer_2 = get_chatbot_response(test_question_2, personal_data)
        print("Test Question 2:", test_question_2)
        print("Chatbot's Answer 2:", answer_2)