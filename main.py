# import backend.model as model
from backend.model import LlamaThread

file = open("test-data/harsh-resume-raw.txt", mode="r")

raw_data = file.read()

job_desc = open("test-data/job-description-1.txt", mode="r")

job_description = job_desc.read()

context = f'"This is my current resume: {raw_data}. EDIT the resume based on this jobs description {job_description} and give me a suitable resume"'

question = f'"This is my resume {raw_data}. \n\n I want you to act as an ai resume editor giving me just the edited, newer version of my resume based on this job description: {job_description}. \n\n"'
# print(question)


question = prompt + f'"\nThis is my resume {raw_data}. \n\n Job description: {job_description}."'
model = LlamaThread("llama-2-7b-chat")
model.start()
output = model.ask_question("", question)

print(output)
