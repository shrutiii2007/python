class animal:
    def __init__(self, name):
        self.name = name  # Instance Variable

    def show_details(self):
        print(f"Animal name :-: {self.name}")

lion = animal("Lion")
tiger = animal("Tiger")

lion.show_details()
tiger.show_details()