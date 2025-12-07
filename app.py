import streamlit as st
import time
import os

# ==========================================
# 1. THE BRAIN (Infrastructure)
# ==========================================
# Try to import openai, handle error if not installed
try:
    from openai import OpenAI
except ImportError:
    OpenAI = None

def talk_to_artificial_intelligence(prompt):
    """
    Sends the prompt to OpenAI if a key is found, otherwise mocks it.
    """
    # Check session state for key if not in env
    api_key = os.environ.get("OPENAI_API_KEY") or st.session_state.get("openai_api_key")
    
    # --- REAL MODE ---
    if api_key and OpenAI:
        try:
            client = OpenAI(api_key=api_key)
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a world-class expert agent."},
                    {"role": "user", "content": prompt}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error calling AI: {str(e)}"

    # --- SIMULATION MODE ---
    time.sleep(1) # Simulate thinking
    lower_prompt = prompt.lower()
    if "hello" in lower_prompt: return "Hello! I am your AI assistant."
    if "analyze" in lower_prompt: return "### 🧠 Deep Analysis\nThe market is currently over-indexed on hype. The **REAL** opportunity lies in vertical integration. While everyone is building platforms, the smart money is moving into specialized coherent workflows.\n\n**Bottom Line**: Stop building generic tools. Build for specific pain points."
    if "personalizi" in lower_prompt or "tell this user" in lower_prompt: return "### 🎯 Impact Report\nAs a **Tech Entrepreneur**, this shift means your current roadmap might be too broad. \n\n**Immediate Action**: Pivot your pitch deck to focus on 'Problem-Specific' solutions rather than 'All-in-one' AI."
    if "guide" in lower_prompt: return "### 💰 Money-Making Strategy\n\n**1. The Hook**: \"Why 99% of AI Startups Are Dead Wrong (And How You Can Win)\"\n\n**2. Keywords**: Vertical AI, Agentic Workflows, SaaS Consolidation.\n\n**3. Execution**: Write a thread contrasting 'Tool Fatigue' with 'Agent Relief'. Pitch your product as the cure."
    return "Simulation Mode: I received your request."

# ==========================================
# 2. THE AGENTS (Logic)
# ==========================================
def miner_agent(topic):
    """Agent 1: Mines the best sources"""
    best_data = [
        f"Source (Deep Technical Paper): {topic} architecture is shifting towards Sparse MoE models...",
        f"Source (Insider Analysis): The market consolidation for {topic} is creating a winner-take-all dynamic...",
        f"Source (Expert Interview): The unspoken truth about {topic} is that 90% of current use cases are invalid..."
    ]
    return best_data

def analyst_agent(raw_data_list):
    """Agent 2: Analyzes for bottom line"""
    combined_text = "\n".join(raw_data_list)
    prompt = f"Analyze these sources. Give me the profound bottom line:\n{combined_text}"
    return talk_to_artificial_intelligence(prompt)

def integrator_agent(analysis_text, user_profile):
    """Agent 3: Personalizes for user"""
    prompt = f"User is {user_profile['role']}. Analysis: {analysis_text}. What does this mean for their career/wallet?"
    return talk_to_artificial_intelligence(prompt)

def output_agent(personalized_insight, user_role, demand="build_audience"):
    """Agent 4: Creates strategy"""
    prompt = f"User Goal: {demand}. Insight: '{personalized_insight}'. Create a viral content strategy and money-making guide."
    return talk_to_artificial_intelligence(prompt)

# ==========================================
# 3. USER INTERFACE (Frontend)
# ==========================================
st.set_page_config(page_title="Frontline Reporter", page_icon="⚡", layout="wide")

# --- CUSTOM CSS ---
st.markdown("""
<style>
    /* Global Styles */
    .stApp {
        background: linear-gradient(to right, #0f0c29, #302b63, #24243e);
        color: white;
    }
    h1, h2, h3 {
        color: #00d2ff !important;
        font-family: 'Helvetica Neue', sans-serif;
    }
    .stButton>button {
        background: linear-gradient(45deg, #FF512F, #DD2476);
        color: white;
        border: none;
        border-radius: 25px;
        height: 50px;
        font-size: 18px;
        font-weight: bold;
        width: 100%;
        transition: transform 0.2s;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        color: white;
    }
    .report-box {
        background-color: rgba(255, 255, 255, 0.1);
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #00d2ff;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/4712/4712035.png", width=100)
    st.title("Control Center")
    
    st.subheader("🔑 Access")
    api_key_input = st.text_input("OpenAI API Key", type="password", help="Leave empty for Simulation Mode")
    if api_key_input:
        st.session_state["openai_api_key"] = api_key_input
        st.success("Real Intelligence Active")
    
    st.subheader("🎯 Target")
    topic = st.text_input("Topic", value="Generative AI")
    role = st.text_input("Role", value="Founder")
    demand = st.selectbox("Goal", ["Viral Content", "Investment Signal", "Market Analysis"])
    
    st.markdown("---")
    st.markdown("Built with **Frontline Agents**")

# --- MAIN PAGE ---
st.title("⚡ Frontline Reporter")
st.markdown("### The AI Agent that builds your wealth via information arbitrage.")

if st.button("🚀 IGNITE AGENT PIPELINE"):
    
    # Progress Container
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    # Phase 1
    status_text.text("Phase 1: Mining Intelligence...")
    progress_bar.progress(25)
    time.sleep(0.5)
    raw_data = miner_agent(topic)
    
    # Phase 2
    status_text.text("Phase 2: Analyzing Hidden Patterns...")
    progress_bar.progress(50)
    analysis = analyst_agent(raw_data)
    
    # Phase 3
    status_text.text("Phase 3: Personalizing Impact...")
    progress_bar.progress(75)
    user_profile = {"role": role}
    personalized = integrator_agent(analysis, user_profile)
    
    # Phase 4
    status_text.text("Phase 4: Generating Strategy...")
    progress_bar.progress(100)
    final_output = output_agent(personalized, role, demand)
    time.sleep(0.5)
    status_text.empty()
    progress_bar.empty()
    
    # --- DISPLAY RESULTS ---
    st.markdown("## 💎 Intelligence Report")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="report-box">', unsafe_allow_html=True)
        st.subheader("🧠 Bottom Line")
        st.markdown(analysis)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="report-box">', unsafe_allow_html=True)
        st.subheader("🎯 Personal Impact")
        st.markdown(personalized)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="report-box">', unsafe_allow_html=True)
        st.subheader(f"🚀 Execution Plan: {demand}")
        st.markdown(final_output)
        st.markdown('</div>', unsafe_allow_html=True)

else:
    st.info("Ready to mine the internet? Set your parameters on the left and click IGNITE.")
