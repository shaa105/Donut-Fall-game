from openai import OpenAI

#client = OpenAI(api_key="your_own_OpenAI_api_key")
prompt = ""

while True:
    prompt = input("You :")
    chat_completion = client.chat.completions.create(
        messages= [
            {"role": "user", "content": prompt}
        ],
        model="gpt-3.5"
    )

    response = chat_completion.choices[0].message
    print("AI :", response)