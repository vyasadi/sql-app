import streamlit as st
import pandas as pd

# DB Mgmt
import sqlite3

conn = sqlite3.connect('swiggy.db')
c = conn.cursor()


# Fxn Make Execution
def sql_executor(sql_code):
    c.execute(sql_code)
    data = c.fetchall()
    return data




st.title("SQLPractice")

menu = ["Home", "About"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Home":
    st.subheader("HomePage")

    # Columns/Layout
    col1, col2 = st.columns(2)

    with col1:
        with st.form(key='query_place'):
            sql_code = st.text_area("SQL Type Here")
            submit_code = st.form_submit_button("Execute")

    # Results Layouts
    with col2:
        if submit_code:
            st.info("Query Submitted")
            st.code(sql_code)

            # Results
            query_results = sql_executor(sql_code)
            with st.expander("Results"):
                st.write(query_results)

            with st.expander("Table"):
                query_df = pd.DataFrame(query_results)
                st.dataframe(query_df)


else:
    st.subheader("About")