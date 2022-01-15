def data_to_list(data):
    result = []     # final output
    locations = []  # helper variable
    for i in range(len(data)):
        data[i] = data[i].replace('\n','')  # clean \n
        data[i] = data[i].replace(',','')   # clean ,
        if i <= 1:
            result.append(list(data[i].split(" "))) # split the text into list
        elif i == 2:
            i2 = list(data[i].split(" "))
            locations.append(i2)
        else:
            ii = list(data[i].split(" "))
            change = False
            for j in range(len(locations)):
                if ii[0] == locations[j][0] and ii[1] == locations[j][1]: 
                    # check if there is same location 
                    if ii[2] >= locations[j][2]:
                        locations[j][2] = ii[2]     # replace if the second one is bigger
                        change = True
            if change == False:
                locations.append(ii)                # if there is no replacement
    result.extend(locations)                        # put the helper variable into final result
    return result


def paragraph(list):
    result = ""
    # first line that includes the robot characteristics
    for j in range(int(list[0][0])):
        result += "Robot Name: " + str(list[j+1][0]) + "; Movement Efficiency: "\
    + str(list[j+1][1]) + "; Cleaning Efficiency: " + str(list[j+1][2]) + ";" + "\n"

    # other lines that includes including locations
    for i in range(int(list[0][1])):
        add = "Location Number: " + str(i+1) + "; Time required: " + \
        list[i+int(list[0][0])+1][2] + "; Location: " + list[i+int(list[0][0])+1][0] \
        + " " + list[i+int(list[0][0])+1][1] + ";" + "\n"
        result += add
    return result

def read_and_write():
    for i in "a","b","c":
        filename_in = "1" +str(i) + ".in"
        f = open(filename_in,"r")
        data = f.readlines()    
        f.close()
        list_result = data_to_list(data)            # transfer to list format
        paragraph_result = paragraph(list_result)   # transfer to paragraph fomat
        filename_out = "1" +str(i) + ".out"         # create output code
        g = open(filename_out,"w")                  # write
        g.write(paragraph_result)
        g.close()


if __name__ == '__main__':
    read_and_write()
