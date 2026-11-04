
import json
import os

FILE_NAME = "books.json"

books = [
    {"id": 1, "title": "Python Basics", "author": "John"},
    {"id": 2, "title": "Clean Code", "author": "Robert"},
    {"id": 3, "title": "Atomic Habits", "author": "James"}
]

def add_book(book):
    for existing in books:
        if existing["id"] == book["id"]:
            print("Error: Duplicate book ID!")
            return False

    books.append(book)
    print("Book added successfully!")
    return True


def save_books():
    with open(FILE_NAME, "w") as file:
        json.dump(books, file, indent=4)

    print("Books saved successfully!")

def restore_books():
    global books

    if not os.path.exists(FILE_NAME):
        print("No saved catalog found.")
        return

    with open(FILE_NAME, "r") as file:
        books = json.load(file)

    print("Books restored successfully!")



def display_books():
    for book in books:
        print(book)

add_book({
    "id": 4,
    "title": "Deep Work",
    "author": "Cal Newport"
})

# Attempt duplicate ID
add_book({
    "id": 2,
    "title": "New Book",
    "author": "Unknown"
})


save_books()

restore_books()

display_books()
