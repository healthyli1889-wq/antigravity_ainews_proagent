from infrastructure import talk_to_artificial_intelligence

def hello_world_agent():
    """
    A multi-modal agent that introduces itself to the world.
    
    Logic Flow:
    1. Input: None (it starts on its own)
    2. Think: Asks the AI to generate a greeting.
    3. Act: Prints the greeting to the screen.
    """
    
    # Step 1: Define what we want the AI to do (The Prompt)
    my_instruction = "Please generate a friendly hello world message for a new user learning about AI agents."
    
    # Step 2: Send it to the 'Brain' (The Function Call)
    print("Agent is thinking...")
    response = talk_to_artificial_intelligence(my_instruction)
    
    # Step 3: Output the result
    print("Agent says:")
    print(response)

if __name__ == "__main__":
    hello_world_agent()
