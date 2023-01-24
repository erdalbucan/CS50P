#pip install

import requests
import sys


if len(sys.argv) != 2:
    sys.exit("Too Fell Arguments")

request = requests.get(
    "https://itunes.apple.com/search?entity=song&limit=1&term="+sys.argv[1]
)

print(request.json())

