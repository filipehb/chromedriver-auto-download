import os
import subprocess
import sys

class Environment:

    def __linuxEnv(self):
        os.environ['CHROMEDRIVER_PATH'] = self.file_path
        return "Linux"
    
    def __windowsEnv(self):
        os.environ['CHROMEDRIVER_PATH'] = self.file_path
        return "Windows"

    def __setEnv(self):
        platform_list = {
            1: self.__linuxEnv(),
            2: self.__windowsEnv()
        }
        platform_list.get(self.platform, lambda: "Invalid argument")

    def __init__(self, platform, file_path):
        self.platform = platform
        self.file_path = file_path
        self.__setEnv()

    