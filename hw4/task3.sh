#!/bin/bash

gawk -F, '
    BEGIN { 
        sum = 0; count = 0; filtered_records = 0;
    }
    {gsub(/^ +| +$/, "", $12);}
    NR == 1 { 
        # Skip the header row
        next 
    } 
    $3 == 2 && $13 == "S" { 
        # Replace male/female with M/F
        if ($6 == "male") $6 = "M"; 
        else if ($6 == "female") $6 = "F"; 
        filtered_records += 1;
        # Add to sum if age exists
        if ($7 != "") { 
            sum += $7; count++; 
        }

        # Print the filtered rows
        print "Filtered: " $0
    }
    END { 
        # Calculate and print average age
        if (count > 0) {
            print "\nAverage Age:", sum / count 
            print "\n Total Records: ", filtered_records
        } else {
            print "\nAverage Age: N/A" 
        }
    }
' dataset/titanic.csv
