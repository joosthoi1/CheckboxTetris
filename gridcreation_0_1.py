from tkinter import *
class grid:
    def __init__(self, numberx, numbery=None, text = ''):

        self.text = text
        self.root = Tk()
        self.boxlist, self.varlist = [], []
        self.numberx, self.numbery = numberx, numbery
        self.xgrid, self.ygrid = 0, 0
        self.root.title('gridcreation')

        self.coordrost = [[i for i in range(self.numberx*x,self.numberx+self.numberx*x)] for x in range(numbery)]
        for i in range(10000):
            self.varlist.append(IntVar())
            #self.boxlist.append(Checkbutton(self.root, text=f'{self.uncoords(i)} ({i})', variable=self.varlist[i]))
            self.boxlist.append(Checkbutton(self.root, text=self.text, variable=self.varlist[i]))
            self.boxlist[i].grid(row=self.ygrid, sticky=W, column=self.xgrid)
            self.boxlist[i].configure(bg='light gray')
            self.xgrid += 1
            if self.xgrid == self.numberx:
                self.ygrid += 1
                self.xgrid = 0

            if self.ygrid == self.numbery:
                break


    def coords(self, x, y=None):
        if type(x) == tuple or type(x) == list:
            x, y = x[0], x[1]
        elif not y:
            print('Please enter a y')
            return
        return self.coordrost[y-1][x-1]
    def uncoords(self, coord):
        for i in range(len(self.coordrost)):
            if coord in self.coordrost[i]:
                x1 = self.coordrost[i].index(coord) + 1
                y1 = i + 1
                return [x1, y1]

if __name__ == '__main__':
    grid1 = grid(20, 20)
    print(grid1.coords([3, 19])) # 362
    print(grid1.uncoords(362)  ) # [3, 19]
    grid1.root.mainloop()
