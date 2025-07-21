from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
#use_case = "bot detection"
chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant specialized in AI security."),
    ("human", "Explain how to use Retrieval-Augmented Generation in AI agents for {use_case}.")
])
messages = chat_prompt.format_messages(use_case="bot detection")

from langchain_openai import ChatOpenAI
llm = ChatOpenAI(model="gpt-4o", temperature=0)
response = llm.invoke(messages)

print(response.content)
