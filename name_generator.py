from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI 
from dotenv import load_dotenv
import os
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
llm = OpenAI(openai_api_key=openai_api_key)
prompt=PromptTemplate.from_template("Give {number} name for a {domain} startup?")
chain = prompt | llm
print(chain.invoke({'number':'5','domain':'cooking'}))
print(chain.invoke({'number':'2','domain':'AI'}))
