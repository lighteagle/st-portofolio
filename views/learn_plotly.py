import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

st.title("📈 Learn Plotly")
# Introduction
st.write(
    """
Welcome to the Plotly tutorial! Plotly is a powerful library for creating interactive graphs and visualizations in Python. In this tutorial, we'll cover various types of charts using Plotly. 
Feel free to interact with the inputs to see how the charts update in real time!
"""
)

# Sidebar for Interactive Inputs
st.sidebar.header("Customize Data")
num_points = st.sidebar.slider("Number of Point", min_value=5, max_value=100, value=10)
seed = st.sidebar.number_input("Random Seed", min_value=0, max_value=100, value=77)

# Generate Random Data
np.random.seed(seed)

data = {
    "Date": pd.date_range(start="2024-01-01", periods=num_points, freq="D"),
    "Value": np.random.randint(0, 100, num_points),
    "Value2": np.random.randint(0, 100, num_points),
    "Category": np.random.choice(["Apple", "Banana", "Melon"], num_points),
}
df = pd.DataFrame(data)
# st.write(df)


# Section for Line Chart
with st.expander("Line Chart"):
    st.write("How to create a Line Chart")

    fig = px.line(df, x="Date", y="Value", title="Line Chart")
    st.plotly_chart(fig)

    code = """ 
    # Use px.line to create Line Chart
    fig = px.line(df, x='Date',y='Value',title='Line Chart')
    
    # Use plotly_chart to show chart into Streamlit
    st.plotly_chart(fig)
    """

    st.code(code)


# Section for Bar Chart
with st.expander("Bar Chart"):
    st.write("How to Create a Bar Chart")

    fig = px.bar(df, x="Date", y="Value", title="Bar Chart")
    st.plotly_chart(fig)

    code = """
    # Use px.bar to create a Bar Chart and give arguments (Dataframe, x, y, and title)
    fig = px.bar(df,x='Date',y='Value',title="Bar Chart")
    st.plotly_chart(fig)
    """
    st.code(code)

# Section for Scatter Plot
with st.expander("Scatter Plot"):
    st.write("How to create a Scatter Plot")

    fig = px.scatter(df, x="Value", y="Value2", color="Category", title="Scatter Plot")
    st.plotly_chart(fig)

    code = """ 
    # Use px.scatter to create a Scatter Plot
    fig = px.scatter(df,x='Value',y='Value2',color='Category',title='Scatter Plot')
    st.plotly_chart(fig)
    """

    st.code(code)

# Section for Pie Chart
with st.expander("Pie Chart"):
    st.write("How to create a Pie Chart")

    fig = px.pie(df, names="Category", title="Pie Chart")
    st.plotly_chart(fig)

    code = """ 
    # Use px.pie to create a Pie Chart
    fig = px.pie(df, names='Category', title='Pie Chart')
    st.plotly_chart(fig)
    """

    st.code(code)

# Section for Histogram
with st.expander("Histogram"):
    st.write("How to create a Histogram")

    fig = px.histogram(df, x="Value", title="Histogram")
    st.plotly_chart(fig)

    code = """ 
    # Use px.histogram to create a histogram
    fig = px.histogram(df, x='Value', title='Histogram')
    st.plotly_chart(fig)
    """

    st.code(code)

# Section for Box Plot
with st.expander("Box Plot"):
    st.write("How to create a Box Plot")

    fig = px.box(df, x="Category", y="Value", title="Box Plot")
    st.plotly_chart(fig)

    code = """
    # Use px.box to create a Box Plot
    fig = px.box(df,x='Category',y='Value',title='Box Plot')
    st.plotly_chart(fig)
    """
    st.code(code)


# Section for Violin Plot
with st.expander("Violin Plot"):
    st.write("How to create a Violin Plot")

    fig = px.violin(df, x="Category", y="Value", title="Violin Plot")
    st.plotly_chart(fig)

    code = """
    # Use px.violin to create a Violin Plot
    fig = px.violin(df, x="Category", y="Value", title="Violin Plot")
    st.plotly_chart(fig)
    """

    st.code(code)


# Section for Area Chart
with st.expander("Area Chart"):
    st.write("How to create an Area Chart")

    fig = px.area(df, x="Date", y="Value", title="Area Chart")
    st.plotly_chart(fig)

    code = """
    # Use px.area to create an Area Chart
    fig = px.area(df, x='Date', y='Value', title= "Area Chart")
    st.plotly_chart(fig)
    """

    st.code(code)


# Section for Density Heatmap
with st.expander("Density Heatmap"):
    st.write("Density Heatmap")

    fig = px.density_heatmap(df, x="Value", y="Value2", title="Density Heatmap")
    st.plotly_chart(fig)

    code = """
    # Use px.density_heatmap to create a Density Heatmap 
    fig = px.density_heatmap(df, x='Value', y='Value2', title='Density Heatmap')
    st.plotly_chart(fig)
    """
    st.code(code)
