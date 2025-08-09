#!/usr/bin/env python3

import dns.resolver
import re
import urllib3

url = 'candiharvest.infomanihack.ch'


def txt_record():
    """
    Function to fetch TXT records for a given URL.
    """
    try:
        result = dns.resolver.resolve(url, 'TXT')

        for val in result:
            id = val.to_text()
            id = re.sub(r'"', '', id)
            print(id)
    except Exception as e:
        print(f"Error fetching TXT record: {e}")
        return None

def header():
    """
    Function to fetch headers from a URL using urllib3.
    """
    
    resp = urllib3.request(
        "GET",
        "https://candiharvest.infomanihack.ch",
        headers={
            "X-Candidate-Id": "value"
        }
    )
    
    print(resp.data.decode('utf-8'))

if __name__ == "__main__":
    # main()
#    txt_record()
    header()
