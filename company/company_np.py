import numpy as np
from operationClass import IntArray

def productivity_of_company(order,data_frame):

    return np.sum(data_frame[order])

def max_product(data_frame):
    i = 0
    bestCompany = i + 1
    sumProducts = 0

    for i in range(len(data_frame)):
        result = productivity_of_company(i,data_frame)
        if result > sumProducts:
            sumProducts = result
            bestCompany = i + 1
    return print(f'The best company is the {bestCompany} with {sumProducts} products')
def min_product(data_frame):
    i = 0
    worstCompany = i + 1
    sumProducts = productivity_of_company(0,data_frame)
    for i in range(len(data_frame)):
        result = productivity_of_company(i,data_frame)
        if  result <= sumProducts:
            sumProducts = result
            worstCompany = i + 1
    return print(f'The worst company is the {worstCompany} with {sumProducts}')
def fileHandling():

    lines = []

    with open('company/company_datas.txt','r') as file:
        for line in file:
            values = line.strip().split(',')
            int_values = [int(val) for val in values]
            lines.append(int_values)

        data_frame = np.array([np.array(row) for row in lines] , dtype='object')
        return data_frame

def main():
    data_frame = fileHandling()

    print(data_frame)

    firstBranch = IntArray(data_frame[0])
    # firstBranch.display()
    # firstBranch.salary()
    # firstBranch.showData()
    min_product(data_frame)
    max_product(data_frame)
main()