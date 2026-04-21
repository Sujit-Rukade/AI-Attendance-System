import streamlit as st

def header_home():
    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"
    
    st.markdown(f"""
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:30px; margin-top:30px; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">
            <img src='{logo_url}' style='height:110px; margin-bottom: 10px; drop-shadow: 0px 4px 6px rgba(0,0,0,0.1);' />
            <h1 style='text-align:center; color:#E0E3FF'>SNAP<br/>CLASS</h1>
            <p style='text-align:center; color:#E0E3FF; font-size: 1.2rem; font-weight: 500; letter-spacing: 1.5px; margin-top: 5px; text-transform: uppercase;'>
                Intelligent AI Attendance System
            </p>
        </div>
    """, unsafe_allow_html=True)


def header_dashboard():
    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"
    
    st.markdown(f"""
        <div style="display:flex; align-items:center; justify-content:center; gap:15px; margin-bottom: 20px; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">
            <img src='{logo_url}' style='height:80px;' />
            <div style="display:flex; flex-direction:column; justify-content:center;">
                <h2 style='text-align:left; color:#5865F2; font-size: 2.2rem; font-weight: 800; margin: 0; line-height: 1.1;'>
                    SNAP CLASS
                </h2>
                <span style='text-align:left; color:#6B7280; font-size: 0.95rem; font-weight: 600; letter-spacing: 0.5px;'>
                    Intelligent AI Attendance System
                </span>
            </div>
        </div>
    """, unsafe_allow_html=True)