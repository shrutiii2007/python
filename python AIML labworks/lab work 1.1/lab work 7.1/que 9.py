def info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

info(firstname="Bob", lastname="Smith", location="London")

# output:-
# firstname: Bob
# lastname: Smith
# location: London