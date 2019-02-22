import platform as plt
from environment import Environment
from downloader import Downloader
import sys

def main(argv):
  print("Platform: {0}".format(plt.system()))
  print("Argument: {0}".format(str(argv)))
  down = Downloader(plt.system())
  down.downloadDriver(str(argv))
  print("file_exec_path: {0}".format(down.file_exec_path))
  Environment(plt.system(), down.file_exec_path)

  
  
if __name__== "__main__":
  try:
    main(sys.argv[1])
  except IndexError:
    print("invalid quantity of arguments")