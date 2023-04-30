from prettytable import PrettyTable

if __name__ == '__main__':
    # Инициализируем таблицу.
    yp_table = PrettyTable()
    yp_table.field_names = (
        '№ когорты',
        'Кол-во студентов',
        'Средний балл',
    )
    yp_table.add_rows(
        (
            (18, 211, 4.3),
            (19, 300, 5),
        )
    )

    print(yp_table)
