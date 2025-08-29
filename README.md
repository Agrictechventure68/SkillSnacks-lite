# 📚 SkillSnacks Lite – AI Study Buddy

**SkillSnacks Lite** is an AI-powered study companion that simplifies learning.  
Paste a topic or text, and the app generates:
- 📖 Simplified Explanations  
- 🎯 Quiz Questions  
- 🧭 Learning Tips & Resources  

⚡ *Lightweight Deployment* – runs online in minutes.

## 📌 Prompt Engineering Approach
We used a **stepwise prompt design** to guide GPT-4 outputs.

### Prompt 1 – Simplified Explanation  
> "You are a study assistant. Explain the following in simple language for a beginner: [user input]"

### Prompt 2 – Quiz Generation  
> "Create 5 quiz questions (mix of MCQ and short-answer) with answers based on: [user input]"

### Prompt 3 – Learning Tips  
> "Suggest 3 learning strategies or resources for better understanding of: [user input]"

👉 Full logs available in [prompts.md](./prompts.md)

## 🔗 Working Prototype
👉 [Live Demo on Streamlit](https://skillsnacks-lite.streamlit.app)  
*(Update with your actual Streamlit Cloud link after deployment)*

---
## 💻 LOCAL SETUP 
### Clone the repository
```bash
git clone https://github.com/Agrictechventure68/SkillSnacks-Lite.git
cd SkillSnacks-Lite
Create and activate a virtual environment
bash
Copy code
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/Mac:
source venv/bin/activate

Install dependencies
bash
Copy code
pip install -r requirements.txt

Configure environment variables
Create a .env file in the project root:

ini
Copy code
OPENAI_API_KEY=your_openai_api_key_here
Run locally
bash
Copy code
streamlit run app.py

📂 REPOSITORY STRUCTURE
SkillSnacks-Lite/
│── app.py             # Streamlit app
│── requirements.txt   # Dependencies
│── README.md          # Documentation
│── prompts.md         # Prompt logs & responses
│── .env.example       # Example environment file
📸 Screenshots / Demo
(Add screenshots of the app after deployment)

🏆 HACKATHON FIT
This project demonstrates:

📝 Prompt Engineering – clear, multi-stage design

🎓 Practical AI Application – supports students & learners

🌐 Deployed Prototype – functional, testable in real-time

👤 AUTHOR
Bright Doro
Educator | Agricultural & Software Development Consultant | AI Innovator