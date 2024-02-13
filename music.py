import os, random, time, sys, subprocess, threading


def getFiles(path, extension, recursive=True):
    files = []
    directories = []
    for path, directory, element in os.walk(path, False):
        if recursive:
            directories += directory
    print("Loading music from: " + path)
    tmparray = element
    for i in range(0, len(tmparray) - 1):
        if len(tmparray[i]) >= 4 and tmparray[i].endswith('.' + extension):
            files.append('"' + os.path.normpath(path + '\\' + tmparray[i]) + '"')
    print("Loaded " + str(len(files)) + " files, of " + str(len(element)) + " total")


    for directory in directories:
        files += getFiles(os.path.join(path, directory), extension, recursive)

        return files

print(str(sys.argv))
mediapath = os.path.abspath(sys.argv[1])
play_count = 30
if len(sys.argv) >= 3: play_count = int(sys.argv[2])
mp3s = getFiles(mediapath, 'mp3')
random.shuffle(mp3s)
subprocess.Popen(['C:\\Program Files\\Windows Media Player\\vlcplayer.exe', mp3s[:play_count]])
