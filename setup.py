import platform as plt
from environment import Environment
from downloader import Downloader
import sys

def main(argv):
  print("Platform: {0}".format(plt.system()))
  print("Argument: {0}".format(str(argv)))
  down = Downloader(plt.system())
  down.downloadDriver(str(argv))
  #env = Environment(plt.system(), down.file_path)

  
  
if __name__== "__main__":
  main(sys.argv[1])