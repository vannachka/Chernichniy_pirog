import os
import platform
import json
import socket
import sys
from datetime import datetime


def get_os_info():
    """Определение и сбор основных параметров ОС."""

    system = platform.system()

    if system == "Windows":
        os_name = "Windows"
    elif system == "Linux":
        os_name = "Linux"
    elif system == "Darwin":
        os_name = "macOS"
    else:
        os_name = system

    return {
        "name": os_name,
        "version": platform.version(),
        "release": platform.release(),
        "architecture": platform.machine(),
        "processor": platform.processor(),
        "hostname": socket.gethostname(),
        "username": os.getlogin()
    }


def get_python_info():
    """Информация о Python."""

    return {
        "version": platform.python_version(),
        "implementation": platform.python_implementation(),
        "executable": sys.executable
    }


def get_system_info():
    """Общая информация о системе."""

    return {
        "operating_system": get_os_info(),
        "python": get_python_info(),
        "current_directory": os.getcwd(),
        "home_directory": os.path.expanduser("~"),
        "date_time": datetime.now().isoformat()
    }


def save_to_json(data, filename="system_info.json"):
    """Сохранение информации в JSON-файл."""

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def main():
    print("Сбор информации о текущей операционной системе...")

    system_info = get_system_info()

    save_to_json(system_info)

    print("Информация успешно сохранена в файл system_info.json")


if __name__ == "__main__":
    main()