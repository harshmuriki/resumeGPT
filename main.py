# import backend.model as model
from backend.model import LlamaThread

file = open("test-data/harsh-resume-raw.txt", mode="r")

raw_data = file.read()

job_desc = open("test-data/job-description-1.txt", mode="r")

job_description = job_desc.read()

context = f'"My current resume {raw_data}. Edit the resume based on this jobs description {job_description} and give me a suitable resume"'

model = LlamaThread("llama-2-70b-chat")
model.start()
output = model.ask_question("", context)

print(output)