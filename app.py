import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="SkillSnacks Lite – AI Study Buddy", layout="wide")

st.title("📚 SkillSnacks Lite – AI Study Buddy")
st.write("Simplify your learning with AI. Paste a topic or text below:")

# Input from user
user_input = st.text_area("✍ Enter your study text or topic here:", height=200)

# Tabs
tab1, tab2, tab3 = st.tabs(["📖 Explanation", "🎯 Quiz", "🧭 Learning Tips"])

def get_ai_response(prompt, role="You are a helpful study assistant."):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": role},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500,
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"⚠ Error: {e}"

if user_input:
    with tab1:
        st.subheader("📖 Simplified Explanation")
        explanation = get_ai_response(f"Explain the following in simple language for a beginner:\n\n{user_input}")
        st.write(explanation)

    with tab2:
        st.subheader("🎯 Quiz Questions")
        quiz = get_ai_response(f"Create 5 quiz questions (MCQ + short-answer) with answers based on:\n\n{user_input}")
        st.write(quiz)

    with tab3:
        st.subheader("🧭 Learning Tips")
        tips = get_ai_response(f"Suggest 3 learning strategies or resources for better understanding of:\n\n{user_input}")
        st.write(tips)

st.markdown("---")

# Optional API key test (new syntax)
try:
    client.models.list()
    print("✅ API Key is valid and working!")
except Exception as e:
    print(f"⚠ API Key test failed: {e}")

st.markdown("🔗 Built for TechGig GenAI Hackathon 2025 by Bright Doro")