# Arithmetic Mean of grouped data

# lists of grouped data
marks = ['0-10', '10-20', '20-30', '30-40', '40-50', '50-60']
no_of_students = [5, 10, 25, 30, 20, 10]

i=0
sum_of_f = 0
sum_of_fm = 0
length = len(no_of_students)

while i < length:
    list1 = marks[i]
    list2 = no_of_students[i]
    line = list1.split('-')
    start_marks = int(line[0])
    end_marks = int(line[1])
    mid_point = (start_marks + end_marks)/2
    sum_of_f = sum_of_f + list2
    sum_of_fm = sum_of_fm + (list2 * mid_point)
    i += 1

grp_arithmetic_mean = sum_of_fm/sum_of_f

print("Arithmetic Mean of grouped data is:", grp_arithmetic_mean)


# Arithmetic Mean of ungrouped data

import statistics

# list of ungrouped data
list = [46, 25, 72, 18, 94, 51, 18]
ungrp_arithmetic_mean = statistics.mean(list)

print("Arithmetic Mean of ungrouped data,", list , "is :", ungrp_arithmetic_mean)



# Harmonic Mean of grouped data

interval = ['10-15', '15-20', '20-25', '25-30', '30-35']
frequency = [2, 13, 21, 14, 5]

i = 0
sum_of_f = 0
sum_of_fx = 0
length = len(interval)

while i < length:
    list1 = interval[i]
    list2 = frequency[i]
    line = list1.split('-')
    start_interval = int(line[0])
    end_interval = int(line[1])
    mid_point = (start_interval + end_interval) / 2
    sum_of_f = sum_of_f + list2
    sum_of_fx = sum_of_fx + (list2/mid_point)
    i+= 1

grp_harmonic_mean = sum_of_f/sum_of_fx

print("Harmonic Mean of grouped data is :", grp_harmonic_mean)


# Harmonic Mean of ungrouped data

import statistics

# list of ungrouped data
list = [46, 25, 72, 18, 94, 51, 18]
ungrp_harmonic_mean = statistics.harmonic_mean(list)

print("Harmonic Mean of ungrouped data,", list, "is :", ungrp_harmonic_mean)



# Geometric Mean of grouped data

import math

interval = ['60-80', '80-100', '100-120', '120-140', '140-160']
frequency = [22, 38, 45, 35, 20]

# interval = ['0-30', '30-50', '50-80', '80-100']
# frequency = [20, 30, 40, 10]

i = 0
sum_of_f = 0
sum_of_fLogx = 0
length = len(interval)

while i < length:
    list1 = interval[i]
    list2 = frequency[i]
    line = list1.split('-')
    start_interval = int(line[0])
    end_interval = int(line[1])
    mid_point = int((start_interval + end_interval) / 2)
    f_log_x = list2 * math.log10(mid_point)
    sum_of_f = sum_of_f + list2
    sum_of_fLogx = sum_of_fLogx + f_log_x
    antilog = 10 ** (sum_of_fLogx / sum_of_f)
    i += 1

grp_geometric_mean = antilog

print("Geometric Mean of grouped data is :", grp_geometric_mean)


# Geometric Mean of ungrouped data

import statistics

# list of ungrouped data
list = [46, 25, 72, 18, 94, 51, 8]
ungrp_geometric_mean = statistics.geometric_mean(list)

print("Geometric Mean of ungrouped data,", list, "is :", ungrp_geometric_mean)



# Mode of grouped data

import pandas as pd

#data_frame = pd.DataFrame.from_dict({'low_range':[10, 15, 20, 25, 30, 35], 'high_range':[15, 20, 25, 30, 35, 40], 'frequency':[11, 20, 35, 20, 8, 6]})
data_frame = pd.DataFrame.from_dict({'low_range': [0, 10, 20, 30, 40, 50, 60, 70], 'high_range': [10, 20, 30, 40, 50, 60, 70, 80], 'frequency': [40, 53, 58, 64, 72, 49, 36, 25]})

max_frequency = data_frame['frequency'].max()

index = data_frame['frequency'].idxmax()
L1 = data_frame['low_range'][index]
frequency_before = data_frame['frequency'][index - 1]
frequency_after = data_frame['frequency'][index + 1]
width = data_frame['high_range'][index + 1] - data_frame['low_range'][index + 1]
grp_mode = L1 + ((max_frequency - frequency_before)/((max_frequency - frequency_before) + (max_frequency - frequency_after))) * width

grp_mode = round(grp_mode)

print("Maximum frequency is :", max_frequency)
print("Index of maximum frequency is :", index)
print("Lower Boundary is :", L1)
print("Frequency before modal class is :", frequency_before)
print("Frequency after modal class is :", frequency_after)
print("Width is :", width)

print("Mode of grouped data is :", grp_mode)


# Mode of ungrouped data

import statistics

# list of ungrouped data
list = [46, 25, 72, 18, 94, 51, 18]
ungrp_mode = statistics.mode(list)

print("Mode of ungrouped data,", list, "is :", ungrp_mode)



# Median of grouped data

import pandas as pd

data_frame = pd.DataFrame.from_dict({'low_range':[10, 15, 20, 25, 30, 35], 'high_range':[15, 20, 25, 30, 35, 40], 'frequency':[11, 20, 35, 20, 8, 6]})

N = data_frame['frequency'].sum()
index = abs(data_frame['frequency'].cumsum() - N/2).idxmin()
L1 = data_frame['low_range'][index + 1]
cf_before = data_frame['frequency'].cumsum()[index]
freq_medain = data_frame['frequency'][index + 1]
width = data_frame['high_range'][index + 1] - data_frame['low_range'][index + 1]

grp_median = int(L1 + (N/2 - cf_before ) / freq_medain * width)

print("Median of grouped data is :", grp_median)


# Median of ungrouped data

# list of ungrouped data
list = [13, 25, 72, 18, 94, 46, 51]
# list = [17, 20, 43, 45, 50, 53, 55, 59, 62]

list.sort()
list_length = len(list)

if list_length % 2 == 0:
    index1 = int(list_length/2)
    value1 = list[index1 - 1]
    index2 = int((list_length/2) + 1)
    value2 = list[index2 - 1]
    ungrp_median = int((value1 + value2)/2)
else:
    index1 = int((list_length + 1)/2)
    ungrp_median =  list[index1 - 1]

print("Median of ungrouped data,", list, "is :", ungrp_median)
