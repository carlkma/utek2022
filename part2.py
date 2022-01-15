def data_to_list(data):
    result = []
    locations = []
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
            for j in range(len(locations)):
                if ii[0] == locations[j][0] and ii[1] == locations[j][1]:
                    if ii[2] >= locations[j][2]:
                        locations[j][2] = ii[2]
                        change = True
            if change == False:
                locations.append(ii)
    result.extend(locations)
    return result

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

def next_move(small_list_before_remove,after_remove,position_cleaned):
    list2 = after_remove[:]
    list2.sort()
    minimum = list2[1]
    position = small_list_before_remove.index(minimum)
    while True:
        if position not in position_cleaned:
            break
        else:
            list3 = small_list_before_remove[:]
            list3[position] = -1
            position = list3.index(minimum)
    return position

def remove(small_list,position_cleaned):
    position_cleaned.sort(reverse=True)
    small_list_copy = small_list[:]
    for i in range(len(position_cleaned)):
        if position_cleaned[i] < len(small_list_copy):
            small_list_copy.pop(position_cleaned[i])
    return small_list_copy

def process(big_list):
    global position_cleaned
    ### starting from the origin
    position_cleaned = [0]
    position_routine = []
    position = next_move(big_list[0],big_list[0],position_cleaned)
    while True:
        next_position = position
        position_routine.append(next_position)
        next_position_list = big_list[next_position]
        next_after_remove = remove(next_position_list,position_cleaned)
        position_cleaned.append(next_position)
        if len(next_after_remove) == 1:
            break
        else:
            position = next_move(next_position_list,\
            next_after_remove,position_cleaned)
    return position_routine

def printx(list_data,position_routine,x,y):
    result = "Robot " + str(list_data[1][0]) + "\n"
    x.append(0)
    y.append(0)
    current_location = [0,0]
    for i in range(len(position_routine)+1):
        destination = [x[i+1],y[i+1]]
        while current_location != destination:
            if x[i+1]-current_location[0] > 0:
                if y[i+1]-current_location[1] > 0:
                    current_location[0] += 1
                    current_location[1] += 1
                    result += "move " + str(current_location[0]) + " " +\
                    str(current_location[1]) + "\n"

                elif y[i+1]-current_location[1] < 0:
                    current_location[0] += 1
                    current_location[1] += -1
                    result += "move " + str(current_location[0]) + " " +\
                    str(current_location[1]) + "\n"

                elif y[i+1]-current_location[1] == 0:
                    current_location[0] += 1
                    current_location[1] += 0
                    result += "move " + str(current_location[0]) + " " +\
                    str(current_location[1]) + "\n"

            elif x[i+1]-current_location[0] < 0:
                if y[i+1]-current_location[1] > 0:
                    current_location[0] += -1
                    current_location[1] += 1
                    result += "move " + str(current_location[0]) + " " +\
                    str(current_location[1]) + "\n"

                elif y[i+1]-current_location[1] < 0:
                    current_location[0] += -1
                    current_location[1] += -1
                    result += "move " + str(current_location[0]) + " " +\
                    str(current_location[1]) + "\n"

                elif y[i+1]-current_location[1] == 0:
                    current_location[0] += -1
                    current_location[1] += 0
                    result += "move " + str(current_location[0]) + " " +\
                    str(current_location[1]) + "\n"

            elif x[i+1]-current_location[0] == 0:
                if y[i+1]-current_location[1] > 0:
                    current_location[0] += 0
                    current_location[1] += 1
                    result += "move " + str(current_location[0]) + " " +\
                    str(current_location[1]) + "\n"

                elif y[i+1]-current_location[1] < 0:
                    current_location[0] += 0
                    current_location[1] += -1
                    result += "move " + str(current_location[0]) + " " +\
                    str(current_location[1]) + "\n"
        else:
            if current_location != [0,0]:
                result += "clean " + str(destination[0]) + " " +\
                str(destination[1]) + "\n"
            else:
                result += "rest"
    return result

def read_and_write():
    for i in "a","b","c":
        filename_in = "2" +str(i) + ".in"
        f = open(filename_in,"r")
        data = f.readlines()
        f.close()
        list_result = data_to_list(data)
        x,y = change_location_to_list_we_need(list_result)
        matrix = getMatrix(x,y)
        routine = process(matrix)
        result = printx(list_result,routine,x,y)
        filename_out = "2" +str(i) + ".out"
        g = open(filename_out,"w")
        g.write(result)
        g.close()



if __name__ == '__main__':
    read_and_write()