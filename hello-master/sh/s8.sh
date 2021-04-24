#!/bin/bash

arr=("aaa" "bbb" "ccc" 123)

echo "arr=$arr"
echo "arr=${arr[1]}"
echo ${arr[1]}

len=${#arr[@]}
arr[$len]="44444"

arr[6]=66
arr[8]=88
arr[8]=888

echo "#### ${#arr} : ${#arr[@]}"

echo ${arr[@]}

echo "-----------------"
for a in ${arr[@]}
do
    echo $a
done
