import yaml
from MarketWatchBI.scrap import Scrap
from MarketWatchBI.populate import Populate

if __name__ == "__main__":
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
