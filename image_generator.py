from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
from langchain_core.runnables import RunnableLambda
from dotenv import load_dotenv
import openai

load_dotenv()

# Set up Prompt and LLM
prompt = PromptTemplate(
    template="Generate an image based on the following description: {image_desc}.",
    input_variables=["image_desc"]
)

llm = OpenAI()

# Custom image generator using raw OpenAI API
def generate_image_url(desc: str) -> str:
    response = openai.images.generate(
        model="dall-e-3",
        prompt=desc,
        n=1,
        size="1024x1024"
    )
    return response.data[0].url

# Wrap it as a Runnable
image_generator = RunnableLambda(generate_image_url)

# Build the chain
chain = prompt | llm | image_generator

# Run it
print(chain.invoke({"image_desc": "folk playing tennis"}))
