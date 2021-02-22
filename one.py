class Pen:
    def __init__(self,name,price,ink):
        self.name=name
        self.price=price
        self.ink=ink
    def writing(self):
        print('The Pen is Writing')
    def information(self):
        print('The Pens name is'+ self.name + 'The Pen is of ' + self.ink + 'Its price is' + str(self.price) )

pen1= Pen('Jel',20,'blue')
pen1.writing()
pen1.information()