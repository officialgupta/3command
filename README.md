# 3command
## A tool to quickly get the location of a what3words address

## Usage
* You must create a what3words account to obtain an API key. This must be places into the key.config file.
* The requirements for this program are click and what3words. These can be installed with `pip install -r requirements.txt`

To run the program use `python3 3c.py <options> w1 w2 w3`
#### Example
```
python3 3c.py --map shovels unity orchestra
```

## Options
```
  -m, --map     [DEFAULT] Open map for the words (opens in google maps)
  -c, --coords  Get co-ordinates for the words
  -w, --where   Get approximate place for the words
  --help        Show this message and exit.
```
