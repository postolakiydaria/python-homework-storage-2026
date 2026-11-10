#!/usr/bin/env python3


import argparse
import os

def process_file(input_path, output_path, replace_arg, footer, force):
    """
    Копирует файл, применяя замену и добавляя футер.
    :param input_path: Путь к исходному файлу.
    :param output_path: Путь к выходному файлу.
    :param replace_arg: Строка замены в формате OLD=NEW.
    :param footer: Строка для добавления в конец.
    :param force: Разрешить перезапись.
    :return: Количество выполненных замен.
    :raises FileNotFoundError: Если входной файл не существует.
    :raises FileExistsError: Если выходной файл существует, а force=False.
    :raises ValueError: Если replace_arg неверного формата.
    """
    if not os.path.exists(input_path):
        raise FileNotFoundError("Ошибка: Входной файл не найден!")
    if os.path.exists(output_path) and not force:
        raise FileExistsError("Ошибка: Выходной файл уже существует. Используйте флаг --force для перезаписи.")

    old_str = None
    new_str = None
    if replace_arg:
        if "=" not in replace_arg:
            raise ValueError("Ошибка: Аргумент --replace должен быть в формате OLD=NEW.")
        old_str, new_str = replace_arg.split("=", 1)

    with open(input_path, "r", encoding="utf-8") as file:
        content = file.read()

    replace_count = 0
    if old_str is not None:
        replace_count = content.count(old_str)
        content = content.replace(old_str, new_str)

    if footer:
        if not content.endswith("\n"):
            content += "\n"
        content += footer + "\n"

    mode = "w" if force else "x"
    with open(output_path, mode, encoding="utf-8") as file:
        file.write(content)
    return replace_count

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog="file_copier",
                                     description="Утилита для копирования файлов с заменой строк и добавлением футера.",
                                     epilog="Готово!")

    parser.add_argument("-i", "--input", type=str, required=True, help="Путь к входному файлу")
    parser.add_argument("-o", "--output", type=str, required=True, help="Путь к выходному файлу")
    parser.add_argument("-r", "--replace", type=str, help="Замена в формате OLD=NEW")

    parser.add_argument("-a", "--append-footer", type=str, help="Строка для добавления в конец")
    parser.add_argument("-f", "--force", action="store_true", help="Разрешить перезапись выходного файла")

    args = parser.parse_args()

    try:
        count = process_file(args.input, args.output, args.replace, args.append_footer, args.force)
        print(f"Файл успешно обработан!")
        if args.replace:
            print(f"Выполнено замен: {count}")
    except (FileNotFoundError, FileExistsError, ValueError) as e:
        print(e)
