import zmq

context = zmq.Context()
 
publisher = context.socket (zmq.PUB)
publisher.bind ("tcp://*:48080")

while True:
    publisher.send('1')
    
    