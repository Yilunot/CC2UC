import csv

def search_school(csv_file, search_query):
    results = []
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)  # Assuming the first row contains headers
        for row in reader:
            for item in row:
                if search_query.lower() in item.lower():
                    results.append(row)
                    break  # Break the loop once a match is found
    return results

def main():
    csv_file = "Data/school.csv"
    search_query = input("Enter the search query: ")
    search_results = search_school(csv_file, search_query)
    
    if search_results:
        print("Search results:")
        for result in search_results:
            print(result)
    else:
        print("No matching results found.")

if __name__ == "__main__":
    main()