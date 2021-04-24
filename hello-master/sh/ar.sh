#!/bin/bash

arr=("aaa" "bbb" "ccc" 123)

echo $arr
echo ${arr}
arr[4]="444 $(( ${arr[3]} ** 3 ))"

len=${#arr[@]}
last=$(($len - 1))
echo "len=$len , $last" 

echo "4=> ${arr[4]} : ${arr[$last]}"

echo "---------------------------"
for i in ${arr[@]}; do
    echo "===> $i"
done
