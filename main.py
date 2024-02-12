import streamlit as st

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)
#with col1:
 #   st.image("images/")

with col2:
    st.title("Mohamed Aboul-Fath")
    content = '''Hi I am Mohamed, Iam an aspiring Software engineer, currently building my Python portfolio
    to gain hands on expreience in py
    '''
    st.info(content)


