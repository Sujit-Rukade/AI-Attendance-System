import streamlit as st
import datetime

def footer_home():
    year = datetime.datetime.now().year
    
    st.markdown(f"""
        <hr style="border: 0; height: 1px; background: rgba(255, 255, 255, 0.15); margin: 3rem 0 1rem 0;">
        <div style="display: flex; justify-content: center; align-items: center; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">
            <p style="margin: 0; font-size: 14px; color: rgba(255, 255, 255, 0.8); letter-spacing: 0.5px;">
                © {year} Developed by <strong>Snap Class Team</strong>
            </p>  
        </div>
    """, unsafe_allow_html=True)


def footer_dashboard():
    year = datetime.datetime.now().year
    
    st.markdown(f"""
        <hr style="border: 0; height: 1px; background: rgba(0, 0, 0, 0.1); margin: 3rem 0 1rem 0;">
        <div style="display: flex; justify-content: center; align-items: center; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">
            <p style="margin: 0; font-size: 14px; color: rgba(0, 0, 0, 0.7); letter-spacing: 0.5px;">
                © {year} Developed by <strong>Snap Class Team</strong>
            </p>  
        </div>
    """, unsafe_allow_html=True)