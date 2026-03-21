def bill(**kwargs):
    name = kwargs.get("name")
    price = kwargs.get("price", 0)
    quantity = kwargs.get("quantity", 1)
    # Agar name mil gaya uska value de dega isliye get likha hai nhi hoga to nhi dega 
    # Agar name NA milay error nahi dega, bas None de dega
    #or agar bina get likhe likha to Aur name key dictionary me na ho, toh error aayega:
    total = price * quantity
        #   =  20*5=100

    return f"Product: {name}, Total Cost: {total}"

print(bill(name="Pen", price=20, quantity=5))

# output:-
# Product: Pen, Total Cost: 100