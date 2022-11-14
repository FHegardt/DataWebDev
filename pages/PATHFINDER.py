import streamlit as st
import time
import numpy as np
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time
from pages.Path_functions.pathfunctions import randomize_x_y, create_dataset, create_list_of_coord, get_new_x_y, create_list_gif

st.set_page_config(layout="wide")


def generate_path_list_gif(amount_coord):
    x,y = randomize_x_y(amount_coord)
    l1,x1,y1 = create_list_of_coord(x,y)
    dataset = create_dataset(x,y,l1)
    new_x1, new_y1, l1 = get_new_x_y(dataset, x1, y1)
    list_gif_both = create_list_gif(x1,y1,new_x1,new_y1,l1)
    return list_gif_both

def run_list_gif(list_gif_both):
    for i in range(len(list_gif_both)):
        placeholder.image(list_gif_both[i], width=1000)
        time.sleep(.5)

with st.container():
    left_column, middle_column, right_column = st.columns([4,4,2])
    with left_column:
        st.subheader("Path-finding visualized")
        #st.markdown(path_text, unsafe_allow_html=True)
        st.write("Below you will find a path-finding algorithm visualized based on random coordinates. The solver will find the shortes path between the coordinates")
    with middle_column:
        st.subheader("Choose amount of X")
        amount = st.radio(
        "Make your choice",
        ('8', '15', '25'))
    with right_column:
        st.subheader("Run it!")
        run_algorithm_button_holder = st.empty()
        run_second_algorithm_button_holder = st.empty()

with st.container():
    placeholder = st.empty()
     

if run_algorithm_button_holder.button('Run alogrithm_a'):
    run_list_gif(st.session_state.hello)

if run_second_algorithm_button_holder.button('Run algorithm_b'):
    run_list_gif(st.session_state.hello)


if amount == '8':
    list_gif_both = generate_path_list_gif(10)
    placeholder.image(list_gif_both[0], width=1000)
elif amount == '15':
    list_gif_both = generate_path_list_gif(15)
    placeholder.image(list_gif_both[0], width=1000)
elif amount == '25':
    list_gif_both = generate_path_list_gif(25)
    placeholder.image(list_gif_both[0], width=1000)
st.session_state.hello = list_gif_both



#list_gif_both = generate_path_list_gif(10)
#placeholder.image(list_gif_both[0], width=1000)
    






    
    


    


