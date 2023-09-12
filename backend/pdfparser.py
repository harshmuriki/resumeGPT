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
    init_prompt = "You are an AI assistant that separates sections in the resume."
    output = openai_test.prompt(init_prompt, question)
    return str(output).split('---------------')


def edit_resume_section(job_desc, resume_sub_section):
    question = f'This is the job description: \n {job_desc}. Edit this resume section \n {resume_sub_section} based on the job description.'
    init_prompt = "You are an AI assistant that takes in a part of a resume and edits it based on the below job description."
    output = openai_test.prompt(init_prompt, question)

    return output


def edit_resume():
    pdfPath = "../test-data/Resume_Harsh_Muriki_SWE.pdf"

    with open("../test-data/job-description-1.txt", "r") as myfile:
        job_desc = myfile.read()
        
    resume_Data = read_pdf(pdfPath)

    new_section = edit_resume_section(job_desc, resume_Data)
    print(new_section)
    
    exit()
    # print(job_desc)
    sections = split_subsections(pdfPath)
    print("Finished dividing the sections")
    print(len(sections))
    
    for i in sections:
        print("\n\n")
        print("!!!Section: ", i)
        print("------END-----")
    

    # for sub_section in sections:
    #     new_section = edit_resume_section(job_desc, sub_section)

    #     print("Old Section:", sub_section)
    #     print("New Section", new_section)
    #     print("--------")

edit_resume()
