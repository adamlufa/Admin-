# Linear Search and Binary Search

customer_id = [50, 60, 40, 20, 80, 90, 100, 10]


def linear_search(ids, target):
    for i, value in enumerate(ids):
        if value == target:
            return i
    return -1


def binary_search(ids, target):
    # Binary search requires a sorted list.
    low = 0
    high = len(ids) - 1

    while low <= high:
        mid = (low + high) // 2
        if ids[mid] == target:
            return mid
        elif ids[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def main():
    while True:
        print("\\n***** Searching Techniques *****")
        print("1. Linear Search")
        print("2. Binary Search")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("Customer IDs:", customer_id)
            target = int(input("Enter customer ID to search: "))
            index = linear_search(customer_id, target)
            if index != -1:
                print("Customer ID found at index", index)
            else:
                print("Customer ID not found")

        elif choice == "2":
            sorted_ids = sorted(customer_id)
            print("Unsorted list:", customer_id)
            print("Sorted list:", sorted_ids)
            target = int(input("Enter customer ID to search: "))
            index = binary_search(sorted_ids, target)
            if index != -1:
                print("Customer ID found at index", index,
                      "in the sorted list")
            else:
                print("Customer ID not found")

        elif choice == "3":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
