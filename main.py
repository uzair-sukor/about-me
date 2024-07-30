import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu(
        menu_title= None,   # To ignore menu title    
        # menu_title= "Main Menu", # To give menu title
        options= ["Home","Projects","Activities","Contact"],
        icons= ["house-door-fill","rocket-takeoff","clipboard2-check","whatsapp"]
    )

if selected == "Home":
    col1, col2 = st.columns(2)
    with col1:
        st.title ("Hi, I'm :blue[Uzair]")
        st.header ("|:blue[Project Manufacturer] |:blue[IATF Project]")
        st.header ("|:blue[Data Analysis]")
        st.header ("from :blue[Johor Bahru], :blue[Malaysia]")
    with col2:
        st.image('profile.png', caption='Nice to meet you.')
if selected == "Projects":
    st.title(f"{selected}")
if selected == "Activities":
    st.title(f"{selected}")
if selected == "Contact":
    st.title(f"{selected}")