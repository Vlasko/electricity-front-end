import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octopus_display.settings')

import django
django.setup()

from smart_plug.models import Instance

# Third Party Imports
import pandas as pd

# Pull csv data into script
file  = '/Users/gianluca/Documents/Projects/electricity-processing/files/cleaned_data/2019-12-18_2020-07-19.csv'
data = pd.read_csv(file,index_col='Timestamp')

def populate(data):
    for timestamp, row in data.iterrows():
        demand = row[0]
        unit_price = row[1]
        price = row[2]

        inst = Instance.objects.get_or_create(timestamp = timestamp,
                                              demand = demand,
                                              unit_price = unit_price,
                                              price = price
                                              )
    
