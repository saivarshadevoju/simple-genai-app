import os
from dotenv import load_dotenv
load_dotenv()

from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


# LangSmith Tracking
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_TRACING_V2'] = "true"
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")

## Prompt Temaplate 
prompt = ChatPromptTemplate(
    [
        ("system","You are helpful assistant. PLease respond to the question asked"),
        ("user", "Question:{question}")
    ]
)

## Streamlit framework 

st.title("Langchain Demo with TinyLLAMA")
input_text = st.text_input("What question you have in mind?")


## Ollama TinyLlama model
llm = Ollama(model="tinyllama")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    str.write(chain.invoke({"question":input_text}))


