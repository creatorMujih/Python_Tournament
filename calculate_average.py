def calculate_average(scores):
    if not scores:
        return 0

    return sum(scores) / len(scores)


print(calculate_average([80, 90, 70]))   
print(calculate_average([50, 60]))    
print(calculate_average([]))          
print(calculate_average([100]))       