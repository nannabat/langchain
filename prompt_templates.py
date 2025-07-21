from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
llm = OpenAI()
prompt = PromptTemplate.from_template("Suggest {number} names for a {domain} startup?")
chain = prompt | llm
print(chain.invoke({'number':'2','domain':'AI'}))
