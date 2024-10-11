import time
import subprocess
from subprocess import Popen


# Функция для получения номера последней обработанной строки из файла
def get_last_processed_line():
    try:
        with open('progress.txt', 'r') as progress_file:
            return int(progress_file.read().strip())
    except FileNotFoundError:
        return 0  # Если файл не найден, начинаем с первой строки
    except ValueError:
        return 0  # Если файл пуст или имеет неверный формат, начинаем с первой строки


# Функция для записи номера последней обработанной строки в файл
def save_last_processed_line(line_number):
    with open('progress.txt', 'w') as progress_file:
        progress_file.write(str(line_number))


# Функция для отображения шкалы прогресса
def display_progress(current, total):
    progress_percentage = (current / total) * 100
    bar_length = 40  # Длина прогресс-бара
    filled_length = int(bar_length * current // total)
    bar = '█' * filled_length + '-' * (bar_length - filled_length)
    print(f'\rProgress: |{bar}| {progress_percentage:.2f}% Complete', end='')


# Основная логика программы
with open('ips.txt') as f:
    # Читаем файл ips.txt как список строк
    lines = f.readlines()
    total_lines = len(lines)  # Общее количество строк

    # Получаем номер последней обработанной строки
    last_processed_line = get_last_processed_line()

    # Начинаем обработку строк, начиная с last_processed_line + 1
    for lineNumber, line in enumerate(lines, start=1):
        if lineNumber <= last_processed_line:
            continue  # Пропускаем строки, которые уже обработаны

        programName = "example.exe"
        print(f"{programName} {line.strip(' \t\n\r')}")
        p = Popen([programName, line.strip(' \t\n\r')])

        # Сохраняем номер текущей строки в progress.txt
        save_last_processed_line(lineNumber)

        # Отображаем прогресс
        display_progress(lineNumber, total_lines)

        # После каждых 7 строк делаем паузу в 15 секунд
        if lineNumber % 7 == 0:
            time.sleep(15)

# Бесконечный цикл, чтобы программа продолжала работу
while True:
    time.sleep(60)
