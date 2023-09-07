import together
together.api_key = "998051c798c4822419ca2ad5cfb32fa66d5f33e02666c69e94ca87071f7cd929"


together.Models.start('togethercomputer/LLaMA-2-7B-32K')




output = together.Complete.create(
prompt="Isaac Asimov's Three Laws of Robotics are:\n\n1. ",
model="togethercomputer/LLaMA-2-7B-32K",
max_tokens=70,
temperature=0.6,
top_k=90,
top_p=0.8,
repetition_penalty=1.1,
stop=['</s>']
)


print(output)
