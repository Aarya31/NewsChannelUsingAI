import streamlit as st
try:
    from altair.vegalite.v4.api import Chart
except ImportError as e:
    st.error(f"Altair import error: {e}")
    st.stop()

from langchain_openai import ChatOpenAI
from langchain_community.tools import DuckDuckGoSearchResults
from langchain.docstore.document import Document
from langchain.chains import load_summarize_chain
from langchain.prompts import PromptTemplate
from genvideo import genvideo
from downloadvideo import download_video
import time

# from langchain_openai import ChatOpenAI

# Replace "your_openai_api_key" with your actual OpenAI API key
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.0)

# llm = ChatOpenAI(model="gpt-4", temperature=0.0)

ts = """
you are a news anchor for a global news channel, with this context generate a concise summary of the following
{text}
"""
pt = PromptTemplate(template=ts, input_variables=["text"])

st.set_page_config(page_title="24/7 NEWS CHANNEL POWERED BY AI DRIVEN NEWS ANCHOR")
st.header("What you want to hear and watch")

qsn = st.text_area("Enter your query")

search = DuckDuckGoSearchResults(backend="news")

if st.button("Submit", type="primary"):
    if qsn:
        result = search.run(qsn)
        data = result.replace("[snippet: ", "")
        data = data[:-1]
        docs = [Document(page_content=t) for t in data]
        chain = load_summarize_chain(llm, chain_type="stuff", prompt=pt)
        summary = chain.run(docs)
        id = genvideo("https://clips-presenters.d-id.com/lana/uXbrIxQFjr/kzlKYBZ2wc/image.png", summary, "en-US-JaneNeural")
        time.sleep(100)
        url = download_video(id)
        st.video(url)
