# shopping_list_manager.py

def main():
    shopping_list = []

    while True:
        print("\n1. Add\n2. Remove\n3. View\n4. Exit")
        choice = input("Choice: ").strip()

        if choice == '1':
            item = input("Add: ").strip()
            if item:
                shopping_list.append(item)
        elif choice == '2':
            item = input("Remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
            elif shopping_list:
                print("Not found")
        elif choice == '3':
            print("\nList:", *shopping_list if shopping_list else "Empty")
        elif choice == '4':
            print("Bye!")
            break
        else:
            print("Invalid")


if __name__ == "__main__":
    main()
