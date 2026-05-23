def load_database():
    author  = []
    title   = []
    year    = []
    sales   = []

    try:
        with open("books_record.csv", "r") as file:
            for line in file:
                data = line.strip().split(",")
                author  .append(data[0])
                title   .append(data[1])
                year    .append(int(data[2]))
                sales   .append(int(data[3]))
    except FileNotFoundError:
        print("Error: File not found!")


def display_menu():
    load_database()
    while True:
        print("\n Menu")
        print("1. Add new book")
        print("2. Delete a book")
        print("3. Update the sales")
        print("4. Find books by an author")
        print("5. Find the oldest book")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            delete_book()
        elif choice == "3":
            update_sales()
        elif choice == "4":
            find_by_author()
        elif choice == "5":
            oldest_book()
        elif choice == "6":
            print("Quiting...")
            break
        else:
            print("Invalid choice. Please try again.")


def add_book():
    print("Adding a book...")
    author = input("Name of the author: ")
    title = input("Title of the book: ")
    year = int(input("Year that the book was published: "))
    sales = int(input("How many sales: "))
    try:
        with open("books_record.csv", "a") as file:
            file.write(f"\n{author},{title},{year},{sales}")
    except IOError as e:
        print(f"Error: {e}")
    else:
        print(f"Book {title} added successfully.")
    finally:
        display_menu()

def delete_book():
    print("Deleting a book...")
    title_to_delete = input("Title of the book to delete: ").title()

    try:
        with open("books_record.csv", "r") as file:
            lines = file.readlines()

        remaining_lines = []
        was_deleted = False
        for line in lines:
            if title_to_delete not in line:
                remaining_lines.append(line)
            else:
                was_deleted = True

        with open("books_record.csv", "w") as file:
            file.writelines(remaining_lines)

    except IOError as e:
        print(f"Error: {e}")
    else:
        if was_deleted:
            print(f"Book '{title_to_delete}' deleted successfully.")
        else:
            print(f"Book '{title_to_delete}' not found.")
    finally:
        display_menu()

def update_sales():
    print("Updating sales...")
    title_to_update = input("Title of the book to update: ").title()

    try:
        with open("books_record.csv", "r") as file:
            lines = file.readlines()

        was_updated = False
        for i, line in enumerate(lines):
            data = line.strip().split(",")
            if title_to_update == data[1]:
                sales = int(input(f"New sales for '{title_to_update}': "))
                updated_line = f"{data[0]},{data[1]},{data[2]},{sales}\n"
                lines[i] = updated_line
                was_updated = True
                break

        if was_updated:
            with open("books_record.csv", "w") as file:
                file.writelines(lines)
            print(f"Sales for '{title_to_update}' updated successfully.")
        else:
            print(f"Book '{title_to_update}' not found.")

    except IOError as e:
        print(f"Error: {e}")

    finally:
        display_menu()


def find_by_author():
    print("Finding books by an author...")
    author_to_find = input("Name of the author: ").title()

    try:
        with open("books_record.csv", "r") as file:
            lines = file.readlines()

        found_books = []
        for line in lines:
            data = line.strip().split(",")
            if author_to_find == data[0]:
                found_books.append(data[1])

        if found_books:
            print(f"Books by '{author_to_find}':")
            for book in found_books:
                print(f"- {book}")
        else:
            print(f"No books found by '{author_to_find}'.")

    except IOError as e:
        print(f"Error: {e}")

    finally:
        display_menu()

def oldest_book():
    try:
        with open("books_record.csv", "r") as file:
            lines = file.readlines()
            years = []
            oldest_book_list = []

            for line in lines:
                data = line.strip().split(",")
                years.append(int(data[2]))

            for line in lines:
                data = line.strip().split(",")
                if int(data[2]) == min(years):
                    oldest_book_list.append(data[1])
        if len(oldest_book_list) == 1:
            print(f"The oldest book is '{oldest_book_list[0]}'.")
        else:
            print("The oldest books are:")
            for book in oldest_book_list:
                print(f"- {book}")

    except FileNotFoundError:
        print("Error: File not found!")

    finally:
        display_menu()

def main():
    display_menu()

if __name__ == "__main__":
    main()
