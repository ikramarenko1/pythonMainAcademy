# Використовуючи бібліотеку argparse, створіть програму, яка приймає шлях до файлу та визначає його розмір.
import os
import argparse


def get_file_size(file_path):
    return os.path.getsize(file_path)


parser = argparse.ArgumentParser(description='Визначення розміру файлу.')
parser.add_argument('path', help='Шлях до файлу, розмір якого потрібно визначити.')

args = parser.parse_args()
file_size = get_file_size(args.path)

print(f'Розмір файлу "{args.path}" складає {file_size} байтів.')
