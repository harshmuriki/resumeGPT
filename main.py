import backend.pdfparser as openaiLLM


resumePath = "test-data/Resume_Harsh_Muriki_SWE.pdf"
jobDesPath = "test-data/job-description-1.txt"

job_link = "https://jobs.lever.co/picklerobot/4b6b262e-a821-44f9-80b6-7f4067de36ac"
website_data = openaiLLM.get_JobData(job_link)  # scraping

exit()
jobDescription = openaiLLM.get_JobDescription(
    job_link)  # gets the job description only

print("jobDescription", jobDescription)

edited_resume = openaiLLM.edit_complete_resume(resumePath, jobDescription)

print(edited_resume)

formated_latex = openaiLLM.convert_to_latex(edited_resume)

# print(formated_latex)
with open('formatexLatex.txt', 'w') as f:
    f.write(formated_latex)
