import streamlit as st
from streamlit_autorefresh import st_autorefresh
from pathlib import Path

# Set up autorefresh to run every 2000 milliseconds (2 seconds)
st_autorefresh(interval=2000, key="book_md_refresh")

def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text()

markdown_content = read_markdown_file("./ZhanChaJingLun/book.md")

st.markdown(markdown_content)
