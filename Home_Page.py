import streamlit as st
import info

st.title("Web Development Lab 1")
st.header("CS 1301")
st.subheader(info.full_name)

col1, col2 = st.columns([1, 3])
with col1:
    st.image(info.home_picture, width=200)
with col2:
    st.write("Georgia Institute of Technology, Fall 2026")

st.divider()

# one line per page
st.write("""
Welcome to my Streamlit Web Development Lab 1 app! You can navigate between the pages using the sidebar on the left. The pages are:

1. **Portfolio**: My online portfolio, with my education, experience, projects, skills, and the ways to contact me.
2. **Quiz**: An interactive quiz that matches you with a beach in Ceará, Brazil, based on your answers.
""")
