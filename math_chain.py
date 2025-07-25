from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
llm = OpenAI(model="gpt-4o-mini", temperature=0)
prompt = PromptTemplate.from_template("what is the 3rd root of 1498")
chain = prompt | llm 
print(chain.invoke({}))