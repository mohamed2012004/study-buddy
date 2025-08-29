from langchain_groq import ChatGroq
from src.config.setting import Settings

def get_groq_llm():
    return ChatGroq(
        api_key=Settings.GROQ_API_KEY,
        model_name=Settings.MODEL_NAME,
        temperature=Settings.TEMPERATURE
        )