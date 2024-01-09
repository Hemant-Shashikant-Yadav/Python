from openai import OpenAI



client = OpenAI(
    api_key="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"
)

prompt = "10 car names"

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": prompt
        },
    ],
    model="gpt-3.5-turbo"
)

print(chat_completion.choices[0].message.content)
