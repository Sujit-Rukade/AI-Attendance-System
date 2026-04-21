import streamlit as st

def teacher_screen():
    st.title("Welcome to the Teacher Screen")
    st.write("This is where teachers can manage their classes and view attendance records.")
    if st.button("Logout"):
        st.session_state['login_type'] = None
        st.rerun()
    