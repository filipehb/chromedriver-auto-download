import os
import subprocess
import sys

class Environment:

    def __linuxEnv(self):
        """Set chrome environment on Linux"""
        # TODO Need to test
        print('Command: PATH="{0}:$PATH"'.format(self.file_path + "chromedriver"))
        os.system("PATH=\"{0}:$PATH\"".format(self.file_path + "chromedriver"))
    
    def __windowsEnv(self):
        """Set chrome environment on Windows"""
        print('Command: setx Path "%Path%;{0}"'.format(self.file_path))
        os.system("setx Path \"%Path%;{0}\"".format(self.file_path))

    def __setEnv(self):
        """Switch between platforms.

        Variables:
        separator -- platform directory separator
        """
        if self.platform == "Linux":
            self.__linuxEnv()
        elif self.platform == "Windows":
            self.__windowsEnv()
        else:
            print("Invalid platform argument")

    def __init__(self, platform, file_path):
        self.platform = platform
        self.file_path = file_path
        self.__setEnv()

    