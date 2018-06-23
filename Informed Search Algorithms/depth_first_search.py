import csv
import copy

# Initializing starting and goal state
init_state = [[], [], [], [3, 1, 2]]
end_state = [[], [], [], [0, 0, 0]]


# Initializing a list of offers by extracting from initial list
def init_offer_list(rows):
    lst = []
    for row in rows:
        row = row[1:]
        offer = [(i,eval(row[i])) for i in range(len(row)) if eval(row[i]) != 0]
        lst.append(offer)
    return lst


# Reading rows from CSV file
def read_file(filename):
    row_list = []
    with open(filename) as file:
        rows = csv.reader(file, delimiter=',')
        next(rows)
        for row in rows:
            row_list.append(row)
    return row_list


# Depth-first search algorithm which takes initial state, goal state and offer list as parameters
def depth_first_search(initial_state, goal_state, lst):
    visited = []
    stack = [initial_state]  # First, added initial state to the stack
    idx = 0

    while stack:
        current = stack.pop()  # Fetching the top element from the stack (reversed list)

        if current not in visited:
            visited.append(current)  # Current node has been added to visited list

        if current[3] == goal_state[3]:
            return visited[-1]  # The path is the last element in visited list

        department_idx = lst[idx][0][0]

        accepted = copy.deepcopy(current)  # Accepted state

        if accepted[3][department_idx] > 0:  # If still hiring for the relevant department, then
            accepted[department_idx].append(idx)  # hire,
            accepted[3][department_idx] = accepted[3][department_idx] - 1

        if accepted[3] == current[3]:
            stack.append(accepted)

        children = [accepted, current]  # Rejected state considered as current state

        for child in reversed(children):  # Reversed of list considered as stack
            if child not in visited:
                stack.append(child)  # Added child to the stack

        idx = idx + 1

    return visited[-1]


rows = read_file('<FILENAME>')
offer_list = init_offer_list(rows)
dfs_path = depth_first_search(init_state, end_state, offer_list)
print(dfs_path)
