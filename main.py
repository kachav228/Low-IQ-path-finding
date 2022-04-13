# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



def check_map_if_available(point, map):
   # l1 = len(map)
   # l2 = len(map[point[0]])
    if(point[0] >= 0 and point[1] >= 0 and point[0] < len(map) and point[1] < len(map[point[0]])):
        if(map[point[0]][point[1]] == 0):
            return True
    return False

def gen_points(point, map):
    result = []
    if(check_map_if_available((point[0] + 1, point[1]), map)):
        result.append((point[0] + 1, point[1]))
    if (check_map_if_available((point[0] - 1, point[1]), map)):
        result.append((point[0] - 1, point[1]))
    if (check_map_if_available((point[0], point[1] + 1), map)):
        result.append((point[0], point[1] + 1))
    if (check_map_if_available((point[0], point[1] - 1), map)):
        result.append((point[0], point[1] - 1))
    return result

def find_path(map, st_point, fn_point):
    path_array = [[st_point]]
    explored = []
    fin_path = []
    cur_point = st_point

    for t in map:
        print(t)
    flag = False
    while (len(path_array) > 0):
        dels = []
        print("path")
        for p in path_array:
            print(p)
        ############
        for i in range(0, len(path_array)):
            path = path_array[i]
            mp = False
            l = len(path) - 1
            for p in gen_points(path[l], map):
                if(p not in explored):
                    if(p == fn_point):
                        if(mp):
                            del path[-1]
                        path.append(p)
                        fin_path = path
                        flag = True
                        break
                    if(not mp):
                        mp = 1
                        path.append(p)
                    else:
                        np = path.copy()
                        del np[-1]
                        np.append(p)
                        path_array.append(np)
            explored.append(path[l])
            if(not mp):
                dels.append(i)
            if(flag):
                break
        for i in range(0, len(dels)):
            del path_array[dels[i] - i]
        if (flag):
            break
    return fin_path

map = [[0, 1 , 0, 0, 1, 0, 0],
       [0, 1 , 0, 0, 1, 1, 0, 0],
       [0, 1 , 0, 1, 0, 0, 1, 0],
       [0, 1 , 0, 0, 0, 0, 0, 0],
       [0, 1 , 0, 1, 1, 0],
       [0, 0 , 0, 0, 0, 0],]

st_point = (0, 0)
fn_point = (0, 5)

fin_path = find_path(map, st_point, fn_point)

print(fin_path)

for p in fin_path:
    map[p[0]][p[1]] = 20

for i in map:
    for j in i:
        if(j == 20):
            print('x', end='')
        else:
            print(j, end='')
    print()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
