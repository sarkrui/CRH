from bs4 import BeautifulSoup
import csv

# Load the file
with open('table-hk-sz.html', 'r', encoding='utf-8') as f:
    contents = f.read()

soup = BeautifulSoup(contents, 'html.parser')

# Find the divs with class 'ticket-info clearfix'
divs = soup.find_all('div', class_='ticket-info clearfix')

# Prepare the data
data = []
for div in divs:
    train_div = div.find('div', class_='train')
    cdz_div = div.find('div', class_='cdz')
    start_t_span = div.find('strong', class_='start-t')
    color999_span = div.find('strong', class_='color999')

    # Skip this div if any of the required elements are missing
    if not all([train_div, cdz_div, start_t_span, color999_span]):
        continue

    checi = train_div.get_text(strip=True)
    checi = checi.replace('查看票价', '')  # Remove '查看票价'

    # Find the train type in the '车次'
    if '和谐号' in checi:
        train_type = '和谐号'
        checi = checi.replace('和谐号', '')
    elif '复' in checi:
        train_type = '复'
        checi = checi.replace('复', '')
    elif '动感号' in checi:
        train_type = '动感号'
        checi = checi.replace('动感号', '')
    else:
        train_type = 'N/A'

    stations = cdz_div.find_all('strong')

    # Skip this div if there are not exactly two stations
    if len(stations) != 2:
        continue

    chufazhan = stations[0].get_text(strip=True)
    daodazhan = stations[1].get_text(strip=True)
    chufashijian = start_t_span.get_text(strip=True)
    daodashijian = color999_span.get_text(strip=True)

    row = [checi, train_type, chufazhan, daodazhan, chufashijian, daodashijian]
    data.append(row)

# Write the data to a CSV file
with open('table.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['t_code', 't_type', 'depart_sta', 'arrive_sta', 'depart_ts', 'arrive_ts'])
    writer.writerows(data)
