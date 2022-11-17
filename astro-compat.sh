#!/bin/bash

SIGNS=(aries taurus gemini cancer leo virgo libra scorpio sagittarius capricorn aquarius pisces all)


if [[ ! " ${SIGNS[*]}"  =~ " ${1} " ]]; then
  echo 'the only arguement must be one of the following:'
  echo "${SIGNS[*]}"
  exit 1
fi


#python astro-compat.py | egrep '^ |^-'; python astro-compat.py | grep "$1"$ | sort -k 14 -n
python astro-compat.py | grep -E '^ |^-'; python astro-compat.py | grep "$1"$ | sort -k 14 -n
