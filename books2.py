
from typing import Optional

from fastapi import FastAPI ,Path, Query ,HTTPException
from pydantic import BaseModel , Field

from starlette import status

app=FastAPI()

class Book:
    id :int
    title : str
    author : str
    description : str
    rating : int
    published_date:int

    def __init__(self,id,title,author,description,rating,published_date):
        self.id=id
        self.title=title
        self.author=author
        self.description=description
        self.rating=rating
        self.published_date=published_date


BOOKS=[
    Book(1,"Book title 1","Amar","desc1",5,2020),
    Book(2,"Book title 2","Amar","desc2",5,1999),
    Book(3,"Book title 3","Amar","desc3",5,2021),
    Book(4,"Book title 4","Amar","desc4",5,2014),
    Book(5,"Book title 5","Amar","desc5",5,2025),
    Book(6,"Book title 6","Amar","desc6",5,1998)
]


class BookRequest(BaseModel):
    id:Optional[int]=Field(description="Id id not needed for create", default=None) # this is way to make any attribute as optional in python
    title:str =Field(min_length=3)
    author:str = Field(min_length=1)
    description:str = Field(min_length=1 , max_length=100)
    rating:int = Field(gt=-1 , lt=6)
    published_date: int= Field(gt=1999, lt=2031)

    model_config = {
        "json_schema_extra":{
            "example":{
                "title":"A new book",
                "author":"codingwithroby"
            }
        }
    }


@app.get("/books")
async def read_all_books():
    return BOOKS



@app.post("/create-book",status_code=status.HTTP_200_OK)
async def create_book(book_request: BookRequest):
    new_book=Book(**book_request.model_dump())
    print(type(new_book))
    BOOKS.append(get_id(new_book))

@app.get("/get-book/{book_id}" ,status_code=status.HTTP_200_OK)
async def get_book(book_id:int = Path(gt=0)):
    for book in BOOKS:
        if book.id==book_id:
            return book
    raise HTTPException(status_code=404 , detail="Item not found")

@app.get("/books/",status_code=status.HTTP_200_OK)
async def read_book_by_rating(book_rating:int =Query(gt=0 , lt=6)):
    book_to_return=[]
    for book in BOOKS:
        if book.rating==book_rating:
            book_to_return.append(book)

    return book_to_return

@app.put("/books/update_book",status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book:BookRequest):
    status : bool= False
    for i in range(len(BOOKS)):
        if BOOKS[i].id==book.id :
            BOOKS[i]=book
            status=True

    if not status:
        raise HTTPException(status_code=404,detail="Item not found so can not update")


@app.delete("/books/{book_id}",status_code=status.HTTP_200_OK)
async  def delete_book(book_id:int =Path(gt=0)):
    for i in range(len(BOOKS)):
        if BOOKS[i].id==book_id:
            BOOKS.pop(i)
            break



def get_id(book:Book):
    if len(BOOKS)>0:
        book.id = BOOKS[-1].id+1
    else:
        book.id=1

    return  book
