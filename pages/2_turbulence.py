import streamlit as st
from streamlit_app import reactors_choices, solvents_page, suspensions_page

st.session_state["button_turbulence_disabled"] = True

def calculate_turbulence():
    return

col1, col2 = st.columns(2, vertical_alignment="bottom")


with col1:
    reactor = st.selectbox("Raector", options=reactors_choices, key="reactor")
    volume_liq = st.number_input("Volume liquids", value=20)
    power_number = st.number_input("Power number [-]")
 


with col2:
    solvent_mi = st.text_input("Solvent mixture", key="solvent_mix")
    density = st.number_input("Density [kg/m3]", key="density")
    d_viscosity = st.number_input("Dynamic viscosity [cP]", key="d_viscosity")


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

      