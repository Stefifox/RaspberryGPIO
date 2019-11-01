# This code is logger code for various app
import time


def log(message):
    data = str(time.strftime("%d-%m-%Y"))
    hour = str(time.strftime("%H:%M:%S"))
    file = open(".//Log//Log" + data + ".txt", "a")
    file.write("[" + hour + "] " + message + "\n")
    file.close()


def log(message, n_file):
    hour = str(time.strftime("%H:%M:%S"))
    file = open( ".//" + n_file, "a")
    file.write("[" + hour + "] " + message + "\n")
    file.close()