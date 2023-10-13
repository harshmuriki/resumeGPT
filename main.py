import backend.pdfparser as openaiLLM


resumePath = "test-data/Resume_Yash.pdf"
jobDesPath = "test-data/job-description-1.txt"

job_link = "https://www.linkedin.com/jobs/collections/recommended/?currentJobId=3729882071"
website_data = openaiLLM.get_JobData(job_link)  # scraping

jobDescription = openaiLLM.get_JobDescription(
    job_link)  # gets the job description only

print("jobDescription", jobDescription)

resume_subsections = openaiLLM.edit_resume_subsection(resumePath, jobDescription)
print(resume_subsections)
# edited_resume = openaiLLM.edit_complete_resume(resumePath, jobDescription)

# print("Here is the customized resume")
# print(edited_resume)

# formated_latex = openaiLLM.convert_to_latex(edited_resume)

# print(formated_latex)
# with open('formatexLatex.txt', 'w') as f:
#     f.write(formated_latex)
