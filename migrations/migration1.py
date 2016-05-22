import requests
import psycopg2
import psycopg2.extras

url = "https://reading-list-stage.herokuapp.com/"

#connect to postgres
connect_addr = "host='localhost' dbname='reading-list-backup'"
conn = psycopg2.connect(connect_addr)

#declare the cursor
cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

#fetch all the books
cursor.execute("SELECT * FROM red_book;")
books = cursor.fetchall()



