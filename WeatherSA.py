import requests
from bs4 import BeautifulSoup

#!/usr/bin/env python3

def main():

    URL = "https://www.weathersa.co.za/"
    page = requests.get(URL)

    print(page.text)

    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="tablePopCities")

    print(results.prettify)

    City_elements = results.find_all("div", class_="col-sm-7 topCities")


        
    headers = []
    for th in results.find_all("th"):
      headers.append(th.text.strip())
    
    rows = []
    for row in results.find_all("tr"):
        cells = []
        for td in row.find_all("td"):
            cells.append(td.text.strip())
        if cells:
         rows.append(cells)
        
    print(headers)
    for row in rows:
        print(row)
        print()
        print("-" * 100)

    print("-" * 100)

if __name__ == '__main__':
    print(main())
    