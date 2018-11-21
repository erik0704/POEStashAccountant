# Overview

POEStashAccountant is a lightweight Path of Exile tool to calculate your private stash networth, inspired by Currency Cop.

## Requirements

Python 3.3+ installed.

## Installation

```bash
pip install -r requirements.txt
```

## Configuration (*important*)

1. On browser, login [Path of Exile homepage](https://www.pathofexile.com/)
2. Find your POESESSID by following [this comprehensive guide in Currency Cop main thread](https://www.pathofexile.com/forum/view-thread/1989935/page/9#p14857124)
3. Edit `settings.json` with your POESESSID, account name and the league your stash is in.

## How to use

Currently the program can only analyse one stash tab at a time. The stash tab should have a unique name among all your other tabs in that league.

### On Windows
```python
python main.py [your_stash_tab_name]
```

Above is the script running in CMD. 
In Powershell it would be something like `python .\main.py quadtabdump`

### On Linux
```terminal
# python ./main.py my_currency_tab
```

## Acknowledgement

Path of Exile stash API is provided by Grinding Gear Game. Item value rate is provided by [poe.ninja](https://poe.ninja/)