import streamlit as st
import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="SkillSnacks Lite – AI Study Buddy", layout="wide")

st.title("📚 SkillSnacks Lite – AI Study Buddy")
st.write("Simplify your learning with AI. Paste a topic or text below:")

# Input from user
user_input = st.text_area("✍ Enter your study text or topic here:", height=200)

# Tabs
tab1, tab2, tab3 = st.tabs(["📖 Explanation", "🎯 Quiz", "🧭 Learning Tips"])

def get_ai_response(prompt, role="You are a helpful study assistant."):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",  # GPT-4 lightweight model
            messages=[
                {"role": "system", "content": role},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500,
            temperature=0.7
        )
        return response.choices[0].message['content']
    except Exception as e:
        return f"⚠ Error: {e}"

if user_input:
    with tab1:
        st.subheader("📖 Simplified Explanation")
        prompt1 = f"Explain the following in simple language for a beginner:\n\n{user_input}"
        explanation = get_ai_response(prompt1)
        st.write(explanation)

    with tab2:
        st.subheader("🎯 Quiz Questions")
        prompt2 = f"Create 5 quiz questions (MCQ + short-answer) with answers based on:\n\n{user_input}"
        quiz = get_ai_response(prompt2)
        st.write(quiz)

    with tab3:
        st.subheader("🧭 Learning Tips")
        prompt3 = f"Suggest 3 learning strategies or resources for better understanding of:\n\n{user_input}"
        tips = get_ai_response(prompt3)
        st.write(tips)

st.markdown("---")
# Optional test to confirm key works
try:
    response = openai.Model.list()  # just lists models
    print("✅ API Key is valid and working!")
except Exception as e:
    print(f"⚠ API Key test failed: {e}")

st.markdown("🔗 Built for TechGig GenAI Hackathon 2025 by Bright Doro")