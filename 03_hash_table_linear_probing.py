# Hash table using division method and linear probing.


class LinearProbingHashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size
        self.deleted = "<DELETED>"

    def hash_function(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash_function(key)
        start = index

        while self.table[index] not in (None, self.deleted):
            if self.table[index] == key:
                print(f"Key {key} already exists at index {index}.")
                return
            index = (index + 1) % self.size
            if index == start:
                print("Hash table is full. Cannot insert.")
                return

        self.table[index] = key
        print(f"Key {key} inserted at index {index}.")

    def search(self, key):
        index = self.hash_function(key)
        start = index

        while self.table[index] is not None:
            if self.table[index] == key:
                print(f"Key {key} found at index {index}.")
                return index
            index = (index + 1) % self.size
            if index == start:
                break

        print(f"Key {key} not found.")
        return None

    def delete(self, key):
        index = self.search(key)
        if index is not None:
            self.table[index] = self.deleted
            print(f"Key {key} deleted from index {index}.")

    def display(self):
        print("Hash Table:")
        for i, key in enumerate(self.table):
            print(f"Index {i}: {key}")


def main():
    table = LinearProbingHashTable()
    while True:
        print("\\n===== Menu =====")
        print("1. Insert")
        print("2. Search")
        print("3. Delete")
        print("4. Display")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            table.insert(int(input("Enter key to insert: ")))
        elif choice == "2":
            table.search(int(input("Enter key to search: ")))
        elif choice == "3":
            table.delete(int(input("Enter key to delete: ")))
        elif choice == "4":
            table.display()
        elif choice == "5":
            print("Program exits")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
