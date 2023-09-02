import streamlit, pandas, requests

streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach, & Rocket Smoothie')
streamlit.text('🐔 Hard-Boil Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
# Putting example fruit in the picklist for the customer to see
# Selected fruits go into fruits_selected list
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

# Allows us to just display fruits that have been chosen by customer
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

#New section to display the fruityvice api response and a new header
streamlit.header('Fruityvice Fruit Advice!')

#Adding a text entry box and sending the input to the Fruityvice API
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

#pulling the data from the API
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")

#normalizes the json formatted data and then stores it in variable 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())

# Creates a new table for the normalized data to be displayed
streamlit.dataframe(fruityvice_normalized)
