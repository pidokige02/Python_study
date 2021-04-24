#!/bin/bash
echo "$0 $@ $1 $#"

First=$1

say_hello() {
	echo "Hello $0 $First by $2!! ($#)"
}

say_hello "Jade" "Jeon"

