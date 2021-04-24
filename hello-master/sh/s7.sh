#!/bin/bash

for i in {2..9}
do
    for j in {1..9}
    do
        echo "$i * $j = $(( $i * $j ))"
    done
    echo "--------------------------------"
done
