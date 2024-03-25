import numpy as np

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

main()