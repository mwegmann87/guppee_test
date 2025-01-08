import streamlit as st
from streamlit_app import reactors_choices, solvents_page, suspensions_page

st.session_state["button_turbulence_disabled"] = True

def calculate_turbulence():
    return

col1, col2 = st.columns(2, vertical_alignment="bottom")


with col1:
    reactor = st.selectbox("Raector", options=reactors_choices, key="reactor")
    reactor_diameter = st.number_input("Reactor diameter [m]", key="reactor_diameter")
    impeller_diameter = st.number_input("Impeller diameter [m]", key="impeller_diameter")
    power_number = st.number_input("Power number (fully baffled) [-]", key="power_number")
    liquids_mass = st.number_input("Liquids mass [kg]", key="liquids_mass")
 


with col2:
    solvent_mix = st.text_input("Solvent mixture", key="solvent_mix")
    total_density = st.number_input("Total density [kg/m3]", key="total_density")
    density_liq = st.number_input("Density liquids [kg/m3]", key="density_liq")
    d_viscosity = st.number_input("Dynamic viscosity [cP]", key="d_viscosity")
    liq_volume = st.number_input("Liquids volume [L]", key="liq_volume")

# comments box

# table for buttons
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("< Previous", type="secondary"):
        st.switch_page(solvents_page)

with col2:
    if st.button("Calculate", on_click=calculate_turbulence, type="primary"):
        st.session_state["button_turbulence_disabled"] = False

with col3:
    if st.button("Continue >", type="secondary", disabled=st.session_state.get("button_turbulence_disabled")):
        st.switch_page(suspensions_page)

      