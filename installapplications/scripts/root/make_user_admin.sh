#!/bin/bash

USER="$(/usr/bin/stat -f "%Su" /dev/console)"

/usr/sbin/dseditgroup -o edit -a $USER -t user admin