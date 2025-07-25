from langchain.agents import create_react_agent, AgentExecutor
from langchain_community.tools import Tool, YouTubeSearchTool
from langchain_community.tools.wikipedia.tool import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.memory import ConversationBufferMemory

from langgraph.graph import StateGraph
from typing import TypedDict
from dotenv import load_dotenv
import uuid 
from datetime import datetime
load_dotenv()

# Tools
youtube = YouTubeSearchTool()
wiki = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
tools = [
    Tool(name="youtube", func=youtube.run, description="Find YouTube videos"),
    Tool(name="wiki", func=wiki.run, description="Search Wikipedia"),
]

# Prompt
# prompt = ChatPromptTemplate.from_messages([
#     ("system", "You can use the following tools:\n\n{tools}\n\nTool names: {tool_names}"),
#     MessagesPlaceholder("chat_history"),
#     ("human", "{input}"),
#     ("system", "{agent_scratchpad}"),
# ])
prompt = ChatPromptTemplate.from_messages([
    ("system", """You are a helpful AI agent. You can use the following tools:

{tools}

When answering a question, you must use the following format **exactly**:

Thought: [what you are thinking]
Action: [the name of a tool to use, must be one of: {tool_names}]
Action Input: [the input to that tool]

Then wait for the observation. You can continue reasoning or answer once you have enough information.

Here is an example:

Question: What is the weather in New York?

Thought: I should check a weather source.
Action: weather
Action Input: New York

If you have enough information to answer, respond in this format:
Thought: I now know the final answer.
Final Answer: [your answer here]

Only show tool results once. Do not repeat tool outputs or links that have already been shown.



Begin."""),
    MessagesPlaceholder("chat_history"),
    ("human", "{input}"),
    ("system", "{agent_scratchpad}"),
])
# LLM + Agent + Memory
llm = ChatOpenAI(model="gpt-4o", temperature=0)
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
agent = create_react_agent(llm=llm, tools=tools, prompt=prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, memory=memory, verbose=False, handle_parsing_errors=True)

# AgentLangGraph Node
def agent_node(state: dict) -> dict:
    user_input = state["input"]
    session_id = str(uuid.uuid4())
    print(f"\n🧠 AGENT SESSION [{session_id}] STARTED")
    print(f"📥 INPUT: {user_input}\n")
    output = agent_executor.invoke({"input": user_input})
    print(f"\n✅ FINAL ANSWER: {output['output']}")
    print(f"📄 SESSION [{session_id}] COMPLETE @ {datetime.now()}")
    return {"output": output}

# LangGraph setup
class AgentState(TypedDict):
    input: str
    output: str

graph = StateGraph(state_schema=AgentState)
graph.add_node("agent", agent_node)
graph.set_entry_point("agent")
graph.set_finish_point("agent")

workflow = graph.compile()

# Run
result = workflow.invoke({"input": "Tell me something about Nara Chandra Babu Naidu and get his speech on YouTube"})
#print(result["output"])

