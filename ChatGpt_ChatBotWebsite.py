import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "You are a Dentist."}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Digital Dentist")

demo.launch(share=True)