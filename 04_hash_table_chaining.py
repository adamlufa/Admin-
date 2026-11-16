# Hash table using division method and separate chaining.


class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash_function(key)
        if key not in self.table[index]:
            self.table[index].append(key)
            print(f"Key {key} inserted at index {index}.")
        else:
            print(f"Key {key} already exists.")

    def delete(self, key):
        index = self.hash_function(key)
        if key in self.table[index]:
            self.table[index].remove(key)
            print(f"Key {key} deleted.")
            return True
        print(f"Key {key} not found.")
        return False

    def search(self, key):
        index = self.hash_function(key)
        if key in self.table[index]:
            print(f"Key {key} found at index {index}.")
            return True
        print(f"Key {key} not found.")
        return False

    def display(self):
        print("Hash Table:")
        for index, bucket in enumerate(self.table):
            print(f"Index {index}: {bucket}")


def main():
    ht = HashTable()
    while True:
        print("\\n===== Menu =====")
        print("1. Insert")
        print("2. Delete")
        print("3. Search")
        print("4. Display")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            ht.insert(int(input("Enter key to insert: ")))
        elif choice == "2":
            ht.delete(int(input("Enter key to delete: ")))
        elif choice == "3":
            ht.search(int(input("Enter key to search: ")))
        elif choice == "4":
            ht.display()
        elif choice == "5":
            print("Program exits")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
