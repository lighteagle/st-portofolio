import streamlit as st 

# Hero Section
col_photo, col_about = st.columns([1,3], gap="medium")

with col_photo:
    st.image("assets/ninja-laptop.png")

with col_about:
    st.title("Quantum Ninja")
    st.write("""
        _In the deep learning dojo, a quantum blade spins,_
        _Weaving through data where the true magic begins._
        _With stealthy precision, insights emerge anew,_
        _Unveiling hidden patterns as the Quantum Ninja would do._
        """)


# Experience & Skills Section
col_exp, col_skills = st.columns(2, gap="medium")

with col_exp:
    st.title("Experience")
    st.write("""
            - 5 years experience as a Quant Developer
            - 3 years experience as a Data Scientist
            - Strong analytical and problem solving skills
            - Excellent communication and collaboration skills
            """)
    
with col_skills:
    st.title("Skills")
    st.write("""
            - Programming Languages: Python, SQL, Javascript
            - Tools: Streamlit, Plotly, Pandas
            - Machine Learning: TensorFlow, PyTorch
            - Data Visualization: Matplotlib, Plotly
            - Databases : PostgreSQL, MySQL, MongoDB
            """)

# Projects Section
st.title("Projects")
st.write("""
        - [Quantum Ninja Web App](https://github.com/quantum-ninja/quantum-ninja-web-app)
        - [Quantum Ninja Backend API](https://github.com/quantum-ninja/quantum-ninja-backend-api)
        """)