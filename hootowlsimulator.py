import random

orange=0
blue=1
purple=2
red=3
yellow=4
green=5

board = [orange,blue,purple,red,blue,purple,red,yellow,green,blue,orange,red,purple,yellow,green,orange,blue,purple,red,green,yellow,orange,blue,purple,red,yellow,green,blue,orange,red,purple,yellow,green,blue,orange,red,purple]
owls = [0,1,2,3]


def rearmost_owl():
    return owls.index(min(owls))

def all_home():
    for i in range(4):
        if(owls[i]<=36): return 0
    return 1

def game_done(array):
    for i in range(4):
        if(array[i]<=36): return 0
    return 1

def owl_in_spot(position):
    for i in range(4):
        if(owls[i]==position): return 1
    return 0

def spot_has_owl(array,position):
    for i in range(4):
        if(array[i]==position):return 1
    return 0

def drawcard():
    return random.randint(0,5)

def color(value):
    colornames = ["orange ","blue   ","purple ","red    ","yellow ","green  "]
    return colornames[value]

def showboard():
    if(all_home()): gameover="yes"
    else: gameover="no"
    print("Turn #"+str(turncounter)+", finished:"+gameover +", rearmost owl #"+str(rearmost_owl()))
    for i in range(len(board)):
        spacenum=str(i)
        if(i<10): spacenum=" "+spacenum
        owllabel=" "
        for j in range(4):
            if(owls[j]==i):
                owllabel="Owl_"+str(j)
        print(spacenum + ":" + color(board[i])+owllabel)

def move_owl(owlnumber, color):
    position=owls[owlnumber]
    while True:
        position+=1
        if(position>36):
            owls[owlnumber]=37
            break
        if(board[position]==color and owl_in_spot(position)==0):
            owls[owlnumber]=position
            break

def spot_has_owl(array,position):
    for i in range(4):
        if(array[i]==position): return 1
    return 0

def owl_move(array, owlnumber, color):
    position=array[owlnumber]
    while True:
        position+=1
        if(position>36):
            return 37
        if(board[position]==color and spot_has_owl(array,position)==0):
            return position
        
def move_length(owlnumber, color):
    position=owls[owlnumber]
    startposition=position
    while True:
        position+=1
        if(position>36):
            return position-startposition
        if(board[position]==color and owl_in_spot(position)==0):
            return position-startposition

def length(array,owlnumber, color):
    position=array[owlnumber]
    startposition=position
    while True:
        position+=1
        if(position>36):
            return position-startposition
        if(board[position]==color and spot_has_owl(array,position)==0):
            return position-startposition
        
def longest_move(color):
    movelengths=[0,0,0,0]
    lengths = "lengths "
    for i in range(4):
        movelengths[i]=move_length(i,color)
        if(owls[i]>36): movelengths[i]=-1
        lengths+=str(movelengths[i])
        lengths+=" "
    #print(lengths)
    return movelengths.index(max(movelengths))

def longest(array,color):
    movelengths=[0,0,0,0]
    lengths = "lengths "
    for i in range(4):
        movelengths[i]=length(array,i,color)
        if(array[i]>36): movelengths[i]=-1
        lengths+=str(movelengths[i])
        lengths+=" "
    #print(lengths)
    return movelengths.index(max(movelengths))

def run_game_rearmost():
    turncount=0
    global owls
    owls = [0,1,2,3]
    while not all_home():
        turncount+=1
        newcard=drawcard()
        #print("card drawn: "+color(newcard) + ", moving owl #" + str(rearmost_owl()))
        move_owl(rearmost_owl(),newcard)
        #owlstate="owl positions: "
        #for i in range(4):
        #    owlstate+=str(owls[i])
        #    owlstate+=" "
        #showboard()
        #input("...")
        #print(owlstate)
    return turncount

def run_game_longest():
    turncount=0
    global owls
    owls = [0,1,2,3]
    #showboard()
    while not all_home():
        turncount+=1
        newcard=drawcard()
        #print("\r\ncard drawn: "+color(newcard) + ", moving owl #" + str(longest_move(newcard)))
        move_owl(longest_move(newcard),newcard)
        #owlstate="owl positions: "
        #for i in range(4):
        #    owlstate+=str(owls[i])
        #    owlstate+=" "
        #showboard()
        #input("...")
        #print(owlstate)
    return turncount

def run_both_games():
    owls_long=[0,1,2,3]
    owls_rear=[0,1,2,3]
    long_turns=0
    rear_turns=0
    while game_done(owls_long)==0 or game_done(owls_rear)==0:
        if not game_done(owls_long): long_turns+=1
        if not game_done(owls_rear): rear_turns+=1
        newcard=drawcard()
        owls_long[longest(owls_long,newcard)]=owl_move(owls_long,longest(owls_long,newcard),newcard)
        owls_rear[owls_rear.index(min(owls_rear))]=owl_move(owls_rear,owls_rear.index(min(owls_rear)),newcard)
    return long_turns, rear_turns
##        owlstate="long game: "
##        for i in range(4):
##            owlstate+=str(owls_long[i])
##            owlstate+=" "
##        owlstate+="   rear game: "
##        for i in range(4):
##            owlstate+=str(owls_rear[i])
##            owlstate+=" "
##        print(owlstate)
        

while True:
    try:
        num_games=int(input("input number of games to run:"))
        break
    except:
        print("invalid entry")
        
sums=[0,0]
long_wins=0
rear_wins=0
ties=0
for games in range(num_games):
    newgame=run_both_games()
    sums[0]+=newgame[0]
    sums[1]+=newgame[1]
    if(newgame[0]<newgame[1]): long_wins+=1
    elif(newgame[0]>newgame[1]): rear_wins+=1
    else: ties+=1
    print("game "+str(games+1)+": long strategy won in "+str(newgame[0])+" moves, rear strategy won in "+str(newgame[1])+" moves")
sums[0]/=num_games
sums[1]/=num_games
print("long strategy won in "+str(sums[0])+" moves and rear strategy won in "+str(sums[1])+" moves on average")
print(sums)
print("long strategy won "+str(long_wins)+" times, rear won "+str(rear_wins)+" times, " +str(ties)+" ties")
if(sums[0]<sums[1]): print("longest move strategy was best in this set")
else: print("rearmost move strategy was best in this set")

##moves_avg_rear=0
##moves_avg_long=0
##num_games=5000
##
##for games in range(num_games):
##    newgame_long=run_game_longest()
##    newgame_rear=run_game_rearmost()
##    print("game "+str(games)+": longest "+str(newgame_long)+" moves, rearmost "+str(newgame_rear)+" moves")
##    moves_avg_rear+=newgame_rear
##    moves_avg_long+=newgame_long
##moves_avg_rear/=num_games
##moves_avg_long/=num_games
##print("longest: average moves "+str(moves_avg_long))
##print("rearmost: average moves "+str(moves_avg_rear))

##turncounter=0
##showboard()
##while not all_home():
##    turncounter+=1
##    newcard=drawcard()
##    print("\r\ncard drawn: "+color(newcard) + ", moving owl #" + str(longest_move(newcard)))
##    move_owl(longest_move(newcard),newcard)
##    owlstate="owl positions: "
##    for i in range(4):
##        owlstate+=str(owls[i])
##        owlstate+=" "
##    showboard()
##    input("...")
##    print(owlstate)
##print("game finished in " + str(turncounter) + " moves")
        
 

