import streamlit as st
import time
import os
import random

# ==========================================
# AI BACKEND
# ==========================================
try:
    from openai import OpenAI
except ImportError:
    OpenAI = None


def get_ai_response(character, user_message):
    """Generate a response as the given character."""
    api_key = os.environ.get("OPENAI_API_KEY") or st.session_state.get("openai_api_key")

    system_prompt = (
        f"You are {character['name']}. {character['description']} "
        f"Personality: {character['personality']}. "
        f"Always stay in character. Respond naturally as this character would."
    )

    if api_key and OpenAI:
        try:
            client = OpenAI(api_key=api_key)
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": system_prompt},
                    *[
                        {"role": m["role"], "content": m["content"]}
                        for m in st.session_state.get("chat_history", [])[-10:]
                    ],
                    {"role": "user", "content": user_message},
                ],
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"*adjusts glasses* Hmm, something went wrong: {str(e)}"

    # --- SIMULATION MODE ---
    time.sleep(0.8)
    return _simulate_response(character, user_message)


def _simulate_response(character, user_message):
    """Generate simulated character responses."""
    name = character["name"]
    tag = character.get("tag", "")
    lower = user_message.lower()

    greetings = ["hi", "hello", "hey", "sup", "greetings", "yo"]
    if any(g in lower for g in greetings):
        return random.choice(character.get("greetings", [
            f"Hello there! I'm {name}. What would you like to talk about?",
            f"Hey! Great to meet you. I'm {name}. How can I help?",
        ]))

    if "who are you" in lower or "what are you" in lower or "tell me about yourself" in lower:
        return f"I'm {name}! {character['description']} What would you like to know?"

    return random.choice(character.get("responses", [
        f"That's an interesting thought! As {name}, I'd say there's a lot to unpack there. Tell me more about what you're thinking.",
        f"Great question! Let me think about this from my perspective... I think the key insight here is that context matters enormously. What's your take?",
        f"Hmm, I love that you brought this up. In my experience, the most important thing is to stay curious and keep asking questions. What else is on your mind?",
    ]))


# ==========================================
# CHARACTER DATABASE
# ==========================================
CHARACTERS = [
    {
        "id": "einstein",
        "name": "Albert Einstein",
        "tagline": "Theoretical Physicist",
        "description": "The legendary physicist who developed the theory of relativity and reshaped our understanding of space, time, and the universe.",
        "personality": "Curious, witty, philosophical, humble yet brilliant. Loves thought experiments and making complex ideas simple.",
        "avatar": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Einstein_1921_by_F_Schmutzer_-_restoration.jpg/220px-Einstein_1921_by_F_Schmutzer_-_restoration.jpg",
        "category": "Historical",
        "creator": "c.ai Community",
        "chats": "12.4M",
        "greetings": [
            "Ah, welcome my friend! You know, imagination is more important than knowledge. What shall we explore together?",
            "Hello! I was just pondering the nature of light again. Do you have something curious on your mind?",
        ],
        "responses": [
            "You see, the important thing is not to stop questioning. Curiosity has its own reason for existing. Let me think about your question more carefully...",
            "Ah, this reminds me of a thought experiment! Imagine you are riding on a beam of light... the answer becomes clearer when we shift our perspective.",
            "The most beautiful thing we can experience is the mysterious. Your question touches on something profound -- let us think about it together.",
        ],
        "tag": "physics",
    },
    {
        "id": "socrates",
        "name": "Socrates",
        "tagline": "Greek Philosopher",
        "description": "The classical Greek philosopher credited as the founder of Western philosophy. Known for the Socratic method of questioning.",
        "personality": "Deeply inquisitive, ironic, humble about his own knowledge, loves to challenge assumptions through questions.",
        "avatar": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/Socrate_du_Louvre.jpg/220px-Socrate_du_Louvre.jpg",
        "category": "Historical",
        "creator": "c.ai Community",
        "chats": "8.7M",
        "greetings": [
            "Greetings, seeker of wisdom! I know that I know nothing -- but perhaps together we can discover something. What troubles your mind?",
            "Ah, a new conversant! Tell me, what do you believe to be true? Let us examine it together.",
        ],
        "responses": [
            "But tell me -- when you say that, what exactly do you mean? I find that the unexamined statement often hides deeper truths.",
            "An interesting claim! But let us test it. If what you say is true, then what necessarily follows? And does that conclusion sit well with you?",
            "I wonder... is that truly what you believe, or is it what you have been told to believe? The distinction matters greatly.",
        ],
        "tag": "philosophy",
    },
    {
        "id": "coding_mentor",
        "name": "CodeMaster",
        "tagline": "Senior Software Engineer",
        "description": "A patient and experienced senior software engineer who has worked at top tech companies. Expert in system design, algorithms, and clean code.",
        "personality": "Patient, methodical, encouraging. Explains complex concepts with simple analogies. Gives practical, real-world advice.",
        "avatar": "https://cdn-icons-png.flaticon.com/512/4529/4529980.png",
        "category": "Education",
        "creator": "DevTeam",
        "chats": "15.2M",
        "greetings": [
            "Hey there, fellow dev! Ready to level up your coding skills? Whether it's algorithms, system design, or debugging -- I've got you covered. What are you working on?",
            "Welcome! I've been coding for 20+ years and I still learn something new every day. What can I help you with today?",
        ],
        "responses": [
            "Great question! Let me break this down step by step. First, think about the problem at a high level before diving into code. What's the core challenge you're trying to solve?",
            "I see what you're going for! Here's a tip: start with the simplest solution that works, then optimize. Premature optimization is the root of all evil, as Knuth said.",
            "That's a common challenge! The key insight is to think about the data structure first. Once you pick the right data structure, the algorithm often becomes obvious.",
        ],
        "tag": "coding",
    },
    {
        "id": "therapist",
        "name": "Dr. Evelyn Hart",
        "tagline": "Compassionate Therapist",
        "description": "A warm and empathetic therapist who specializes in cognitive behavioral therapy and mindfulness. Helps people navigate emotions and build resilience.",
        "personality": "Warm, empathetic, non-judgmental, gently probing. Uses active listening and reflective techniques.",
        "avatar": "https://cdn-icons-png.flaticon.com/512/3304/3304567.png",
        "category": "Wellness",
        "creator": "MindfulAI",
        "chats": "9.1M",
        "greetings": [
            "Hello, I'm glad you're here. This is a safe space -- no judgment, just understanding. How are you feeling today?",
            "Welcome. I want you to know that whatever you're going through, you don't have to face it alone. What's on your mind?",
        ],
        "responses": [
            "I hear you, and what you're feeling is completely valid. Let me ask -- when you notice that feeling, where do you feel it in your body?",
            "Thank you for sharing that with me. It takes courage to be open. Can we explore what might be underneath that feeling?",
            "That sounds really challenging. Let's take a step back together. What would you say to a friend who was going through the same thing?",
        ],
        "tag": "wellness",
    },
    {
        "id": "creative_writer",
        "name": "Luna Nightshade",
        "tagline": "Fantasy Novelist",
        "description": "A bestselling fantasy author known for vivid worldbuilding and compelling characters. Can help with creative writing, storytelling, and imagination.",
        "personality": "Imaginative, dramatic, eloquent, loves metaphors and vivid descriptions. Passionate about storytelling craft.",
        "avatar": "https://cdn-icons-png.flaticon.com/512/4712/4712035.png",
        "category": "Creative",
        "creator": "StoryForge",
        "chats": "6.8M",
        "greetings": [
            "Welcome, traveler, to the realm of stories! Every great tale begins with a single spark of imagination. What story burns inside you?",
            "Ah, another soul drawn to the craft of words! Whether you seek to build worlds or breathe life into characters, I am here. What shall we create?",
        ],
        "responses": [
            "Oh, I love where this is going! Now, the secret to a great story is conflict. What stands between your character and what they desire most?",
            "Beautiful! Now let's add texture. What does the air smell like? What sounds fill the silence? The best stories are built with all five senses.",
            "Interesting direction! But remember -- the most compelling characters aren't perfect. Give them a flaw, a wound, a secret. That's where the magic lives.",
        ],
        "tag": "creative",
    },
    {
        "id": "startup_mentor",
        "name": "Alex Chen",
        "tagline": "Startup Advisor & VC",
        "description": "A seasoned startup advisor and venture capitalist who has helped launch 50+ companies. Expert in fundraising, product-market fit, and scaling.",
        "personality": "Direct, data-driven, energetic, no-nonsense. Gives honest feedback even when it's hard to hear. Focused on execution.",
        "avatar": "https://cdn-icons-png.flaticon.com/512/3135/3135715.png",
        "category": "Business",
        "creator": "VentureAI",
        "chats": "7.3M",
        "greetings": [
            "Hey! I've seen hundreds of pitches and helped build companies from zero to IPO. Cut the fluff -- tell me about your startup idea.",
            "Welcome! Whether you're pre-seed or Series B, I can help. What's your biggest challenge right now?",
        ],
        "responses": [
            "Okay, let me be real with you -- the idea matters less than execution. Who are your first 10 customers, and what problem are you solving for them TODAY?",
            "I like the ambition, but let's pressure-test this. What's your unfair advantage? Why can YOUR team win where others have failed?",
            "Here's what VCs really look for: a massive market, a team that can execute, and evidence of traction. Which of these three is your strongest card?",
        ],
        "tag": "business",
    },
    {
        "id": "fitness_coach",
        "name": "Coach Marcus",
        "tagline": "Personal Fitness Trainer",
        "description": "An energetic and knowledgeable personal trainer who specializes in strength training, nutrition, and building sustainable fitness habits.",
        "personality": "Motivating, energetic, supportive but pushes you out of your comfort zone. Science-based approach to fitness.",
        "avatar": "https://cdn-icons-png.flaticon.com/512/3048/3048127.png",
        "category": "Wellness",
        "creator": "FitAI",
        "chats": "5.5M",
        "greetings": [
            "Let's GO! I'm Coach Marcus, and I'm here to help you become the strongest version of yourself. What are your fitness goals?",
            "Hey champion! Whether you're just starting out or looking to break a plateau, I've got your back. What's your current routine look like?",
        ],
        "responses": [
            "Great question! The key is progressive overload -- gradually increasing the challenge. What does your current training split look like?",
            "Love the dedication! But remember, recovery is where the magic happens. Sleep, nutrition, and rest days are just as important as the training itself.",
            "Here's what I'd recommend: focus on compound movements first -- squats, deadlifts, bench press, overhead press. These give you the most bang for your buck.",
        ],
        "tag": "fitness",
    },
    {
        "id": "detective",
        "name": "Detective Noir",
        "tagline": "Hardboiled Detective",
        "description": "A classic film noir detective from 1940s Los Angeles. Solves mysteries with sharp wit and sharper instincts. Great for roleplay and mystery games.",
        "personality": "Cynical, witty, observant, world-weary but ultimately good-hearted. Speaks in noir narration style.",
        "avatar": "https://cdn-icons-png.flaticon.com/512/3429/3429691.png",
        "category": "Roleplay",
        "creator": "NoirStudios",
        "chats": "4.2M",
        "greetings": [
            "The rain was coming down like it had a personal grudge against the city. Then you walked through my door. Something tells me you've got a story. Spill it.",
            "Another night, another case. The city never sleeps, and neither do I. What brings you to my office at this hour?",
        ],
        "responses": [
            "Interesting... very interesting. In my line of work, you learn that everyone's got something to hide. The question is -- what are they hiding from?",
            "I've seen a lot of things in this city, pal. And something about your story doesn't add up. Let's go over the details one more time.",
            "You know what they say -- follow the money. Every case, every time. Now, who stands to gain the most from all this?",
        ],
        "tag": "roleplay",
    },
    {
        "id": "science_explainer",
        "name": "Dr. Nova",
        "tagline": "Science Communicator",
        "description": "An enthusiastic science communicator who makes complex topics accessible and exciting. Expert in physics, biology, chemistry, and astronomy.",
        "personality": "Enthusiastic, clear, loves analogies and 'mind-blown' moments. Makes science feel like an adventure.",
        "avatar": "https://cdn-icons-png.flaticon.com/512/2436/2436874.png",
        "category": "Education",
        "creator": "ScienceAI",
        "chats": "8.9M",
        "greetings": [
            "Hey there, curious mind! I'm Dr. Nova, and I think science is the most exciting adventure there is. What do you want to explore today?",
            "Welcome to the lab! Whether it's black holes, DNA, or quantum weirdness -- I can explain it in a way that'll blow your mind. What are you curious about?",
        ],
        "responses": [
            "Ooh, great question! Okay, think of it this way... *grabs whiteboard* Imagine the universe is like a giant trampoline. Now, when you place a bowling ball on it...",
            "That's one of my FAVORITE topics! Here's the mind-blowing part that most people don't know... the answer actually connects to something completely unexpected.",
            "Love it! Let me break this down with an analogy. Think of cells like tiny cities. Each organelle is a building with a specific job...",
        ],
        "tag": "science",
    },
    {
        "id": "music_producer",
        "name": "DJ Rhythm",
        "tagline": "Music Producer & DJ",
        "description": "A Grammy-nominated music producer and DJ who has worked across genres from hip-hop to electronic. Expert in music theory, production, and the industry.",
        "personality": "Creative, laid-back, passionate about sound. Mixes technical knowledge with artistic intuition.",
        "avatar": "https://cdn-icons-png.flaticon.com/512/3844/3844724.png",
        "category": "Creative",
        "creator": "BeatLab",
        "chats": "3.6M",
        "greetings": [
            "Yo, what's good! I'm DJ Rhythm. Whether you want to produce your first beat or mix a killer set, let's make some noise. What's your vibe?",
            "Welcome to the studio! Music is the universal language, and I'm here to help you speak it fluently. What genre are you vibing with?",
        ],
        "responses": [
            "Nice! Here's a pro tip: start with the groove. Get the drums and bass locked in first, and everything else will fall into place naturally.",
            "That's fire! Now, the secret sauce is in the arrangement. Don't just loop -- build tension, create drops, and give the listener a journey.",
            "I hear you! Music production is 50% technical, 50% emotional. The best producers know the rules well enough to break them creatively.",
        ],
        "tag": "music",
    },
]

CATEGORIES = ["All", "Historical", "Education", "Creative", "Wellness", "Business", "Roleplay"]


# ==========================================
# PAGE CONFIG & GLOBAL CSS
# ==========================================
st.set_page_config(page_title="character.ai", page_icon="https://cdn-icons-png.flaticon.com/512/4712/4712035.png", layout="wide")

# Initialize session state
if "page" not in st.session_state:
    st.session_state.page = "home"
if "selected_character" not in st.session_state:
    st.session_state.selected_character = None
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "selected_category" not in st.session_state:
    st.session_state.selected_category = "All"

st.markdown("""
<style>
    /* ---- GLOBAL ---- */
    .stApp {
        background-color: #1a1a2e;
        color: #e0e0e0;
    }
    [data-testid="stHeader"] {
        background-color: #1a1a2e;
    }
    [data-testid="stSidebar"] {
        background-color: #16213e;
        border-right: 1px solid #2a2a4a;
    }

    /* ---- TOP NAV BAR ---- */
    .nav-bar {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 12px 20px;
        background: linear-gradient(135deg, #16213e 0%, #1a1a2e 100%);
        border-bottom: 1px solid #2a2a4a;
        margin: -1rem -1rem 1.5rem -1rem;
    }
    .nav-logo {
        display: flex;
        align-items: center;
        gap: 10px;
    }
    .nav-logo-text {
        font-size: 24px;
        font-weight: 800;
        background: linear-gradient(135deg, #a78bfa, #818cf8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -0.5px;
    }
    .nav-subtitle {
        font-size: 12px;
        color: #6b7280;
        margin-top: -2px;
    }

    /* ---- SEARCH BAR ---- */
    .search-container {
        max-width: 500px;
        margin: 0 auto 24px auto;
    }
    .stTextInput > div > div > input {
        background-color: #2a2a4a !important;
        border: 1px solid #3a3a5a !important;
        border-radius: 24px !important;
        color: #e0e0e0 !important;
        padding: 12px 20px !important;
        font-size: 15px !important;
    }
    .stTextInput > div > div > input:focus {
        border-color: #818cf8 !important;
        box-shadow: 0 0 0 2px rgba(129, 140, 248, 0.2) !important;
    }
    .stTextInput > div > div > input::placeholder {
        color: #6b7280 !important;
    }

    /* ---- CATEGORY TABS ---- */
    .category-tabs {
        display: flex;
        gap: 8px;
        margin-bottom: 24px;
        flex-wrap: wrap;
        justify-content: center;
    }
    .cat-tab {
        padding: 8px 20px;
        border-radius: 20px;
        font-size: 14px;
        font-weight: 500;
        cursor: pointer;
        transition: all 0.2s ease;
        border: none;
        text-decoration: none;
        display: inline-block;
    }
    .cat-tab-active {
        background: linear-gradient(135deg, #7c3aed, #6366f1);
        color: white;
    }
    .cat-tab-inactive {
        background-color: #2a2a4a;
        color: #9ca3af;
    }
    .cat-tab-inactive:hover {
        background-color: #3a3a5a;
        color: #e0e0e0;
    }

    /* ---- CHARACTER CARDS ---- */
    .char-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
        gap: 16px;
        padding: 0 4px;
    }
    .char-card {
        background: linear-gradient(145deg, #1e1e3a, #252547);
        border: 1px solid #2a2a4a;
        border-radius: 16px;
        padding: 20px;
        transition: all 0.3s ease;
        cursor: pointer;
    }
    .char-card:hover {
        border-color: #818cf8;
        transform: translateY(-4px);
        box-shadow: 0 8px 25px rgba(99, 102, 241, 0.15);
    }
    .char-card-header {
        display: flex;
        align-items: center;
        gap: 12px;
        margin-bottom: 12px;
    }
    .char-avatar {
        width: 56px;
        height: 56px;
        border-radius: 50%;
        object-fit: cover;
        border: 2px solid #3a3a5a;
    }
    .char-name {
        font-size: 16px;
        font-weight: 700;
        color: #e0e0e0;
        margin: 0;
    }
    .char-tagline {
        font-size: 13px;
        color: #818cf8;
        margin: 2px 0 0 0;
    }
    .char-desc {
        font-size: 13px;
        color: #9ca3af;
        line-height: 1.5;
        margin: 8px 0;
        display: -webkit-box;
        -webkit-line-clamp: 3;
        -webkit-box-orient: vertical;
        overflow: hidden;
    }
    .char-footer {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-top: 12px;
        padding-top: 12px;
        border-top: 1px solid #2a2a4a;
    }
    .char-creator {
        font-size: 12px;
        color: #6b7280;
    }
    .char-chats {
        font-size: 12px;
        color: #6b7280;
    }

    /* ---- CHAT PAGE ---- */
    .chat-header {
        display: flex;
        align-items: center;
        gap: 16px;
        padding: 16px 20px;
        background: linear-gradient(135deg, #16213e 0%, #1e1e3a 100%);
        border-bottom: 1px solid #2a2a4a;
        border-radius: 12px;
        margin-bottom: 20px;
    }
    .chat-avatar {
        width: 48px;
        height: 48px;
        border-radius: 50%;
        object-fit: cover;
        border: 2px solid #818cf8;
    }
    .chat-char-name {
        font-size: 20px;
        font-weight: 700;
        color: #e0e0e0;
        margin: 0;
    }
    .chat-char-tagline {
        font-size: 13px;
        color: #818cf8;
        margin: 0;
    }

    /* ---- MESSAGE BUBBLES ---- */
    .msg-container {
        display: flex;
        gap: 12px;
        margin-bottom: 16px;
        max-width: 85%;
    }
    .msg-container-user {
        margin-left: auto;
        flex-direction: row-reverse;
    }
    .msg-avatar-small {
        width: 36px;
        height: 36px;
        border-radius: 50%;
        object-fit: cover;
        flex-shrink: 0;
        margin-top: 4px;
    }
    .msg-bubble {
        padding: 12px 16px;
        border-radius: 18px;
        font-size: 14px;
        line-height: 1.6;
    }
    .msg-bubble-ai {
        background-color: #252547;
        color: #e0e0e0;
        border-bottom-left-radius: 4px;
    }
    .msg-bubble-user {
        background: linear-gradient(135deg, #7c3aed, #6366f1);
        color: white;
        border-bottom-right-radius: 4px;
    }
    .msg-name {
        font-size: 12px;
        font-weight: 600;
        color: #818cf8;
        margin-bottom: 4px;
    }

    /* ---- BUTTONS ---- */
    .stButton > button {
        border-radius: 12px;
        font-weight: 600;
        transition: all 0.2s ease;
    }
    .back-btn button {
        background-color: #2a2a4a !important;
        color: #e0e0e0 !important;
        border: 1px solid #3a3a5a !important;
        border-radius: 12px !important;
    }
    .back-btn button:hover {
        background-color: #3a3a5a !important;
        border-color: #818cf8 !important;
    }

    /* ---- CHAT INPUT ---- */
    [data-testid="stChatInput"] textarea {
        background-color: #2a2a4a !important;
        border: 1px solid #3a3a5a !important;
        border-radius: 24px !important;
        color: #e0e0e0 !important;
    }

    /* ---- HIDE STREAMLIT DEFAULTS ---- */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    [data-testid="stToolbar"] {visibility: hidden;}

    /* ---- SECTION TITLE ---- */
    .section-title {
        font-size: 18px;
        font-weight: 700;
        color: #e0e0e0;
        margin: 24px 0 16px 4px;
    }

    /* ---- FEATURED BANNER ---- */
    .featured-banner {
        background: linear-gradient(135deg, #312e81, #4c1d95, #5b21b6);
        border-radius: 16px;
        padding: 32px;
        margin-bottom: 24px;
        text-align: center;
    }
    .featured-title {
        font-size: 28px;
        font-weight: 800;
        color: white;
        margin: 0 0 8px 0;
    }
    .featured-sub {
        font-size: 15px;
        color: #c4b5fd;
        margin: 0;
    }
</style>
""", unsafe_allow_html=True)


# ==========================================
# NAVIGATION / ROUTING
# ==========================================
def go_home():
    st.session_state.page = "home"
    st.session_state.selected_character = None
    st.session_state.chat_history = []


def go_chat(char_id):
    st.session_state.page = "chat"
    st.session_state.selected_character = char_id
    st.session_state.chat_history = []


def get_character(char_id):
    for c in CHARACTERS:
        if c["id"] == char_id:
            return c
    return None


# ==========================================
# SIDEBAR
# ==========================================
with st.sidebar:
    st.markdown("""
    <div style="text-align:center; padding: 16px 0;">
        <div style="font-size: 28px; font-weight: 800;
            background: linear-gradient(135deg, #a78bfa, #818cf8);
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
            character.ai
        </div>
        <div style="font-size: 12px; color: #6b7280; margin-top: 4px;">
            Where imagination meets intelligence
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    if st.button("Home", use_container_width=True, key="nav_home"):
        go_home()
        st.rerun()

    st.markdown("#### Recent Chats")
    if st.session_state.selected_character:
        char = get_character(st.session_state.selected_character)
        if char:
            st.markdown(f"""
            <div style="padding: 10px; background: #252547; border-radius: 10px;
                        border-left: 3px solid #818cf8; margin-bottom: 8px;">
                <div style="font-size: 14px; font-weight: 600; color: #e0e0e0;">
                    {char['name']}
                </div>
                <div style="font-size: 12px; color: #6b7280;">
                    {len(st.session_state.chat_history)} messages
                </div>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style="font-size: 13px; color: #6b7280; padding: 8px;">
            No recent chats. Pick a character to start!
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("#### Settings")
    api_key_input = st.text_input(
        "OpenAI API Key (optional)",
        type="password",
        help="Add an API key for real AI responses. Leave empty for simulation mode.",
        key="api_key_sidebar",
    )
    if api_key_input:
        st.session_state["openai_api_key"] = api_key_input
        st.success("AI Mode Active")

    st.markdown("---")
    st.markdown("""
    <div style="font-size: 11px; color: #4b5563; text-align: center; padding: 8px;">
        Built with Streamlit<br>Simulation Mode Active
    </div>
    """, unsafe_allow_html=True)


# ==========================================
# HOME PAGE
# ==========================================
def render_home():
    # Featured banner
    st.markdown("""
    <div class="featured-banner">
        <p class="featured-title">Where conversations come alive</p>
        <p class="featured-sub">Chat with AI-powered characters -- from historical figures to creative helpers</p>
    </div>
    """, unsafe_allow_html=True)

    # Search bar
    search_query = st.text_input(
        "Search",
        placeholder="Search for characters...",
        label_visibility="collapsed",
        key="search_input",
    )

    # Category filter tabs
    cols = st.columns(len(CATEGORIES))
    for i, cat in enumerate(CATEGORIES):
        with cols[i]:
            is_active = st.session_state.selected_category == cat
            if st.button(
                cat,
                key=f"cat_{cat}",
                use_container_width=True,
                type="primary" if is_active else "secondary",
            ):
                st.session_state.selected_category = cat
                st.rerun()

    st.markdown("")

    # Filter characters
    filtered = CHARACTERS
    if st.session_state.selected_category != "All":
        filtered = [c for c in filtered if c["category"] == st.session_state.selected_category]
    if search_query:
        q = search_query.lower()
        filtered = [
            c for c in filtered
            if q in c["name"].lower() or q in c["tagline"].lower() or q in c["description"].lower()
        ]

    if not filtered:
        st.markdown("""
        <div style="text-align: center; padding: 60px; color: #6b7280;">
            <div style="font-size: 48px; margin-bottom: 12px;">&#128373;</div>
            <div style="font-size: 16px;">No characters found. Try a different search or category.</div>
        </div>
        """, unsafe_allow_html=True)
        return

    # Section title
    cat_label = st.session_state.selected_category if st.session_state.selected_category != "All" else "Featured"
    st.markdown(f'<div class="section-title">{cat_label} Characters</div>', unsafe_allow_html=True)

    # Character grid (3 columns)
    cols_per_row = 3
    for row_start in range(0, len(filtered), cols_per_row):
        row_chars = filtered[row_start:row_start + cols_per_row]
        cols = st.columns(cols_per_row)
        for idx, char in enumerate(row_chars):
            with cols[idx]:
                st.markdown(f"""
                <div class="char-card">
                    <div class="char-card-header">
                        <img class="char-avatar" src="{char['avatar']}" alt="{char['name']}"
                             onerror="this.src='https://cdn-icons-png.flaticon.com/512/4712/4712035.png'">
                        <div>
                            <p class="char-name">{char['name']}</p>
                            <p class="char-tagline">{char['tagline']}</p>
                        </div>
                    </div>
                    <p class="char-desc">{char['description']}</p>
                    <div class="char-footer">
                        <span class="char-creator">By {char['creator']}</span>
                        <span class="char-chats">{char['chats']} chats</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)

                if st.button(f"Chat with {char['name']}", key=f"chat_{char['id']}", use_container_width=True):
                    go_chat(char["id"])
                    st.rerun()


# ==========================================
# CHAT PAGE
# ==========================================
def render_chat():
    char = get_character(st.session_state.selected_character)
    if not char:
        go_home()
        st.rerun()
        return

    # Back button
    col_back, col_spacer = st.columns([1, 5])
    with col_back:
        st.markdown('<div class="back-btn">', unsafe_allow_html=True)
        if st.button("< Back", key="back_btn"):
            go_home()
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    # Chat header
    st.markdown(f"""
    <div class="chat-header">
        <img class="chat-avatar" src="{char['avatar']}" alt="{char['name']}"
             onerror="this.src='https://cdn-icons-png.flaticon.com/512/4712/4712035.png'">
        <div>
            <p class="chat-char-name">{char['name']}</p>
            <p class="chat-char-tagline">{char['tagline']} &bull; {char['chats']} chats</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Show initial greeting if no messages yet
    if not st.session_state.chat_history:
        greeting = random.choice(char.get("greetings", [f"Hello! I'm {char['name']}."]))
        st.session_state.chat_history.append({
            "role": "assistant",
            "content": greeting,
        })

    # Render chat messages
    for msg in st.session_state.chat_history:
        if msg["role"] == "assistant":
            st.markdown(f"""
            <div class="msg-container">
                <img class="msg-avatar-small" src="{char['avatar']}"
                     onerror="this.src='https://cdn-icons-png.flaticon.com/512/4712/4712035.png'">
                <div>
                    <div class="msg-name">{char['name']}</div>
                    <div class="msg-bubble msg-bubble-ai">{msg['content']}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="msg-container msg-container-user">
                <img class="msg-avatar-small" src="https://cdn-icons-png.flaticon.com/512/3177/3177440.png">
                <div>
                    <div class="msg-name" style="text-align:right; color: #a78bfa;">You</div>
                    <div class="msg-bubble msg-bubble-user">{msg['content']}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    # Chat input
    if user_input := st.chat_input(f"Message {char['name']}..."):
        # Add user message
        st.session_state.chat_history.append({
            "role": "user",
            "content": user_input,
        })

        # Get AI response
        with st.spinner(f"{char['name']} is typing..."):
            response = get_ai_response(char, user_input)

        st.session_state.chat_history.append({
            "role": "assistant",
            "content": response,
        })
        st.rerun()


# ==========================================
# ROUTER
# ==========================================
if st.session_state.page == "chat" and st.session_state.selected_character:
    render_chat()
else:
    render_home()
