#!/bin/bash
grep -rl "sample" dataset/dataset1/ | xargs -I {} bash -c 'count=$(grep -o "CSC510" {} | wc -l); [ $count -ge 3 ] && echo "$count $(wc -c < {}) {}"' | sort -rnk1,1 -rnk2,2 | cut -d' ' -f3 | sed 's/file_/filtered_/'
