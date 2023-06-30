import os
from dotenv import load_dotenv
from langchain.llms import OpenAI

#Load environment variables from .env file
load_dotenv()

#Access the openai api key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

llm = OpenAI(temperature=0.9) # the temperature ranges from 0 to 1 if 0, the model will be deterministic and if 1, the model will be more creative

query = "What are 5 great vacation destinations in Karnataka during the month of August"
print(llm(query))