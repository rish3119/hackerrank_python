if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    # Remove duplicates and sort
unique_scores = sorted(set(arr))

# Runner-up is the second last element
print(unique_scores[-2])