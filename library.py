""" main library module """
import csv
import datetime
from tkinter import *

from retrieval import general_search
from retrieval import id_retrieve

class Account:
    """ library user account """
    def __init__(self):
        self._borrowed = []
        self._fees = 0 #_feecalculator(self._borrowed)
        self._favorites = []

    @classmethod
    def _feecalculator (cls, lst):
        """ calculate fees -> $1/overdue day, two week borrow period"""
        pass

    def borrow_book(self, lst):
        """ borrow book given name and google book id (for easy referencing) """
        string = [lst['id'], datetime.datetime.now()]
        self._borrowed.append({lst['title']: string})

    def return_book(self, index):
        """ return book given index"""
        try:
            self._borrowed.pop(index)
        except KeyError:
            return "this book does not exist"

    def renew_book(self, index):
        """ renew borrowing period for already borrowed book """
        temp = self._borrowed[index]
        del self._borrowed[index]
        #self._borrowed.append({list(temp.keys())[0]: [list(temp.values())})


def writetocsv(data):
    """ write transaction to books csv """
    pass

def sortdata(lst):
    """ sort data from singular entry only"""
    temp = {'title': lst[1]['title'],
            'authors': lst[1]['authors'],
            'isbn-10': lst[1]['industryIdentifiers'][0]['identifier'],
            'pages': lst[1]['pageCount'],
            'id': lst[0]}
    return temp
##TKINTER CODE BELOW

##TEST CODE
tracy_account = Account()

unsorted = general_search('flowers')
sortdata(unsorted[0]) #unsorted has 10 results
#borrow first result
