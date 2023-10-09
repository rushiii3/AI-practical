initial_state = (3,3,'left',0,0)
goal_state = (0,0,'right',3,3)
solution_path = []
def is_valid(state):
    cl,ml,boat,cr,mr = state
    return (
        0<=cl<=3 and
        0<=ml<=3 and
        0<=cr<=3 and
        0<=mr<=3 and
        (ml==0 or ml>=cl) and
        (mr==0 or mr>=cr))
def succors(state):
        children=[]
        cl,ml,boat,cr,mr = state
        moves = [(0,1),(1,0),(1,1),(0,2),(2,0)]
        if(boat == 'left'):
            for move in moves:
                new_state = (
                    cl-move[0],
                    ml-move[1],
                    'right',
                    cr+move[0],
                    mr+move[1]                    
                    )
                if is_valid(new_state):
                    children.append(new_state)
        else:
            for move in moves:
                new_state = (
                    cl+move[0],
                    ml+move[1],
                    'left',
                    cr-move[0],
                    mr-move[1]                    
                    )
                if is_valid(new_state):
                    children.append(new_state)
        return children

def dfs(current_state,path):
        if current_state == goal_state:
            return path+[current_state]
        for child_state in succors(current_state):
            if child_state not in path:
                new_path = path + [current_state]
                solution = dfs(child_state,new_path)
                if solution:
                    return solution
        return None
def print_solution(solution):
        if solution:
            for state in solution:
                print(state)
solution = dfs(initial_state,[])
print_solution(solution)

            
            
        
