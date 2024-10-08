#!/bin/sh

for srcfile in src/json/*.erb; do
  dstfile="docs/json/`basename $srcfile .erb`"
  if [ "$srcfile" -nt "$dstfile" ]; then
    if scripts/erb2json.rb < "$srcfile" > "$dstfile"; then
      echo "$dstfile"
    else
      echo "Failed to convert $srcfile to $dstfile"
      rm -f "$dstfile"
      exit 1
  	fi
  fi
done