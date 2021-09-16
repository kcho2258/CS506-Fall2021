def read_triangle(path_to_file):
    # input is a string representing the file location 
    # returns a list of list of ints

    f = open(path_to_file, 'r')
    lines = f.readlines()
    triangle = []
    for line in lines:
        triangle.append([int(x) for x in line.split(' ')])
    f.close()
    return triangle
print(read_triangle("./triangle.txt"))

def add_levels(x, y):
    # assume x and y have the same length
    res = [] 
    for i in range(len(x)):
        res.append(x[i] + y[i])
    return res

def elementwise_max(x,y):
    if len(x) != len(y):
        raise ValueError("lengths not equal")
    
    res = [] 
    for i in range(len(x)):
        res.append(max(x[i] + y[i]))
    return res

def fold_level(cur, nxt):
    right_options = add_levels([0] + cur, nxt)
    left_options = add_levels(cur + [0], nxt)
    max_options = elementwise_max(right_options, left_options)
    return max_options

# top down approach 
def fold(triangle):
    # returns a list of max path sums 
    # does not work when triangle length is 1 
    current_level = triangle[0]
    for level in triangle:
        current_level = fold_level(current_level, level)
    return current_level

print(max(fold(read_triangle("./triangle.txt"))))