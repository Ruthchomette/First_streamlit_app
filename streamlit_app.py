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


