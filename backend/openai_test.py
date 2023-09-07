import openai


def prompt(question):
    openai.api_key = "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"

    # response = openai.ChatCompletion.create(
    #     model="gpt-3.5-turbo-0613",
    #     prompt=question,
    #     temperature=0.7,
    #     max_tokens=5000,
    #     top_p=1,
    #     frequency_penalty=0,
    #     presence_penalty=0,
    #     messages=""
    # )

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question}
        ]
    )

    print()

    # arr = response["choices"][0]["text"]

    arr = response.choices[0].message.content

    return arr
