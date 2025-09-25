def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def main():
    shopping_list = []
    while True:
        display_menu()
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_item = input("Enter the item to add: ").strip().lower()
            shopping_list.append(add_item)
            print(f"{add_item} added to list")



        elif choice == 2:
            remove_item = input("Please enter your item to remove: ").strip().lower()
            if remove_item in shopping_list:
                shopping_list.remove(remove_item)
                print(f"{remove_item} removed from list")
            else:
                print(f"{remove_item} is not in your shopping list")


        elif choice == 3:
            if not shopping_list:
                print("You have not added item yet")

            else:
                print(f"This is your shopping list: {shopping_list}")


        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again")



main()