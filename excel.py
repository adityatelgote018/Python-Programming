import os
import openpyxl

EXCEL_FILE = "books.xlsx"


# Create Excel file if it does not exist
def initialize_excel():
    if not os.path.exists(EXCEL_FILE):
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet.title = "Books"

        sheet.append(["Book ID", "Book Name", "Author", "Category", "Price"])

        workbook.save(EXCEL_FILE)
        workbook.close()


# Add a new book
def add_book():
    print("\n--- ADD BOOK ---")

    book_id = input("Enter Book ID: ").strip()

    if book_id == "":
        print("Book ID cannot be empty!")
        return

    workbook = openpyxl.load_workbook(EXCEL_FILE)
    sheet = workbook.active

    # Check duplicate ID
    for row in range(2, sheet.max_row + 1):
        if str(sheet.cell(row, 1).value).strip() == book_id:
            print("Book ID already exists!")
            workbook.close()
            return

    book_name = input("Enter Book Name: ").strip()
    author = input("Enter Author: ").strip()
    category = input("Enter Category: ").strip()
    price = input("Enter Price: ").strip()

    sheet.append([book_id, book_name, author, category, price])

    workbook.save(EXCEL_FILE)
    workbook.close()

    print("Book added successfully!")
    print("Data saved in books.xlsx")


# View all books
def view_books():
    print("\n--- ALL BOOKS ---")

    workbook = openpyxl.load_workbook(EXCEL_FILE)
    sheet = workbook.active

    if sheet.max_row <= 1:
        print("No books found.")
        workbook.close()
        return

    print("-" * 80)
    print(f"{'ID':<10}{'Book Name':<25}{'Author':<20}{'Category':<15}{'Price':<10}")
    print("-" * 80)

    for row in range(2, sheet.max_row + 1):
        book_id = sheet.cell(row, 1).value
        book_name = sheet.cell(row, 2).value
        author = sheet.cell(row, 3).value
        category = sheet.cell(row, 4).value
        price = sheet.cell(row, 5).value

        print(
            f"{str(book_id):<10}"
            f"{str(book_name):<25}"
            f"{str(author):<20}"
            f"{str(category):<15}"
            f"{str(price):<10}"
        )

    print("-" * 80)

    workbook.close()


# Update book
def update_book():
    print("\n--- UPDATE BOOK ---")

    book_id = input("Enter Book ID to update: ").strip()

    workbook = openpyxl.load_workbook(EXCEL_FILE)
    sheet = workbook.active

    found = False

    for row in range(2, sheet.max_row + 1):

        if str(sheet.cell(row, 1).value).strip() == book_id:

            found = True

            print("\nBook Found!")
            print("Leave blank to keep old value.")

            old_name = sheet.cell(row, 2).value
            old_author = sheet.cell(row, 3).value
            old_category = sheet.cell(row, 4).value
            old_price = sheet.cell(row, 5).value

            print("Current Book Name:", old_name)
            print("Current Author:", old_author)
            print("Current Category:", old_category)
            print("Current Price:", old_price)

            new_name = input("Enter new Book Name: ").strip()
            new_author = input("Enter new Author: ").strip()
            new_category = input("Enter new Category: ").strip()
            new_price = input("Enter new Price: ").strip()

            if new_name:
                sheet.cell(row, 2).value = new_name

            if new_author:
                sheet.cell(row, 3).value = new_author

            if new_category:
                sheet.cell(row, 4).value = new_category

            if new_price:
                sheet.cell(row, 5).value = new_price

            workbook.save(EXCEL_FILE)
            workbook.close()

            print("Book updated successfully!")
            print("Changes saved in books.xlsx")
            return

    if not found:
        print("Book ID not found.")

    workbook.close()


# Delete book
def delete_book():
    print("\n--- DELETE BOOK ---")

    book_id = input("Enter Book ID to delete: ").strip()

    workbook = openpyxl.load_workbook(EXCEL_FILE)
    sheet = workbook.active

    for row in range(2, sheet.max_row + 1):

        if str(sheet.cell(row, 1).value).strip() == book_id:

            sheet.delete_rows(row, 1)

            workbook.save(EXCEL_FILE)
            workbook.close()

            print("Book deleted successfully!")
            print("Data updated in books.xlsx")
            return

    workbook.close()

    print("Book ID not found.")


# Main program
def main():

    initialize_excel()

    while True:

        print("\n==============================")
        print("   LIBRARY MANAGEMENT SYSTEM")
        print("==============================")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Update Book")
        print("4. Delete Book")
        print("5. Exit")
        print("==============================")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_book()

        elif choice == "2":
            view_books()

        elif choice == "3":
            update_book()

        elif choice == "4":
            delete_book()

        elif choice == "5":
            print("\nThank you for using Library Management System!")
            break

        else:
            print("Invalid choice! Please enter 1 to 5.")


# Start program
if __name__ == "__main__":
    main()