from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain.schema import StrOutputParser
from dotenv import load_dotenv

load_dotenv()
prompt = ChatPromptTemplate.from_template("What is the city {person} is from? Translate:{sentence}in the city native language")
llm = ChatOpenAI()
chain = prompt | llm | StrOutputParser()
print(chain.invoke({"person":"Nara Chandra Babu Naidu","sentence":"how are you?"}))