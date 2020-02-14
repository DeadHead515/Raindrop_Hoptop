import requests
from bs4 import BeautifulSoup

URL = 'http://www.hopslist.com/hops/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='post-401')
hop_elems = results.find_all(class_='listing-item')

for hop_elem in hop_elems:
    hop_name = hop_elem.find(class_='title')
    hops_url = URL + hop_name.text
    page = requests.get(hops_url)
    soup = BeautifulSoup(page.content,'html.parser')
    table_results = soup.find("table")
    
    for table_result in table_results:
        cells = table_result.find("body").find('tr').find_all('td')
        for cell in cells:
            print(cell.text)
    


    

