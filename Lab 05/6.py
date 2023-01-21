import ast
points_list = input()
points_list = ast.literal_eval(points_list)
length = float(input())
def length_of_line(points_list, length):
    import math
    for i in range(len(points_list)):
        x1 = points_list[i][0][0]
        y1 = points_list[i][0][1]
        x2 = points_list[i][1][0]
        y2 = points_list[i][1][1]
        l = round(math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2)), 2)
        if l == length:
            return i
    return -1

print(length_of_line(points_list, length))
