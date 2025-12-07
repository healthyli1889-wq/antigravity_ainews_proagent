from infrastructure import talk_to_artificial_intelligence

    # Agent 1: The Miner
def miner_agent(topic):
    """
    Goal: Mine and extract the MOST VALUABLE sources from the messy world.
    Input: A topic string (e.g. "Generative AI")
    Output: A list of text extracted from only the BEST sources.
    """
    print(f"\n--- [Agent 1: Miner] Mining 'Profound' info on: {topic} ---")
    
    # In a real scenario, this would use Google Search + a filtering step.
    # We simulate the filtering here.
    print("  > Searching the web for top-tier sources...")
    print("  > Filtering out noise (low quality news, clickbait)...")
    print("  > Extracting 'Diamond' grade information...")
    
    # Simulating that we found 100 links but only kept the top 3 "Profound" ones
    best_data = [
        f"Source (Deep Technical Paper): {topic} architecture is shifting towards Sparse MoE models...",
        f"Source (Insider Analysis): The market consolidation for {topic} is creating a winner-take-all dynamic...",
        f"Source (Expert Interview): The unspoken truth about {topic} is that 90% of current use cases are invalid..."
    ]
    
    return best_data

# Agent 2: The Analyst
def analyst_agent(raw_data_list):
    """
    Goal: Analyze sources and provide the BOTTOM LINE summary.
    Input: List of raw text strings.
    Output: A "World-Class" deep analysis string.
    """
    print("\n--- [Agent 2: Analyst] Performing Deep Analysis ---")
    
    # Combine data for the brain
    combined_text = "\n".join(raw_data_list)
    
    # UPDATED PROMPT: Requesting "Profound" analysis
    prompt = (
        f"Analyze these high-quality sources about the topic.\n"
        f"Do NOT give me a basic summary.\n"
        f"Give me the 'Bottom Line' truth that no one else is seeing.\n"
        f"Find the hidden patterns and the most profound insight.\n"
        f"Sources:\n{combined_text}"
    )
    
    analysis = talk_to_artificial_intelligence(prompt)
    return analysis

# Agent 3: The Integrator
def integrator_agent(analysis_text, user_profile):
    """
    Goal: Nurture the user. Tell them EXACTLY what this means for them.
    Input: Analysis text, User profile dictionary.
    Output: Personalized "What this means for you" section.
    """
    print(f"\n--- [Agent 3: Integrator] Personalizing for {user_profile['role']} ---")
    
    prompt = (
        f"The user is a {user_profile['role']}.\n"
        f"Here is a deep market analysis: {analysis_text}\n"
        f"Tell this user EXACTLY what this means for their career and wallet.\n"
        f"Be specific. No fluff. Give them a competitive advantage."
    )
    
    personalized_insight = talk_to_artificial_intelligence(prompt)
    return personalized_insight

# Agent 4: The Output Guide (The "Result" Agent)
def output_agent(personalized_insight, user_role, demand="build_audience"):
    """
    Goal: Feed the user with RESULTS. Help them build audience and make money.
    Input: Insight text, user role, specific demand.
    Output: A strategy guide for self-promotion and monetization.
    """
    print(f"\n--- [Agent 4: Output Guide] Generating 'Money-Making' Strategy ({demand}) ---")
    
    # UPDATED PROMPT: Focus on Results (Money, Audience)
    prompt = (
        f"User Goal: {demand} (and ultimately, Make Money).\n"
        f"Insight to Leverage: '{personalized_insight}'\n"
        f"Create a 'Content Guide' or 'Strategy' for this user.\n"
        f"1. Give them the Keyword Magic bits for SEO/Virality.\n"
        f"2. Write a viral hook for LinkedIn/Twitter.\n"
        f"3. Explain how to monetize this specific insight.\n"
        f"4. Match their content with users who are searching similar keywords.\n"
        f"5. Generate the content that tailored to each of the user groups.\n"
        f"Help them self-promote effectively."
    )
    
    final_output = talk_to_artificial_intelligence(prompt)
    return final_output
