import gevent
from gevent import Timeout
import pudb


def pollingLoop():
    i = 0
    while True:
        #pudb.set_trace()
        job = gevent.spawn(myfunc, i)
        try:
            job.join(timeout=3)
        except Timeout as e:
            print "Timed out %s" % e
        i = (i + 1) % 3
        gevent.sleep(1)

def myfunc(i):
    #pudb.set_trace()
    gevent.sleep(4)
    d = {0: "HERE I AM",
        1: "ROCK YOU LIKE A HURRICANE",
        2: "YAAAA"}
    print d[i]

if __name__ == "__main__":
    loop_job = gevent.spawn(pollingLoop)
    gevent.joinall([loop_job])
