#include "zmq.h"

int main(int argc, char ** argv)
{
  void *context = zmq_init (1);

  // Socket to talk to clients
  void *subscriber = zmq_socket (context, ZMQ_SUB);
  zmq_connect (subscriber, "tcp://localhost:48080");
  zmq_setsockopt (subscriber, ZMQ_SUBSCRIBE, "", 0);
  
  int count = 0;

  while(1)
  {
    if(count > 1000000)
      break;

    zmq_msg_t msg;
    zmq_msg_init (&msg);
    zmq_recv (subscriber, &msg, 0);
    count += atoi(zmq_msg_data(&msg));
    zmq_msg_close (&msg);
  }
}
