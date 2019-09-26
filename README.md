# MarketWatchBI
Reserve Bank of India NDS-OM converts the page data to an excel sheet.

## Usage
If using firefox, need to install geckodriver (https://github.com/mozilla/geckodriver/releases)
Run script and an excel file will be outputted.

## Configuration
```
# MarketWatchBI Configuration
url: https://www.ccilindia.com/OMMWCG.aspx
table_id: grdMWCG
# Make sure file format is .xlsx
output_file: output.xlsx
```
url is the website url
table_id is the HTML id for the table containing the data

## To do
  - Work for the BSE Bombay Stock Exchange
  - Multiple page support
  - Multiple runs aka run every 3 minutes, different output file
