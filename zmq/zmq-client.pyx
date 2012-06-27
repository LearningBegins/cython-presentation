from zmq.core.socket cimport Socket
from libc.stdlib cimport atoi

def main_loop(Socket subscriber):
    cdef int count = 0
    while True:
        if count > 1000000:
            break
        tmp_msg = subscriber.recv()
        count += atoi(<char *>tmp_msg)
        