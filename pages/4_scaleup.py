import streamlit as st


col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    reactor1 = st.selectbox("Reactor 1", key="reactor1", index=None, placeholder="Reactor 1", options=[])
    volume_liq1 = st.number_input("Volume liquids 1 [L]", key="vol_liq1")
    mass_sol1 = st.number_input("Amount solids 1 [kg]", key="mass_sol1")
    volume_total1 = st.number_input("Total volume 1 [L]", key="total_vol1")
    


with col2:
    scale_factor = st.number_input("Scale factor [-]", key="scale_factor")


with col3:
    reactor2 = st.selectbox("Reactor 2", key="reactor2", index=None, placeholder="Reactor 2", options=[])    
    volume_liq2 = st.number_input("Volume liquids 2", key="vol_liq2")
    mass_sol2 = st.number_input("Amount solids 2 [kg]", key="mass_sol2")
    volume_total2 = st.number_input("Total volume 2 [L]", key="total_vol2")

col1, col2, col3 = st.columns([1, 1, 1], vertical_alignment="bottom")

with col1:
    stir_speed1 = st.number_input("Stir speed reactor 1 [rpm]", key="stir_speed1")

with col2:
    scalup_parameter = st.selectbox("Scale up parameter", key="scaleup_parameter", options=[])

with col3:
    stir_speed2 = st.number_input("Stir speed reactor 2 [rpm]", key="stir_speed2")        
    