if __name__ == '__main__':
    students = []  # Step 1: storage
    
    for _ in range(int(input())):
        name = input().strip()
        score = float(input())
        students.append([name, score])  # store as nested list
    
    # Step 2: find second lowest grade
    grades = sorted(set([score for name, score in students]))
    second_lowest = grades[1]
    
    # Step 3: collect names with second lowest grade
    names = [name for name, score in students if score == second_lowest]
    
    # Step 4: print alphabetically
    for name in sorted(names):
        print(name)