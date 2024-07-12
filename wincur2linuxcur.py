#!/usr/bin/env python
import os 
import shutil
import argparse
import csv

def get_args():
    parser = argparse.ArgumentParser(
        prog = "Windows cursor theme to linux cursor theme",
        description = "Convert a windows cursor theme to a linux cursor theme"
    )
    parser.add_argument("output_path")
    parser.add_argument("cursor_csv_path")
    parser.add_argument("linux_cursor_theme_path")
    parser.add_argument("windows_cursor_theme_path")

    argvs = parser.parse_args()
    return argvs

def main():
    argvs = get_args()
    output_path = argvs.output_path
    linux_cursor_path = argvs.linux_cursor_theme_path
    cursor_csv_path = argvs.cursor_csv_path
    window_cursor_path = argvs.windows_cursor_theme_path

    # linux_cursors = [file for file in os.listdir(linux_cursor_path) if os.path.isfile(os.path.join(linux_cursor_path,file))]
    # window_cursors = [file for file in os.listdir(window_cursor_path) if os.path.isfile(os.path.join(window_cursor_path, file))]
    parsed_csv = []
    with open(cursor_csv_path, "r") as cursor_csv:
        reader = csv.reader(cursor_csv, delimiter=",")
        next(reader)
        for line in reader:
            parsed_csv.append((line[0], line[1]))


    for win_cur, linux_cur in parsed_csv:
        if win_cur == "":
            src = os.path.join(linux_cursor_path, linux_cur)
            dst = os.path.join(output_path, linux_cur)
        else:
            src = os.path.join(window_cursor_path, win_cur)
            dst = os.path.join(output_path, linux_cur)
        print(f"Copied {src} to {dst}")
        shutil.copy(src, dst)


if __name__ == "__main__":
    main()