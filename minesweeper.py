from random import randint

import zmq
import sys
import time
class Minesweeper:

    def __init__(self):
        grid_size=0 
        port = "5556"
        context = zmq.Context()
        self.socket = context.socket(zmq.PAIR)
        self.socket.bind("tcp://*:%s" % port)
        self.zmq_pair()


    def zmq_pair(self):


        self.socket.send('PLAYING MINESWEAPER Y or N')
        msg = self.socket.recv()
        print msg
        if msg == 'Y':
            #self.socket.send('enter the SIZE OF THE GRID')
            self.grid_size = int(self.socket.recv())
            print self.grid_size
            actual_grid = self.fill_actual_grid(self.grid_size)
            self.view_grid(actual_grid)
            self.check_grid(actual_grid)
    
    def check_grid(self,actual_grid):
        chk = True
        while chk:
           # self.socket.send('enter the poition of the cell you want to clear or s for soulution ')
            grid_cod = self.socket.recv()
            
            try:
                if grid_cod == 's':
                    self.view_grid(actual_grid)
                    break
                else: 

                    a,b = grid_cod.split(' ')
                    print '\n'+ a +'\n'
                    print b + '\n'
                    clear_x=int(b)
                    clear_y=int(a)
                    clear_x-=1
                    clear_y-=1
                    if actual_grid[clear_x][clear_y]=='m':
                        HEADER = '\033[95m'
                        #self.socket.send('\033[91mYOU LOST LANDED ON A !!!!!!!!!!!!!!!!!!MINE!!!!!!!!!MINE!!!!!!!!!!!!!!!MINe!!!!!!!!!!!!!!!!!!\033[0m')
                        self.socket.send('m')
                        self.view_grid(actual_grid)
                        break
                    #if actual_grid[clear_x][clear_y] == 0
                    self.socket.send(str(actual_grid[clear_x][clear_y]))
                    print '\n  The grid valuw is   '
                    print actual_grid[clear_x][clear_y]
                   # player_grid[clear_x][clear_y]=actual_grid[clear_x][clear_y]
                    #self.view_grid(player_grid)
            except ValueError:
                pass
            


    #def enter_cell(self):
        size = int(raw_input('ENTER YOUR DIFFICULTY LEVEL'))
        actual_grid = self.fill_actual_grid(size)
        player_grid = self.generate_actual_grid(size,'x')
        #self.zmq_pair(actual_grid)
        self.view_grid(player_grid)
        #self.view_grid(actual_grid)
        while True:
            x = raw_input('''\n enter the positon of the cell to clear or 's' for solution''')
            try:
                if x == 's':
                    self.view_grid(actual_grid)
                    break
                else: 

                    a,b = x.split(' ')
                    clear_x=int(b)
                    clear_y=int(a)
                    clear_x-=1
                    clear_y-=1
                    if actual_grid[clear_x][clear_y]=='m':
                        HEADER = '\033[95m'
                        print HEADER + '\033[91mYOU LOST LANDED ON A !!!!!!!!!!!!!!!!!!MINE!!!!!!!!!MINE!!!!!!!!!!!!!!!MINe!!!!!!!!!!!!!!!!!!\033[0m' + HEADER
                        self.view_grid(actual_grid)
                        break
                    #if actual_grid[clear_x][clear_y] == 0
                        
                    player_grid[clear_x][clear_y]=actual_grid[clear_x][clear_y]
                    self.view_grid(player_grid)
            except ValueError:
                print 'Invalid Option Try again'
    
    def view_grid(self,pgrid):
        for x in range(0,len(pgrid)):
            print '\n'
            for y in range(0,len(pgrid)):
                print(str(pgrid[x][y]) + '  '),
            
    def fill_actual_grid(self,size):
        act_grid = self.generate_actual_grid(size,0)
        for t in range(0,(size + 3)):
                rand_x=randint(0,(size-1))
                rand_y=randint(0,(size-1))
                act_grid[rand_x][rand_y] = 'm'                
        #self.view_grid(act_grid)
        for x in range(0,size):        
            for y in range(0,size):
                #prtin  x,y
                #prtin  act_grid[x][y]
                num = 0
                    
                if act_grid[x][y] != 'm':
                    
                    try:
                        if act_grid[x][y-1] == 'm':
                            num = num + 1
                            #prtin  '1 x y-1 '
                    except IndexError:
                        pass
                    try:
                        if act_grid[x][y+1] == 'm':
                            num = num + 1
                            #prtin  '1 x y+1'
                    except IndexError:
                        pass
                    try:
                        if act_grid[x+1][y] == 'm':
                            num = num + 1
                            #prtin  '1 x+1 y'
                    except IndexError:
                        pass
                    try:
                        if act_grid[x-1][y] == 'm':
                            num = num + 1
                            #prtin  '1 x-1 y'
                    except IndexError:
                        pass
                    try:
                        if act_grid[x-1][y+1] == 'm':
                            num = num + 1
                            #prtin  '1 x-1 y+1'
                    except IndexError:
                        pass
                    try:
                        if act_grid[x+1][y-1] == 'm':
                            num = num + 1
                            #prtin  '1 x+1 y-1' 
                    except IndexError:
                        pass
                    try:
                        if act_grid[x-1][y-1] == 'm':
                            num = num + 1
                            #prtin  '1 x-1 y-1'
                    except IndexError:
                        pass
                    try:
                        if act_grid[x+1][y+1] == 'm':
                            num = num + 1
                            #prtin  '1 x+1 y+1'
                    except IndexError:
                            pass
                    act_grid[x][y] = num
        return act_grid

    def generate_actual_grid(self,size,char):
        a=[]
        for n in range(0,size):
            a.append([char])
            for x in range(0,size):
                a[n].append(char)

        return a
                
                  

        

if __name__ == '__main__':
    mine = Minesweeper()
    mine.enter_cell()
