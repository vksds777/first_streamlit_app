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
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)
import snowflake.connector
streamlit.header('Fruit List Contains')
#my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#my_cur = my_cnx.cursor()
#snowflake-related functions
def get_fruit_load_list();
    with my_cnx.cursor() as my_cur;
         my_cur.execute("select * from fruit_load_list")
         return my_cur.fetchall()
# add a button to load the fruit
if streamlit.button('Get fruit load list');
   my_cnx = snowflake.connector.connect()**streamlit.secrets[snowflake])
   my_data_rows=get_fruit_load_list()
   streamlit.dataframe(my_data_rows)
