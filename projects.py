import streamlit as st

def projects_section():
        tab1, tab2, tab3 =st.tabs(["Manufacturing","IATF","System"])
        with tab1:
            st.header("Manufacturing Projects")
            with st.expander("Rubber Extrusion"):
                st.write("This is more content")        
            with st.expander("Rubber Compression Molding"):
                st.write("This is more content")
        with tab2:
            st.header("IATF Projects")      
            with st.expander("APQP Documentation"):
                st.write("This is more content")
            with st.expander("PPAP Documentation"):
                st.write("This is more content")
        with tab3:
            st.header("System Projects")      
            with st.expander("Operation Index"):
                st.write("This is more content")
            with st.expander("ERP Development"):
                st.write("This is more content")