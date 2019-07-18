# MarketWatchBI
Web scrapper for Reserve Bank of India
Converts the page data to an excel sheet

# Usage
If using firefox, need to install geckodriver (https://github.com/mozilla/geckodriver/releases)
Run script and an excel file will be outputted

# Configuration
```
# MarketWatchBI Configuration
url: https://www.ccilindia.com/OMMWCG.aspx
table_id: grdMWCG
# Make sure file format is .xlsx
output_file: output.xlsx
```
url is the website url
table_id is the HTML id for the table containing the data

