def find_common(column_counts, lines, index, ox_cr, c02_cr):
    # count number of 0's and 1's in each column
    ox_cr.clear()
    c02_cr.clear()
    for line in lines:
        line = line.rstrip()
        for i in range(index, len(line)):
            if line[i] == '0':
                column_counts[i][0] += 1
            elif line[i] == '1':
                column_counts[i][1] += 1

    for bit_list in column_counts:
        if bit_list[0] > bit_list[1]:
            #print(bit_list[0], '>', bit_list[1])
            ox_cr.append(0)
            c02_cr.append(1)
        elif (bit_list[0] < bit_list[1]) or (bit_list[0] == bit_list[1]):
            #print(bit_list[0], '<', bit_list[1], 'or equal')
            ox_cr.append(1)
            c02_cr.append(0)
        else:
            return -1
    

def get_ratings(file):
    lines = file.readlines()
    #filter lines based on criteria
    # oxygen
    
    oxygen = []
    for column in range(len(lines[0])):
        if not(len(lines) == 1):
            #find the most/least common bit for this column

            bit_count = [0, 0]
            for row in lines:
                if row[column] == '0':
                    bit_count[0] += 1
                elif row[column] == '1':
                    bit_count[1] += 1

            #print(bit_count[0])
            #print(bit_count[1])

            if bit_count[0] > bit_count[1]:
                #print('first one bigger', bit_count[0], bit_count[1])
                common_bit = 0
            elif bit_count[0] < bit_count[1]:
                #print('second one bigger', bit_count[0], bit_count[1])
                common_bit = 1
            elif bit_count[0] == bit_count[1]:
                #print('equal', bit_count[0], bit_count[1])
                common_bit = 1
            else:
                #print('um', bit_count[0], bit_count[1])
                return -1

            line_num = 0
            while not(line_num == len(lines)):
                lines[line_num] = lines[line_num].rstrip()
                if not(lines[line_num][column] == str(common_bit)):
                    #print(lines[line_num][column], '!=', common_bit)
                    #print('pop', lines[j], 'for not', oxygen_criteria[column], 'at', column)
                    lines.pop(line_num)
                else:
                    #print(lines[line_num][column], '=', common_bit)
                    line_num += 1
    
    oxygen = lines
    print(oxygen)



    # rebuild for next filter
    file.seek(0)
    lines = file.readlines()

    co2 = []
    for column in range(len(lines[0])):
        if not(len(lines) == 1):
            #find the most/least common bit for this column

            bit_count = [0, 0]
            for row in lines:
                if row[column] == '0':
                    bit_count[0] += 1
                elif row[column] == '1':
                    bit_count[1] += 1

            #print(bit_count[0])
            #print(bit_count[1])

            if bit_count[0] > bit_count[1]:
                print('second one smaller', bit_count[0], bit_count[1])
                common_bit = 1
            elif bit_count[0] < bit_count[1]:
                print('first one smaller', bit_count[0], bit_count[1])
                common_bit = 0
            elif bit_count[0] == bit_count[1]:
                print('equal', bit_count[0], bit_count[1])
                common_bit = 0
            else:
                print('um', bit_count[0], bit_count[1])
                return -1

            line_num = 0
            while not(line_num == len(lines)):
                lines[line_num] = lines[line_num].rstrip()
                if not(lines[line_num][column] == str(common_bit)):
                    #print(lines[line_num][column], '!=', common_bit)
                    #print('pop', lines[j], 'for not', oxygen_criteria[column], 'at', column)
                    lines.pop(line_num)
                else:
                    #print(lines[line_num][column], '=', common_bit)
                    line_num += 1
    
    co2 = lines
    print(co2)
    

    file.close()
    return [oxygen, co2]

def main():
    file = open("input.txt", 'r')
    ratings = get_ratings(file)
    #oxygen = ratings[0]
    #co2 = ratings[1]
    oxygen = int("".join([str(bit) for bit in ratings[0]]), 2)
    co2 = int("".join([str(bit) for bit in ratings[1]]), 2)

    print("{}".format(oxygen))
    print("{}".format(co2))
    print("{}".format(oxygen*co2))

if __name__ == '__main__':
    main()