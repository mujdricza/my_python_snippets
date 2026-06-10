"""
https://superfastpython.com/multiprocessing-pool-for-loop/
"""

from functools import wraps
from multiprocessing import Pool, Process, Queue
import os
from time import time

TIMES = {}
def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        # print('func:%r args:[%r, %r] took: %2.4f sec' % (f.__name__, args, kw, te-ts))
        print('func:%r took: %2.4f sec' % (f.__name__, te-ts))
        TIMES.setdefault(f, []).append(te-ts)
        return result
    return wrap

# task that operates on an item

def task(item):
    return item[0]+item[1]

def task_queue(items, queue):  # maybe not appropriate implementation
    for item in items:
        result = task(item)
        queue.put(result)

@timing
def my_simpleprocess(items):
    reslist = []
    for i, item in enumerate(items):
        reslist.append((i, task(item)))
    #print("Done simpleprocess: ")
    #print(f"{reslist[:10]} ...")
    return reslist


@timing
def my_simpleprocess_map(items):
    reslist = []
    for i, result in enumerate(map(task, items)):
        # for i, result in enumerate(pool.imap_unordered(task, items, chunksize=len(cpus))):
        #print(f"{i}: {result}")
        reslist.append((i, result))
    #print("Done simpleprocess: ")
    #print(f"{reslist[:10]} ...")
    return reslist


def chunking(items, chunksize):
    return [items[x:x + chunksize] for x in range(0, len(items), chunksize)]

@timing
def my_multiprocess_process_queue(items, cpus):
    reslist = []
    q = Queue()
    item_chunks = chunking(items, cpus)
    for item_chunk in item_chunks:
        p = Process(target=task_queue, args=(item_chunk, q,))
        p.Daemon = True
        p.start()
    for item_chunk in item_chunks:
        p.join()
    for i in range(len(item_chunks)):
        r = q.get()
        reslist.append(r)
    return reslist


@timing
def my_multiprocess_pool(items, cpus):

    # create a process pool that uses all cpus
    reslist = []
    with Pool() as pool:
        # call the function for each item in parallel with multiple arguments
        #for i, result in enumerate(pool.imap_unordered(task, items, chunksize=cpus)):
        #for i, result in enumerate(pool.map(task, items, chunksize=cpus)):
        for i, result in enumerate(pool.imap(task, items, chunksize=cpus)):
            reslist.append((i, result))
        # shutdown the process pool
        pool.close()
        # wait for all issued task to complete
        pool.join()
    #print("Done multiprocess: ")
    #print(f"{reslist[:10]} ...")
    return reslist


cpus = len(os.sched_getaffinity(0))
print(f"CPUs: {cpus}")
n = 5

items = [(i,i+1) for i in range(0,100,2)]
print(f"Items length = {len(items)}")
for i in range(n):
    rs = my_simpleprocess(items)
    rsm = my_simpleprocess_map(items)
    rmp = my_multiprocess_pool(items, cpus)
    rmpq = my_multiprocess_process_queue(items, cpus)
    print(f"Result: {str(rs)[:100]}")
    if rs != rsm != rmp != rmpq:
        print(f"--> Different results")

for fct, ts in TIMES.items():
    print(f"Fct {fct} has {len(ts)} processes with avg. = {sum(ts)/n}, max = {max(ts)}, min = {min(ts)}")

"""
eva@axx-PF1PXVZP:/mnt/c/emm/DTK/gitlab/magenta-voice/magenta/nlu-coli/internal_projects/eva_mujdricza-maydt/misc/src/exp/mutliprocessing (main)$ python mp_exp1.py
CPUs: {0, 1, 2, 3, 4, 5, 6, 7}
Done multiprocess:
func:'my_multiprocess' took: 0.1933 sec
Done simpleprocess:
func:'my_simpleprocess_map' took: 0.0012 sec
Done simpleprocess:
func:'my_simpleprocess' took: 0.0014 sec
Done multiprocess:
func:'my_multiprocess' took: 0.1681 sec
Done simpleprocess:
func:'my_simpleprocess_map' took: 0.0010 sec
Done simpleprocess:
func:'my_simpleprocess' took: 0.0011 sec
Done multiprocess:
func:'my_multiprocess' took: 0.1542 sec
Done simpleprocess:
func:'my_simpleprocess_map' took: 0.0010 sec
Done simpleprocess:
func:'my_simpleprocess' took: 0.0010 sec
Done multiprocess:
func:'my_multiprocess' took: 0.1774 sec
Done simpleprocess:
func:'my_simpleprocess_map' took: 0.0010 sec
Done simpleprocess:
func:'my_simpleprocess' took: 0.0010 sec
Done multiprocess:
func:'my_multiprocess' took: 0.1628 sec
Done simpleprocess:
func:'my_simpleprocess_map' took: 0.0010 sec
Done simpleprocess:
func:'my_simpleprocess' took: 0.0011 sec
Fct <function my_multiprocess at 0x7f66025ba3a0> has 5 processes with avg. = 0.17117204666137695, max = 0.19330978393554688, min = 0.15422844886779785
Fct <function my_simpleprocess_map at 0x7f660271d0d0> has 5 processes with avg. = 0.001062154769897461, max = 0.0012462139129638672, min = 0.00099945068359375
Fct <function my_simpleprocess at 0x7f66025ba280> has 5 processes with avg. = 0.0011114120483398438, max = 0.0014071464538574219, min = 0.0009505748748779297
"""