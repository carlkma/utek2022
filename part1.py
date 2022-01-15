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


def paragraph(list):
    result = "Robot Name: " + list[1][0] + "; Movement Efficiency: "\
    + list[1][1] + "; Cleaning Efficiency: " + list[1][2] + ";" + "\n"
    for i in range(2,len(list)):
        add = "Location Number: " + str(i-1) + "; Time required: " + \
        list[i][2] + "; Location: " + list[i][0] + " " + list[i][1] + ";" \
        + "\n"
        result += add
    return result

def read_and_write():
    for i in "a","b","c":
        filename_in = "1" +str(i) + ".in"
        f = open(filename_in,"r")
        data = f.readlines()
        f.close()
        list_result = data_to_list(data)
        paragraph_result = paragraph(list_result)
        filename_out = "1" +str(i) + ".out"
        g = open(filename_out,"w")
        g.write(paragraph_result)
        g.close()


if __name__ == '__main__':
    read_and_write()
