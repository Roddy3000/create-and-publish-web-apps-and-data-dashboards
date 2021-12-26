import streamlit as st
import pandas 

data = {
  'Series_1':[1,2,4,5,7],
  'Series_2':[10,30,40,100,250]
}

df = pandas.Dataframe(data)

st.title('first streamlit app')
st.subheader('Introduction')
st.write('''This is our fisrt web app
Enjoy it'''
)

st.write(df)