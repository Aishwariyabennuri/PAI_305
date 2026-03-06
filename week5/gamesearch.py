class TicTacToe:
    def __init__(self):
        self.b=[' ']*9
        self.p='X'

    def show(self):
        for i in range(0,9,3):
            print("|".join(self.b[i:i+3]))
            if i<6: print("-----")

    def win(self,x):
        w=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
        return any(self.b[a]==self.b[b]==self.b[c]==x for a,b,c in w)

    def full(self):
        return ' ' not in self.b

    def over(self):
        return self.win('X') or self.win('O') or self.full()

    def moves(self):
        return [i for i,v in enumerate(self.b) if v==' ']

    def move(self,m):
        self.b[m]=self.p
        self.p='O' if self.p=='X' else 'X'

    def undo(self,m):
        self.b[m]=' '
        self.p='O' if self.p=='X' else 'X'


def minimax(g,maxp):
    if g.over():
        if g.win('X'): return -1
        if g.win('O'): return 1
        return 0

    best=-999 if maxp else 999
    for m in g.moves():
        g.move(m)
        v=minimax(g,not maxp)
        g.undo(m)
        best=max(best,v) if maxp else min(best,v)
    return best


def best_move(g):
    bm,be=None,-999
    for m in g.moves():
        g.move(m)
        v=minimax(g,False)
        g.undo(m)
        if v>be: bm,be=m,v
    return bm


g=TicTacToe()
while not g.over():
    g.show()
    if g.p=='X':
        m=int(input("Move(0-8): "))
        if m not in g.moves():
            print("Invalid"); continue
        g.move(m)
    else:
        print("AI thinking...")
        m=best_move(g)
        print("AI:",m)
        g.move(m)

g.show()
print("You win!" if g.win('X') else "You lose!" if g.win('O') else "Draw")
