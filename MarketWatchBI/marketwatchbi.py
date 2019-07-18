import yaml
from MarketWatchBI.scrap import Scrap
from MarketWatchBI.populate import Populate

if __name__ == "__main__":
    """ Load Config """
    with open("config.yml", "r") as f:
        cfg = yaml.safe_load(f)

    """ Scrapper """
    scrap = Scrap(cfg, cfg['url'])
    data = scrap.read('table', {'id': cfg['table_id']})

    for d in data:
        print(d)

    """ Excel populate """
    out = Populate(cfg)
    out.write(data)
    out.save("test.xlsx")
