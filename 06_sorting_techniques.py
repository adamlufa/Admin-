# Bubble Sort, Selection Sort, and Top Five Salaries.

salaries = [
    46897.50, 73589.39, 82456.98, 24900.87,
    97235.84, 26755.89, 55823.13
]


def bubble_sort(arr):
    result = arr.copy()
    n = len(result)
    for i in range(n):
        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
    return result


def selection_sort(arr):
    result = arr.copy()
    n = len(result)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if result[j] < result[min_index]:
                min_index = j
        result[i], result[min_index] = result[min_index], result[i]
    return result


def display_top_five(sorted_arr):
    print("Top 5 Salaries:")
    for salary in reversed(sorted_arr[-5:]):
        print(f"{salary:.2f}")


def main():
    print("Salaries:", salaries)
    while True:
        print("\\n***** Sorting Techniques *****")
        print("1. Bubble Sort")
        print("2. Selection Sort")
        print("3. Top 5 Salaries")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("Sorted salaries:", bubble_sort(salaries))
        elif choice == "2":
            print("Sorted salaries:", selection_sort(salaries))
        elif choice == "3":
            display_top_five(sorted(salaries))
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
