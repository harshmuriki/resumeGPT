import openai


def openai_prompt(init_prompt, question):
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
        model="gpt-3.5-turbo-16k",
        messages=[
            {"role": "system", "content": init_prompt},
            {"role": "user", "content": question}
        ]
    )

    # response = openai.Completion.create(
    #     engine="text-embedding-ada-002",  # You can choose the appropriate engine
    #     prompt=question,
    #     max_tokens=16385  # Adjust this number to control the length of the response
    # )
    # generated_text = response.choices[0].text

    # arr = response["choices"][0]["text"]

    arr = response.choices[0].message.content

    return arr
