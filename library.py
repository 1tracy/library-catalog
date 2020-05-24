""" main library module """
import csv
from tkinter import *

from retrieval import general_search
from retrieval import id_retrieve

class Account:
    """ library user account """
    def __init__(self):
        self._borrowed = []
        self._fees = 0
        self._favorites = []

def writetocsv(data):
    """ write transaction to books csv """
    pass

def sortdata(lst):
    """ sort data from retrieval file """
    pass
##TKINTER CODE BELOW

print(general_search('flowers'))
