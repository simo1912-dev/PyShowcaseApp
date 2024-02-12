import pandas
import streamlit as st
import pandas as pd  # third party library to handle csv files

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

content1 = '''
Below you can find some of the apps I have built in Py
'''
st.write(content1)

col3, col4 = st.columns(2)
df = pandas.read_csv("data.csv", sep=";")

with col3: # layout management ...
    for index, row in df[:10].iterrows(): # this enables iterating over each row
        st.header(row["title"])
with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])








