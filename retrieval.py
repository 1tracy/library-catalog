"""
retrieves book data from google books api

"""

import json
import requests

def getrequest(url):
    """ get and return response """
    response = requests.get(url)
    return response

def test_connection(url):
    """ test if connection is working """
    request = getrequest(url)
    return request.status_code == 200

def id_retrieve(BookID):
    """ retrieve first google book result """
    url = "https://www.googleapis.com/books/v1/volumes?q=id="+BookID
    response = getrequest(url)
    print(json.loads(response.content)['items'][0])

def search(term):
    """ search and return first 10 results """
    pass

def main():
    """ testing functions :) """
    id_retrieve('buc0AAAAMAAJ')

if __name__ == "__main__":
    main()
