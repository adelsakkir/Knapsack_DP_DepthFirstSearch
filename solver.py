#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple
import numpy as np
Item = namedtuple("Item", ['index', 'value', 'weight'])

def Sort(items):

    items.sort(key = lambda x: x[3],reverse=True)
    return items

def dynamic_programming(capacity,item_count,items):
    
    dp_table = np.zeros((capacity+1,item_count+1))
    #dp_table=[[0 for x in range(capacity+1)] for y in range(item_count+1)]

    for item in range(item_count+1):
        for cap in range(capacity+1):
            if item ==0:
                dp_table[cap,item]=0
            elif items[item-1].weight <=cap:
                dp_table[cap,item]=max(dp_table[cap,item-1],items[item-1].value+dp_table[cap-items[item-1].weight,item-1])
            else:
                dp_table[cap,item]=dp_table[cap,item-1]

    optimal_value=int(dp_table[capacity,item_count])
    rem_cap=capacity 
    print (dp_table)

    taken = [0]*len(items)
    for col in range(item_count,0,-1):
        if dp_table[rem_cap,col]!=dp_table[rem_cap,col-1]:
    #         print ("item %d is selected" %(col))
            taken[col-1]=1
            rem_cap-=items[col-1].weight
            if rem_cap <=0:break
    
    # prepare the solution in the specified output format
    output_data = str(optimal_value) + ' ' + str(1) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data

def greedy_value_density(capacity,item_count,items):
    
    item_density= []
    for i in range(0, item_count):
#         line = lines[i]
#         parts = line.split()
        item_density.append([i, items[i].value,items[i].weight,items[i].value/items[i].weight])


    Sort(item_density)
    
#     print(item_density)

    # a trivial algorithm for filling the knapsack
    # it takes items in-order until the knapsack is full
    value = 0
    weight = 0
    taken = [0]*len(items)
    
    for item in item_density:
        if weight + item[2] <= capacity:
            taken[item[0]] = 1
            value += item[1]
            weight += item[2]
        
    
    # prepare the solution in the specified output format
    output_data = str(value) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data


    
def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []

    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i-1, int(parts[0]), int(parts[1])))
    
    #Calling relavant algorithm based on input
    if item_count <400:
        return dynamic_programming(capacity,item_count,items)
    else :
        return greedy_value_density(capacity,item_count,items)

if __name__ == '__main__':

    import sys
    if len(sys.argv) > 1:
        file_location = ".\\data\\ks_400_0"
        
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')

