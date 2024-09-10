import requests
from bs4 import BeautifulSoup

url = 'https://www.timesjobs.com/candidate/job-search.html?searchType=Home_Search&from=submit&asKey=OFF&txtKeywords=&cboPresFuncArea=35'
htmlText = requests.get(url).text

soup = BeautifulSoup(htmlText, 'lxml')
job = soup.find('li', class_ = 'clearfix job-bx wht-shd-bx')

jobInfo = job.find('h2')
jobDescInfo = job.find('ul', class_ = "list-job-dtl clearfix").li.text.strip().split('\n')

jobCompanyName = job.find('h3', class_ = "joblist-comp-name").text.strip().split('\n')
jobReq = job.find('ul', class_="top-jd-dtl clearfix")

jobExp = jobReq.find_all('li')
keySkillsList = job.find('span', class_ = "srp-skills").text.strip().split(',')
keySkillStr = ""
for skill in keySkillsList:
    keySkillStr += skill.strip()
    keySkillStr += ' '

print(keySkillStr)
print('Job Information')
print(f'Job Name : {jobInfo.text.strip()}')
print(f'Company Name : {jobCompanyName[0]}')
print(f'Skills Required : {keySkillStr}')
