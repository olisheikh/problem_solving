landStartTime = [5]
landDuration = [3]
waterStartTime = [1]
waterDuration = [10]

min_land_start_time = min(landStartTime)
min_water_start_time = min(waterStartTime)

if min_land_start_time < min_water_start_time:
    min_start = landDuration[landStartTime.index(min_land_start_time)] + min_land_start_time
    min_start += waterDuration[landStartTime.index(min_land_start_time)] 
else:
    min_start = waterDuration[waterStartTime.index(min_water_start_time)] + min_water_start_time
    min_start += landDuration[waterStartTime.index(min_water_start_time)]


print(min_start)