#!/bin/bash

PRE_IFS=$IFS

IFS="
"

cd /home/dooo

FileName="bin_files.txt"
touch $FileName

echo " -------------------------------------------- "
TOT=0
for i in `ls -al /bin`; do
    #arr=(`echo $i | awk '{print $5}'` `echo $i | awk '{print $9}'`)
    tmp=`echo $i | awk '{print $5 " " $9}'`
    echo "tmp=$tmp"
    arr=()
    IFS=" "
    for t in $tmp; do
        arr[${#arr[@]}]=$t
    done
    IFS="
"
    
    echo "0=${arr[0]}, 1=${arr[1]}"

    if [ "${arr[1]}" == "." ]; then
    #if [ "$F" == "." ] || [ "$F" == ".." ] || [ "$F" == "" ]; then
        continue
    fi

    #TOT=`expr $TOT + $S`

    echo "${arr[@]}"
done

echo "Total Size is $TOT"

IFS=$PRE_IFS
