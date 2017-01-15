#!/bin/bash

token=`curl 'http://jio4gservice.ml/' -H 'Origin: http://jio4gservice.ml' -H 'Accept-Encoding: gzip, deflate' -H 'Accept-Language: en-US,en;q=0.8,ml;q=0.6' -H 'Upgrade-Insecure-Requests: 1' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' -H 'Cache-Control: max-age=0' --compressed | sed -n 's/.*<input type="hidden" name="token" value="\([0-9a-f]\+\)">/\1/p'`

echo

[ "$token" == "30382d30362d3136" ] && echo "No changes in token." || echo "Token changed to $token!"
