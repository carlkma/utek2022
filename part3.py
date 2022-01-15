from operator import add
# for tuple (i.e. coordinate) addition

def data_to_list(data):
    result = []
    locations = []
    obstacle = []
    for i in range(len(data)):
        data[i] = data[i].replace('\n','')
        data[i] = data[i].replace(',','')
        if i <= 1:
            result.append(list(data[i].split(" ")))
        elif i == 2:
            i2 = list(data[i].split(" "))
            locations.append(i2)
        else:
            ii = list(data[i].split(" "))
            change = False
            if len(ii) == 3:
                for j in range(len(locations)):
                    if ii[0] == locations[j][0] \
                    and ii[1] == locations[j][1]:
                        if ii[2] >= locations[j][2]:
                            locations[j][2] = ii[2]
                            change = True
                if change == False:
                    locations.append(ii)
            if len(ii) == 4:
                obstacle.extend(ii)
    result.extend(locations)
    return result,obstacle


def change_location_to_list_we_need(location):
    x=[0]
    y=[0]
    for i in range(2,len(location)):
        x.append(int(location[i][0]))
        y.append(int(location[i][1]))
    return x,y

def getMatrix(x,y):
    res = []
    for i in range(len(x)):
        not_rly_res = []
        for j in range(len(y)):
            inter = (min(abs(x[j]-x[i]),abs(y[j]-y[i]))+\
             abs(abs(x[j]-x[i])-abs(y[j]-y[i])))
            not_rly_res.append(inter)
        res.append(not_rly_res)
    return res


def collision(x,y,list_of_obstacles):
    for obstacle in list_of_obstacles:
        if x >= obstacle[0] and x <= obstacle[2] and y>= obstacle[1] and y<=obstacle[3]:
            return True
    return False


def get_direction(x1,y1,x2,y2):
    if x2 - x1 > 0 and y2 - y1>0:
        return (1,1)
    if x2 - x1> 0 and y2 - y1 <0:
        return (1,-1)
    if x2 - x1 < 0 and y2 - y1 >0:
        return (-1,1)
    if x2 - x1 < 0 and y2 - y1 < 0:
        return (-1,-1)
    if x2 - x1 == 0 and y2 - y1 >0:
        return (0,1)
    if x2 - x1 == 0 and y2 - y1 <0:
        return (0,-1)
    if x2 - x1 > 0 and y2 - y1 == 0:
        return (1,0)
    if x2 - x1 < 0 and y2 - y1 == 0:
        return (-1,0)


def move(current_position, destination):
    x1, y1 = current_position
    x2, y2 = destination
    direction = get_direction(x1,y1,x2,y2)
    new_position = tuple(map(add, current_position, direction))
    x, y = new_position
    if collision(x,y,list_of_obstacles):
        return detour(current_position)
    return new_position



def detour(current_position):
    x1, y1 = current_position
    if collision(x,y+1,list_of_obstacles)==False and collision(x, y-1, list_of_obstacles)==False:
        new_position = (x, y+1)
        return new_position
    if collision(x+1,y,list_of_obstacles)==False and collision(x-1, y, list_of_obstacles)==False:
        new_position = (x+1, y)
        return new_position

    # four corner situations
    if collision(x+1,y,list_of_obstacles) and collision(x, y-1, list_of_obstacles): # top left corner
        new_position = (x+1, y)
        return new_position
    if collision(x+1,y,list_of_obstacles) and collision(x, y+1, list_of_obstacles): # bottom left corner
        new_position = (x+1, y)
        return new_position
    if collision(x-1,y,list_of_obstacles) and collision(x, y+1, list_of_obstacles): # bottom right corner
        new_position = (x-1, y)
        return new_position
    if collision(x-1,y,list_of_obstacles) and collision(x, y-1, list_of_obstacles): # top right corner
        new_position = (x-1, y)
        return new_position




#main
condition = current_position == (0,0) and len(list_of_locations)==0
while not condition:
    move()
