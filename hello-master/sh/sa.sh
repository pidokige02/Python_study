#!/bin/bash

echo "IFS=${IFS}."

PRE_IFS=$IFS
IFS="
"

SUM=0
echo "+++++++++++++++++++++++++++++++++++++++++++++++"
for i in `ls -al /bin`; do
    #echo "i= `echo $i | awk '{print $9}'`"
    S=`echo $i | awk '{print $5}'`
    F=`echo $i | awk '{print $9}'`

    #echo "s=$S, f=$F"

    if [ "$F" == "." ] || [ "$F" == ".." ]; then
        continue
    fi

    #SUM=$(( $SUM + $S ))
    SUM=`expr $SUM + $S`

    echo "filename=$F  SUM=$SUM"
done

IFS=$PRE_IFS
