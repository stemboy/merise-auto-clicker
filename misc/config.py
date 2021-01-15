import os

from kivy.config import ConfigParser

from misc import user_data_dir

Config = ConfigParser()
Config.read(os.path.join(user_data_dir, "config.ini"))


def create():
    for section in Config.sections():
        Config.remove_section(section)

    Config.add_section("Mining")
    Config.add_section("Gui")

    Config.set("Mining", "mode", "Ghost")
    Config.set("Mining", "url", "https://app.memrise.com/signin")
    Config.set("Gui", "webpage_image_update_interval", 1)


    with open(os.path.join(user_data_dir, "config.ini"), 'w'):
        Config.write()
