#!/usr/bin/env python3

import what3words
import click
import json
import webbrowser
import sys

@click.command()
@click.argument('w1')
@click.argument('w2')
@click.argument('w3')
@click.option('--map', '-m', is_flag=True, help='Open map for the words')
@click.option('--coords', '-c', is_flag=True, help='Get co-ordinates for the words')
@click.option('--where', '-w', is_flag=True, help='Get approximate place for the words')
def main(w1,w2,w3,map,coords,where):
    """
    A tool to quickly get the location of a what3words address
    """

    key = file_get_contents("key.config")

    geocoder = what3words.Geocoder(key)
    res = geocoder.convert_to_coordinates(f"{w1}.{w2}.{w3}")
    if 'error' in res:
        print(res['error']['message'])
        sys.exit()

    if coords:
        print(f"{res['coordinates']['lat']},{res['coordinates']['lng']}")
    elif map:
        url = f"https://www.google.com/maps/search/?api=1&query={res['coordinates']['lat']}%2C{res['coordinates']['lng']}"
        webbrowser.open(url)
    elif where:
        print(f"{res['nearestPlace']},{res['country']}")
    else:
        url = f"https://www.google.com/maps/search/?api=1&query={res['coordinates']['lat']}%2C{res['coordinates']['lng']}"
        webbrowser.open(url)

def file_get_contents(filename):
    with open(filename) as f:
        return f.read()

if __name__ == "__main__":
    main()