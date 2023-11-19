tsv_path="tsv/"

# Merge all .tsv files into merged_courses.tsv
# Create a new merged file or clear it if it already exists
> merged_courses.tsv

# Concatenate all .tsv files into one, each file content on a new line
for file in "$tsv_path"/*.tsv; do
    cat "$file" >> merged_courses.tsv
    # Ensure that each entry ends with a newline
    echo "" >> merged_courses.tsv
done

file="merged_courses.tsv"


#which country offers the most Master's Degrees?
most_country=$(cut -f11 "$file" | sort | uniq -c | sort -nr | head -n 1)
echo "Country with the most Master's Degrees: $most_country"

#which city offers the most Master's Degrees?
most_city=$(cut -f10 "$file" | sort | uniq -c | sort -nr | head -n 1)
echo "City with the most Master's Degrees: $most_city"

#how many colleges offer Part-Time education?
colleges_part_time=$(awk -F"\t" '$4 == "Part time" {print $2}' "$file" | sort -u | wc -l)
echo "Number of colleges offering Part-Time education: $colleges_part_time"

#percentage of courses in Engineering
total_courses=$(wc -l < "$file")
engineering_courses=$(grep -i 'Engineer' "$file" | wc -l)
percentage_engineering=$((engineering_courses*100/total_courses))
echo "Percentage of Engineering courses: $percentage_engineering%"

exit 0
