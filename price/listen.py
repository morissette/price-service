"""
Price Listen
"""
import logging
import zmq
from config import PORT, TOPICS


def listen_topics():
    """
    Listen to all topics
    """
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.connect ("tcp://localhost:%s" % PORT)

    for topicfilter in TOPICS:
        socket.setsockopt(zmq.SUBSCRIBE, topicfilter)

    while True:
        string = socket.recv()
        topic, payload = string.split()
        logging.debug("topic: %s", topic)
        logging.debug("payload: %s", payload)
