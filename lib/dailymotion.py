from subprocess import call
import os

if __name__ == "__main__":
    Dailymotion


class Dailymotion:

    def start(self):
        exit = False
        while not exit:
            choice = int(
                input("1. Movie\n0. Exit\n=:>> "))
            if choice == 1:
                URL = input("Enter movie URL: ")
                self.__get_movie(URL)
            elif choice == 0:
                exit = True
            else:
                print("Use --help for reading manual")

    def __get_movie(self, URL):
        info = "youtube-dl " + URL + " -F"
        call(info, shell=False)
        download_command = "youtube-dl -f best "  + URL + " -c"
        os.chdir("Downloads")
        call(download_command, shell=False)
        
      