import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octopus_display.settings')

import django
django.setup()

import pandas as pd
import glob
from smart_plug.models import Demand

# Import csv data from

def data_pull():
    directory  = '/Users/gianluca/Documents/Projects/electricity-processing/files/'
    datatype = ['demand/', 'prices/']
    filetype = '*.csv'

    type_dict = {}
    for type in datatype:
        data_list=[]
        for file in glob.glob(directory + type + filetype):
            data = pd.read_csv(os.path.join(directory, file),
                               index_col='Timestamp')
            data_list.append(data)
        data_combined = pd.concat(data_list)
        type_dict.update({type[:-1]:data_combined})

    return type_dict

imported_data_dict = data_pull()

imported_data_dict['demand']

def populate(data):
    #figure out how to populate database here
