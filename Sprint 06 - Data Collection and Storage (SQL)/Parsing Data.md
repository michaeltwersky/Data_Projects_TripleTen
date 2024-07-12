```
import requests
from bs4 import BeautifulSoup
import pandas as pd

URL='https://practicum-content.s3.us-west-1.amazonaws.com/data-analyst-eng/moved_chicago_weather_2017.html'
req = requests.get(URL)

soup = BeautifulSoup(req.text, 'lxml')

table = soup.find('table', attrs={"id": "weather_records"})

heading_table=[]
for row in table.find_all('th'):
    heading_table.append(row.text)   

content=[]
for row in table.find_all('tr'):
    if not row.find_all('th'):
        content.append([element.text for element in row.find_all('td')])

weather_records = pd.DataFrame(content, columns = heading_table)
print(weather_records)
```