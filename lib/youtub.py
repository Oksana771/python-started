from subprocess import call
import os
if __name__ == "__main__":
    Youtube


class Youtube:

    def start(self):
        exit = False
        while not exit:
            choice = int(
                input("1. Movie\n2. Audio\n3. Playlist\n0. Exit\n=:>> "))
            if choice == 1:
                URL = input("Enter movie URL: ")
                self.__get_movie(URL)
            elif choice == 2:
                URL = input("Enter movie URL: ")
                self.__get_audio(URL)
            elif choice == 3:
                URL = input("Enter movie URL: ")
                self.__get_playlist(URL)
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

    def __get_audio(self, URL):
        info = "youtube-dl " + URL + " -F"
        call(info, shell=False)
        download_command = "youtube-dl -f 140 "  + URL + " -c"
        os.chdir("Downloads")
        call(download_command, shell=False)

    def __get_playlist(self, URL):
        info = "youtube-dl " + URL + " -F"
        call(info, shell=False)
        download_command = "youtube-dl -f 140 "  + URL + " -c"
        os.chdir("Downloads")
        call(download_command, shell=False)
