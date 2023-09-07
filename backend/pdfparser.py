from PyPDF2 import PdfReader
from model import LlamaThread
import openai_test

def read_pdf(pdf):
    rawData = PdfReader(pdf)
    text = rawData.pages[0].extract_text()
    # print(text)

    return text


def split_subsections(pdf):
    pdfData = read_pdf(pdf)
    question = f'Separate this document into subsections by each job or experience and add a new line character and 15 dashes after each sub-sub section. {pdfData}'
    # print(question)
    # model = LlamaThread("llama-2-70b-chat")
    # model.start()
    # output = model.ask_question(question)
    output = openai_test.prompt(question)
    # output = huggingface.query(question)

    # print(output)
    
    return str(output).split('---------------')


pdfPath = "../test-data/Resume_Harsh_Muriki_SWE.pdf"

opt = split_subsections(pdfPath)

print(opt)

# from gpt4all import GPT4All
# model = GPT4All("orca-mini-3b.ggmlv3.q4_0.bin")
# output = model.generate("The capital of France is ", max_tokens=3)
# print(output)
