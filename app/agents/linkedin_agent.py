from llm.ollama_client import call_ollama
from prompts.linkedin_prompt import build_prompt
from tools.file_tool import save_post

def generate_post(user_input):
    prompt = build_prompt(user_input)
    result = call_ollama(prompt)
    save_post(result)
    return result