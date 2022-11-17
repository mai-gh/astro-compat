#!/bin/bash


ALL_SIGNS="aries taurus gemini cancer leo virgo libra scorpio sagittarius capricorn aquarius pisces"


for i in $ALL_SIGNS; do
    for j in $ALL_SIGNS; do
        URL="https://www.astrology-zodiac-signs.com/compatibility/$i-$j/"
        OUTFILE="$i-$j.html"
        wget "$URL" -O "$OUTFILE"
    done
done
