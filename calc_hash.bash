#!/bin/bash

echo 'Enter the absolute path of the directory:'
read search_dir

for entry in $search_dir/*
do
        md5=($(md5sum $entry))
        echo "$entry" $'\t' "$md5" >> result.txt
done