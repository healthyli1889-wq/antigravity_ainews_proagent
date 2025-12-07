import streamlit as st
import time
from agents import miner_agent, analyst_agent, integrator_agent, output_agent

# Use the full page width
st.set_page_config(layout="wide")

# Title and Header
st.title("AI Pro")
st.markdown("### Mine Truth. Analyze Deeply. Monetize Results.")

# Sidebar for User Inputs
with st.sidebar:
    st.header("Configuration")
    topic = st.text_input("Topic to Research", value="Generative AI Agents")
    role = st.text_input("Your Role", value="Tech Entrepreneur")
    demand = st.selectbox("Your Goal", ["Build Audience", "Uncover Market Gaps", "Investment Strategy"])
    
    st.info("This interface connects directly to your Python agents.")

# Main Action Button
if st.button("Start Agent Pipeline", type="primary"):
    
    # --- Step 1: Miner ---
    st.subheader("1. ⛏️ The Miner")
    with st.spinner(f"Mining 'Profound' sources for '{topic}'..."):
        # Artificial sleep to show the UI working (since our mock is too fast)
        time.sleep(1) 
        raw_data = miner_agent(topic)
        st.success("Mining Complete")
        with st.expander("View Raw Sources"):
            for item in raw_data:
                st.text(item)

    # --- Step 2: Analyst ---
    st.subheader("2. 🧠 The Analyst")
    with st.spinner("Analyzing for bottom-line truth..."):
        time.sleep(1)
        analysis = analyst_agent(raw_data)
        st.markdown(f"**Bottom Line:** {analysis}")

    # --- Step 3: Integrator ---
    st.subheader(f"3. 🤝 The Integrator (For {role})")
    with st.spinner("Personalizing insights..."):
        time.sleep(1)
        user_profile = {"role": role}
        personalized = integrator_agent(analysis, user_profile)
        st.info(personalized)

    # --- Step 4: Output Guide ---
    st.subheader(f"4. 💰 The Output Guide (Goal: {demand})")
    with st.spinner("Generating growth strategy..."):
        time.sleep(1)
        final_strategy = output_agent(personalized, role, demand)
        st.success("Strategy Generated!")
        st.code(final_strategy, language="markdown")

else:
    st.write("👈 Enter your topic in the sidebar and click 'Start Agent Pipeline' to begin.")
