## Train Schedule API

This is a Flask-based API that provides upcoming train schedule based on present time for a given query and route.

### Prerequisites

*   Python 3.6 or above
*   Flask
*   Pandas
*   Gunicorn

Install them using pip:

bash

```bash
pip install flask pandas gunicorn
```

### Usage

Clone the repository to your local machine:

bash

```bash
git clone https://github.com/sarkrui/CRH.git
```

Navigate to the project directory:

bash

```bash
cd CRH
```

Run the Flask app:

bash

```bash
gunicorn -w 4 server:app -b 0.0.0.0:8000
```

Your server should now be running at `http://0.0.0.0:8000`.

### Endpoints

The API has a single endpoint:

*   `/now?dest={destination}` - Returns the departure times of upcoming trains for the given destination.

Replace `{destination}` with either 'SZ' or 'HK'. 'SZ' corresponds to "福田" and 'HK' corresponds to "香港西九龙".

### Sample Request & Response
Request:

`http://0.0.0.0:8000/now?dest=SZ`

Response:

json

```json
{
  "depart_times": [
    "20:40",
    "21:25",
    "21:31",
    "21:55"
  ]
}
```
The `html2csv.py`script extracts train ticket information from an HTML file containing a table of train data. The script uses the BeautifulSoup library to parse the HTML content and retrieve specific details about each train ticket. It then prepares the extracted data and writes it to a CSV file for further analysis or use.

## Requirements
- BeautifulSoup 4 (bs4)


```bash
pip install beautifulsoup4
```

### Note
1.  Place the HTML file containing the train ticket data in the same directory as this script. The file should be named `table-hk-sz.html`.
    
2.  Execute the script:
    
```bash
python html2csv.py.py
```

3.  The script will extract the ticket information and save it in a CSV file named `table.csv`.

## Output

The CSV file will contain the following columns:

*   `t_code`: The train code (车次) of the ticket.
*   `t_type`: The train type (e.g., '和谐号', '复', '动感号') or 'N/A' if not specified.
*   `depart_sta`: The departure station (出发站) of the train.
*   `arrive_sta`: The arrival station (到达站) of the train.
*   `depart_ts`: The departure time (出发时间) from the departure station.
*   `arrive_ts`: The arrival time (到达时间) at the arrival station.
