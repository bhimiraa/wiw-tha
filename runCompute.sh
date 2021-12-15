#!/bin/sh

if [ "$#" -ne 3 ]; then
  echo "Wrong usage"
  echo "Usage: ./runCompute.sh <path to directory store the result> <url of source path> <debug flag value>"
  exit 1
fi

result_path=$1
source_root_url=$2
debug_flag=$3

if [ $debug_flag != "True" ]; then
    echo "Debug value is 'False' by default. To enable debug set it to 'True'"
fi


start_process () {
     python3 computeTimeTakenAtEachPath.py  $1 $2 $3
 }

start_process $result_path $source_root_url $debug_flag

