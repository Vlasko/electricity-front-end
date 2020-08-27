import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octopus_display.settings')

import django
django.setup()

from smart_plug.models import Instance

# Third Party Imports
import pandas as pd
import glob

# Pull csv data into script
file  = '/Users/gianluca/Documents/Projects/electricity-processing/files/cleaned_data/2019-12-18_2020-07-19.csv'
data = pd.read_csv(file,index_col='Timestamp')

def populate(data):
    #figure out how to populate database here
