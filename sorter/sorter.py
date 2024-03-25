def main():
    intro()


def intro():
    print("Hello and welcome to sorter!")
    print(
        "Enter a common seperated list of letters and numbers and we will sort it for you :)"
    )
    data = get_list()
    sorted_data = quick_sort(data, 0, len(data)-1)
    print(f"Here is the sorted list: {sorted_data}")


def get_list():
    while True:
        input_data = input("Enter list of items here: ")
        if "," in input_data:
            input_list = input_data.split(",")
            input_data = [int(x) for x in input_list]
            return input_data
        else:
            print("Please enter a comma seperated list of letters")


def partition(array, low, high):

    pivot = array[high]

    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1

            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1


def quick_sort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quick_sort(array, low, pi - 1)
        quick_sort(array, pi + 1, high)
    return array

if __name__ == "__main__":
    main()
