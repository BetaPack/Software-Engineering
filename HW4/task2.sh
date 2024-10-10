# List files in the dataset1 directory
cd dataset
echo "Listing files in dataset1:"
ls dataset1

# Count the number of files in the dataset1 directory
echo "Counting the number of files:"
ls dataset1 | wc -l

# Filter files containing the word "CSC510" exactly 3 times
echo "Filtering files that contain 'CSC510' exactly 3 times:"
grep -c "CSC510" dataset1/file* | grep -E ":3$" | cut -d: -f1

# Sort files based on size
echo "Sorting files by size:"
grep -c "CSC510" dataset1/file* | grep -E ":3$" | cut -d: -f1 | xargs ls -l | sort -k5,5nr

# Rename files based on the pattern
echo "Renaming files:"
grep -c "CSC510" dataset1/file* | grep -E ":3$" | cut -d: -f1 | xargs ls -l | sort -k5,5nr | sed 's/file_/the_name_/' | gawk '{ print $9 "_filtered" }'
