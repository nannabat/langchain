from operator import itemgetter
from langchain.prompts import ChatPromptTemplate
from langchain_openai  import ChatOpenAI
from langchain.schema import StrOutputParser
from dotenv import load_dotenv

load_dotenv()
prompt1 = ChatPromptTemplate.from_template("Which country won the {game} worldcup ?")
prompt2 = ChatPromptTemplate.from_template("Suggest the best {entity} from {country}")
llm = ChatOpenAI()
chain1 = prompt1 | llm | StrOutputParser()
chain2 = ({"country":chain1, "entity":itemgetter("entity")} | prompt2 | llm | StrOutputParser())
print(chain2.invoke({"game":"cricket","entity":"dish"}))