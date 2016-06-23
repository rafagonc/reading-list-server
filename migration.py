r__author__ = 'rafagonc'

import requests
import psycopg2
import psycopg2.extras
import json

url = "https://reading-list-prod.herokuapp.com/"
#url = "http://192.168.1.31:5000/"

#connect to postgres
connect_addr = "host='localhost' dbname='reading-list-backup'"
conn = psycopg2.connect(connect_addr)

#declare the cursor
cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

#fetch all the books
cursor.execute("SELECT BOO.name as book_name, AUT.name as author_name, CAT.name as category_name, RAT.rating as rating FROM red_book as BOO INNER JOIN red_author as AUT ON BOO.author_id = AUT.id INNER JOIN red_category as CAT ON BOO.category_id = CAT.id JOIN red_rating as RAT ON BOO.id = RAT.book_id;")

up = []
book_dicts = cursor.fetchall()[601::]
print(book_dicts)
for book_dict in book_dicts:
    book = dict(book_name=book_dict['book_name'], author_name=book_dict['author_name'], category_name=book_dict['category_name'], rating=book_dict['rating'])
    up.append(book)

books = {"books" : up}

print(json.dumps(books))
r = requests.post(url + "mrating", json=books)
print(r.text)

