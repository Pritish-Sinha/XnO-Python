import random
play=[0 for pos in range(9)]
turn=0
def screen():
    print("\t    X 'n' O",end='\n\t')
    for pos in range(9):
        print('[',' ' if not(play[pos]) else play[pos],']',end='\n\t' if (pos+1)%3==0 else '')
    print()
    
def getxy():
    x=int(input("ENTER x CO-ORDINATE :"))
    y=int(input("ENTER y CO-ORDINATE :"))
    position=6+x-3*y
    play[position]="X"
    
def random_move():
    while(1):
        position=random.choice([0,1,2,3,4,5,6,7,8])
        if not play[position]:break
    play[position]="O"
    
def win_lose_check():
    player=None
    for var in range(3):
        if play[3*var]==play[3*var+1] and play[3*var]==play[3*var+2] and play[3*var]!=0:player=play[3*var]
        elif play[var]==play[var+3] and play[var]==play[var+6] and play[var]!=0:player=play[var]
    for var in [0,2]:
        if play[var]==play[4] and play[4]==play[8-var] and play[var]!=0:player=play[var]
    if player=='X':return [False,"WON"]
    elif player=='O':return [False,"LOST"]
    else:return [True]

def check_row(row):
    var=9
    if play[row[0]]==play[row[1]] and play[row[0]]:var=row[2]
    elif play[row[0]]==play[row[2]] and play[row[0]]:var=row[1]
    elif play[row[1]]==play[row[2]] and play[row[2]]:var=row[0]
    if var!=9 and not play[var]:return var
    else: return 9
    
def make_stop_win():
    for var in range(3):
        position=check_row([3*var,3*var+1,3*var+2])
        if position!=9:break
        position=check_row([var,var+3,var+6])
        if position!=9:break
    if position==9:
        for var in [0,2]:
            position=check_row([var,4,8-var])
            if position!=9:break
    if position!=9:
        play[position]='O'
        return True

def computer_move(turn):
    played=False
    corners=[0,2,6,8,0]
    edges=[1,3,5,7,1]
    if turn==1:
        if play[4]=='X':position=random.choice([0,2,6,8])
        elif play.index('X')in corners:position=4
        elif play.index('X') in edges:
            position=random.choice([4,0])
            if not position:position=8-play.index('X')
        play[position]='O'
        played=True
      
    elif turn==2:
        played=make_stop_win()
        if not played:
            isposition=True
            if play[4]=='X' and (play[0 or 2 or 6 or 8]=='X'):
                num=random.choice([0,1])
                if num:
                    for pos in range(4):
                        if corners[pos]==play.index('O'):position=corners[pos+1]
                else:
                    for pos in range(1,5):
                        if corners[pos]==play.index('O'):position=coners[pos-1]
            elif play[4]=='O' and (play[0 and 8]=='X' or play[2 and 6]=='X'):position=random.choice([1,3,5,7])
            elif play[4]=='O' and ((play[0]=='X' and play[5 or 7]=='X') or (play[2]=='X' and play[3 or 7]=='X') or (play[6]=='X' and play[1 or 5]=='X') or (play[8]=='X' and play[1 or 5]=='X')):
                for pos in range(4):
                    if play[corners[pos]]=='X':position=8-corners[pos]
            elif play[1 or 3 or 5 or 7]=='X':
                if play[4]=='X':position=random.choice([0,2,6,8])
                elif play[4]!='X' and play[4]!='O':
                    if play[1]=='X':position=random.choice([0,2])
                    elif play[3]=='X':position=random.choice([0,6])
                    elif play[5]=='X':position=random.choice([2,8])
                    elif play[7]=='X':position=random.choice([6,8])
                elif play[4]=='O':
                    if play[1 and 3]=='X':position=random.choice([0,2,6])
                    elif play[3 and 7]=='X':position=random.choice([0,6,8])
                    elif play[7 and 5]=='X':position=random.choice([2,6,8])
                    elif play[1 and 5]=='X':position=random.choice([0,2,8])
                    else:isposition=False
            if isposition:
                play[position]='O'
                played=True
    if not played:random_move()
    
def new_game():
    for pos in range(9):play[pos]=0
    turn=0
    screen()
    running=True
    while(running):
        turn+=1
        getxy()
        result=win_lose_check()
        running=result[0]
        if running:computer_move(turn)
        result=win_lose_check()
        running=result[0]
        screen()
    print("\t   YOU "+result[1])
    yes_no=input("PLAY AGAIN ?(y/n)").lower()
    if yes_no=='y':new_game()   
new_game()