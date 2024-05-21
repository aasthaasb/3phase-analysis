import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

# Define functions for simulation and analysis
def simulate_system(connection_type, phase_voltage, phase_current, resistance, inductance, capacitance):
    if connection_type == 'Y-Y':
        # Calculate line currents and line voltages for Y-Y connection
        line_voltage = phase_voltage * np.sqrt(3)
        line_current = phase_current
    elif connection_type == 'Y-D':
        # Calculate line currents and line voltages for Y-D connection
        line_voltage = phase_voltage * np.sqrt(3)
        line_current = phase_current * np.sqrt(3)
    elif connection_type == 'D-Y':
        # Calculate line currents and line voltages for D-Y connection
        line_voltage = phase_voltage
        line_current = phase_current / np.sqrt(3)
    elif connection_type == 'D-D':
        # Calculate line currents and line voltages for D-D connection
        line_voltage = phase_voltage
        line_current = phase_current / np.sqrt(3)
    
    # Placeholder simulation results
    simulation_results = {
        'Line Voltage': line_voltage,
        'Line Current': line_current,
        'Power Factor': 0.95,
        'RMS Voltage': 220,
        'RMS Current': 10,
        'THD Voltage': 0.05,
        'THD Current': 0.1
    }
    
    return simulation_results

# Create Streamlit app
st.title('Three-Phase Power System Analysis')

# Create sliders for user input
phase_voltage = st.slider('Phase Voltage', min_value=0.0, max_value=500.0, value=230.0, step=1.0)
phase_current = st.slider('Phase Current', min_value=0.0, max_value=50.0, value=10.0, step=0.1)
resistance = st.slider('Resistance', min_value=0.000, max_value=100.00, value=10.00, step=0.1)
inductance = st.slider('Inductance', min_value=0.00, max_value=1.00, value=0.100, step=0.01)
capacitance = st.slider('Capacitance', min_value=0.000, max_value=0.1, value=0.001, step=0.001)
connection_type = st.selectbox('Connection Type', ['Y-Y', 'Y-D', 'D-Y', 'D-D'])

# Simulate the system
simulation_results = simulate_system(connection_type, phase_voltage, phase_current, resistance, inductance, capacitance)

# Plot phase voltage vs. line voltage
st.write('**Phase Voltage vs. Line Voltage Plot:**')
plt.figure(figsize=(8, 4))
plt.plot(['Phase Voltage', 'Line Voltage'], [phase_voltage, simulation_results['Line Voltage']], marker='o')
plt.xlabel('Voltage Type')
plt.ylabel('Voltage')
plt.title('Phase Voltage vs. Line Voltage')
plt.grid(True)
st.pyplot(plt)

# Plot phase current vs. line current
st.write('**Phase Current vs. Line Current Plot:**')
plt.figure(figsize=(8, 4))
plt.plot(['Phase Current', 'Line Current'], [phase_current, simulation_results['Line Current']], marker='o')
plt.xlabel('Current Type')
plt.ylabel('Current')
plt.title('Phase Current vs. Line Current')
plt.grid(True)
st.pyplot(plt)

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




