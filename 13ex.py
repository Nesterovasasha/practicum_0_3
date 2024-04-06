def find_position(rows, columns, entry_number):
    entries_per_page = rows * columns
    page_number = (entry_number - 1) // entries_per_page + 1
    remaining_entries = (entry_number - 1) % entries_per_page
    column_number = remaining_entries // rows + 1
    row_number = remaining_entries % rows + 1
    return page_number, column_number, row_number

rows = int(input("Введите количество строк на каждой странице: "))
columns = int(input("Введите количество столбцов на странице: "))
entry_number = int(input("Введите номер записи в справочнике: "))

page, column, row = find_position(rows, columns, entry_number)
print(f"Номер страницы: {page}, Номер столбца: {column}, Номер записи в столбце: {row}")