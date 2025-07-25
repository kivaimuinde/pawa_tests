# app/utils/prompt_engineering.py

def build_prompt(user_input: str) -> str:
    return (
        "You are an intelligent travel advisor AI. Respond in a clear, organized format.\n"
        f"User question: {user_input}\n\n"
        "Structure the answer with clear headings (e.g., Visa, Passport, Travel Advisories, etc.)"
    )
