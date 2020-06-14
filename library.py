""" main library module """
import csv
import datetime

from retrieval import general_search
from retrieval import id_retrieve

class Account:
    """ library user account """
    def __init__(self):
        self._borrowed = []
        self._fees = 0 #_feecalculator(self._borrowed)
        self._favorites = []

    def fees(self): return self._fees
    def borrowed(self): return self._borrowed
    def favorites(self): return self._favorites

    @classmethod
    def _feecalculator (cls, lst):
        """ calculate fees -> $1/overdue day, two week borrow period"""
        pass

    def borrow_book(self, lst):
        """ borrow book given name and google book id (for easy referencing) """
        lst['date'] = datetime.datetime.now()
        title = lst['title']
        del lst['title']
        self._borrowed.append({title: lst})

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

##TEST CODE
def testcodes():
    """ testing code """
    tracy = Account()

    unsorted = general_search('flowers')
    book1 = sortdata(unsorted[0]) #unsorted has 10 results

    #borrow first result
    tracy.borrow_book(book1)
    #print('borrowed', tracy.borrowed())

    #return first books
    tracy.return_book(0)
    #print('borrowed', tracy.borrowed())

