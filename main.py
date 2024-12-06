# Library Management System with User Login, Role-Based Access, and Book Availability Check

print("Welcome to the Library Management System")
print("Please enter your details below:")

# General Book Categories
book_categories = {
    1: "Fiction",
    2: "Non-Fiction",
    3: "Children's Books",
    4: "Young Adult",
    5: "Classic Literature",
    6: "Comics and Graphic Novels",
    7: "Religious and Spiritual",
    8: "Science and Technology",
    9: "Business and Economics"
}

# Dictionary to store books in the library
library_books = {
    "World Without End": {
        "Author": "Ken Follett",
        "Category": "Fiction",
        "Year": 2007,
        "Status": "available",
        "Reserved By": None,
    },
    "War and Peace": {
        "Author": "Leo Tolstoy",
        "Category": "Fiction",
        "Year": 1869,
        "Status": "available",
        "Reserved By": None,
    },
    "The Complete Magician's Tables": {
        "Author": "Stephen Skinner",
        "Category": "Non-Fiction",
        "Year": 2007,
        "Status": "available",
        "Reserved By": None,
    },
    "Practical Ayurveda": {
        "Author": "Sivananda Yoga Vedanta Centre",
        "Category": "Non-Fiction",
        "Year": 2018,
        "Status": "available",
        "Reserved By": None,
    },
    "Healing Power of Herbs": {
        "Author": "Michael T. Murray",
        "Category": "Non-Fiction",
        "Year": 2004,
        "Status": "available",
        "Reserved By": None,
    },
    "Test": {
        "Author": "Tester",
        "Category": "Fiction",
        "Year": 2024,
        "Status": "available",
        "Reserved By": None,
    },
}

# Sample users with roles for testing

users = {
    "admin": {"password": "admin", "role": "admin", "borrowed books": []},
    "user": {"password": "user", "role": "user", "borrowed books": []}
}


# Function to display all categories
def view_categories():
    print("\nGeneral Book Categories:")
    for number, category in book_categories.items():
        print(f"{number}. {category}")
    print()


# View all books
def view_all_books():
    print("\nBooks in the Library:")
    if not library_books:
        print("No books available.")
    else:
        for title, details in library_books.items():
            reserved = f"Reserved by: {details['Reserved By']}" if details["Reserved By"] else "Not reserved"
            print(
                f"Title: {title} | "
                f"Author: {details['Author']} | "
                f"Category: {details['Category']} | "
                f"Year: {details['Year']} | "
                f"Status: {details['Status']} | "
                f"{reserved}"
            )


# Function to add a new book (Admin only)
def add_book():
    print("\nAdd a New Book:")
    while True:
        title = input("Enter book title: ").strip()
        if title:
            break
        print("Error: Title cannot be blank.")

    if title in library_books:
        print(f"Book '{title}' already exists.")
        return

    while True:
        author = input("Enter author name: ").strip()
        if author:
            break
        print("Error: Author cannot be blank.")

    print("\nSelect a category for the book:")
    view_categories()
    while True:
        try:
            category_choice = int(input("Enter the number corresponding to the category: ").strip())
            if category_choice in book_categories:
                category = book_categories[category_choice]
                break
            else:
                print(f"Invalid choice. Please select a valid category number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        try:
            year = int(input("Enter publication year: ").strip())
            break
        except ValueError:
            print("Invalid year. Please enter a valid numeric value.")

    library_books[title] = {
        "Author": author,
        "Category": category,
        "Year": year,
        "Status": "available",
        "Reserved By": None,
    }
    print(f"Book '{title}' has been added successfully.")


# Function to View the Books by Category
def view_books_by_category():
    print("\nView Books by Category")
    print("Select a category from the list below:")
    view_categories()

    while True:
        try:
            category_choice = int(input("Enter the number corresponding to the category: ").strip())
            if category_choice in book_categories:
                selected_category = book_categories[category_choice]
                break
            else:
                print(f"Invalid choice. Please select a valid category number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    books_in_category = [
        (title, details) for title, details in library_books.items()
        if details['Category'] == selected_category
    ]

    if not books_in_category:
        print(f"No books found in the category '{selected_category}'.")
        return

    print(f"\nBooks in Category: {selected_category}")
    for title, details in books_in_category:
        reserved = f"Reserved by: {details['Reserved By']}" if details['Reserved By'] else "Not reserved"
        print(
            f"Title: {title} | "
            f"Author: {details['Author']} | "
            f"Year: {details['Year']} | "
            f"Status: {details['Status']} | "
            f"{reserved}"
        )


# Function to edit specific book details (Admin only)
def edit_book_details():
    title = input("Enter the title of the book to edit: ")

    if title not in library_books:
        print(f"Book '{title}' not found in the library.")
        return

    book = library_books[title]
    print(f"\nCurrent details of '{title}':")
    print(f"Author: {book['Author']}")
    print(f"Category: {book['Category']}")
    print(f"Year: {book['Year']}")
    print(f"Status: {book['Status']}")
    print(f"Reserved By: {book['Reserved By'] if book['Reserved By'] else 'Not reserved'}")

    while True:
        print("\nWhat would you like to edit?")
        print("1. Author")
        print("2. Category")
        print("3. Year")
        print("4. Cancel")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            library_books[title]["Author"] = input("Enter the new author: ")
            print("Author updated successfully!")
        elif choice == "2":
            view_categories()
            library_books[title]["Category"] = input("Enter the new category: ")
            print("Category updated successfully!")
        elif choice == "3":
            while True:
                try:
                    library_books[title]["Year"] = int(input("Enter the new publication year: "))
                    print("Year updated successfully!")
                    break
                except ValueError:
                    print("Invalid year. Please enter a numeric value.")
        elif choice == "4":
            print("Edit canceled.")
            break
        else:
            print("Invalid choice. Edit canceled.")
            break


# Function to search for a book
def search_book():
    search_term = input("Enter book title or author to search: ").strip().lower()
    found = False

    for title, details in library_books.items():
        if search_term in title.lower() or search_term in details["Author"].lower():
            reserved_status = f"Reserved by: {details['Reserved By']}" if details["Reserved By"] else "Not reserved"
            print(
                f"Title: {title} | "
                f"Author: {details['Author']} | "
                f"Category: {details['Category']} | "
                f"Year: {details['Year']} | "
                f"Status: {details['Status']} | "
                f"{reserved_status}"
            )
            found = True

    if not found:
        print("No matching books found.")


# Function to display books associated with a user
def my_books(username):
    print("\nMy Books:")
    user_books = users[username]["borrowed books"]
    if len(user_books) < 1:  # Check if the user has no books
        print("You do not have any books.")
        return
    # Display Books User has Checked-out or Reserved
    print(f"Books checked out by {username}:")
    for title in user_books:
        if title in library_books:  # Ensure the book exists in the library
            print(f"-> Title: {title}")
        else:
            print(f"Book '{title}' is no longer available in the library.")


# Function to reserve a book
def reserve_book(username):
    title = input("Enter the title of the book you want to reserve: ").strip()
    if title in library_books:
        book = library_books[title]
        if book["Status"] == "available":
            book["Status"] = "reserved"
            book["Reserved By"] = username
            print(f"Book '{title}' has been reserved successfully.")
            if "borrowed books" in users[username]:
                users[username]["borrowed books"].append(title)
        else:
            print(f"Book '{title}' is currently unavailable.")
    else:
        print(f"Book '{title}' not found.")

    print(users)


# Function to Check out Book (Admin only)
def check_out_book():
    print("\nAdmin - Check out Book")
    title = input("Enter the title of the book you want to check out: ").strip().lower()
    # Search for the book by case-insensitive title
    matched_title = next((t for t in library_books if t.lower() == title), None)

    if matched_title:
        book = library_books[matched_title]
        if book["Status"] == "available":
            book["Status"] = "checked out"
            book["Reserved By"] = "admin"
            print(f"Book '{matched_title}' has been checked out successfully.")
        else:
            print(f"Book '{matched_title}' is currently unavailable.")
    else:
        print(f"Book '{title}' not found in the library.")

# Function to Check In Book(Admin only)
def check_in_book():
    print("\nAdmin - Check-In Book")
    title = input("Enter the title of the book you want to return: ").strip().lower()
    # Search for the book by case-insensitive title
    matched_title = next((t for t in library_books if t.lower() == title), None)

    if matched_title:
        book = library_books[matched_title]
        if book["Status"] == "checked out":
            book["Status"] = "available"
            book["Reserved By"] = None
            print(f"Book '{matched_title}' has been returned successfully.")
        else:
            print(f"Book '{matched_title}' is not currently checked out.")
    else:
        print(f"Book '{title}' not found in the library.")


# Function to Remove Book(Admin only)
def remove_book():
    print("\nAdmin - Remove Book")
    title = input("Enter the title of the book to remove: ").strip().lower()

    # Search for the book by case-insensitive title
    matched_title = next((t for t in library_books if t.lower() == title), None)

    if matched_title:
        del library_books[matched_title]
        print(f"Book '{matched_title}' has been removed from the library.")
    else:
        print(f"Book '{title}' not found in the library.")


# Function to sort books alphabetically (Admin only)
def sort_books():
    print("\nSort Books:")
    print("1. A-Z (Alphabetical Order)")
    print("2. Z-A (Reverse Alphabetical Order)")
    choice = input("Enter your choice (1 or 2): ").strip()

    # Retrieve and sort book titles
    book_titles = list(library_books.keys())

    if choice == "1":
        sorted_books = sorted(book_titles)
        print("\nBooks Sorted A-Z:")
        for title in sorted_books:
            print(f"- {title}")
    elif choice == "2":
        sorted_books = sorted(book_titles, reverse=True)
        print("\nBooks Sorted Z-A:")
        for title in sorted_books:
            print(f"- {title}")
    else:
        print("Invalid choice. Returning to Admin Menu.")


# Function to change the user's password
def change_password(username):
    current_password = input("Enter your current password: ")
    if users[username]["password"] == current_password:
        new_password = input("Enter your new password: ")
        confirm_password = input("Confirm your new password: ")
        if new_password == confirm_password:
            users[username]["password"] = new_password
            print("Password changed successfully!")
        else:
            print("Passwords do not match.")
    else:
        print("Incorrect current password.")


# Function for Admin to change their own password
def admin_change_password(username):
    print("\nAdmin Password Change:")
    current_password = input("Enter your current password: ").strip()

    # Validate the current password
    if users[username]["password"] == current_password:
        new_password = input("Enter your new password: ").strip()
        confirm_password = input("Confirm your new password: ").strip()

        # Check if the new password matches the confirmation
        if new_password == confirm_password:
            users[username]["password"] = new_password
            print(f"Password for Admin '{username}' changed successfully!")
        else:
            print("Passwords do not match. No changes made.")
    else:
        print("Incorrect current password. No changes made.")


# Admin menu
def admin_menu(username):
    while True:
        print("\nAdmin Menu:")
        print("1. View All Books")
        print("2. View Books by Category")
        print("3. Add Book")
        print("4. Remove Book")
        print("5. Edit Book Details")
        print("6. Check Out Book")
        print("7. Check In Book")
        print("8. Search Book")
        print("9.Sort Books")
        print("10.Change Password")
        print("11. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_all_books()
        elif choice == "2":
            view_books_by_category()
        elif choice == "3":
            add_book()
        elif choice == "4":
            remove_book()
        elif choice == "5":
            edit_book_details()
        elif choice == "6":
            check_out_book()
        elif choice == "7":
            check_in_book()
        elif choice == "8":
            search_book()
        elif choice == "9":
            sort_books()
        elif choice == "10":
            admin_change_password(username)
        elif choice == "11":
            print(f"User '{username}' logged out...")
            main()
        else:
            print("Invalid choice. Please enter a valid option.")


# User menu
def user_menu(username):
    while True:
        print("\nUser Menu:")
        print("1. View All Borrowed Books")
        print("2. Search for a Book")
        print("3. Reserve Book")
        print("4. Change Password")
        print("5. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            my_books(username)
        elif choice == "2":
            search_book()
        elif choice == "3":
            reserve_book(username)
        elif choice == "4":
            change_password(username)
        elif choice == "5":
            print(f"User '{username}' logged out...")
            main()
        else:
            print("Invalid choice. Please enter a valid option.")


# Main function to handle login
def main():
    while True:
        print("--------------------- LOGIN PANEL ---------------------")
        username = input("Username: ").strip()
        password = input("Password: ").strip()

        # Check if the username exists and the password matches
        if username in users and users[username]["password"] == password:
            print(f"Welcome, {username}!")

            # Determine the role and navigate to the appropriate menu
            if users[username]["role"] == "admin":
                admin_menu(username)
            else:
                user_menu(username)
            break  # Exit the loop after successful login
        else:
            print("Invalid credentials. Please try again.")


# Run the program
main()
