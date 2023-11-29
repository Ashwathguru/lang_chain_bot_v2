import openai
import streamlit as st
from langchain.agents import create_csv_agent, create_pandas_dataframe_agent
from langchain.llms import OpenAI

openai.api_key = st.secrets["OPENAI_API_KEY"]


def get_answer_csv(query: str) -> str:
    file = "raw.csv"
    agent = create_csv_agent(OpenAI(temperature=0), file, verbose=False)
    answer = agent.run(query)
    return answer


st.header("Chat with TicketGPT")
#uploaded_file = st.file_uploader("Upload a csv file", type=["csv"])

#if uploaded_file is not None:
query = st.text_area("Ask any question related to the tickets")
button = st.button("Submit")
if button:
  st.write(get_answer_csv(query))