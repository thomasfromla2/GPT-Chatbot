# GPT-3 text Interface 

# Chatbot that retains the conversation : Works!
#    To Do: 
#         pre-prompt with a personality file
#         have it sum up and save the conversation
#         have it send commands to the serial port
#         add voice INPUT
#         add voice OUTPUT
#         add higher level commands

# # WORKS!  WORKS!  WORKS!  WORKS!  WORKS!  WORKS!  WORKS!  WORKS!  WORKS! 

import openai #for the GPT 3 library

openai.api_key = "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" 

# Initialize conversation history as an empty list
conversation_history = ["User: How are you"]

def chat_with_openai(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=50  # You can adjust this for desired response length
        )

        return response.choices[0].text.strip()

    except Exception as e:
        return str(e)

# Example usage:
print("Bruce: Hello! How are you today?")
while True:
    user_input = input("User: ")
    if user_input.lower() == "bye":
        break

    conversation_history.append(f"User: {user_input}") # Add user input to the conversation history

    # Combine conversation history into a single prompt
    prompt = "\n".join(conversation_history)
    response = chat_with_openai(prompt)

    
    conversation_history.append(f"Bruce: {response}") # Add AI response to the conversation history

    # Display AI response
    #print(f"Bruce: {response}")
    print(f"{response}")



