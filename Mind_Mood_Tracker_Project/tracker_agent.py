from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()


llm = ChatOllama(model="mistral")

def analyse_entry(user_input : str ) -> dict:
    prompt = PromptTemplate.from_template(
    """
You are a wellness assistant that tracks a user's mood and energy.

Your job is to:
1. Analyze emotional or physical states (like "I'm tired", "Feeling anxious", "Very energetic").
2. If the input matches this, return:
   - Mood: [mood]
   - Energy: [Give the rating out of 10 something like 3/10]
   - Suggestion: [short tip]

⚠️ If the input is **not** about how the user feels (e.g., it's a technical question, command, greeting, etc.), you MUST respond only with:

    "Hi Mate , I am your emotional assistant . Please share how you're currently feeling — emotionally or physically."

Never attempt to answer anything else. Do not provide any mood or energy analysis unless it's clearly emotional or physical input.

---

User: {entry}

Your response:
"""
    )
    full_prompt = prompt.format(entry=user_input)
    response = llm.invoke(full_prompt)
    return response.content



