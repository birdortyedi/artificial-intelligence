import csv
import copy
import queue as Q

# Initializing starting and goal state
init_state_ucs = [[], [], [], [3, 1, 2]]
end_state_ucs = [[], [], [], [0, 0, 0]]


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


# Uniform search algorithm which takes initial state, goal state and offer list as parameters
def uniform_cost_search(initial_state, goal_state, lst):
    visited = []
    queue = Q.PriorityQueue()  # For getting the minimum cost at the first element of queue
    queue.put((0, initial_state, 0))

    while queue:
        print('queue: ' + str(queue.queue))
        cost, current, idx = queue.get()  # Fetching the element with the minimum cost on the queue

        department_idx = lst[idx][0][0]
        print('department: ' + str(department_idx))

        possible_costs = [lst[idx][0][1], 0]

        visited.append(current)  # Current node has been added to visited list

        if current[3] == goal_state[3]:
            return visited[-1]  # The path is the last element in visited list

        print('cost: ' + str(cost))
        print('visited: ' + str(visited))

        accepted = copy.deepcopy(current)  # Accepted state
        rejected = copy.deepcopy(current)  # Rejected state

        if accepted[3][department_idx] > 0:  # If still hiring for the relevant department, then
            accepted[department_idx].append(idx)  # hire,
            accepted[3][department_idx] = accepted[3][department_idx] - 1

        children = [accepted, rejected]

        for possible_cost, child in zip(possible_costs, children):
            if idx < len(lst)-1:
                total_cost = cost + int(possible_cost)  # Calculating the total cost
                queue.put((total_cost, child, idx + 1))  # Add to the queue

    return visited[-1]


rows = read_file('<FILENAME>')
offer_list = init_offer_list(rows)
ucs_path = uniform_cost_search(init_state_ucs, end_state_ucs, offer_list)
print(ucs_path)
