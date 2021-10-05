#!/bin/bash
while read line
do
    eval echo "$line"
done < "./inventory.txt"
