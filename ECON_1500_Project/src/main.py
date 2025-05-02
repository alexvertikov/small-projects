#Importing packages
import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

#Importing functions from the other pilots
from data_loader import load_data, calculate_balance
from maps import create_map


#Setting the streamlit page configuration
st.set_page_config(layout="wide", page_title="North American Trade Visualization")

#Creating Title
st.title("An Interactive Visualization of 2024 North American Trade for U.S. States")

#Header for a subtitle
st.subheader("Created by Alex Vertikov as a Final Project for the Spring 2025 Iteration of ECON 1500 at Brown University, taught by Professor Fernando Duarte. Please see the README for more details on the motivation and implementation of this project.")

#Loading and processing data
@st.cache_data

def get_processed_data():
    """"
    A function to process the data and give us our final dataframe
    """
    #Extracting the all_data dataframe
    df = load_data()

    #We need to call calculate_balance on all_data
    df = calculate_balance(df)

    return df

#The final dataframe
trade_data = get_processed_data()

#Printing the final dataframe for error checking
print(trade_data)

#Creating and displaying the map
fig = create_map(trade_data)


st.plotly_chart(fig, use_container_width=True)



