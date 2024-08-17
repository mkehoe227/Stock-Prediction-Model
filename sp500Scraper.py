import requests
from bs4 import BeautifulSoup

def getCompanyList():
    # Make request to Wikepedia page
    url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    rec = requests.get(url)
    
    # Scrape HTML with BS and locate the cprrect table
    soup = BeautifulSoup(rec.text, 'html.parser')
    table = soup.find('table', id="constituents")

    # Find the body of the 
    tbody = table.find('tbody')
    rows = list(tbody.children)
    companyList = []

    # Iterate through rows ( Every other index is a new line so use step=2 )
    for index in range(2, len(rows), 2):
        rowChildren = list(rows[index].children)
        # Get symbol row and append to list
        symbolBox = rowChildren[1].get_text(strip=True)
        # Change . to - for yfinance use
        if '.' in symbolBox:
            symbolBox = symbolBox.replace('.', '-')
        companyList.append(symbolBox)
    return companyList

# Test
if __name__ == "__main__":
    returned = getCompanyList()
    print(returned)