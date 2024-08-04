import streamlit as st

def activities_section():
    #activities images
    training_202406 = "activities/202406_training.jpeg"
    training1_202406 = "activities/202406_training1.png"
    training_202312 = "activities/202312_training.jpg"
    training1_202312 = "activities/202312_training1.jpeg"
    training2_202312 = "activities/202312_training2.jpg"
    training_202308 = "activities/202308_training.jpeg"
    training1_202308 = "activities/202308_training1.jpeg"
    training2_202308 = "activities/202308_training2.jpeg"
    training_201912 = "activities/201912_training.jpg"
    training1_201912 = "activities/201912_training1.jpg"
    training2_201912 = "activities/201912_training2.jpg"
    training_201901 = "activities/201901_training.jpg"
    training1_201901 = "activities/201901_training1.jpg"
    training2_201901 = "activities/201901_training2.jpg"
    training_201603 = "activities/201603_training.png"
    training1_201603 = "activities/201603_training1.png"
    exibition_201810 = "activities/201810_exhibition.jpg"
    exibition1_201810 = "activities/201810_exhibition1.jpg"
    exibition2_201810 = "activities/201810_exhibition2.jpg"
    exibition_201705 = "activities/201705_exhibition.jpg"
    exibition1_201705 = "activities/201705_exhibition1.jpg"
    others_202401 = "activities/202401_others.jpg"
    others1_202401 = "activities/202401_others1.jpg"
    others2_202401 = "activities/202401_others2.jpg"
    others_202309 = "activities/202309_others.jpg"

    tab1, tab2, tab3 =st.tabs(["Training","Exhibition","Others"])
    with tab1:
        st.header("Training Activities")
        with st.expander("2024"):
            st.write("This is some content for the year 2024.")        
            st.subheader("2024-06 :blue[Cybersecurity Awareness Workshop]")
            st.write("Full-day cybersecurity workshop covering 10 modules, including cyber attacks, IoT security, and Wi-Fi threats. This online workshop, conducted via Microsoft Teams, is organized by the Malaysian Rubber Council (MRC).")
            col1, col2 = st.columns(2)
            with col1:
                st.image(training_202406, caption="Cybercesurity Participant")
            with col2:    
                st.image(training1_202406, caption="Cybercesurity Trainer: Ts. Alan Yau Ti Dun")
        with st.expander("2023"):
            st.write("This is some content for the year 2023.")
            st.subheader("2023-12 :blue[Industrial First Aid & CPR AED]")
            st.write("This is more content")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.image(training_202312, caption="Training Participant")
            with col2:    
                st.image(training1_202312, caption="CPR Training")
            with col3:    
                st.image(training2_202312, caption="First Aid head bandage training")
            st.subheader("2023-08 :blue[Ergonomics, Manual Handling & OSH Training]")
            st.write("This is more content")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.image(training_202308, caption="Training Participant")
            with col2:    
                st.image(training1_202308, caption="Ergonomic Trainer: Ts. Yusof Kadikon")
            with col3:    
                st.image(training2_202308, caption="Safety Trainer: N. Asagon Nadaraj")              
            st.subheader("2023-06 :blue[Automotive Core Tools Boot Camp Training]")
            st.write("This is more content")
            st.subheader("2023-03 :blue[Training 6S - Understanding & Implementing]")
            st.write("This is more content")
        with st.expander("2021"):
            st.write("This is some content for the year 2021.")
            st.subheader("2021-03 :blue[Managerial Leadership Training]")
            st.write("This is more content")
        with st.expander("2020"):
            st.write("This is some content for the year 2020.")
            st.subheader("2020-11 :blue[Project Management and Problem Solving]")
            st.write("This is more content")
        with st.expander("2019"):
            st.write("This is some content for the year 2019.")
            st.subheader("2019-12 :blue[Lean production Planning & Control]")
            st.write("This is more content")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.image(training_201912, caption="Training Participant")
            with col2:    
                st.image(training1_201912, caption="Lean Group Activity")
            with col3:    
                st.image(training2_201912, caption="Group Presentation")
            st.subheader("2019-MM :blue[Internal Auditor Training (IATF 16949:2016) & (ISO 9001:2015)]")
            st.write("This is more content")
            st.subheader("2019-MM :blue[Understanding Requirement of IATF 16949:2016]")
            st.write("This is more content")
            st.subheader("2019-01 :blue[Emergency Response Preparedness (Fire Fighting) Training]")
            st.write("This is more content")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.image(training_201901, caption="Fire Figthing Participant")
            with col2:    
                st.image(training1_201901, caption="Fire Figthing Trainer: Encik Norhizam")
            with col3:    
                st.image(training2_201901, caption="Hose Drill Training") 
        with st.expander("2018"):
            st.write("This is some content for the year 2018.")
            st.subheader("2018-07 :blue[Productivity Strategies for Production]")
            st.write("This is more content")
        with st.expander("2017"):
            st.write("This is some content for the year 2017.")
            st.subheader("2017-07 :blue[Smart Scope Keyence IM Series Operation Training]")
            st.write("A briefing and explanation on the operation of the Keyence IM Smart Scope, covering basic GD&T measurement systems, machine automatic measurement settings, and data file saving for analysis and study. The briefing is conducted by Keyence.")
        with st.expander("2016"):
            st.write("This is some content for the year 2016.")
            st.subheader("2016-07 :blue[Factory Fire Prevention, Fire Fighting Squad and Emergency Response Team Training]")
            st.write("This year, I'm involve in the company Fire Fighting Squad and Emergency Response Team. The training involve participation in hose drills, fire extinguisher use, and fire prevention planning. This full-day training is conducted by BOMBA.")
            st.subheader("2016-03 :blue[Smart Scope ZIP and CNC Series Operation Training]")
            st.write("Full-day training on operating the OGP SmartScope models ZIP and CNC. Training covers datum, measurement systems, device automatic setup, and basic GD&T application using these two SmartScope models.")
            col1, col2 = st.columns(2)
            with col1:
                st.image(training_201603, caption="Smart Scope ZIP Model")
            with col2:    
                st.image(training1_201603, caption="Smart Scope CNC Model")
        with st.expander("2015"):
            st.write("This is some content for the year 2015.")
            st.subheader("2015-07 :blue[Restriction of Hazardous Substance (RoHS) awareness]")
            st.write("A briefing and explanation awareness about Restriction of Hazardous Substance (RoHS). This involve explanation on the documentation of RoHS, list of Hazardous substance that is restricted and example of case scenario that have issue related to RoHS.")

    with tab2:
        st.header("Exhibition Activities")
        with st.expander("2018-10 ITAP: Industrial Transformation ASIA-PACIFIC"):
            st.write("This is more content")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.image(exibition_201810, caption="ITAP 2018")
            with col2:    
                st.image(exibition1_201810, caption="SAP Booth")
            with col3:    
                st.image(exibition2_201810, caption="IR4.0 Overview")         
        with st.expander("2017-05 IRICE: International Rubber Industry Conference and Exhibition"):
            st.write("This is more content")
            col1, col2 = st.columns(2)
            with col1:
                st.image(exibition_201705, caption="IRICE 2017")
            with col2:    
                st.image(exibition1_201705, caption="IRICE 2017 Participant")

    with tab3:
        st.header("Others Activities")
        with st.expander("2024-01 Emergency Fire Drills and Chemicals Spillage"):
            st.write("We are conducting our annual fire drills for 2024. This year, I am involved as the Fire Extinguisher Coordinator. Representatives from each department will participate to learn and practice the PASS procedure for using fire extinguishers.")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.image(others_202401, caption="Emergency Fire Drills")
            with col2:    
                st.image(others1_202401, caption="Fire Extinguisher Drills")
            with col3:    
                st.image(others2_202401, caption="Chemical Spillage Drills") 
        with st.expander("2023-09 Ergonomics Briefing"):
            st.write("This is more content")
            col1, col2, col3 = st.columns(3)
            with col1:            
                st.image(others_202309, caption='Ergonomic Participant')   