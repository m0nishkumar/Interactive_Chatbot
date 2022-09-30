class parent():
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def parent1(self):
        print(f"Parent1 {self.x}")
        print(f"Parent1 {self.y}")

class child(parent):

    attr="mama"

    def __init__(self,x,y):
        self.x=x
        self.y=y

        parent.__init__(self,x,y)

    def addition(self):
        print(f"child{self.x}")


g=child("mo","kum")
print(g.__class__.attr)
g.addition()
g.parent1()