"""
Price Service Handler
"""
import logging
from price.store import Store
from price.cache import CacheEntity
from price.projection import Projection
from price.listen import listen_topics

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    logging.debug("Starting Price Service")

    store = Store()

    logging.debug("Getting current events since last restart")
    events = store.ReadStream()

    if events is not None:
        logging.debug("Getting current state for each price entity")
        entities = Projection(events)

        logging.debug("Caching entities")
        for entity in entities:
            CacheEntity(entity)

    logging.debug("Listening for new events")
    listen_topics()
