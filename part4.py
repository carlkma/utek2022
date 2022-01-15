# multiple robots and no obstacles

# import data_to_list(data) from part3.py
# changing the data to list form that we can use

# function one:
# input: the result from the imported data_to_list(data) function 
# output: a dictionary that gives the location number of the position that need to be cleaned
# as key, and the xy coordinated representation as value

# function two:
# input: the result from the imported data_to_list(data) function 
# output: a dictionary that gives the name of the robot as keys
# and [moveEff,cleanEff] as value

# function three:
# input: the dictionary from function one; the dictionary from function two
# output: the division of work in the format of a dictionary:
# the name of the robot as key
# the location each robot need to clean as value
#
# brief explanation of how to divide:
# adding up the xy coordinate value for each point: ie. point (1,2) will get a value of 3
# adding up the total value of all points: ie. (1,2),(3,4),(8,9) will get 3+7+17=27
# divide the number to number of robots: ie. two robots: 27/2 = 13.5
# write a helper function to test which orientation will provide a minimum variance:
# ie. (8,9) for one robot, (1,2),(3,4) for the other
# another helper function to select which robot for work:
# the (8,9) one only clean once, choosing the one with smaller cleanEff
# (1,2),(3,4) with higher cleanEff

# helper functions 4 and 5 as discribed above

# function six:
# import function process(big_list) from part2.py
# take in the dictionary, call the imported function
# output: the position routine of each robot

# import printx(list_data,position_routine,x,y) from part2.py
# imput: the result from function six
# output: the result required to write in 4a.out

# function seven:
# read_and_write()
# read the provided info and write to 4a.out