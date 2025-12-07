import time

def talk_to_artificial_intelligence(prompt):
    """
    This function simulates sending a message to a powerful AI like Gemini or GPT.
    
    In a real app, this would use an API key and send a request over the internet.
    For this learning phase, we will return a simulated response so you can see
    how the logic works without needing to pay for keys yet.
    """
    print(f"\n[System] Sending data to AI Brain...\n[Prompt]: {prompt[:50]}... (truncated)\n")
    time.sleep(1) # Simulate thinking time
    
    # Simple logic to return fake answers based on what we asked
    # In the future, we replace this massive 'if' logic with a real AI call.
    
    lower_prompt = prompt.lower()
    
    if "hello" in lower_prompt:
        return "Hello! I am your AI assistant. I am ready to help you build your agent system."
        
    if "summarize" in lower_prompt:
        return "This is a summary of the text you provided. The key takeaway is that agents are powerful tools for automation."
        
    if "extract" in lower_prompt:
        return "- Source A: High value\n- Source B: Medium value\n- Source C: Low value"
    
    return "I received your instruction. As a simulated AI, I acknowledge this request."

# Educational Comment:
# An "Interface" is just a standard way to interact with something.
# Here, 'talk_to_artificial_intelligence' is our interface to the Brain.
