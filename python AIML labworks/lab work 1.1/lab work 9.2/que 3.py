class Area:
    def __init__(self,width,length):
        self.width = width
        self.length = length
        self.area = length*width  # formula

    def show_details(self):
        print(self.width,self.length,self.area)

area1 = Area(12,2)
area1.show_details()   # to show

area2 = Area(10 ,10)
area2.show_details()   # to show

# output:-
# 12 2 24
# 10 10 100