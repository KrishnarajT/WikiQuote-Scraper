#!/bin/bash

# Get the current directory
current_dir=$(pwd)

# Loop through all the files in the current directory
for file in *; do

  # Run the command "strfile" on the file
  strfile "$file"

done
