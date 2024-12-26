import streamlit as st


st.title("Guppee Test")

solvents_dict = {
    "Acetonitrile": {
        "density": 1200,
        "d_viscosity": 0.25
    },
    "DMF": {
        "density": 1100,
        "d_viscosity": 0.89
    },
    "THF": {
        "density": 900,
        "d_viscosity": 1.10
    }

}

solvents_choices = solvents_dict.keys()

col1, col2, col3, col4, col5, col6, col7 = st.columns([2, 1, 1, 1, 1, 1, 1])

def set_values(field_id):
    label = "solvent" + field_id
    solvent = st.session_state[label]
    st.session_state["density" + field_id] = solvents_dict[solvent]["density"]
    


with col1:
    solvent1 = st.selectbox("Solvent 1", solvents_choices, index=None, on_change=set_values, args="1", key="solvent1")
    solvent2 = st.selectbox("Solvent 2", solvents_choices, index=None, on_change=set_values, args="2", key="solvent2")
    solvent3 = st.selectbox("Solvent 3", solvents_choices, index=None, on_change=set_values, args="3", key="solvent3")
    st.write("Sum:")
    

with col2:
    vol1 = st.text_input("Volume [L]", key = "volume1")
    vol2 = st.text_input("Volume [L]", key = "volume2", label_visibility="hidden")
    vol3 = st.text_input("Volume [L]", key = "volume3", label_visibility="hidden")
    sum_liq1 = st.empty()


with col3:
    mass_perc1 = st.text_input("Mass ratio", key = "mass_ratio1")
    mass_perc2 = st.text_input("Mass ratio", key = "mass_ratio2", label_visibility="hidden")
    mass_perc3 = st.text_input("Mass ratio", key = "mass_ratio3", label_visibility="hidden")


with col4:
    vol_perc1 = st.text_input("Vol. ratio", key = "vol_ratio1")       
    vol_perc2 = st.text_input("Vol. ratio", key = "vol_ratio2", label_visibility="hidden")
    vol_perc3 = st.text_input("Vol. ratio", key = "vol_ratio3", label_visibility="hidden")


with col5:
    amount1 = st.text_input("Amount [kg]", key = "amount1")
    amount2 = st.text_input("Amount [kg]", key = "amount2", label_visibility="hidden")
    amount3 = st.text_input("Amount [kg]", key = "amount3", label_visibility="hidden")


with col6:
    density1 = st.text_input("Density [kg/m3]", key = "density1")
    density2 = st.text_input("Density", key = "density2", label_visibility="hidden")
    density3 = st.text_input("Density", key = "density3", label_visibility="hidden")


with col7:
    visc1 = st.text_input("Viscosity [cP]", key = "viscosity1")
    visc2 = st.text_input("Viscosity [cP]", key = "viscosity2", label_visibility="hidden")
    visc3 = st.text_input("Viscosity [cP]", key = "viscosity3", label_visibility="hidden")



col1, col2, col3, col4, col5, col6 = st.columns([2, 1, 1, 1, 1, 1])  

with col1:
    col1.write(' ')
    solid = st.text_input("Undissolved Solid", key = "solid")
    st.write("Sum (slurry):")

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