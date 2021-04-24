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
    S=`echo $i | awk '{print $5}'`
    F=`echo $i | awk '{print $9}'`

    if [ "$F" == "." ] || [ "$F" == ".." ] || [ "$F" == "" ]; then
        continue
    fi

    #TOT=$(( $TOT + $S ))
    TOT=`expr $TOT + $S`

    echo "$S $F" >> $FileName
done

echo "Total Size is $TOT"

IFS=$PRE_IFS
