from model import Book, Magazine, DVD, Member

book = Book("Python 101", 1, "A. Rao")
magazine = Magazine("Tech Today", 2, 42)
dvd = DVD("Intro to Algorithms", 3, 95)
book2 = Book("Python Advanced", 4, "BN. Rao")

alice = Member("Alice", 101)
bob = Member("Bob", 102, max_items=1)
charlie = Member("Charlie", 103, max_items=2)

# 1. Borrowing with error handling
try:
    alice.borrow(book)
    print("Alice borrowed:", book.describe())
    bob.borrow(book)  # should fail: already borrowed
except ValueError as e:
    print("Could not borrow:", e)
    
# 2. TODO: trigger the borrow-limit error and the not-borrowed error, catching each
print("\n--- Borrow limit ---")
try:
    bob.borrow(magazine)
    print("Bob borrowed:", magazine.describe())
    bob.borrow(dvd)  # should fail: Bob's limit is 1
except ValueError as e:
    print("Could not borrow:", e)

print("\n--- Alice fills her limit of 3 ---")
try:
    alice.borrow(dvd)
    alice.borrow(book2)
    print("Alice now holds:", alice.borrowed_titles())
    alice.borrow(Book("Fourth Book", 5, "Anon"))  # should fail: limit of 3
except ValueError as e:
    print("Could not borrow:", e)


# 3. Polymorphism: one loop, no type checks
items = [book, magazine, dvd, book2]
for item in items:
    print(item.describe(), "-> late fee for 3 days: Rs", item.late_fee(3))
# 4. Class attribute shared by all objects
print("Total items created:", Book.total_items)