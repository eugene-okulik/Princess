temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23]

high_temperatures = filter(lambda temp: temp > 28, temperatures)
high_temperatures = list(high_temperatures)
min_temp = min(high_temperatures)
max_temp = max(high_temperatures)
average_temp = round(sum(high_temperatures)/len(high_temperatures), 2)

print(max_temp)
print(min_temp)
print(average_temp)
