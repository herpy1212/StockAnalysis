#!/bin/sh

for i in $(seq 20200401 20200430)
do
	curl -x http://1.255.48.197:8080/ 'https://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date='$i'&type=02' -o $i.csv
	echo $?
	sleep 5
done

#curl -x http://1.255.48.197:8080/ 'https://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date=20200710&type=02' -o 20200710.csv

