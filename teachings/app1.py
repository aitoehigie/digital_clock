#!/usr/bin/env python

import json
data = json.loads(open('1.1 data.json.json'))

def translate(key):
    try:
        if key in data:
            return data[key]
        else:
            return "key doesnt exist"
    except:
        return "An error occured"

if __name__ == "__main__":
    print(translate(input("enter the key")))


