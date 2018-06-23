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


# Breadth-first search algorithm which takes initial state, goal state and offer list as parameters
def breadth_first_search(initial_state, goal_state, lst):
    queue = [initial_state]  # First, added initial state to the queue
    visited = [initial_state]
    idx = 0

    while queue:
        current = queue.pop(0)  # Fetching the first element from the queue

        if current[3] == goal_state[3]:
            return visited[-1]  # The path is the last element in visited list

        department_idx = lst[idx][0][0]

        rejected = copy.deepcopy(current)  # Rejected state
        accepted = copy.deepcopy(current)  # Accepted state
        if accepted[3][department_idx] > 0:  # If still hiring for the relevant department, then
            accepted[department_idx].append(idx)  # hire,
            accepted[3][department_idx] = accepted[3][department_idx] - 1

        if accepted[3] == rejected[3]:
            queue.append(accepted)

        children = [accepted, rejected]

        for child in children:
            if child not in visited:
                queue.append(child)  # Added child to the queue
                visited.append(child)  # Added child to visited list

        idx = idx + 1  # Increasing the number of interviewed candidates

    return visited[-1]


rows = read_file('<FILENAME>')
offer_list = init_offer_list(rows)
bfs_path = breadth_first_search(init_state, end_state, offer_list)
print(bfs_path)
