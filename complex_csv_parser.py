from typing import List
import json
import csv

def parse_csv(csvs: str, separator: str=',', quote: str='"') -> List[List[str]]:
    
    mlist = []
    #return []
    nlist = []
    if len(csvs) == 0:
      return [[""]]
    lines = csvs.splitlines(True)
    #print(lines)
    reader = csv.reader(lines, delimiter = separator, quotechar=quote)
    parsed_csv = list(reader)
    for nl in parsed_csv:
      nlist = []
      #print(nl)
      if len(nl) == 0:
        nlist.append("j")
        nlist.append("")
        nlist.pop(0)
        print(nlist)
        mlist.append(nlist)
        nlist = []
          
      else:
        #print(nl)
        mlist.append(nl)
  
    #print(type(mlist))
    #return list(mlist)
    return mlist
