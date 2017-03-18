#!/usr/bin/python
import waving1
import waving2
# import movement
import warnings
import json
warnings.filterwarnings("ignore")  # Never print matching warnings

from dejavu import Dejavu
from dejavu.recognize import MicrophoneRecognizer

# load config from a JSON file (or anything outputting a python dictionary)
with open("dejavu.cnf.SAMPLE") as f:
    config = json.load(f)

if __name__ == '__main__':

    print "\n\nWelcome to the Dancing Robot project, please play a song that is in the list:\n \
            Song 1: Name of Song 1\n \
            Song 2: Name of Song 2\n \
            Song 3: Not avaliable right now\n \
            Song 4: Not avaliable right now\n \
            Song 5: Not avaliable right now\n \
            Song 6: Not avaliable right now\n \
            Song 7: Not avaliable right now\n \
            Song 8: Not avaliable right now\n \
            Song 9: Not avaliable right now\n \
            Song 10: Not avaliable right now\n"

    # create a Dejavu instance
    djv = Dejavu(config)

    # Fingerprint all the mp3's in the directory we give it
    djv.fingerprint_directory("mp3", [".mp3"])

    # Recognize audio from a file
    # song = djv.recognize(FileRecognizer, "mp3/Sean-Fournier--Falling-For-You.mp3")
    # print "From file we recognized: %s\n" % song

    # Or recognize audio from your microphone for `secs` seconds
    secs = 5
    song = djv.recognize(MicrophoneRecognizer, seconds=secs)
    if song is None:
        print "Invalid song, please play songs in the list.\n"
    else:
        print "From mic with %d seconds, the name of the song is: %s\n" % (secs, song)

    # # Or use a recognizer without the shortcut, in anyway you would like
    # recognizer = FileRecognizer(djv)
    # song = recognizer.recognize_file("mp3/Josh-Woodward--I-Want-To-Destroy-Something-Beautiful.mp3")
    # print "No shortcut, we recognized: %s\n" % song

        if song == 'name of song 1':
            waving1.wave_pose1()

        else:
            waving2.wave_pose2()

        # elif song == 3:
        #     movement.pose3()

        # elif song == 4:
        #     movement.pose4()

        # elif song == 5:
        #     movement.pose5()

        # elif song == 6:
        #     movement.pose6()

        # elif song == 7:
        #     movement.pose7()

        # elif song == 8:
        #     movement.pose8()

        # elif song == 9:
        #     movement.pose9()

        # elif song == 10:
        #     movement.pose10()
