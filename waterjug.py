#3 water jug problem


capacity = (12, 8, 5) # Maximum capacities of the 3 jugs -> x, y, z
x, y, z = capacity
memory = {} # to mark visited states
ans = [] # store solution path

def get_all_states(state):
    # Let the 3 jugs be called a,b,c
    a, b, c = state
    
    # if current state is already visited earlier
    if (a, b, c) in memory:
        return False
    
    # mark current state as visited
    memory[(a, b, c)] = 1
    
    # if we have reached the goal state, append it to ans and return True
    if a == 6 and b == 6 and c == 0:
        ans.append(state)
        return True
    
    # empty jug a
    if a > 0:
        # empty a into b
        if a + b <= y:
            if get_all_states((0, a + b, c)):
                ans.append(state)
                return True
        else:
            if get_all_states((a - (y - b), y, c)):
                ans.append(state)
                return True
        
        # empty a into c
        if a + c <= z:
            if get_all_states((0, b, a + c)):
                ans.append(state)
                return True
        else:
            if get_all_states((a - (z - c), b, z)):
                ans.append(state)
                return True
    
    # empty jug b
    if b > 0:
        # empty b into a
        if a + b <= x:
            if get_all_states((a + b, 0, c)):
                ans.append(state)
                return True
        else:
            if get_all_states((x, b - (x - a), c)):
                ans.append(state)
                return True
        
        # empty b into c
        if b + c <= z:
            if get_all_states((a, 0, b + c)):
                ans.append(state)
                return True
        else:
            if get_all_states((a, b - (z - c), z)):
                ans.append(state)
                return True
    
    # empty jug c
    if c > 0:
        # empty c into a
        if a + c <= x:
            if get_all_states((a + c, b, 0)):
                ans.append(state)
                return True
        else:
            if get_all_states((x, b, c - (x - a))):
                ans.append(state)
                return True
        
        # empty c into b
        if b + c <= y:
            if get_all_states((a, b + c, 0)):
                ans.append(state)
                return True
        else:
            if get_all_states((a, y, c - (y - b))):
                ans.append(state)
                return True
    
    return False

initial_state = (12, 0, 0)
print("Starting work...\n")
get_all_states(initial_state)

# reverse the order of elements in each tuple in ans to obtain the solution path from initial to goal state.
ans.reverse()
for i in ans:
    print(i)
