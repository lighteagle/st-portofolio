import streamlit as st 
import pandas as pd

st.title("🐼 Learn Pandas")
st.write(
    """
    Welcome to the ultimate guide to learning Pandas with Streamlit! 
    Let's make data manipulation fun and easy
    .🚀In this tutorial, we'll use a fictional fruit sales dataset 
    to demonstrate various operations and visualizations.
    """
)

with st.expander("Step 1 : Intialize Data"):
    st.subheader("Step 1 : Intialize Data")
    st.write("How to initialize Dataframe using List & Dictionary")
    
    fruit = ["Apple", "Orange", "Melon"]
    qty = [14, 16, 10]
    price = [10_000, 5_000, 7_000]

    data = {
        "Fruit" : fruit,
        "Qty" :qty,
        "Price" : price
    }
    
    df = pd.DataFrame(data)
    
    st.code(
        """
        # Create 3 Lists : fruit, qty, price
        fruit = ["Apple", "Orange", "Melon"]
        qty = [14, 16, 10]
        price = [10_000, 5_000, 7_000]

        # Create a Dictionary from 3 lists
        data = {
            "Fruit" : fruit,
            "Qty" :qty,
            "Price" : price
        }
        
        # Create a Dataframe from Dictionary
        df = pd.DataFrame(data)
        
        # Print the Dataframe
        print(df)
        """
    )

    st.write("Initialize Dataframe")
    st.write(df)
    
    
with st.expander("Step 2: Add new Rows"):
    st.subheader("Step 2: Add new Rows")
    st.write("How to add new Rows in Pandas Dataframe")
    
    new_data =[{
        "Fruit" : "Grape",
        "Qty" :12,
        "Price" : 12_000
    },{
        "Fruit" : "Banana",
        "Qty" :24,
        "Price" : 3_000
    }]

    df = pd.concat([df,pd.DataFrame(new_data)], ignore_index=True)
    st.code(
        """
        # Create a List of Dictionary
        new_data =[{
            "Fruit" : "Grape",
            "Qty" :12,
            "Price" : 12_000
        },{
            "Fruit" : "Banana",
            "Qty" :24,
            "Price" : 3_000
        }]

        # Use pd.concat to merge / add new data to the Dataframe
        df = pd.concat([df,pd.DataFrame(new_data)], ignore_index=True)
        
        # Print the Dataframe
        print(df)
        """
    )
    st.write("Dataframe after we add new rows")
    st.write(df)
    
with st.expander("Step 3: Delete a row by Index"):
    st.subheader("Step 3: Delete a row by Index")
    st.write("How to Delete a row by Index")
    
    df = df.drop(0)
    st.code(
        """
        # Use methode drop to delete a row by index
        df = df.drop(0)
        """
    )
    st.write("The Dataframe after we delete index 0")
    st.write(df)
    
    
with st.expander("Step 4: Basic analysis in Pandas Dataframe"):
    st.subheader("Step 4: Basic analysis in Pandas Dataframe")
    st.write("How to Analyze the Dataframe")
    st.code(
        """
        # Use len to count
        len(df)         # Count Rows
        len(df.columns) # Count Colums
        
        # Use simple stat like : .sum(), .mean, etc
        df["Qty"].sum()
        df["Price"].mean()
        """
    )
    st.write("Total Rows :", len(df))
    st.write("Total Rows :", len(df.columns))
    st.write("Total Quantity :", df["Qty"].sum())
    st.write("Average Price :", df["Price"].mean())
