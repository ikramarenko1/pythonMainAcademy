# Використовуючи бібліотеку shutil, створіть програму, яка видаляє всі файли з певного каталогу,
# які старше заданої дати.
import os
import shutil
from datetime import datetime, timedelta


def remove_old_files(directory, days_old):
    threshold_date = datetime.now() - timedelta(days=days_old)

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        file_modification_time = datetime.fromtimestamp(os.path.getmtime(file_path))

        if file_modification_time < threshold_date:
            if os.path.isfile(file_path):
                shutil.rmtree(file_path, ignore_errors=True)
                print(f"Файл {filename} видалено.")


directory_path = "."
days_old = 5
remove_old_files(directory_path, days_old)
