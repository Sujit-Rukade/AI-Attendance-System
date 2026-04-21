import streamlit as st

def student_screen():
    st.title("Welcome to the Student Screen")
    st.write("This is where students can view their attendance and other information.")
    if st.button("Logout"):
        st.session_state['login_type'] = None
        st.rerun()
    