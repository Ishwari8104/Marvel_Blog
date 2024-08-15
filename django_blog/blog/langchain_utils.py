import os
from sqlalchemy import create_engine
import pandas as pd
from langchain_openai import ChatOpenAI
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent

# Load the dataset and create the SQL database
df = pd.read_csv(r"C:\Users\Admin\Desktop\MARVELBLOG\Marvel_Blog\django_blog\blog\Marvel_Comics.csv")

# Setting up the SQLite engine
engine = create_engine("sqlite:///comics.db")
df.to_sql("comics", engine, index=False, if_exists='replace')

# Setting up the database for Langchain
db = SQLDatabase(engine=engine)

# Initialize the Langchain model
os.environ["OPENAI_API_KEY"] = ""  # Replace with your actual OpenAI API key
llm = ChatOpenAI(model="gpt-3.5-turbo-0125")
agent_executor = create_sql_agent(llm, db=db, agent_type="openai-tools", verbose=True)

def query_comics(user_input):
    # Run the Langchain model
    response = agent_executor.invoke({"input": user_input})
    
    # Return the response
    return response['output']
