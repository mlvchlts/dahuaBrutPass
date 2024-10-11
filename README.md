IP Processing Script
Описание
Этот скрипт на Python предназначен для обработки IP-адресов из файла ips.txt. Он запускает внешнюю программу example.exe для каждого IP-адреса, который не был обработан ранее. Программа отслеживает прогресс и сохраняет номер последней обработанной строки в файле progress.txt.

Возможности
Чтение IP-адресов из файла ips.txt.
Запуск внешней программы с каждым IP-адресом в качестве аргумента.
Отображение прогресса обработки в виде прогресс-бара.
Сохранение состояния обработки в файл для продолжения в будущем.
Пауза после каждых 7 обработанных строк.
Требования
Python 3.x
Установленная программа example.exe (должна быть доступна в той же директории или указанный путь к ней должен быть корректным).
Файл ips.txt, содержащий IP-адреса (один адрес на строку).
Установка
Скачайте или скопируйте этот скрипт на ваш компьютер.
Убедитесь, что у вас установлен Python 3.x. Если нет, скачайте его с официального сайта Python.
Создайте файл ips.txt в той же директории, что и скрипт, и добавьте IP-адреса, которые вы хотите обработать.
Убедитесь, что файл example.exe находится в той же директории или укажите полный путь к нему в коде.
Использование
Откройте терминал или командную строку.

Перейдите в директорию, где находится скрипт.

Запустите скрипт с помощью следующей команды:

bash
Копировать код
python your_script_name.py
Замените your_script_name.py на имя вашего скрипта.

Примечания
Скрипт будет продолжать работать в бесконечном цикле, проверяя файл ips.txt и обрабатывая строки. Если хотите остановить скрипт, используйте комбинацию клавиш Ctrl+C.
Прогресс обработки отображается в консоли, и при завершении каждой группы из 7 строк происходит пауза в 15 секунд.
Лицензия
Этот проект доступен под лицензией MIT. Свободно используйте и изменяйте его по своему усмотрению.