# In this programme we are scrapping Books from flipkart and some other information about books 
# like BOOK TTITLE, AUTHOR NAME and PRICE of the book
# and then exporting data in csv

# Note- Sometimes this programe will not work due to connection problem so try again after some time.

import csv              
import requests
import bs4

url=('https://www.flipkart.com/books/pr?sid=bks&otracker=categorytree&page={}')

book_list=[]     
price_list=[]
author_list=[]


for n in range(1,2):           # this loop is for pages range
    
    scrapurl=(url.format(n))   
    res=requests.get(scrapurl)  # Making request to fetch the data

    soup=bs4.BeautifulSoup(res.text,'lxml')   # Parsing data into LXML

    book=soup.select(".s1Q9rs")             # All these are classes names 
    price=soup.select("._30jeq3")           # You will find these class name during inspecting the website in HTML code
    author=soup.select("._3Djpdu")


    for a in book:                         # Iterating through every item on page
        book_list.append(a.text)           # append the all the data into list
    for b in price:
        price_list.append(b.text)  
    for c in author:
       author_list.append(c.text)

# file=open('Data.csv','w')           # Creating CSV file and giving some field names
# writer=csv.writer(file)
# writer.writerow(['Titles', 'Author_name ', 'Price'])       
       
print(len(book_list))
print(len(author_list))
print(len(price_list))


# for x in range(len(price_list)):            #Index for loop
#     book_list[x] +' : ' + author_list[x] + " : " + price_list[x]  #By using the index we get the element from all the list

#     p=author_list[x]
#     p=(p[p.rindex(",")+2:-1])               # Flitering only author name from the string

#     writer.writerow([book_list[x],p,price_list[x]]) 

# file.close()

