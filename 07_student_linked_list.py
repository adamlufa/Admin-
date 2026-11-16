# Student Record Management System using a Singly Linked List.
# Supports Add, Display, Delete, Update, Search, and Sort.


class Node:
    def __init__(self, rollno, name, marks):
        self.rollno = int(rollno)
        self.name = name
        self.marks = float(marks)
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, rollno, name, marks):
        if self.search_node(int(rollno)) is not None:
            print("Roll number already exists.")
            return
        new_node = Node(rollno, name, marks)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        print("Student record inserted.")

    def search_node(self, rollno):
        current = self.head
        while current:
            if current.rollno == int(rollno):
                return current
            current = current.next
        return None

    def search(self, rollno):
        node = self.search_node(rollno)
        if node:
            print(f"Record found: {node.rollno} | {node.name} | {node.marks:g}")
            return True
        print("Record not found.")
        return False

    def delete(self, rollno):
        current = self.head
        previous = None
        while current:
            if current.rollno == int(rollno):
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                print("Student record deleted.")
                return
            previous = current
            current = current.next
        print("Student record not found.")

    def update(self, old_rollno, new_rollno):
        node = self.search_node(old_rollno)
        if node is None:
            print("Student record not found.")
            return
        new_rollno = int(new_rollno)
        duplicate = self.search_node(new_rollno)
        if duplicate is not None and duplicate is not node:
            print("New roll number already exists.")
            return
        node.rollno = new_rollno
        print("Record updated.")

    def display(self):
        print("Roll No\\tName\\tMarks")
        current = self.head
        if current is None:
            print("No student records.")
            return
        while current:
            print(f"{current.rollno}\\t{current.name}\\t{current.marks:g}")
            current = current.next

    def sort(self, field, descending=False):
        records = []
        current = self.head
        while current:
            records.append(current)
            current = current.next

        if field == "roll":
            records.sort(key=lambda item: item.rollno, reverse=descending)
        elif field == "name":
            records.sort(key=lambda item: item.name.lower(), reverse=descending)
        elif field == "marks":
            records.sort(key=lambda item: item.marks, reverse=descending)
        else:
            print("Invalid sort field.")
            return

        self.head = None
        for record in records:
            record.next = None
            if self.head is None:
                self.head = record
                tail = record
            else:
                tail.next = record
                tail = record
        print("Records sorted.")


def main():
    students = LinkedList()
    while True:
        print("\\n===== Student Record Menu =====")
        print("1. Add")
        print("2. Display")
        print("3. Delete")
        print("4. Update roll number")
        print("5. Search")
        print("6. Sort")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            roll = int(input("Enter roll number: "))
            name = input("Enter name: ")
            marks = float(input("Enter marks: "))
            students.append(roll, name, marks)
        elif choice == "2":
            students.display()
        elif choice == "3":
            students.delete(int(input("Enter roll number to delete: ")))
        elif choice == "4":
            old_roll = int(input("Enter old roll number: "))
            new_roll = int(input("Enter new roll number: "))
            students.update(old_roll, new_roll)
        elif choice == "5":
            students.search(int(input("Enter roll number to search: ")))
        elif choice == "6":
            field = input("Sort by roll, name, or marks: ").strip().lower()
            order = input("Ascending or descending (a/d): ").strip().lower()
            students.sort(field, descending=(order == "d"))
            students.display()
        elif choice == "7":
            print("Exiting.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
