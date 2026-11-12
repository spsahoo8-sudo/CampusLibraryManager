1. Why is LibraryItem abstract, and what happens if DVD forgets to write late_fee()? 
LibraryItem is abstract because it only describes what every item has in common 
(title, ID, availability) and is never a real item on its own. Declaring late_fee() 
with @abstractmethod forces each child class to supply its own rate. 
If DVD forgets it, Python raises a TypeError as soon as you try to create a DVD, 
so the mistake is caught immediately instead of surfacing later during a fee calculation.

2. What happens when you read item.__available from outside the class, 
and why do we use is_available() instead? 
Reading item.__available from outside the class raises an AttributeError: 
Python name-mangles the attribute declared in LibraryItem to _LibraryItem__available, 
so the plain __available name isn’t found. We use is_available() so outside code can 
only read availability through a method,and only mark_borrowed() and mark_returned() can 
change it. That keeps the state consistent and lets us change the internals later 
without breaking other code.

3. What is the difference between LibraryItem.total_items and self.title? 
total_items is a class attribute: one value shared by every item, stored on the class 
and increased by 1 each time any item is created. self.title is an instance attribute: 
each object has its own copy, so every book, magazine and DVD keeps its own title.