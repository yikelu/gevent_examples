import gevent
from gevent import Timeout
import pudb


def pollingLoop():
    i = 0
    while True:
        job = gevent.spawn(myfunc, i)
        job.join()
        i = (i + 1) % 3
        gevent.sleep(1)

def myfunc(i):
    timeout = Timeout(3)
    timeout.start()
    try:
        gevent.sleep(4)
        d = {0: "HERE I AM",
            1: "ROCK YOU LIKE A HURRICANE",
            2: "YAAAA"}
        print d[i]
    except Timeout as e:
        print 'Timeout caught: %s' % e
    finally:
        timeout.cancel()

if __name__ == "__main__":
    loop_job = gevent.spawn(pollingLoop)
    gevent.joinall([loop_job])
