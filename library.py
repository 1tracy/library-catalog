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
        self._fees = _feecalculator(self._borrowed)
        self._favorites = []

    @classmethod
    def _feecalculator (cls, lst):
        """ calculate fees -> $1/overdue day, two week borrow period"""
        pass

    def borrow_book(self, name, id):
        """ borrow book given name and google book id (for easy referencing) """
        string = [id, datetime.datetime.now()]
        self._borrowed.append({name: string})

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
    temp = {'title': lst['title'],
            'authors': lst['authors'],
            'publisher': lst['publisher'],
            'description': lst['description']}
##TKINTER CODE BELOW

unsorted = general_search('flowers')
sortdata(unsorted[0])
