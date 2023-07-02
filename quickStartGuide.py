import os
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

#Load environment variables from .env file
load_dotenv()

#Access the openai api key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

llm = OpenAI(temperature=0.9) # the temperature ranges from 0 to 1 if 0, the model will be deterministic and if 1, the model will be more creative


def simpleQuery():
    query = "What are 5 great vacation destinations in Karnataka during the month of August"
    print(llm(query))
    
def predict():
    query = "What to name a company that makes colorful socks?"
    print(llm.predict(query))
    
    
def queryUsingPromptTemplate(favoriteFood):
    prompt = PromptTemplate(
        input_variables=["food"],
        template="What are 5 vacations destinations in Karnataka for someone who likes to eat {food}",
        )
    print(llm(prompt.format(food=favoriteFood)))
    
queryUsingPromptTemplate("idly")