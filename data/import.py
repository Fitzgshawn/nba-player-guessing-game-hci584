import requests
from bs4 import BeautifulSoup

# Make a GET request to the website
response = requests.get('https://www.nba.com/stats/players/traditional?SeasonType=Regular+Season')

# Parse the HTML response
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table element
table = soup.find('table', class_='nba-stat-table')

# Extract the data
data = []
for row in table.find_all('tr'):
    cells = row.find_all('td')
    data.append([cell.text for cell in cells])

# Save the data to a CSV file
with open('nba_data.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(data)
