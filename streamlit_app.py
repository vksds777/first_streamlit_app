import streamlit
import pandas
import requests
streamlit.title('My Moms new Healthy Dinner')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')                
streamlit.header("Fruityvice Fruit Advice!")
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avacado Toast')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('Fruit')
streamlit.multiselect("Pick Some Fruits:",list(my_fruit_list.index),['Apple','Strawberries'])
streamlit.dataframe(my_fruit_list)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.jason())
