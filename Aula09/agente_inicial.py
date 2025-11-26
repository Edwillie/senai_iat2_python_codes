import os
import google.generativeai as genai

# -------------------------------
# 1. Set up your API key
# -------------------------------
# Make sure you have set your API key as an environment variable:
#   export GEMINI_API_KEY="your_api_key_here"
# or set it directly in code (not recommended for production)
api_key = 'AIzaSyDxngFJdW7MQl-UkkHf7bPQhcx-XdleH50' #os.getenv("GEMINI_API_KEY")
if not api_key:
    raise EnvironmentError("Please set the GEMINI_API_KEY environment variable.")

genai.configure(api_key=api_key)

# -------------------------------
# 2. Create the model
# -------------------------------
model = genai.GenerativeModel("gemini-2.5-flash")

# -------------------------------
# 3. Agent loop
# -------------------------------
print("🤖 Gemini Agent is ready! Type 'exit' to quit.\n")

# Maintain conversation history for context
history = []

while True:
    try:
        user_input = input("You: ").strip()
        if user_input.lower() in {"exit", "quit"}:
            print("Agent: Goodbye! 👋")
            break

        # Append user message to history
        history.append({"role": "user", "parts": [user_input]})

        # Send request with conversation history
        response = model.generate_content(history)

        # Extract and print the model's reply
        reply = response.text.strip()
        print(f"Agent: {reply}")

        # Append model reply to history
        history.append({"role": "model", "parts": [reply]})

    except KeyboardInterrupt:
        print("\nAgent: Goodbye! 👋")
        break
    except Exception as e:
        print(f"⚠️ Error: {e}")
