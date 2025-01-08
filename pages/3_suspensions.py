import streamlit as st
from streamlit_app import reactors_choices, turbulence_page, scaleup_page

st.session_state["button_suspensions_disabled"] = True

def calculate_suspensions():
    return


col1, col2 = st.columns(2, vertical_alignment="bottom")

with col1:
    solvent_mix_susp = st.text_input("Solvent mix")
    density_liq = st.number_input("Density liquids [kg/m3]", key="density_liq")
    d_viscosity = st.number_input("Dynamic viscosity [cP]", key="d_viscosity")
    density_solid = st.number_input("Density solid [kg/m3]", key="density_solid")
    p_diameter = st.number_input("Particle diameter [um]", key="p_diameter")
    mass_frac_solid = st.number_input("w/w ratio solid/liquid [%]", key="mass_frac_solids")

with col2:
    correlation = st.selectbox("Correlation to use", key="correlation", options=("Zwietering", "Greenville, Mak & Brown"))
    geometry_constant = st.number_input("Geometry constant", key="geometry_constant")
    impeller_diameter = st.number_input("Impeller diameter [m]", key="impeller_diameter")
    impeller_clearance = st.number_input("Impeller clearance [m]", key="impeller_clearance")
    power_number = st.number_input("Power number (fully baffled) [-]", key="power_number")
    vol_frac_solid = st.number_input("V/V ratio solid/slurry [%]", key="vol_frac_solid")


# comments box
# 
# table for buttons
# 
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("< Previous", type="secondary"):
        st.switch_page(turbulence_page)

with col3:
    if st.button("Calculate", on_click=calculate_suspensions, type="primary"):
        st.session_state["button_suspension_disabled"] = False

with col4:
    if st.button("Continue >", type="secondary", disabled=st.session_state.get("button_suspensions_disabled")):
        st.switch_page(scaleup_page)
