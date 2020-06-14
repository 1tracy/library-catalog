""" retrieve library data to format in tkinter here """

import tkinter as tk
import csv
from retrieval import general_search
from retrieval import id_retrieve


class MainApplication(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master

        self.nameLabel = tk.Label(self, text="Search", font="Verdana").grid(row=1, column=1)

        self.searchTermsLabel = tk.Label(self, text="Terms ", font=("Verdana", 10)).grid(row=2, column=1)
        self.searchTermVar = tk.StringVar()
        self.searchTermVar.set("flowers")
        self.searchterms = self.searchTermVar.get()
        self.searchTermEntry = tk.Entry(self, width=25, textvariable=self.searchTermVar, font=("Verdana", 10)).grid(row=2, column=2, padx=5)

        self.authorSearchLabel = tk.Label(self, text="Author ", font=("Verdana", 10)).grid(row=3, column=1)
        self.authorSearchVar = tk.StringVar()
        self.authorSearchEntry = tk.Entry(self, width=25, textvariable=self.authorSearchVar, font=("Verdana", 10)).grid(row=3, column=2, padx=5)

        self.titleSearchLabel = tk.Label(self, text="Title", font=("Verdana", 10)).grid(row=4, column=1)
        self.titleSearchVar = tk.StringVar()
        self.titleSearchEntry = tk.Entry(self, width=25, textvariable=self.titleSearchVar, font=("Verdana", 10)).grid(row=4, column=2, padx=5)

        self.favoritesButton = tk.Button(self, text="View Favorites", command=self.viewFavorites, font=("Verdana", 10)).grid(row=6, column=1, columnspan=2)

        self.searchButton = tk.Button(self, text="Search", command=self.lookUp, font=("Verdana",10)).grid(row=7, column=1, columnspan=2)
        self.pack()

    def getsearchterms(self): return self.searchTermVar.get()
    def getauthorterms(self): return self.authorSearchVar.get()
    def gettitleterms(self): return self.titleSearchVar.get()

    def lookUp(self):
        self.getstring = self._formatstring(self.searchTermVar.get(), self.authorSearchVar.get(), self.titleSearchVar.get())
        self.data = general_search(str(self.getstring))

        self.newWindow = tk.Toplevel(self)
        SearchFrame(self)

    def getData(self):
        return self.data

    def viewFavorites(self):
        self.newWindow = tk.Toplevel(self)
        FavoriteFrame(self)

    @classmethod
    def _formatstring(cls, search, author, title):
        """ format string for api call """
        temp = search
        if author != "":
            temp = temp + "+inauthor:" + author
        if title != "":
            temp = temp + "+intitle:" + title
        return temp

class SearchFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master.newWindow)
        self.master = master
        self.page = 0

        self.bookTitleVar = tk.StringVar()
        self.bookTitleLabel = tk.Label(self, textvariable=self.bookTitleVar, font=("Verdana", 10)).grid(row=1, columnspan=2)

        self.bookAuthorVar = tk.StringVar()
        self.bookAuthorLabel = tk.Label(self, textvariable=self.bookAuthorVar, font=("Verdana", 10)).grid(row=2, columnspan=2)

        self.googleIDVar = tk.StringVar()
        self.googleIDLabel = tk.Label(self, textvariable=self.googleIDVar, font=("Verdana", 10)).grid(row=3, columnspan=2)

        self.bookDescriptionVar = tk.StringVar()
        self.bookDescriptionLabel = tk.Message(self, textvariable=self.bookDescriptionVar, font=("Verdana", 10)).grid(row=4, columnspan=2)

        self.get_display(self.page)

        self.addToFavoritesButton = tk.Button(self, text="Favorite", width=25, command=self.addtoFavorites, font=("Verdana", 10)).grid(row=5, columnspan=2)
        self.nextPageButton = tk.Button(self, text="Next Option", width=25, command=self.next_page, font=("Verdana", 10)).grid(row=6, column=1)
        self.prevPageButton = tk.Button(self, text="Previous Option", width=25, command=self.previous_page, font=("Verdana", 10)).grid(row=6, column=0)
        self.quitButton = tk.Button(self, text="Quit", width=25, command=self.close_window, font=("Verdana", 10)).grid(row=7, columnspan=2)
        self.pack()


    def close_window(self):
        """ close window """
        self.master.newWindow.destroy()

    def next_page(self):
        """ move onto next index """
        self.page += 1
        if len(self.master.getData()) == self.page-1:
            self.bookDescriptionVar.set("End of Results")
            self.bookTitleVar.set("")
            self.bookAuthorVar.set("")
            self.googleIDVar.set("")
        else: self.get_display(self.page)

    def previous_page(self):
        """ move onto previous index """
        self.page -= 1
        if self.page == -1:
            print("End of Results")
        else: self.get_display(self.page)

    def update_display(self):
        """ update display when next page """
        self.bookTitleVar.set(self.dataentry[0])
        self.bookAuthorVar.set(self.dataentry[1])
        self.bookDescriptionVar.set(self.dataentry[2])
        self.googleIDVar.set(self.dataentry[3])

    def get_display(self, page):
        """ get display text """

        if page >= len(self.master.getData()): page = int(len(self.master.getData()))-1

        temp = []
        temp.append(self.master.getData()[page][1]['title'])
        temp2 = self.master.getData()[page][1]['authors']

        if len(temp2) == 1:
            temp2 = str(self.master.getData()[page][1]['authors'][0]).replace("}","")
            temp2.replace("{","")
            temp.append(temp2)
        else:
            temp2 = ''
            for i in range(len(self.master.getData()[page][1]['authors'])-1):
                temp2 = temp2 + str(self.master.getData()[page][1]['authors'][i]) + ", "
            temp2 = temp2 + str(self.master.getData()[page][1]['authors'][-1])
            temp.append(temp2)
        try:
            temp.append(self.master.getData()[page][1]['description'])
        except KeyError: temp.append("No Description Provided.")
        temp.append(self.master.getData()[page][0])

        self.dataentry = temp
        self.update_display()

    def addtoFavorites(self):
        """ add selected to favorites """
        with open("books.csv", "a", newline='') as fileOut:
            csvwriter = csv.writer(fileOut)
            csvwriter.writerow(str(self.googleIDVar.get()))

class FavoriteFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master.newWindow)
        self.master = master
        self.pagers = 0

        self.idlist = []
        with open("books.csv", "r", newline='') as fileIn:
            csvreader = csv.reader(fileIn)
            for line in csvreader:
                self.idlist.append(''.join(line))
            if len(self.idlist) == 0:
              print("no favourites")


        self.titleVar = tk.StringVar()
        self.titleLabel = tk.Label(self, textvariable=self.titleVar, font=("Verdana", 10)).grid(row=1, columnspan=2)

        self.authorVar = tk.StringVar()
        self.authorLabel = tk.Label(self, textvariable=self.authorVar, font=("Verdana", 10)).grid(row=2, columnspan=2)

        self.descVar = tk.StringVar()
        self.descLabel = tk.Message(self, textvariable=self.descVar, font=("Verdana", 10)).grid(row=3, columnspan=2)

        self.get_display()

        self.prevButton = tk.Button(self, text="<<", width=15, command=self.prev_page, font=("Verdana",10)).grid(row=4, column=0)
        self.nextButton = tk.Button(self, text=">>", width=15, command=self.next_page, font=("Verdana",10)).grid(row=4, column=1)
        self.removeButton = tk.Button(self, text="Remove", width=25, command=self.remove_from_favorites, font=("Verdana",10)).grid(row=5, columnspan=2)

        self.quitButton = tk.Button(self, text="Quit", width=25, command=self.close_window, font=("Verdana", 10)).grid(row=6, columnspan=2)

        self.pack()

    def close_window(self):
        with open("books.csv","w", newline='') as fileOut:
            csvwriter = csv.writer(fileOut)
            for i in self.idlist:
                csvwriter.writerow(i)
        self.master.newWindow.destroy()

    def next_page(self):
        """ next page """
        self.pagers += 1
        if len(self.idlist) <= (self.pagers+1): self.pagers = (len(self.idlist)-1)
        self.get_display()

    def prev_page(self):
        """ previous page """
        self.pagers -= 1
        if self.pagers == -1: self.pagers = 0
        self.get_display()


    def get_display(self):
        """ work out display """
        if len(self.idlist) == 0:
            self.titleVar.set('')
            self.descVar.set('No Favorites')
        else:
            if len(self.idlist) < (self.pagers-1): self.pagers = len(self.idlist)
            else:
                self.titleVar.set(id_retrieve(self.idlist[self.pagers])['volumeInfo']['title'])
                try: self.descVar.set(id_retrieve(self.idlist[self.pagers])['volumeInfo']['description'])
                except KeyError:
                    self.descVar.set("No Description Provided")
                

    def remove_from_favorites(self):
        """ remove from favorites """
        print(self.idlist[self.pagers])
        temp = str(self.idlist[self.pagers])
        temp2 = []
        with open("books.csv","r", newline='') as fileIn:
            csvreader = csv.reader(fileIn)
            for line in csvreader:
                if line != '':
                    temp2.append(''.join(line))
                    print(''.join(line))
        fileIn.close()

        self.idlist = temp2
        self.idlist.remove(temp)
                        
def main():
    root = tk.Tk()
    app = MainApplication(root)
    root.mainloop()

if __name__ == '__main__':
    main()
