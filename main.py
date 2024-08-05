import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu(
        menu_title= None,   # To ignore menu title    
        # menu_title= "Main Menu", # To give menu title
        options= ["Home","Projects","Activities","Certificates","Contact"],
        icons= ["house-door-fill","rocket-takeoff","clipboard2-check","award","whatsapp"]
    )

#profile image
profile = "profile.png"

#Home section
if selected == "Home":
    col1, col2 = st.columns(2)
    with col1:
        st.title ("Hi, I'm :blue[Uzair]")
        st.header ("|:blue[Project Manufacturer] |:blue[IATF Project]")
        st.header ("|:blue[Data Analysis]")
        st.header ("from :blue[Johor Bahru], :blue[Malaysia]")
        st.write("Nearly a decade of experience in product/process manufacturing, especially rubber. Led efforts to meet automotive/IATF needs. Coordinated manufacturing systems & data analysis (Excel, Power Query). Participated in ISO 9001 & IATF 16949 internal audits to ensure compliance.")
    with col2:
        st.image(profile, caption='Nice to meet you.')

#Projects section
if selected == "Projects":
    st.title(f"{selected}")
    from projects import projects_section #import project_section from projects.py
    projects_section()

#Activities section
if selected == "Activities":
    st.title(f"{selected}")
    from activities import activities_section #import activities_section from activities.py
    activities_section() 

#Certificates section
if selected == "Certificates":
    st.title(f"{selected}")
    from certificates import certificates_section #import certificates_section from certificates.py
    certificates_section()

#contact section
if selected == "Contact":
    st.title(f"{selected}")
    from contact import contact_section #import contact_section from contact.py
    contact_section()
