# SkillSnacks Lite Prompt Documentation

## Prompt 1 – Simplified Explanation
"You are a study assistant. Explain the following in simple language for a beginner: [user input]"

### Example Response
- Converts complex text into easy-to-understand explanation.
- Uses bullet points or numbered steps.
- Highlights key concepts.

## Prompt 2 – Quiz Generation
"Create 5 quiz questions (mix of multiple choice and short-answer) with answers based on: [user input]"

### Example Response
1. Question 1: ...
   - Options: A, B, C, D
   - Answer: B
2. Question 2: ...
- etc.

## Prompt 3 – Learning Tips
"Suggest 3 learning strategies or resources for better understanding of: [user input]"

### Example Response
- Strategy 1: ...
- Strategy 2: ...
- Strategy 3: ...

3️⃣ Installation Steps (Dependencies)
1. Make sure Python 3.10+ is installed.

2. Create a virtual environment (recommended):
* python -m venv venv

3. Activate virtual environment:
* Windows: venv\Scripts\activate
* Linux/Mac: source venv/bin/activate

4. Install dependencies:
* pip install streamlit openai python-dotenv

5. Create .env file in project root:
* OPENAI_API_KEY=your_openai_api_key_here

6. Run locally:
* streamlit run app.py

7. Optional: Push to GitHub → deploy to Streamlit Cloud.