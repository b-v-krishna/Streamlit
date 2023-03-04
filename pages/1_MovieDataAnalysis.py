import streamlit as st
import pandas as pd
import plotly.graph_objs as go
import os

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")


DATA_PATH = os.path.join(dir_of_interest, "data", "IMDb_Data_final.csv")

st.title("Dashboard - Top IMDB RATED MOVIES IN 2022")

df = pd.read_csv(DATA_PATH)


option = st.radio(
    "select option",
    ('Head', 'Shape', 'boxplot','histogram'))

if option == 'Head':
    st.write(df.head())
elif option=='Shape':
    st.write(df.shape)
elif option=='boxplot':
    fig = go.Figure()
    fig.add_trace(go.Box(y=df["Duration"], name="Movie Duration"))

    # Update plot layout
    fig.update_layout(title="Distribution of Movie Durations",
                    xaxis_title="",
                    yaxis_title="Duration (minutes)")

    # Display plot using Streamlit
    st.plotly_chart(fig)
else:
    # Create histogram using Plotly
    fig = go.Figure()
    fig.add_trace(go.Histogram(x=df["IMDb-Rating"], nbinsx=20))

    # Update plot layout
    fig.update_layout(title="Distribution of Movie Ratings",
                    xaxis_title="IMDb Movie Rating",
                    yaxis_title="Count")

    # Display plot using Streamlit
    st.plotly_chart(fig)
            
            
            