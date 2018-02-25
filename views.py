# ----------------------------------------------------------------------------
# Name:         views.py
# Purpose:      This hold the logic for actual representation for Application Program
# Author:       Harshada Mangesh Kakad
# Created:      25th Feb 2018
# Version:      0.1

class TiptView():
    '''
    Object that holds the logic to View the data
    '''
    def __init__(self):
        self.postcode = ""
        self.SFBB = "UnAvailable"
        self.UFBB = "UnAvailable"
        self.NGA = "UnAvailable"
        self.SFBB_Upload_speed = 0.0
        self.SFBB_Download_speed = 0.0
        self.UFBB_Upload_speed = 0.0
        self.UFBB_Download_speed = 0.0
        self.NGA_Upload_speed = 0.0
        self.NGA_Download_speed = 0.0

    def setSFBB(self, availability):
        self.SFBB = availability

    def setUFBB(self, availability):
        self.UFBB = availability

    def setNGA(self, availability):
        self.NGA = availability

    def setSFBB_Upload_speed(self, speed):
        self.SFBB_Upload_speed = speed

    def setSFBB_Download_speed(self, speed):
        self.SFBB_Download_speed = speed

    def setPostcode(self, postcode):
        self.postcode = postcode

    def setUFBB_Upload_speed(self, speed):
        self.UFBB_Upload_speed = speed

    def setUFBB_Download_speed(self, speed):
        self.UFBB_Download_speed = speed

    def setNGA_Upload_speed(self, speed):
        self.NGA_Upload_speed = speed

    def setNGA_Download_speed(self, speed):
        self.UFBB_Download_speed = speed

    def getPostcode(self):
        return self.postcode

    def getSFBB(self):
        return self.SFBB

    def getUFBB(self):
        return self.UFBB

    def getNGA(self):
        return self.NGA

    def getSFBB_Upload_speed(self):
        return self.SFBB_Upload_speed

    def getSFBB_Download_speed(self):
        return self.SFBB_Download_speed

    def getUFBB_Upload_speed(self):
        return self.UFBB_Upload_speed

    def getUFBB_Download_speed(self):
        return self.UFBB_Download_speed

    def getNGA_Upload_speed(self):
        return self.NGA_Upload_speed

    def getNGA_Download_speed(self):
        return self.UFBB_Download_speed

    def start(self):
        '''
        Upon start accept the postcode
        '''
        postcode = raw_input("Enter the Postcode : ")
        self.setPostcode(postcode)

    def ViewData(self):
        '''
        View the data
        '''
        print "| ------ Average download speed (Mbit/s) -- Average upload speed (Mbit/s) -- Availability -- |"
        print "|  SFBB            {}                                {}                      {}     |" \
            .format(self.getSFBB_Download_speed(), self.getSFBB_Upload_speed(), self.getSFBB())
        print "|  UFBB            {}                                {}                      {}     |"\
            .format(self.getUFBB_Download_speed(), self.getUFBB_Upload_speed(), self.getUFBB())
        print "|  NGA             {}                                {}                      {}     |"\
            .format(self.getNGA_Download_speed(), self.getNGA_Upload_speed(), self.getNGA())
        print "|--------------------------------------------------------------------------------------------|"