#!/bin/env python
#----------------------------------------------------------------------------
# Name:         tipt-visualiser.py
# Purpose:      This is the start of the Application Program
# Author:       Harshada Mangesh Kakad
# Created:      25th Feb 2018
# Version:      0.1

import presenters
import models
import views

'''
Creates the Presenter objects with Tipt data, and the way to display them(the View) 
'''
presenters.TiptPresenter(models.Tipt(), views.TiptView())
