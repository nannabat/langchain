from langchain.prompts import PromptTemplate
#from langchain.chains import LLMChain
from langchain_openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()
llm = OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))
prompt = PromptTemplate.from_template(
    " Complete a {length} story using the"
    "given beginning.The genre should be {genre} and the story"
    "should have an apt ending. Beginning:{text}"
    )
chain = prompt | llm
print('\n'.join(chain.invoke({'length':'short','genre':'horror','text':'Once there was a coder'}).replace('\n','.').split('.')))
print('\n'.join(chain.invoke({'length':'short','genre':'rom-com','text':'And Queen died'}).replace('\n','.').split('.')))

