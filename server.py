from flask import Flask, request
import pandas as pd
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/now')
def upcoming_schedule():
    destination = request.args.get('dest')

    if destination:
        destination_dict = {'SZ': '福田', 'HK': '香港西九龙'}
        destination_name = destination_dict.get(destination.upper())

        if destination_name:
            df = pd.read_csv('data.csv')
            df['depart_ts'] = pd.to_datetime(df['depart_ts'], format='%H:%M').dt.time
            now = (datetime.now() + timedelta(minutes=1)).time()  # add one minute to account for processing time
            upcoming_trains = df[(df['depart_sta'] == destination_name) & (df['depart_ts'] > now)]

            if not upcoming_trains.empty:
                upcoming_trains.loc[:, 'depart_ts'] = upcoming_trains['depart_ts'].apply(lambda t: t.strftime('%H:%M'))
                return {"depart_times": upcoming_trains['depart_ts'].tolist()}, 200
            else:
                return {"message": "No upcoming trains found."}, 404

        else:
            return {"message": "Invalid destination. Please use 'SZ' or 'HK'."}, 400

    else:
        return {"message": "Destination not provided."}, 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
