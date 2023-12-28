#!/bin/bash

target_dir="./data/video_frames"

for file in "$target_dir"/*/*.jpg; do

    dir_path=$(dirname "$file")
    file_name=$(basename "$file")

    new_file_name=$(echo "$file_name" | sed 's/0000//')

    new_file_path="$dir_path/$new_file_name"

    mv "$file" "$new_file_path"

    echo "Renamed: $file to $new_file_path"
done
