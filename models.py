# ----------------------------------------------------------------------------
# Name:         models.py
# Purpose:      This holds the logic to read the data from Connected Nation Report and return for visualization
# Author:       Harshada Mangesh Kakad
# Created:      25th Feb 2018
# Version:      0.1 

import pandas as pd
import os

class Tipt(object):
    '''
    This is the object that holds the data for application program.
    '''
    def __init__(self):
        pass

    def GetAreaData(self, postcode):
        '''
        This function takes postcode and lookup for csv file in data directory and sends back the data
        :param postcode: postcode
        :return: data
        '''
        filename = self.get_csv_file_name(postcode)
        data_file_dir = os.path.dirname(__file__)
        rel_path = "2016_fixed_pc_r01/" + filename
        abs_file_path = os.path.join(data_file_dir, rel_path)
        if(os.path.exists(abs_file_path)):
            try:
                data = pd.read_csv(abs_file_path)
            except:
                exit(1)
            return data
        else:
            print("Not a valid Area Code")
            exit(0)

    def get_csv_file_name(self, postcode):
        '''
        Depending on Postcode this function creates the file name
        :param postcode: Postcode
        :return: filename
        '''
        return "2016_fixed_pc_r01_" + postcode[:2] + ".csv"
