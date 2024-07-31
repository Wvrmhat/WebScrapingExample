import requests
from bs4 import BeautifulSoup

#!/usr/bin/env python3

def main():
    URL = "https://realpython.github.io/fake-jobs/"
    page = requests.get(URL)

    print(page.text)

    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="ResultsContainer")

    print(results.prettify)

    print("-"*100)

    job_elements = results.find_all("div", class_="card-content")           # Find elements by HTML class name
    for job_element in job_elements:
        #print(job_element, end="\n"*2) 
        title_element = job_element.find("h2", class_="title")
        company_element = job_element.find("h3", class_="company")
        location_element = job_element.find("p", class_="location")
        print(title_element.text.strip())
        print(company_element.text.strip())
        print(location_element.text.strip())
        print("-" * 100)

    python_jobs = results.find_all(                             # searches for amount of jobs with python 
        "h2", string= lambda text: "python" in text.lower()
        )
    print(len(python_jobs))

    python_job_elements = [h2_element.parent.parent.parent for h2_element in python_jobs]      # list comprehension
        
    for job_element in python_job_elements:
        #print(job_element, end="\n"*2) 
        title_element = job_element.find("h2", class_="title")
        company_element = job_element.find("h3", class_="company")
        location_element = job_element.find("p", class_="location")
        print(title_element.text.strip())
        print(company_element.text.strip())
        print(location_element.text.strip())
        print("-" * 100)
        
        links = job_element.find_all("a")
        for link in links:
        #   link_url = link["href"]         # fetches value of href attributes
            link_url = job_element.find_all("a")[1]["href"]
            print(link.text.strip())
            
if __name__ == '__main__':
    print(main())
    

