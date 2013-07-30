import gevent
from gevent import Timeout
from gevent.coros import Semaphore
import pudb

lock = Semaphore(1)

def pollingLoop():
    i = 0
    while True:
        #pudb.set_trace()
        job = gevent.spawn(myfunc, i)
        job2 = gevent.spawn(myfunc, i)
        gevent.joinall([job, job2])
        i = (i + 1) % 3
        gevent.sleep(1)

def myfunc(i):
    print "entering myfunc, trying to acquire"
    t = Timeout.start_new(2)
    try:
        lock.acquire()
    except Timeout as e:
        print "Deadlocked myfunc: %s  :  %s" % (e, type(e))
        print "Returning without action"
        return
    finally:
        t.cancel()

    print "lock acquired"
    #pudb.set_trace()
    gevent.sleep(4)
    d = {0: "HERE I AM",
        1: "ROCK YOU LIKE A HURRICANE",
        2: "YAAAA"}
    print d[i]
    lock.release()

if __name__ == "__main__":
    loop_job = gevent.spawn(pollingLoop)
    loop_job.join()
    #gevent.joinall([loop_job])
