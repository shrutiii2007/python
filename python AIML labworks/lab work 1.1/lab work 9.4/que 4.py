class transport:
    def travel(self):
        print("transport  is used to travel")

class train(transport):
    def travel(self):
        print("train runs on railway tracks")

class plane(transport):
    def travel(self):
        print("plane fly in air")

a = transport()
b = train()
c = plane()

a.travel()
b.travel()
c.travel()

# output:-
# transport  is used to travel
# train runs on railway tracks
# plane fly in air