#!/bin/sh
echo "$ bash test7.sh"
cut -f1 address.txt | sort | uniq | wc -l
