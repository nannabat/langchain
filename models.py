from langchain_openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()
llm = OpenAI(
    temperature=0,
    max_retries=2,
    api_key=os.getenv("OPENAI_API_KEY"))
llm_model = llm.model_name
print(f"llm model:{llm_model}")
print(llm.invoke("Tell me about stars"))