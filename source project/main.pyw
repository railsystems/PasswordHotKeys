import configparser
import os
import keyboard
import pystray
from pystray import MenuItem as item
from pystray import Icon as icon, Menu as menu
from PIL import Image

CONFIG_FILE = "config.ini"

def create_default_config():
    config = configparser.ConfigParser()
    config["Hotkeys"] = {"ctrl+f1": "Password1", "ctrl+f2": "Password2"}
    with open(CONFIG_FILE, "w") as config_file:
        config.write(config_file)

def read_config():
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)
    return config

def write_config(config):
    with open(CONFIG_FILE, "w") as config_file:
        config.write(config_file)

def load_settings():
    config = read_config()
    if not config.sections():
        create_default_config()
        config.read(CONFIG_FILE)

    hotkeys = config["Hotkeys"]
    password_mapping = {}

    for hotkey, password in hotkeys.items():
        password_mapping[hotkey] = password

    return password_mapping

def enter_password(password):
    keyboard.write(password)

def on_exit(icon, item):
    icon.stop()

def main():
    password_mapping = load_settings()

    menu_options = [item('Выход', on_exit)]
    menu_def = menu(*menu_options)

    image = Image.open("C:\\Users\\r.nabiyev\\PycharmProjects\\keyboard\\dist\\1234.png")  # Укажите путь к вашему изображению
    icon_image = icon("name", image, menu=menu_def)

    for hotkey, password in password_mapping.items():
        keyboard.add_hotkey(hotkey, enter_password, args=(password,))

    print("Программа запущена. Для сворачивания в трей используйте иконку в трее.")

    icon_image.run()

if __name__ == "__main__":
    main()
