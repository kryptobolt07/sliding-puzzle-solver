import copy
state=[[' ',2,3],[1,4,5],[7,8,6]] #make a function to accept initial state
#make a function to check if a solution is feasible for a given initial state
def move(state,move,row,column):
    if move=="l":
        state[row][column],state[row][column-1]=state[row][column-1],state[row][column]
        row,column=row,column-1
    elif move=="r":
        state[row][column],state[row][column+1]=state[row][column+1],state[row][column]
        row,column=row,column+1
    elif move=="t":
        state[row][column],state[row-1][column]=state[row-1][column],state[row][column]
        row,column=row-1,column
    else:
        state[row][column],state[row+1][column]=state[row+1][column],state[row][column]
        row,column=row+1,column
    return state,row,column

def print_state(state):
    for i in range(3):
        for j in range(3):
            print(f"{state[i][j]}",end=" ")
        print("")
    print("\n")

def possible_moves(state,row=1,column=1):
    moves = {
        'l': False,  
        'r': False,  
        't': False,  
        'd': False }
    if column > 0:  
        moves['l'] = True
    if column < 2:  
        moves['r'] = True
    if row > 0:          
        moves['t'] = True
    if row < 2:  
        moves['d'] = True

    return moves

def is_goal(state):
    if state==[[1, 2, 3], [4, 5, 6], [7, 8, ' ']]:
        return True

def dequeue(queue):
    for i in range(len(queue)-1):
        queue[i]=queue[i+1]
    return queue

# Have to try to improve how i store the states of the game and implement a more efficient way of doing things
def BFS(state):
    visited=[]
    queue=[[state,0,0]]
    parent_states={}
    while(True):
        state=queue[0][0]
        row,column=queue[0][1],queue[0][2]
        if(is_goal(state)):
            break
        moves=possible_moves(state,row,column)
        for whatmove,possible in moves.items():
            if possible:
                next_state,next_row,next_column=move(copy.deepcopy(state),whatmove,row,column)
                if(next_state not in visited):
                    visited.append(next_state)
                    queue.append([next_state,next_row,next_column])
                    parent_states[tuple(tuple(inner) for inner in next_state)]=tuple(tuple(inner) for inner in state)
        dequeue(queue)
    backtrack(parent_states)

def backtrack(parent_states,cur_state=((1, 2, 3), (4, 5, 6), (7, 8, ' '))):
    if(cur_state!=(((' ',2,3),(1,4,5),(7,8,6)))):
        backtrack(parent_states,parent_states[cur_state])
    print_state(cur_state)
BFS(copy.deepcopy(state))
