# 📚 SkillSnacks Lite – AI Study Buddy  

## 🚀 PROJECT OVERVIEW 
SkillSnacks Lite is an *AI-powered study assistant* that helps learners simplify complex topics, practice with quizzes, and discover effective learning strategies.  

Built with *Streamlit* and *OpenAI GPT-4, it demonstrates the power of **prompt engineering* in creating useful, lightweight educational tools.  

Developed for the *TechGig GenAI Hackathon 2025*.  

## 🎯 PROBLEM STATEMENT 
Students often face challenges with:  
- Understanding complex content.  
- Retaining knowledge effectively.  
- Accessing reliable supplementary study help.  

SkillSnacks Lite solves this by providing *instant study assistance powered by AI*.  

## 🛠 TECH STACK 
- *Frontend & Backend*: Streamlit  
- *AI Model*: OpenAI GPT-4 (via API)  
- *Version Control*: Git + GitHub  
- *Prompt Engineering*: Multi-stage approach (explanation → quiz → tips)  

## ⚙ FEATURES  
- 📖 *Simplified Explanations* – Break down any concept into beginner-friendly language.  
- 🎯 *Auto-Generated Quizzes* – 5 practice questions with answers.  
- 🧭 *Learning Tips* – Smart study strategies & resources.  
- ⚡ *Lightweight Deployment* – Runs online in minutes.  

## 📌 PROMPT ENGINEERING APPROACH 
We used a *stepwise prompt design* to guide GPT-4 outputs.  

### PROMPT 1 – SIMPLIFIED EXPLANATION  
> "You are a study assistant. Explain the following in simple language for a beginner: [user input]"  

### PROMPT 2 – QUIZ GENERATION  
> "Create 5 quiz questions (mix of MCQ and short-answer) with answers based on: [user input]"  

### PROMPT 3 – LEARNING TIPS  
> "Suggest 3 learning strategies or resources for better understanding of: [user input]"  

(Full logs available in [prompts.md](./prompts.md))  

## 🔗 WORKING PROTYPE  
👉 [Live Demo on Streamlit](#) (update after deployment)  

## 💻 LOCAL SETUP  
Clone repository:  
bash
* git clone https://github.com/<Agrictechventure68/SkillSnacks-Lite.git
* cd SkillSnacks-Lite

Install dependencies:
* pip install -r requirements.txt

Run locally:
* streamlit run app.py

📂 REPOSITORY STRUCTURE:
SkillSnacks-Lite/
│── app.py             # Streamlit app
│── requirements.txt   # Dependencies
│── README.md          # Documentation
│── prompts.md         # Prompt logs & responses


📸 Screenshots / Demo

(Add screenshots after running locally)


🏆 HACKATHON FIT
This project demonstrates:
* Prompt Engineering Skills – clear, multi-stage prompt design.
* Practical AI Application – useful for students & learners.
* Deployed Prototype – functional, testable in real-time.

👤 AUTHOR
Bright Doro
Educator | Agricultural & Software Development Consultant | AI Innovator

## 🔎 Workflow (Your Steps)  
1. **Work in VS Code** (best choice for editing + Git).  
2. Initialize Git repo:  
   bash
   git init
   git add .
   git commit -m "Initial commit - SkillSnacks Lite"
   git branch -M main
   git remote add origin https://github.com/Agrictechventure68/SkillSnacks-Lite.git
   git push -u origin main

3. ✅ Once you push successfully → your repo is live on GitHub.

4. Go to Streamlit Cloud → connect GitHub repo → deploy.

5. Update README with live demo link.

6. Submit hackathon entry with:

* GitHub repo link.
* Streamlit demo link.
* Prompt logs (prompts.md).