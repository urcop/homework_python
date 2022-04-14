#!/bin/bash
cat /dev/null >decodepasswords.txt
cat logpassfile | while read line
  do
    IFS=' ' read -r -a list <<<"$line"
    printf "%s " "${list[0]}" >>decodepasswords.txt
    printf "%s " "${list[1]}" | md5sum >>decodepasswords.txt
  done
