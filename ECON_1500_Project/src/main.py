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
st.title("ECON 1500 Final: An Interactive Visualization of North American Trade for U.S. States")

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

#Creating and displaying the map
fig = create_map(trade_data, "Total Balance")
st.plotly_chart(fig, use_container_width=True)



