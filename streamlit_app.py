import streamlit

streamlit.title("First Page!!")
streamlit.header("Breakfast Menu..")
streamlit.text("🥣 One")
streamlit.text(" 🥗 Two")
streamlit.text("🐔 Three")
streamlit.text("🥑🍞 Four")

streamlit.header("🍌🥭 Build Your Own Fruit Smoothie 🥝🍇")

import pandas as pd
f_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
f_list = f_list.set_index('Fruit')

f_selected = streamlit.multiselect("Pick some fruits:",list(f_list.index),['Avocado','Strawberries'])
f_to_show = f_list.loc[f_selected]
streamlit.dataframe(f_to_show)
