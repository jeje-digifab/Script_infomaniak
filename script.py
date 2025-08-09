#!/usr/bin/env python3

import dns.resolver
#import dns.name
import re

url = 'candiharvest.infomanihack.ch'


# curl --header "X-Candidate-Id:'id={id} https://candiharvest.infomanihack.ch/


# Finding TXT record
result = dns.resolver.resolve(url, 'TXT')

# Printing record
for val in result:
    id = val.to_text()
    id = re.sub(r'"', '', id)
    print(id)
