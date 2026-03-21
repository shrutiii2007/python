class book:
    def __init__(self, title, author):
        self.title = title  
        self.author = author 

    def set_title(self, title):  
        self.title = title

    def set_author(self, author):  
        self.author = author

    def get_title(self): 
        return self.title
    
    def get_author(self):
        return self.author

book1 = book("TITLE :- the last lesson","AUTHOR :- Alphonse Daudet.")

# retrieves :-
print(book1.get_title()) 
print(book1.get_author())

# modifies :-
print()
print("after modifying :-")
print()
book1.set_title("TITLE :- poet and pancakes")  # Modifies the title
book1.set_author("AUTHOR :- ashokamitran")  # Modifies the author

print(book1.get_title())  
print(book1.get_author())

# output:-
# TITLE :- the last lesson
# AUTHOR :- Alphonse Daudet.
# TITLE :- poet and pancakes
# AUTHOR :- ashokamitran