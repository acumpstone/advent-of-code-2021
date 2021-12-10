def get_rates(file):
    gamma = []
    epsilon = []
    # first index is for column of input
    # scond index is a list that contains number of 0's and 1's in the column
    lines = file.readlines()
    column_counts = [[0]*2 for i in range(len(lines[0].rstrip()))]

    # count number of 0's and 1's in each column
    for line in lines:
        line = line.rstrip()
        for i in range(len(line)):
            if line[i] == '0':
                column_counts[i][0] += 1
            else:
                column_counts[i][1] += 1

    file.close()

    #build gamma and epsilon
    for i in range(len(column_counts)):

        if (column_counts[i][0] > column_counts[i][1]):
            print(column_counts[i][0], '>', column_counts[i][1])
            gamma.append(0)
            epsilon.append(1)
        else:
            print(column_counts[i][1], '>', column_counts[i][0])
            gamma.append(1)
            epsilon.append(0)

    return [gamma, epsilon]

def main():
    file = open("input.txt", 'r')
    rates = get_rates(file)
    gamma = int("".join([str(bit) for bit in rates[0]]), 2)
    epsilon = int("".join([str(bit) for bit in rates[1]]), 2)

    print("{}, {}".format(gamma, epsilon))
    print("{}".format(gamma*epsilon))

if __name__ == '__main__':
    main()