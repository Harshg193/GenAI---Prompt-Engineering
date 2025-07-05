# app.py
import streamlit as st
from prompt_engine import run_prompt
import base64

# Page Configuration
st.set_page_config(
    page_title="Prompt Engineering APP | Gemini Prompt Studio",
    page_icon="🔍",
    layout="centered"
)

# Set background image
def set_background(image_file):
    with open(image_file, "rb") as file:
        encoded = base64.b64encode(file.read()).decode()
    st.markdown(f"""
        <style>
        .stApp {{
            background-image: url("data:image/webp;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
    """, unsafe_allow_html=True)

# Apply your image
set_background("assets/promptbg.webp")

# CSS — remove all dark boxes and keep UI minimal
st.markdown("""
    <style>
    /* Remove unwanted black boxes */
    .stTextArea textarea, .stTextInput input {
        background: transparent !important;
        color: white !important;
        border: 2px solid #ff7f50 !important;
        border-radius: 10px !important;
        padding: 10px !important;
        font-size: 1.05em !important;
        box-shadow: none !important;
    }

    .stSelectbox > div {
        background: transparent !important;
        color: white !important;
        border: 2px solid #ff7f50 !important;
        border-radius: 10px !important;
    }

    .stButton > button {
        background: linear-gradient(to right, #ff416c, #ff4b2b);
        color: white;
        padding: 10px 30px;
        border-radius: 30px;
        font-size: 1.1em;
        font-weight: bold;
        border: none;
        margin-top: 15px;
        box-shadow: 0 5px 15px rgba(255, 75, 43, 0.3);
        transition: all 0.3s ease;
    }

    .stButton > button:hover {
        background: linear-gradient(to right, #ff4b2b, #ff416c);
        box-shadow: 0 5px 20px rgba(255, 75, 43, 0.5);
        transform: scale(1.03);
    }

    /* Response box */
    .response-box {
        background-color: rgba(0,0,0,0.8);
        color: white;
        padding: 16px;
        border-radius: 10px;
        border-left: 5px solid #ff7f50;
        font-size: 1em;
        margin-top: 20px;
        white-space: pre-wrap;
    }

    /* Hide scrollbar artifacts */
    ::-webkit-scrollbar, ::-webkit-scrollbar-track, ::-webkit-scrollbar-thumb {
        background: transparent;
    }
    </style>
""", unsafe_allow_html=True)

# Header (no background box)
st.markdown("""
    <h1 style='text-align: center; color: white; font-size: 3em; text-shadow: 2px 2px 8px black;'>
        🔍 Prompt Engineering APP
    </h1>
    <p style='text-align: center; font-size: 1.2em; color: #dddddd; margin-top: -10px; text-shadow: 1px 1px 4px black;'>
        Search Smart. Prompt Better. Powered by Gemini AI ⚡
    </p>
""", unsafe_allow_html=True)

# Prompt type selector
prompt_types = [
    "Zero-Shot",
    "Few-shot",
    "Instruction - Based",
    "Chain-of-Thought",
    "Role-based"
]

selected_prompt = st.selectbox("💬 Select Prompt Type", prompt_types)

# Text input
user_input = st.text_area("🧠 Enter your prompt here:", height=150)

# Generate response
if st.button("🚀 Generate with Gemini"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter a prompt.")
    else:
        with st.spinner("🔍 Thinking..."):
            output = run_prompt(selected_prompt, user_input)
            st.markdown("### 💡 Gemini's Response")
            st.markdown(f"<div class='response-box'>{output}</div>", unsafe_allow_html=True)
