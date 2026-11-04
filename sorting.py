books = [
    {"title": "Python Basics", "rating": 4.5},
    {"title": "Atomic Habits", "rating": 4.8},
    {"title": "Clean Code", "rating": 4.5},
    {"title": "Deep Work", "rating": 4.9},
    {"title": "Algorithms", "rating": 4.8}
]

sorted_books = sorted(
    books,
    key=lambda book: (-book["rating"], book["title"])
)

for book in sorted_books:
    print(book)
