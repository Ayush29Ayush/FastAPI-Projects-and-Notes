from fastapi import Body, FastAPI

app = FastAPI()

#! Create First FastAPI endpoint
@app.get("/")
async def first_api():
    return {"message": "Hello World"}

#! Create Second FastAPI endpoint with dynamic path parameter
@app.get("/test/{dynamic_param}")
async def second_api(dynamic_param):
    return {"message": dynamic_param}


BOOKS = [
    {"title": "Title One", "author": "Author One", "category": "science"},
    {"title": "Title Two", "author": "Author Two", "category": "science"},
    {"title": "Title Three", "author": "Author Three", "category": "history"},
    {"title": "Title Four", "author": "Author Four", "category": "math"},
    {"title": "Title Five", "author": "Author Five", "category": "math"},
    {"title": "Title Six", "author": "Author Two", "category": "math"},
]


@app.get("/books")
async def read_all_books():
    return BOOKS

@app.get("/books/mybook")
async def read_my_book():
    return {"title": "My favorite book"}


@app.get("/books/{book_title}")
async def read_book(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book

# http://127.0.0.1:8000/books/?category=math
@app.get("/books/")
async def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return


# http://127.0.0.1:8000/books/author%20one/?category=science
@app.get("/books/{book_author}/")
async def read_author_category_by_query(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and book.get('category').casefold() == category.casefold():
            books_to_return.append(book)

    return books_to_return


@app.post("/books/create_book")
async def create_book(new_book=Body()):
    print(new_book)
    BOOKS.append(new_book)
    print(BOOKS)


@app.put("/books/update_book")
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book


@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            BOOKS.pop(i)
            break
        
        
'''
Get all books from a specific author using path or query parameters
'''

# http://127.0.0.1:8000/test/assignment/?query_param_author=author%20two
@app.get("/test/assignment/")
async def read_all_books_by_author_query(query_param_author: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == query_param_author.casefold():
            books_to_return.append(book)

    return books_to_return

# http://127.0.0.1:8000/test/assignment/author%20two/
@app.get("/test/assignment/{path_param_author}/")
async def read_all_books_by_author_path(path_param_author: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == path_param_author.casefold():
            books_to_return.append(book)

    return books_to_return