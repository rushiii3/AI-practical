# C:\Users\Lenovo\AppData\Local\Programs\Python\Python311\Scripts
'''download simple ai library by tying "pip install simpleai"  in cmd here '''

from __future__ import print_function
from simpleai.search import astar,SearchProblem
from simpleai.search.viewers import WebViewer

GOAL='''1-2-3
4-5-6
7-e-8'''

INITIAL ='''4-1-2
7-3-e
8-5-6'''

def list_to_string(list):
    return '\n'.join(['-'.join(row) for row in list])

def string_to_list(string):
    return  [row.split('-') for row in string.split("\n")]

def find_location (rows,element_to_find):
    '''Find the location of a piece in the puzzle. Returnsa tuple:row,column'''
    for ir,row in enumerate(rows):
        for ic,element in enumerate(row):
            if element ==element_to_find:
                return ir,ic

'''We creatre a cache for the goal position of each peice , so we dont have to recalculate them every time'''

goal_position={}
rows_goal=string_to_list(GOAL)

for number in '123456789e':
    goal_position[number]=find_location(rows_goal,number)

class EightPuzzleProblem(SearchProblem):
    def actions(self,state):
        '''Returns a list of the pieces we can move to the empty space'''
        rows=string_to_list(state)
        row_e,col_e=find_location(rows,'e')
        actions=[]
        if row_e >0:
            actions.append(rows[row_e-1][col_e])
        if row_e <2 :
            actions.append(rows[row_e+1][col_e])
        if col_e >0:
            actions.append(rows[row_e][col_e -1 ])
        if col_e <2 :
            actions.append(rows[row_e][col_e +1])
        return actions
        
    def result(self,state,action):
        '''Return the resulting state after moving a piece to the empty space.(the "action" parameter contains the piece to move)'''

        rows=string_to_list(state)
        row_e,col_e=find_location(rows,'e')
        row_n,col_n= find_location(rows,action)
        rows[row_e][col_e],rows[row_n][col_n]=rows[row_n][col_n],rows[row_e][col_e]

        return list_to_string(rows)
    
    def is_goal(self,state):
        '''returns true if a state is the goal of state'''
        return state==GOAL
    
    def cost(self,state1,action,state2):
        '''returns the cost of performing an action .Not useful on this problem'''
        return 1
    def heuristic(self,state):
        '''Returns an *estimation* of the distance from a state to the goal.We are using the Manhattan Distance'''

        rows =string_to_list(state)
        distance =0
        for number in '12345678e':
            row_n,col_n =find_location(rows,number)
            row_n_goal,col_n_goal=goal_position[number]
            distance += abs(row_n - row_n_goal) + abs(col_n - col_n_goal)
        return distance

result =astar(EightPuzzleProblem(INITIAL))

for action,state in result.path():
    print('Movenumber',action)
    print(state)


'''OUTPUT
Movenumber None
4-1-2
7-3-e
8-5-6
Movenumber 3
4-1-2
7-e-3
8-5-6
Movenumber 5
4-1-2
7-5-3
8-e-6
Movenumber 8
4-1-2
7-5-3
e-8-6
Movenumber 7
4-1-2
e-5-3
7-8-6
Movenumber 4
e-1-2
4-5-3
7-8-6
Movenumber 1
1-e-2
4-5-3
7-8-6
Movenumber 2
1-2-e
4-5-3
7-8-6
Movenumber 3
1-2-3
4-5-e
7-8-6
Movenumber 6
1-2-3
4-5-6
7-8-e
Movenumber 8
1-2-3
4-5-6
7-e-8
'''
