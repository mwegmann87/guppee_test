import streamlit as st


st.title("Guppee Test")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

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

solvents_page = st.Page("pages/1_solvents.py", title="Solvents")
turbulence_page = st.Page("pages/2_turbulence.py", title="Turbulence")
suspensions_page = st.Page("pages/3_suspensions.py", title="Suspensions")
scaleup_page = st.Page("pages/4_scaleup.py", title="Scale up")
admin_page = st.Page("pages/5_admin.py", title="Admin")
login_page = st.Page("pages/6_login.py", title="Login")

if st.session_state.logged_in:
    pg = st.navigation({
        "Tools": [solvents_page, turbulence_page, suspensions_page, scaleup_page],
        "Admin": [admin_page]
    })
else:
    pg = st.navigation({
        "Tools": [solvents_page, turbulence_page, suspensions_page, scaleup_page],
        "Login": [login_page]
    })    

pg.run()