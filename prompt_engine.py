# prompt_engine.py
import google.generativeai as genai

# Configure Gemini API key
genai.configure(api_key="AIzaSyAp4q9l-nedRAZl7WQk-RQ6692C83SoIZQ")

# Load Gemini model
model = genai.GenerativeModel("models/gemini-2.0-flash-001")

# Prompt Engine Function
def run_prompt(prompt_type, user_input):
    if prompt_type == "Zero-Shot":
        prompt = f"{user_input}"

    elif prompt_type == "Few-shot":
        prompt = (
            "Q: Who is the president of India?\n"
            "A: Droupadi Murmu\n"
            "Q: Who is the president of the US?\n"
            "A: Joe Biden\n"
            f"Q: {user_input}\nA: "
        )

    elif prompt_type == "Instruction - Based":
        prompt = (
            "Instruction: Summarize the following in 3 bullet points.\n"
            f"Text: {user_input}"
        )

    elif prompt_type == "Chain-of-Thought":
        prompt = (
            "Solve this step-by-step:\n"
            f"{user_input}"
        )

    elif prompt_type == "Role-based":
        prompt = (
            "You are an AI assistant. Respond helpfully to:\n"
            f"{user_input}"
        )
    else:
        prompt = user_input

    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"❌ Error: {str(e)}"
