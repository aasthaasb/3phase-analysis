import numpy as np
import streamlit as st

# Function for simulation and analysis
def simulate_system(connection_type, phase_voltage, phase_current, resistance, inductance, capacitance):
    # Simulated results placeholder
    simulation_results = {
        'Line Voltage': phase_voltage * np.sqrt(3) if connection_type in ['Y-Y', 'Y-D'] else phase_voltage,
        'Line Current': phase_current if connection_type in ['Y-Y', 'D-Y'] else phase_current * np.sqrt(3),
        'Power Factor': 0.95,
        'RMS Voltage': 220,
        'RMS Current': 10,
        'THD Voltage': 0.05,
        'THD Current': 0.1
    }
    return simulation_results

# Streamlit app setup
st.title('Three-Phase Power System Analysis')

# User input sliders
phase_voltage = st.slider('Phase Voltage', min_value=0.0, max_value=500.0, value=230.0, step=1.0)
phase_current = st.slider('Phase Current', min_value=0.0, max_value=50.0, value=10.0, step=0.1)
resistance = st.slider('Resistance', min_value=0.000, max_value=100.00, value=10.00, step=0.1)
inductance = st.slider('Inductance', min_value=0.00, max_value=1.00, value=0.100, step=0.01)
capacitance = st.slider('Capacitance', min_value=0.000, max_value=0.1, value=0.001, step=0.001)
connection_type = st.selectbox('Connection Type', ['Y-Y', 'Y-D', 'D-Y', 'D-D'])

# Simulate the system
simulation_results = simulate_system(connection_type, phase_voltage, phase_current, resistance, inductance, capacitance)

# Display simulation results
st.subheader('Simulation Results')
st.write('Line Voltage:', simulation_results['Line Voltage'])
st.write('Line Current:', simulation_results['Line Current'])
st.write('Power Factor:', simulation_results['Power Factor'])
st.write('RMS Voltage:', simulation_results['RMS Voltage'])
st.write('RMS Current:', simulation_results['RMS Current'])
st.write('THD Voltage:', simulation_results['THD Voltage'])
st.write('THD Current:', simulation_results['THD Current'])
# Display advantages of three-phase current
st.write('**Advantages of Three-Phase Current:**')
advantages = [
    "Constant power delivery --> independent of time.",
    "Efficient use due to lower current compared to single-phase systems.",
    "Higher power transmission capacity with the same conductor size compared to single-phase systems."
]

# Display advantages as bullet points
for adv in advantages:
    if st.button(adv):
        # Redirect to Google search for academic papers
        query = "+".join(adv.split())
        search_url = f"https://www.google.com/search?q={query}+academic+papers"
        st.markdown(f"[{adv}]({search_url})")












