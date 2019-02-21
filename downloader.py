import urllib.request
import shutil
import zipfile
import os

class Downloader:

    def __linuxPlatform(self):
        self.url = self.url.format(self.version, "linux64")
    
    def __windowsPlatform(self):
        self.url = self.url.format(self.version, "win32")

    def __getDownloadUrl(self):
        if self.platform == "Linux":
            self.__linuxPlatform()
            self.separator = "/"
        elif self.platform == "Windows":
            self.__windowsPlatform()
            self.separator = "\\"
        else:
            print("Invalid argument")

    def __init__(self, platform):
        self.url = "https://chromedriver.storage.googleapis.com/{0}/chromedriver_{1}.zip"
        self.version = "2.46"
        self.platform = platform
        self.__getDownloadUrl()

    def __extractArchive(self, dir_to_extract):
        print("dir_to_extract: {0}".format(dir_to_extract))
        with zipfile.ZipFile(self.file_path, "r") as zip_ref:
            zip_ref.extractall(dir_to_extract)    

    def downloadDriver(self, dir_to_extract):
        print("url: {0}".format(self.url))
        with urllib.request.urlopen(self.url) as response, open("chromedriver.zip", 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
            self.file_path = os.path.dirname(__file__) + self.separator + "chromedriver.zip"
            print("file_path: {0}".format(self.file_path))
            #self.__extractArchive(dir_to_extract)

    