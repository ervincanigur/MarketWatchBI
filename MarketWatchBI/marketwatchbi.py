import yaml
# from datetime import datetime
import sched
import time
from MarketWatchBI.scrap import Scrap
from MarketWatchBI.populate import Populate


def job():
    print("Starting Job")
    """ Load Config """
    with open("config.yml", "r") as f:
        cfg = yaml.safe_load(f)

    """ Scrapper """
    scrap = Scrap(cfg['url'])
    data = scrap.read('table', {'id': cfg['table_id']})

    """ Excel populate """
    out = Populate()
    out.write(data)
    out.save(cfg['output_file'])


if __name__ == "__main__":
    # Makes job run every minute, for testing
    s = sched.scheduler(time.time, time.sleep)
    s.enter(60, 1, job)
    s.run()
    # TODO: add time restrictions, disabled for debug
    # while True:
    #     if int(datetime.minute) % 3:  # every 3 minutes
    #         job()
