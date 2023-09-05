
import streamlit

streamlit.title('my parents new healthy diner')

streamlit.header('Breakfast favorites')
streamlit.text('🥣omega 3 & bueberry oatmeal')
streamlit.text('🥗kale, spinach & rocket smoothie')
streamlit.text('🐔Hard-boiled free-range Egg')
streamlit.text('🥑🍞Avocado toast')


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
