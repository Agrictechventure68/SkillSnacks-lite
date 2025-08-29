# SkillSnacks Lite – Prompt Documentation

This document captures the **prompt engineering strategy** used in SkillSnacks Lite.  
We designed clear, multi-stage prompts to guide GPT-4 outputs for **explanations, quizzes, and learning tips**.

---

## 📖 Prompt 1 – Simplified Explanation
**Instruction:**  
You are a study assistant. Explain the following in simple language for a beginner: [user input]

**Expected Response Pattern:**
- Converts complex text into easy-to-understand explanation.
- Uses bullet points or numbered steps.
- Highlights key concepts.

---

## 🎯 Prompt 2 – Quiz Generation
**Instruction:**  
Create 5 quiz questions (mix of multiple choice and short-answer) with answers based on: [user input]

**Expected Response Pattern:**
1. Question 1  
   - Options: A, B, C, D  
   - Answer: B  
2. Question 2  
   - Short-answer format  
   - Answer included  
3. And so on…

--
## 🧭 Prompt 3 – Learning Tips
**Instruction:**  
Suggest 3 learning strategies or resources for better understanding of: [user input]

**Expected Response Pattern:**
- Strategy 1: practical technique  
- Strategy 2: online resource / study hack  
- Strategy 3: retention or memory strategy  