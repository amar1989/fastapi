from fastapi import FastAPI,Body

app = FastAPI()

BOOKS = [
    {'title': 'title1', 'author': 'author1', 'category': 'science'},
    {'title': 'title2', 'author': 'author2', 'category': 'geography'},
    {'title': 'title3', 'author': 'author3', 'category': 'history'},
    {'title': 'title4', 'author': 'author4', 'category': 'english'},
    {'title': 'title5', 'author': 'author4', 'category': 'english'},
    {'title': 'title6', 'author': 'author4', 'category': 'science'},
    {'title': 'title7', 'author': 'author4', 'category': 'history'}
]


@app.get("/books")
async def read_all_books():
    return BOOKS

#get request with path param
@app.get("/books/title/{book_title}")
async def read_books(book_title: str):
    for book in BOOKS:
        if book.get("title").casefold() == book_title.casefold():
            return book


@app.get("/books/")
async def read_book_by_category(category:str):
    book_to_return =[]
    for book in BOOKS:
        if book.get("category").casefold()==category.casefold():
            book_to_return.append(book)
    return book_to_return

@app.get("/books/{book_author}/")
async def read_book_by_author_category(author:str,category:str):
    book_to_return=[]
    for book in BOOKS:
        if book.get('author').casefold()==author.casefold() and \
            book.get('category').casefold()==category.casefold():
            book_to_return.append(book)
    return book_to_return

@app.post("/books/create_book")
async def add_new_book(new_book=Body()):
    BOOKS.append(new_book)
    return BOOKS

@app.put("/books/update_book")
async def update_book(new_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold()==new_book.get("title").casefold():
            BOOKS[i]=new_book
    return BOOKS
       


@app.delete("/books/delete_book/{book_title}")
async  def delete_book(book_title:str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold()==book_title.casefold():
            BOOKS.pop(i)
            break

#Assignment
@app.get("/books/{author_name}")
async def get_all_books_of_a_author(author_name:str):
    book_to_return=[]
    for book in BOOKS:
        if book.get("author").casefold()==author_name.casefold():
            book_to_return.append(book)
    return book_to_return