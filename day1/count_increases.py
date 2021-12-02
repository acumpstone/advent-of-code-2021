from collections import deque
import itertools

def get_increases_from_file(file):
    num_of_increases = 0
    list_of_four = deque([])
    window_behind = deque([])
    window_current = deque([])

    for line in file:
        line = int(line.rstrip())
        # fence post
        if len(list_of_four) < 3:
            list_of_four.append(line)
            print(list_of_four[len(list_of_four)-1])
            continue
        
        list_of_four.append(line)

        window_behind = itertools.islice(list_of_four, 0, 3)
        window_current = itertools.islice(list_of_four, 1, 4)
        if sum(window_current) > sum(window_behind):
            num_of_increases += 1

        list_of_four.popleft()

    file.close()
    return num_of_increases

def main():
    file = open("input.txt", 'r')
    num_of_increases = get_increases_from_file(file)
    print(num_of_increases)

if __name__ == '__main__':
    main()