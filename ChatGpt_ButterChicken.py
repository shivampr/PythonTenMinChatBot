import openai

openai.api_key = "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"

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Suggest 3 places in Delhi which serves authentic Butter Chicken and has good ratings."}])
print(completion.choices[0].message.content)