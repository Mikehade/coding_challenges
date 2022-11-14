from typing import List
import json

def parse_csv(csv: str, separator: str=',', quote: str='"') -> List[List[str]]:
    #print(csv)
    #print(len(csv), separator, quote)
    ml = []
    #return []
    nl = []
    for i in range(len(csv)):
      if csv[i] == separator:
        #print(csv[i-1])
        nl.append(csv[i-1])
        #print(nl)
      elif csv[i] == "\n":
        #print(csv[i-1])
        nl.append(csv[i-1])
        #print(nl)
        #nl = [i.replace("'", "") for i in nl]
        js_str = json.dumps(nl)
        print(type(js_str))
        #res = [item.replace("'", "") for item in js_str]
        ml.append(js_str)
        nl = []
      elif csv[i] == csv[-1]:
        #print(csv[-1])
        nl.append(csv[-1])
        #print(nl)
        #nl = [i.replace("'", "") for i in nl]
        js_str = json.dumps(nl)
        print(js_str)
        ml.append(nl)
        nl = []
    #ml = [item.replace("'", "") for item in ml]
    return ml 
