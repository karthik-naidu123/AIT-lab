import os
import openai
import gradio as gr

# ✅ Load your OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# System role prompt
messages = [
    {"role": "system", "content": "You are a financial expert specializing in real estate investment and negotiation."}
]

# Chat function
def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    
    return ChatGPT_reply

# Gradio interface
demo = gr.Interface(
    fn=CustomChatGPT,
    inputs="text",
    outputs="text",
    title="🏠 Intelligent Real Estate Chatbot",
    description="A chatbot specialized in real estate investment and negotiation advice."
)

# Launch app
if __name__ == "__main__":
    demo.launch(share=True)
  
