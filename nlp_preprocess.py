from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()
llm = OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))
prompt = PromptTemplate.from_template(
    "Strictly following the pre processing flags"
    "Preprocess the given text by following the given "
    "steps in sequence. Follow only those steps that have"
    "a yes against them. Remove Number:{number},Remove Punctuations: {punc},"
    "Word stemming:{stem}.Output just the preprocessed text. Text:{text}")
chain = prompt | llm
print(chain.invoke(
    {'text':'Hey!I got 12 out of 20 in Swimming','number':'yes','punc':'yes','stem':'no'}
))
print(chain.invoke(
    {'text':'22 13B is my flat no.Rohit will be joining us for the party','number':'yes','punc':'no','stem':'yes'}
))