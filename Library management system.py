# Library Management System using Python with DSA (with user input)

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.next = None


#for managing books using a linked list
class LinkedList:
    def __init__(self):
        self.head = None

    def add_book(self, title, author):
        new_book = Book(title, author)
        if not self.head:
            self.head = new_book
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_book

    def display_books(self):
        current = self.head
        if not current:
            print("No books in library.")
            return
        while current:
            print(f"Title: {current.title}, Author: {current.author}")
            current = current.next

# Hash Table for quick search by title and author
class BookHashTable:
    def __init__(self):
        self.table = [None] * 100

    def _hash(self, key):
        return sum(ord(c) for c in key) % len(self.table)

    def add_book(self, title, author):
        index = self._hash(title)
        if not self.table[index]:
            self.table[index] = [(title, author)]
        else:
            self.table[index].append((title, author))

    def search_by_title(self, title):
        index = self._hash(title)
        if self.table[index]:
            for book in self.table[index]:
                if book[0] == title:
                    return book
        return None

    def search_by_author(self, author):
        results = []
        for entry in self.table:
            if entry:
                for book in entry:
                    if book[1] == author:
                        results.append(book)
        return results

# Queue for managing book issues
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return None

    def is_empty(self):
        return len(self.queue) == 0

# Stack for managing book returns
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def is_empty(self):
        return len(self.stack) == 0

# System Initialization
library = LinkedList()
hash_table = BookHashTable()
issue_queue = Queue()
return_stack = Stack()

# Menu-based system
while True:
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. Display All Books")
    print("3. Search Book by Title")
    print("4. Search Book by Author")
    print("5. Issue Book")
    print("6. Return Book")
    print("7. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        library.add_book(title, author)
        hash_table.add_book(title, author)
        print("Book added successfully.")

    elif choice == '2':
        print("\nAll Books:")
        library.display_books()

    elif choice == '3':
        title = input("Enter title to search: ")
        book = hash_table.search_by_title(title)
        if book:
            print(f"Found: Title: {book[0]}, Author: {book[1]}")
        else:
            print("Book not found.")

    elif choice == '4':
        author = input("Enter author to search: ")
        results = hash_table.search_by_author(author)
        if results:
            for b in results:
                print(f"Title: {b[0]}, Author: {b[1]}")
        else:
            print("No books found by this author.")

    elif choice == '5':
        title = input("Enter title to issue: ")
        issue_queue.enqueue(title)
        print(f"Book '{title}' issued.")

    elif choice == '6':
        title = input("Enter title to return: ")
        return_stack.push(title)
        print(f"Book '{title}' returned.")

    elif choice == '7':
        print("Exiting system. Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")