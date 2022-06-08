import math
import matplotlib.pyplot as plt
def take_input(traps_count) :
    point_list = []
    x_coordinates = []
    y_coordinates = []
    for i in range(traps_count):
        x, y = [float(i) for i in input().split()]
        y_coordinates.append(y)
        x_coordinates.append(x)
        point_list.append([x,y])
    poly_vertices = convex_hull((point_list), traps_count)
    return poly_vertices,x_coordinates,y_coordinates
def convex_hull(point_list, traps_count) -> [int] :
    if traps_count < 3: 
        return point_list
    bottomost_point = left_index(point_list) 
    hull = [] 
    first_point = bottomost_point
    second_point = 0
    while(True): 
        hull.append(first_point) 
        second_point = (first_point + 1) % traps_count
        for i in range(traps_count): 
            if(orientation(point_list[first_point],  
                           point_list[i], point_list[second_point]) == 1): 
                second_point = i 
        first_point = second_point 
        if(first_point == bottomost_point): 
            break
    vertices = []
    for each in hull:
        vertices.append(point_list[each])
    vertices.append(vertices[0])
    return vertices
def left_index(point_list) :
    minimum = 0
    for i in range(1,len(point_list)): 
        if point_list[i][1] < point_list[minimum][1]: 
            minimum = i 
        elif point_list[i][1] == point_list[minimum][1]: 
            if point_list[i][0] < point_list[minimum][0] : 
                minimum = i 
    return minimum 
def orientation(first_point, second_point, third_point) :
    value = (second_point[1] - first_point[1]) * (third_point[0] - second_point[0]) - (second_point[0] - first_point[0]) * (third_point[1] - second_point[1]) 
    if value == 0:   
        return 0  # collinear
    elif value > 0: 
        return 1  # Clockwise
    else: 
        return 2  # Counterclockwise
def perimeter_length(point_list) -> int :
    perimeter = 0
    if len(point_list)<3:
        return 0
    for i in range(0,len(point_list)) :
        point_1 = point_list[i]
        if i == len(point_list) - 1 :
            break
        else :
            point_2 = point_list[i+1]
        perimeter += math.sqrt(((point_2[0]-point_1[0])**2)+((point_2[1]-point_1[1])**2))
    return round(perimeter,2)
def printing_output(point_list) -> str :
    k=''
    for i in point_list:
        k+=str(tuple(i))+"-"
    print(k[:-1])
def plotting(x,y,point_list) :
    plt.scatter(x,y,color = 'black')
    plt.xlabel("X - Axis")
    plt.ylabel("Y - Axis")
    if len(point_list)<3:
        plt.show()
        return 
    x_points = []
    y_points = []
    points = [point for coordinate in point_list for point in coordinate]
    x_points = points[::2]
    y_points = points[1::2]
    plt.plot(x_points,y_points,color='black')
    # plt.plot(x_points,y_points,color='black')
    plt.legend(["Outline", "Trap Location"], loc ="upper right")
    plt.show()
traps_count=1
while(traps_count!=0) :
    for region in range(1,1000):
        traps_count = int(input())
        if (traps_count == 0):
            break  
        poly_vertices,x_points,y_points = take_input(traps_count)
        print()
        print("Region #",region,":")
        printing_output(poly_vertices)
        print ("Perimeter Length = ",perimeter_length(poly_vertices))
        plotting(x_points,y_points,poly_vertices)
