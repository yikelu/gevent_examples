import gevent
from gevent import Timeout
import pudb


def pollingLoop():
    i = 0
    while True:
        #pudb.set_trace()
        job = gevent.spawn(myfunc, i)
        job.join()
        i = (i + 1) % 3
        gevent.sleep(1)

def myfunc(i):
    #pudb.set_trace()
    try:
        with Timeout(3):
            gevent.sleep(4)
            d = {0: "HERE I AM",
                1: "ROCK YOU LIKE A HURRICANE",
                2: "YAAAA"}
            print d[i]
    except Timeout as e:
        print "Timed out: %s" % e

if __name__ == "__main__":
    loop_job = gevent.spawn(pollingLoop)
    loop_job.join()
    #gevent.joinall([loop_job])
