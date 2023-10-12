#!/usr/bin/env python3
# coding=utf-8
import sys
from DOGZILLALib import DOGZILLA
from SpeechLib import Speech

# V1.0.0
class Dogzilla_Speech(object):

    def __init__(self, dog:DOGZILLA, com='/dev/myspeech', debug=False):
        self.__debug = debug
        self.__com = com
        self.__speech = Speech(self.__com, self.__debug)
        self.__dog = dog

        self.STATE_OK = 0
        self.STATE_NO_OPEN = 1
        self.STATE_DISCONNECT = 2
        self.STATE_KEY_BREAK = 3


    def __del__(self):
        del self.__speech
        if self.__debug:
            print("\n---Dogzilla_Speech DEL---\n")

    # Return state
    def is_Opened(self):
        return self.__speech.isOpen()

    # reset DOGZILLA
    def __dog_reset(self):
        self.__dog.reset()


    def __ctrl_dog(self, cmd):
        if 0 < cmd < 4:
            self.__dog.stop()
        elif cmd == 4:
            self.__dog.forward(12)
        elif cmd == 5:
            self.__dog.back(12)
        elif cmd == 6:
            self.__dog.left(10)
        elif cmd == 7:
            self.__dog.right(10)
        elif cmd == 8:
            self.__dog.turnleft(50)
        elif cmd == 9:
            self.__dog.turnright(50)

    # Control robot
    def __data_processing(self, value):
        cmd = int(value)
        if 0 < cmd < 10:
            self.__speech.write(cmd)
            self.__ctrl_dog(cmd)
            

    # Handles events for speech
    def speech_handle(self):
        if not self.__speech.isOpen():
            return self.STATE_NO_OPEN
        try:
            data = self.__speech.read()
            if 0 < data < 999:
                self.__data_processing(data)
            return self.STATE_OK
        except KeyboardInterrupt:
            if self.__debug:
                print('Key Break Speech')
            return self.STATE_KEY_BREAK


if __name__ == '__main__':
    g_debug = False
    if len(sys.argv) > 1:
        if str(sys.argv[1]) == "debug":
            g_debug = True
    print("debug=", g_debug)

    g_dog = DOGZILLA()
    speech = Dogzilla_Speech(g_dog, com='/dev/ttyUSB0', debug=g_debug)
    try:
        while True:
            state = speech.speech_handle()
            if state != speech.STATE_OK:
                break
    except KeyboardInterrupt:
        pass
    del speech
