import time
import random
import json
import datetime
from tornado import websocket, web, ioloop
from datetime import timedelta
from random import randint

paymentTypes = ["cash", "tab", "visa","mastercard","bitcoin"]
namesArray = ['Ben', 'Jarrod', 'Vijay', 'Aziz']


class WebSocketHandler(websocket.WebSocketHandler):
  #fix connect error 403
  def check_origin(self, origin):
    return True
  
  #on open of this socket
  def open(self):
    print 'Connection established.'
    #ioloop to wait for 3 seconds before starting to send data
    ioloop.IOLoop.instance().add_timeout(datetime.       
    timedelta(seconds=1), self.send_data)
 
 #close connection
  def on_close(self):
    print 'Connection closed.'

  # Our function to send new (random) data for charts
  def send_data(self):
    print "Sending Data"
    #create a bunch of random data for various dimensions we want
    spent = random.randrange(1,150);
    #create a new data point
    point_data = {
    	'Spent': spent,
    }

    print point_data
  
    #write the json object to the socket
    self.write_message(json.dumps(point_data))
    
    #create new ioloop instance to intermittently publish data
    ioloop.IOLoop.instance().add_timeout(datetime.timedelta(seconds=1), self.send_data)

if __name__ == "__main__":
  #create new web app w/ websocket endpoint available at /websocket
  print "Starting websocket server program. Awaiting client requests to open websocket ..."
  application = web.Application([(r'/websocket', WebSocketHandler)])
  application.listen(81)
ioloop.IOLoop.instance().start()

