"""
retrieves book data from google books api
all requests are made here!
"""
import json
import requests

def getrequest(url):
    """ get and return response """
    response = requests.get(url)
    return response

def test_connection(url="https://www.googleapis.com/books/v1/volumes?q=Hc3itAEACAAJ"):
    """ test if connection is working """
    request = getrequest(url)
    return request.status_code == 200

def id_retrieve(bookid):
    """ retrieve and return first google book result data"""
    url = "https://www.googleapis.com/books/v1/volumes?q=id="+bookid
    if test_connection(url):
        response = getrequest(url)
        unfiltered = json.loads(response.content)['items'][0]
        return unfiltered
    return "error"

def general_search(customised):
    """ search and return <=10 most relevant results **can be modified"""
    url = "https://www.googleapis.com/books/v1/volumes?q="+customised
    if test_connection(url):
        response = getrequest(url)
        unfiltered = json.loads(response.content)
        lst = []
        for i in unfiltered['items']:
            lst.append([i['id'], i['volumeInfo']])
        return lst
    return "error"


def main():
    """ testing functions :) """
    print(id_retrieve('Hc3itAEACAAJ')['volumeInfo']['title'])
    #print(general_search('flowers'))

if __name__ == "__main__":
    main()
