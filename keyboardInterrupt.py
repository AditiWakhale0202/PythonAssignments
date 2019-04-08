# import time, sys
#
# x = 1
# while True:
#     try:
#         print x
#         time.sleep(.3)
#         x += 1
#     except KeyboardInterrupt:
#         print "Bye"
#         sys.exit()

#!/usr/bin/env python
import signal
import sys
def signal_handler(signal, frame):
        print('You pressed Ctrl+C!')
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)
print('Press Ctrl+C')
signal.pause()