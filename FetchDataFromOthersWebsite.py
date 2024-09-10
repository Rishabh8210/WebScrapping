import requests
from bs4 import BeautifulSoup
import time

def findJobs():
    url = 'https://www.timesjobs.com/candidate/job-search.html?searchType=Home_Search&from=submit&asKey=OFF&txtKeywords=&cboPresFuncArea=35'
    htmlText = requests.get(url).text
    soup = BeautifulSoup(htmlText, 'lxml')
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
    print(f'Total {len(jobs)} - jobs found\n')
    i = 1
    for job in jobs:
        jobInfo = job.find('h2')
        jobDescInfo = job.find('ul', class_ = "list-job-dtl clearfix")

        jobCompanyName = job.find('h3', class_ = "joblist-comp-name").text.strip().split('\n')
        jobReq = job.find('ul', class_="top-jd-dtl clearfix")

        jobExp = jobReq.find_all('li')
        keySkillsList = job.find('span', class_ = "srp-skills").text.strip().split(',')
        keySkillStr = ""
        for skill in keySkillsList:
            keySkillStr += skill.strip()
            keySkillStr += ' '

        jobDate = job.find('span', class_ = "sim-posted").text.strip()
        forMoreDetail = jobDescInfo.find('a').get('href')
        print(f"{i} - Job information")
        print(f'Status : {jobDate}')
        print(f'Job Name : {jobInfo.text.strip()}')
        print(f'Company Name : {jobCompanyName[0]}')
        print(f'Skills Required : {keySkillStr}')
        print(f'For more details click here {forMoreDetail}')
        print("\n")
        i = i + 1


if(__name__ == '__main__'):
    while True:
        findJobs()
        # Call the findJobs() function every 10 minutes in an infinite loop
        time.sleep(600)

