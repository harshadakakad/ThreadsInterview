# ----------------------------------------------------------------------------
# Name:         presenters.py
# Purpose:      This holds the actual logic to visualise the data and extract the useful information for
# application program
# Author:       Harshada Mangesh Kakad
# Created:      25th Feb 2018
# Version:      0.1

class TiptPresenter(object):
    '''
    This is the object that takes care of the logic of your application.
    This is where you express what happens in your application program
    '''

    def __init__(self, tipt, view):
        self.tipt = tipt
        self.view = view
        self.data = ""
        view.start()
        self.initView()

    def initView(self):
        '''
        This function fetch out the data from tipt object.
        Visualise data and extracts the useful information from data
        '''
        self.data = self.tipt.GetAreaData(self.view.getPostcode())
        self.loadData()
        self.view.ViewData()

    def loadData(self):
        '''
        Visualise data, extract useful information for the postcode
        '''
        postcode_filter = self.data["postcode"] == self.view.getPostcode()
        if len(self.data[postcode_filter]) == 0:
            print "Not a valid Postcode"
        else:
            if self.data[postcode_filter]["SFBB availability (% premises)"].get_values()[0] > 0:
                self.view.setSFBB("Available")
            if self.data[postcode_filter]["UFBB availability (% premises)"].get_values()[0] > 0:
                self.view.setUFBB("Available")
            if self.data[postcode_filter]["NGA availability (% premises)"].get_values()[0] > 0:
                self.view.setNGA("Available")

            self.view.setSFBB_Upload_speed(self.data[postcode_filter]\
                                               ["Average upload speed (Mbit/s) for SFBB lines"].get_values()[0])
            self.view.setSFBB_Download_speed(self.data[postcode_filter]\
                                                 ["Average download speed (Mbit/s) for SFBB lines"].get_values()[0])
            self.view.setUFBB_Upload_speed(self.data[postcode_filter]\
                                               ["Average upload speed (Mbit/s) for UFBB lines"].get_values()[0])
            self.view.setUFBB_Download_speed(self.data[postcode_filter]\
                                                 ["Average download speed (Mbit/s) for UFBB lines"].get_values()[0])
            self.view.setNGA_Upload_speed(self.data[postcode_filter]\
                                              ["Average upload speed (Mbit/s) for Basic BB lines"].get_values()[0])
            self.view.setNGA_Download_speed(self.data[postcode_filter]\
                                                ["Average download speed (Mbit/s) for Basic BB lines"].get_values()[0])

