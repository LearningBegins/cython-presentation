import zmq

context = zmq.Context()
 
subscriber = context.socket (zmq.SUB)
subscriber.connect("tcp://localhost:48080")
subscriber.setsockopt (zmq.SUBSCRIBE, "")
import cython_client
def main_loop(subscriber):
    count = 0
    while True:
        if count > 1000000:
            break
        count += int(subscriber.recv())
    
cython_client.main_loop(subscriber)