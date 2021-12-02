def calculate_position(file):
    position = [0,0]
    aim = 0
    direction_and_amount = []

    for line in file:
        direction_and_amount = line.rstrip().split()
        direction = direction_and_amount[0]
        amount = int(direction_and_amount[1])

        if direction == 'forward':
            position[0] += amount
            position[1] += (amount * aim)
        elif direction == 'down':
            aim += amount
        elif direction == 'up':
            aim -= amount
        else:
            return -1

    file.close()
    return position

def main():
    file = open("input.txt", 'r')
    positions = calculate_position(file)
    print("{}, {}".format(positions[0], positions[1]))
    print("{}".format(positions[0]*positions[1]))

if __name__ == '__main__':
    main()