
exit = False
while not exit:
    choice = int(input("1. Youtube\n2. Dailymotion\n0. Exit\n=:->> "))
    if choice == 1:
        from lib.youtub import Youtube
        youtube = Youtube()
        youtube.start()
    elif choice == 2:
       from lib.dailymotion import Dailymotion
       dailymotion = Dailymotion()
       dailymotion.start()
    elif choice == 0:
        exit = True
        print("Bye!")
    else:
        print("Wrong choice.")






