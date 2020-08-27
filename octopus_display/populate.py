import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octopus_display.settings')

import django
django.setup()

#Import models
from smart_plug.models import Instance

# Third Party Imports
import pandas as pd

# Pull csv data into script
def populate():
    file  = '/Users/gianluca/Documents/Projects/electricity-processing/files/cleaned_data/2019-12-18_2020-07-19.csv'
    collected_data = pd.read_csv(file,index_col='Timestamp')

    for timestamp, row in collected_data.iterrows():
        demand = round(row[0],2)
        unit_price = round(row[1],2)
        price = round(row[2],2)

        inst = Instance.objects.get_or_create(timestamp = timestamp,
                demand = demand,
                unit_price = unit_price,
                price = price)[0]

if __name__ == '__main__':
    print('populating script!')
    populate()
    print('populating complete!')
