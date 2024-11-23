import os


def merge_files(file_names, result_file_name):
    file_data = []

    # Читаем содержимое файлов
    for file_name in file_names:
        with open(file_name, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            file_data.append((file_name, len(lines), lines))

    # Сортируем файлы по количеству строк
    file_data.sort(key=lambda x: x[1])

    # Записываем содержимое в результирующий файл
    with open(result_file_name, 'w', encoding='utf-8') as result_file:
        for file_name, line_count, lines in file_data:
            # Записываем имя файла и количество строк
            result_file.write(f"{file_name}\n{line_count}\n")
            file_base_name = os.path.splitext(file_name)[0]
            for idx, line in enumerate(lines, start=1):
                result_file.write(f"{line.strip()} Строка номер {idx} файла номер {file_base_name}\n")


# Пример использования
file_names = ['2.txt', '1.txt', '3.txt']  # Замените на имена файлов
result_file_name = 'result.txt'
merge_files(file_names, result_file_name)
print(f"Содержимое объединено в файл '{result_file_name}'")
