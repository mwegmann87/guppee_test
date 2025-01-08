import streamlit as st
from streamlit_app import solvents_dict, solvents_choices, turbulence_page

# define session state for continue button
st.session_state["button_solvents_disabled"] = True


col1, col2, col3, col4, col5, col6, col7 = st.columns([2, 1, 1, 1, 1, 1, 1], vertical_alignment="bottom", gap="small")

def set_values(field_id):
    label = "input_solvent" + field_id
    solvent = st.session_state[label]
    if solvent:
        st.session_state["input_density" + field_id] = solvents_dict[solvent]["density"]
        st.session_state["input_viscosity" + field_id] = solvents_dict[solvent]["d_viscosity"]

def get_form_values():
    values_list = []
    for field in [vol1, vol1, vol3, visc1, visc2, visc3]:
        values_list.append(field / 1000)
    for field in [density1, density2, density3]:
        values_list.append(field)
    return values_list  

def calculate_mass(volume, density):
    mass = volume * density
    return mass  

def calculate_values():
    values_list = get_form_values()

    # calculate values and enable continue button
    st.write("Values calculated")
    

with col1:
    solvent1 = st.selectbox("Solvent 1", solvents_choices, index=None, on_change=set_values, args="1", key="input_solvent1",
                            placeholder="Solvent 1", label_visibility="collapsed")
    solvent2 = st.selectbox("Solvent 2", solvents_choices, index=None, on_change=set_values, args="2", key="input_solvent2", 
                            placeholder="Solvent 2", label_visibility="collapsed")
    solvent3 = st.selectbox("Solvent 3", solvents_choices, index=None, on_change=set_values, args="3", key="input_solvent3", 
                            placeholder="Solvent 3", label_visibility="collapsed")
    

with col2:
    vol1 = st.number_input("Volume [L]", key = "volume1", format="%0.3f")
    vol2 = st.number_input("Volume [L]", key = "volume2", format="%0.3f", label_visibility="collapsed")
    vol3 = st.number_input("Volume [L]", key = "volume3", format="%0.3f", label_visibility="collapsed")

with col3:
    amount1 = st.number_input("Amount [kg]", key = "input_amount1")
    amount2 = st.number_input("Amount [kg]", key = "input_amount2", label_visibility="collapsed")
    amount3 = st.number_input("Amount [kg]", key = "input_amount3", label_visibility="collapsed")


with col4:
    mass_perc1 = st.number_input("Mass ratio", key = "mass_ratio1")
    mass_perc2 = st.number_input("Mass ratio", key = "mass_ratio2", label_visibility="collapsed")
    mass_perc3 = st.number_input("Mass ratio", key = "mass_ratio3", label_visibility="collapsed")


with col5:
    vol_perc1 = st.number_input("Vol. ratio", key = "vol_ratio1")       
    vol_perc2 = st.number_input("Vol. ratio", key = "vol_ratio2", label_visibility="collapsed")
    vol_perc3 = st.number_input("Vol. ratio", key = "vol_ratio3", label_visibility="collapsed")


with col6:
    density1 = st.number_input("Density [kg/m3]", key = "input_density1", format="%0.0f")
    density2 = st.number_input("Density", key = "input_density2", format="%0.0f", label_visibility="collapsed")
    density3 = st.number_input("Density", key="input_density3", format="%0.0f", label_visibility="collapsed")


with col7:
    visc1 = st.number_input("Viscosity [cP]", key = "input_viscosity1", format="%0.2f")
    visc2 = st.number_input("Viscosity [cP]", key = "input_viscosity2", format="%0.2f", label_visibility="collapsed")
    visc3 = st.number_input("Viscosity [cP]", key = "input_viscosity3", format="%0.2f", label_visibility="collapsed")

st.write("Sum (liquids)")

col1, col2, col3, col4, col5, col6 = st.columns([2, 1, 1, 1, 1, 1], vertical_alignment="bottom")  

with col1:
    col1.write(' ')
    solid = st.text_input("Undissolved Solid", key = "solid")

with col2:
    col2.write(' ')
    mass_sol = st.text_input("Amount [kg]", key = "amount_sol")  

with col3:
    col3.write (' ')
    vol_sol = st.text_input("Volume [L]", key = "vol_sol")

with col4:
    density_sol = st.text_input("Density [kg/m3]", key = "density_sol")

with col5:
    particle_diameter = st.text_input("Particle diameter [um]", key = "particle_diameter")

# table for buttons

col1, col2 = st.columns(2)

with col1:
    if st.button("Calculate", key="calc_values", type="primary", on_click=calculate_values):
        st.session_state["button_solvents_disabled"] = False

with col2:        
    if st.button("Continue >", key="solvents_continue", disabled=st.session_state.get("button_solvents_disabled")):
        st.switch_page(turbulence_page)

    