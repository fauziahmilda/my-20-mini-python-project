# a function that takes a alist adn target parameters
# multiple variables: middle, start, end, steps
# recursion or while loop
# increase the steps each time a split is done
# condition to track target position

def binary_search(list, element):
    middle = 0
    start = 0
    end = len(list)
    steps = 0

    while (start <= end):
        print(f"Step {steps} : {str(list[start:end+1])}")

        steps = steps + 1
        middle = (start+end)//2

        if element == list[middle]:
            return middle
        if element < list[middle]:
            end = middle - 1
        else:
            start = middle + 1

    # when loop is done
    return -1


my_list = []
x = 1
amount = int(input("How many number in the list: "))
for item in range(amount):
    my_list.append(x)
    x += 1

print(f"List: {my_list} \n")

target = int(input("Target: "))
print("")

binary_search(my_list, target)
