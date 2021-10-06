#!/bin/bash
$VM_PASSWORD

while read line
do
    eval echo "$line"
done < "./inventory.txt"

while read line2
do
    eval echo "$line2"
done < "./playbook.yml"
