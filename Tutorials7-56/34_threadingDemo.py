# A threading demonstration


import threading


class BuckysMessenger(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.currentThread().getName())

x = BuckysMessenger(name='Send Messages')
y = BuckysMessenger(name='Receive Messages')

# The start() function looks for run()
# in class definition and kickstarts run()
x.start()
y.start()

