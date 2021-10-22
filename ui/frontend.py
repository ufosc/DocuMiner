"""
Basic frontend UI
"""

import streamlit as st

st.title('DocuMiner')

document = st.file_uploader("Upload a document", ['txt', 'doc', 'docx', 'pdf'])

clicked = st.button("Create a wiki")
