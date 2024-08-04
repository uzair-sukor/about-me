import streamlit as st

def certificates_section():
    #certificates images
    manufacturing_lean = 'certificates/manufacturing_201912Lean.jpg'
    iatf_coretools = 'certificates/iatf_202306coretools.png'
    iatf_spc = 'certificates/iatf_202306spc.png'
    iatf_fmea = 'certificates/iatf_202305fmea.png'
    iatf_msa = 'certificates/iatf_202304msa.png'
    iatf_apqp = 'certificates/iatf_202303apqp.png'
    iatf_internalauditor = 'certificates/iatf_201904 InternalAuditor.jpg'
    safety_firstaid = 'certificates/safety_202312firstaid.jpg'
    safety_ergonomic = 'certificates/safety_202308ergonomic.PNG'
    safety_firefighting = 'certificates/safety_201901firefighting.jpg'
    system_sysadmin = 'certificates/system_202301sysadmin.png'
    system_excel= 'certificates/system_202301excel.png'

    tab1, tab2, tab3, tab4 =st.tabs(["Manufacturing","IATF","Safety","System"])
    with tab1:
        st.header("Manufacturing Certificates")
        with st.expander("Lean Production Certificates"):
            st.write("Certificates related for Manufacturing")
            st.image(manufacturing_lean, caption='Lean Production Planning & Control')
    with tab2:
        st.header("IATF Certificates")
        with st.expander("Core Tools Certificates"):
            st.write("Certificates related for IATF")
            st.image(iatf_coretools, caption='IATF Core Tools certificate')
        with st.expander("Internal Auditor Certificates"):
            st.write("Certificates related for IATF")
            st.image(iatf_internalauditor, caption='IATF Internal Auditor certificate')
        with st.expander("AIAG Certificates"):
            st.write("Certificates related for IATF from AIAG")
            st.image(iatf_spc, caption='AIAG SPC certificate') 
            st.image(iatf_fmea, caption='AIAG FMEA certificate')
            st.image(iatf_msa, caption='AIAG MSA certificate')
            st.image(iatf_apqp, caption='AIAG APQP certificate')
    with tab3:
        st.header("Safety Certificates")  
        with st.expander("First Aid and CPR AED Certificates"):
            st.image(safety_firstaid, caption='Industrial First Aid and CPR AED')
        with st.expander("Ergonomic Certificates"):
            st.image(safety_ergonomic, caption='Ergonomic and Manual Handling Skill')
        with st.expander("Fire Fighting Certificates"):
            st.image(safety_firefighting, caption='ERP Fire Fighting')
    with tab4:
        st.header("System Certificates")  
        with st.expander("SysAdmin Certificates"):
            st.image(system_sysadmin, caption='System Administrator certificate by Google')
        with st.expander("Excel Certificates"):
            st.image(system_excel, caption='Business Analytic with Excel by Skillup')
