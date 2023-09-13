from PyPDF2 import PdfReader
import backend.openai_LLM as openai_LLM
import requests
from bs4 import BeautifulSoup
import re


def get_JobData(job_link):
    try:
        response = requests.get(job_link)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            # Extract all text from the page
            all_text = soup.get_text()
            cleaned_string = re.sub(r'^\s*$', '', all_text, flags=re.MULTILINE)
            
            return cleaned_string

        else:
            print(
                f"Failed to retrieve the page. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None


def read_pdf(pdf):
    rawData = PdfReader(pdf)
    text = rawData.pages[0].extract_text()
    # print(text)
    return text


def split_subsections(pdf):
    pdfData = read_pdf(pdf)
    question = f'Separate this document into subsections by each job or experience and add a new line character and 15 dashes after each sub-sub section. {pdfData}'
    init_prompt = "You are an AI assistant that separates sections in the resume."
    output = openai_LLM.prompt(init_prompt, question)
    return str(output).split('---------------')


def edit_resume_section(job_desc, resume_sub_section):
    question = f'This is the job description: \n {job_desc}. Edit this resume based on the job description.\n {resume_sub_section}'
    init_prompt = "You are an AI assistant that takes in a part of a resume and edits it based on the below job description."
    init_prompt1 = "Please analyze my resume and the job description I'm targeting. Based on your analysis, automatically edit my resume to tailor it to the job description. After the edits, provide me with the finalized and edited resume for view. If I have any specific preferences or further instructions, I'll let you know during the process. Let's get started!"
    output = openai_LLM.prompt(init_prompt1, question)

    return output


def edit_resume_subsection():
    pdfPath = "../test-data/Resume_Harsh_Muriki_SWE.pdf"

    with open("../test-data/job-description-1.txt", "r") as myfile:
        job_desc = myfile.read()

    # print(job_desc)
    sections = split_subsections(pdfPath)
    print("Finished dividing the sections")
    print(len(sections))

    for i in sections:
        print("\n\n")
        print("!!!Section: ", i)
        print("------END-----")

    for sub_section in sections:
        new_section = edit_resume_section(job_desc, sub_section)

        print("Old Section:", sub_section)
        print("New Section", new_section)
        print("--------")


def edit_complete_resume(resumePath, jobDescription):

    # with open(jobDesPath, "r") as myfile:
    #     job_desc = myfile.read()

    resume_Data = read_pdf(resumePath)

    # Edit this prompt
    question = f'This is the job description: \n {jobDescription}. Edit this resume based on the job description.\n {resume_Data}'
    init_prompt = "You are an AI assistant that takes in a part of a resume and edits it based on the below job description."
    init_prompt1 = "Please analyze my resume and the job description I'm targeting. Based on your analysis, automatically edit my resume to tailor it to the job description. After the edits, provide me with the finalized and edited resume for view. If I have any specific preferences or further instructions, I'll let you know during the process. Let's get started!"
    output = openai_LLM.openai_prompt(init_prompt1, question)

    return output


def convert_to_latex(editedResume, sourcefile="public\jakeresume.txt"):

    with open(sourcefile, "r") as myfile:
        jakeresumetemplate = myfile.read()

    question = f'This is my resume: \n\n {editedResume}. \n\n Edit this based on the given latex file format.'
    init_prompt = f'This is the latex file that I want you to convert my resume into this format so that it fits in one page without editing the main content and removing any special symbols \n\n {jakeresumetemplate}'
    output = openai_LLM.openai_prompt(init_prompt, question)

    return output


def get_JobDescription(allWebsiteData):

    init_prompt = ""
    question = f'This is all the Job data: \n\n{allWebsiteData}. Condense all this data and give me all the technical and non-technical requirements but do not change any of the technical terms'
    output = openai_LLM.openai_prompt(init_prompt, question)

    return output
