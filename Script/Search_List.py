import csv

csv_school = "Data\school.csv"
csv_courses = r"Data\transferable_course.csv"
UC_COURSE_CODE = set()

def search_school(csv_school, search_query):
    results = []
    with open(csv_school, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)  # Assuming the first row contains headers
        for row in reader:
            for item in row:
                if search_query.lower() in item.lower() and 'NON_CC' in row[3]:
                    UC_COURSE_CODE.add(row[1])
                    results.append(row)
                    break  # Break the loop once a match is found
    return results

def print_courses_with_numbers(courses):
    """Print all unique courses with numbers
    """
    unique_courses = set(courses)
    for idx, course in enumerate(unique_courses, start=1):
        print(f"{idx}. {course}")


def extract_uc_course_names(search_results):
    """Extract unique course names from csv_courses based on search results
    """
    uc_course_names = set()
    with open(csv_courses, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            # 0 is id, 1 is name
            split_id = row[0].split('_')
            if split_id[0] in UC_COURSE_CODE:
                uc_course_names.add(row[0])
    return uc_course_names

def get_community_colleges_for_course(course_name):
    community_colleges = set()
    with open(csv_school, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if course_name in row[2]:
                community_colleges.add(row[2])
    return community_colleges


def main():
    search_query = input("Search Name of UC: ")
    search_results = search_school(csv_school, search_query)
    result_courses = sorted(extract_uc_course_names(search_results))
                    
    if search_results:
        print("Search results:")
        for result in search_results:
            print(result)
        print("Associated UC Courses:")
        print_courses_with_numbers(result_courses)
        
        # Allow user to select a course
        course_selection = input("Select a course by number: ")
        try:
            selected_course = result_courses[int(course_selection)]
            print(f"Selected course: {selected_course}")
            community_colleges = get_community_colleges_for_course(selected_course)
            print("Community colleges where you can take this course:")
            for college in community_colleges:
                print(college)
        except (IndexError, ValueError):
            print("Invalid selection.")
    else:
        print("No matching results found.")


if __name__ == "__main__":
    main()
