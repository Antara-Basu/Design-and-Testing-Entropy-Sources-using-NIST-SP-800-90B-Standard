# -*- coding: utf-8 -*-
"""11_codes_of_iid_determination.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1GZesQL3Vn9fcHERyQL0z7pFkXcIkFnO7

5. Testing the IID Assumption

This section includes statistical tests that are designed to find evidence that the samples are not IID and if no evidence is found that the samples are non-IID, then it is assumed that the samples are IID . These tests take the sequence S = (s1,…,sL), where si ϵ A = {x1,…,xk}, as input, and test the hypothesis that the values in S are IID. If the hypothesis is rejected by any of the tests, the values in S are assumed to be non-IID.

Statistical tests based on permutation testing (also known as shuffling tests) are given in Section 5.1.

The tests are applicable to both binary and non-binary data, but for some of the tests, the number of distinct sample values, denoted k (the size of the set A), significantly affects the distribution of the test statistics, and thus the type I error. For such tests, one of the following conversions is applied to the input data, when the input is binary, i.e., k = 2.

CONVERSION 1
"""

def bin_count(lst):

  """
  This function partitions the input binary sequence into 8-bit non-overblocking blocks and counts the number of ones in each block.
  @input: s:string of binary integers.
  @output:result :TEST STATISTIC.
  For eg:
  input = a = [1,0,1,1,0,1,1,1,0,0,1,1,1,0,1,1,0,0,1,1]
  lst of 8-blocks = [[1,0,1,1,0,1,1,1],[0,0,1,1,1,0,1,1],[0,0,1,1,0,0,0,0]]
  output(no: of ones in each 8-bit non-overblocking blocks) = [6,5,2]

  """

  groups = [lst[i:i + 8] for i in range(0, len(lst), 8)]
  result = []
  for j in range(len(groups)):
      res = groups[j].count(1)
      result.append(res)
  return result


lst = [1,0,0,0,1,1,1,0,1,1,0,1,1,0,1,1,0,0,1,1]
no_of_ones = bin_count(lst)
print(no_of_ones)

l1 = [1,0,0,0,1,1,1,0,1,1,0,1,1,0,1,1,0,0,1,1,1,1,1,1,0,0,0,1,0,1,0,0,1,1,0,0,0,0,0,1,1,1,1,0,1,0,0,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,1,0,1,0,1,1,1,1,0,0,1,0,1,0,1,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,1,0,1,0,1,1,0,0,0,1,1,]
no_of_ones1 = bin_count(l1)
print(no_of_ones1)

cubes = [x**3 for x in range(5)]
print(cubes)

"""CONVERSION 2"""

def calculate_decimal_value(bin):

  """
  This function partitions the input sequence into 8-bit non-overblocking blocks and calculates the integer value of each block.
  @input: s:string of binary integers.
  @output:result :TEST STATISTIC.
  For eg:
  input = s = [1,0,1,1,0,1,1,1,0,0,1,1,1,0,1,1,0,0,1,1]
  lst of 8-blocks = [[1,0,1,1,0,1,1,1],[0,0,1,1,1,0,1,1],[0,0,1,1,0,0,0,0]]
  now integer value of each 8-bit block will be calculated and will be appended into a list.
  output lst = [183, 59, 48]

  """

  bin = bin[::-1]
  decimal = 0
  for power in range(len(bin)):
      decimal += bin[power] * (2**power)
  return decimal

def int_con(bin):
  grps = [bin[i:i+8] for i in range(0, len(bin), 8)]
  result = []
  ans = 0
  for grp in grps:
      if(len(grp) == 8):
          ans = calculate_decimal_value(grp)
      else:
          while(len(grp) < 8):
              grp.append(0)
          ans = calculate_decimal_value(grp)
      result.append(ans)
  return result


bin = [1,0,0,0,1,1,1,0,1,1,0,1,1,0,1,1,0,0,1,1]
int_convert = int_con(bin)
print(int_convert)

lst1 = [1,0,0,0,1,1,1,0,1,1,0,1,1,0,1,1,0,0,1,1,1,1,1,1,0,0,0,1,0,1,0,0,1,1,0,0,0,0,0,1,1,1,1,0,1,0,0,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,1,0,1,0,1,1,1,1,0,0,1,0,1,0,1,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,1,0,1,0,1,1,0,0,0,1,1,]
int_convert = int_con(lst1)
print(int_convert)

print(2**3)

l1 = [1,0,1,1,0,1,1,1,0,0,1,1,1,0,1,1,0,0,1,1]
int_convert = int_con(l1)
print(int_convert)

"""5.1 Permutation Testing

5.1.1 Excursion Test Statistic
"""

def excursion_test_statistic(l):

  """
  This function measures the deviation of samples values from its average values at each point of dataset.
  @input: s:string of integers.
  @output: :ans TEST STATISTIC.
  for eg:
  input = l = [1,0,1,1], add = avg = ans = 0
  Avg = 0.75, add = 0 + l[0] = 1,  ans = max(0, abs(1-1*0.75) = max(0,0.25) = 0.25.
  Likewise till the end of lst add and ans will be calculated, and atlast value of ans will be our test statistic.
  output = 0.5

  """

  n = len(l)
  ans = 0
  add = 0
  avg = sum(l)/len(l)
  for i in range(n):
      add += l[i]
      ans = max(ans, abs(add - (i+1)*avg))
  return ans, avg

l = [1,1,0,1,1,0]
excursion_teststat = excursion_test_statistic(l)
print(excursion_teststat)

l = [1,0,1,0,1,1,1,0]
excursion_teststat =  excursion_test_statistic(l)
print(excursion_teststat)

l = [0,0,1,0,1,1,0]
excursion_teststat =  excursion_test_statistic(l)
print(excursion_teststat)

lst2 = [1,0,0,0,1,1,1,0,1,1,0,1,1,0,1,0,0,1,1,1,1,1,1,0,0,0,1,0,1,0,0,1,1,0,0,0,0,0,1,1,1,1,0,1,0,0,1,0,0,0,1,1,1,1,1,1,1,1,0,0,0,1,1,1,0,1,0,1,0,1,0,0,1,1,1,1,1,0,0,0,0,1,1,0,0,0,0,0,0,1,1,1,1,1,0,1,0,0,11]
excursion_teststat =  excursion_test_statistic(lst2)
print(excursion_teststat)

s = (2,15,4,10,9)
test_stat = excursion_test_statistic(s)
print(test_stat)

"""5.1.2 Number of Directional Runs"""

def no_of_directional_runs(var):

  """
  This function  determines the no: of runs constructed using the relations between consecutive samples of string s.
  @input: s:string of integers.
  @output: s_dash and runs: Constructs a new sequence of 1s and -1s and determines its no: of runs.
  for eg: l = [1,1,1,0,0,1,1,0,0,1,0,1,1,1,0,0,1,1,1,1,0,0,1,1]
  output of 1st functn (bin_count)= a = [5,4,6]
  n = 3, a_dash = []
  a[o]>a[1] , so a_dash = [-1] then a[1]<a[2] , so a_dash = [-1,1]. Likewise a_dash lst will be created, a_dash = [-1,1]
  cur = a_dash[0] = -1. ans = 1.
  for -1 in a_dash if -1!=-1 which is false, hence increase x.
  Next 1!=-1 then cur = 1 and ans = 2 .output = ans = 2

  """

  n = len(var)
  var_dash = []
  for i in range(n-1):
    if(var[i] > var[i+1]):
          var_dash.append(-1)
    else:
          var_dash.append(1)
  print(var_dash)

  cur = var_dash[0]
  ans = 1
  for x in var_dash:
      if(x!=cur):
          cur = x
          ans += 1
  return ans

lst = [1,0,0,0,1,1,1,0,1,1,0,1,1,0,1,1,0,0,1,1,1,1,1,1,0,0,0,1,0,1,0,0,1,1,0,0,0,0,0,1,1,1,1,0,1,0,0,1,0,0,0,1,1,1,1,1,1,1,1,0,0,0,1,1,1,0,1,0,1,0,1,0,0,1,1,1,1,1,0,0,0,0,1,1,0,0,0,0,0,0,1,1,1,1,1,0,1,0,0,1]
var = bin_count(lst)
print(var)
dir_runs = no_of_directional_runs(var)
print(dir_runs)

lst3 = [1,0,0,0,1,1,1,0,1,1,0,1,1,0,1,1,0,0,1,1,1,1,1,1,0,0,0,1,0,1,0,0,1,1,0,0,0,0,0,1,1,1,1,0,1,0,0,1,0,0,0,1,1,1,1,1,1,1,1,0,0,0,1,1,1,0,1,0,1,0,1,0,0,1,1,1,1,1,0,0,0,0,1,1,0,0,0,0,0,0,1,1,1,1,1,0,1,0,0,1]
print(len(lst3))

lst4 = [1,1,1,0,1,0,1,0,1,0,0,1,1,1,1,1,0,0,0,0,1,1,0,0,0,0,0,0,1,1,1,1,1,0,1,0,0,1]
no_of_ones = bin_count(lst4)
print(no_of_ones)
dir_runs = no_of_directional_runs(no_of_ones)
print(dir_runs)

lst5 = [1,0,0,0,1,1,1,0,1,1,0,1,1,0,1,1,0,0,1,1]
no_of_ones = bin_count(lst5)
print(no_of_ones)
dir_runs = no_of_directional_runs(no_of_ones)
print(dir_runs)

s = [2,2,2,5,7,7,9,3,1,4,4]
dir_runs = no_of_directional_runs(s)
print(dir_runs)

"""5.1.3 Length of Directional Runs"""

def length_of_directional_runs(var):

  """
  This function  determines the length of the longest run constructed using the relations between consecutive samples of string s.
  @input: s:string of integers.
  @output: s_dash and r: Constructs a new sequence of 1s and -1s and determines the length of the longest of those runs.
  for eg: l = [1,1,1,0,0,1,1,0,0,1,0,1,1,1,0,0,1,1,1,1,0,0,1,1,1,1,1,1,0,0,1,1]
  output of 1st functn (bin_count) a = [5,4,6,6]
  n = 4, a_dash = []
  a[o]>a[1] , so a_dash = [-1] then a[1]<a[2] ,.... so a_dash = [-1,1,1]
  t = 3 if t==1 return 1 , cur_count = max_count = 1
  a_dash[1]!=a_dash[0] i.e, 1!=-1, which is true, so cur_count = 1, max_count = 1
  a_dash[2]!=a_dash[1] i.e, 1!=1, which is false, so cur = 2 ,output = max_count = 2, which is the test_statistic.

  """

  n = len(var)
  var_dash = []
  for i in range(n-1):
    if(var[i] > var[i+1]):
          var_dash.append(-1)
    else:
          var_dash.append(1)
  print(var_dash)

  t = len(var_dash)
  if(t == 1):
     return 1
  cur_count = 1
  max_count = 1
  for i in range(1,t):
      max_count = max(max_count, cur_count)
      if(var_dash[i]!=var_dash[i-1]):
         cur_count = 1
      else:
         cur_count += 1
  max_count = max(max_count, cur_count)
  return max_count

h = [1,1,1,0,0,1,1,0,0,1,0,1,0,1,1,1]
var = bin_count(h)
print(var)
len_runs = length_of_directional_runs(var)
print(len_runs)

h = [1,0,0,0,1,1,1,0,1,1,0,1,1,0,1,1,0,0,1,1,1,1,1,1,0,0,0,1,0,1,0,0,1,1,0,0,0,0,0,1,1,1,1,0,1,0,0,1,0,0,0,1,1,1,1,1,1,1,1,0,0,0,1,1,1,0,1,0,1,0,1,0,0,1,1,1,1,1,0,0,0,0,1,1,0,0,0,0,0,0,1,1,1,1,1,0,1,0,0,1]
var1 = bin_count(h)
print(var1)
len_runs = length_of_directional_runs(var1)
print(len_runs)

s = [2,2,2,5,7,7,9,3,1,4,4]
r = length_of_directional_runs(s)
print(r)

"""5.1.4 Number of Increases and Decreases"""

def no_of_increases_and_decreases(var):

  """
  This function  determines the maximum number of increases or decreases between consecutive sample values of a given string s.
  @input: s:string of integers.
  @output: s_dash and d: Constructs a new sequence consisting of 1s and -1s and determines the max of +1s and -1s of new sequence.
  for eg: l = [1,1,1,0,0,1,1,0,0,1,0,1,1,1,0,0,1,1,1,0,0,0,1,0,1,1,1,0,0,1,1,0]
  output of 1st functn (bin_count) a = [5, 4, 4, 5]
  n = 4, a_dash = []
  a[o]>a[1] , so a_dash = [-1] then a[1]=a[2] ,......
  Likewise a_dash lst will be created. a_dash = [-1,1,1]
  count1 = 0 = count_minus_one,  if -1 == 1  which is false so count_minus_one = 1
  if 1 == 1 then count1 == 1 , if 1 == 1 which is true so count1 = 2
  output : count1 = 2, count_minus_one = 1,  max(count1, count-minus_one) = 2.

  """
  n = len(var)
  var_dash = []
  for i  in range(n-1):
      if(var[i] > var[i+1]):
          var_dash.append(-1)
      else:
          var_dash.append(1)
  print(var_dash)

  count1 = 0
  count_minus_one = 0
  for x in var_dash:
    if x == 1:
      count1+=1
    elif x == -1:
      count_minus_one+=1
  return count1, count_minus_one
  return max(count1, count-minus_one)

bin = [1,1,0,1,0,0,1,1,0,0,1,1,1,0,1,0,1,1,1,0,0,1,0,1,0]
var = bin_count(bin)
print(var)
count1, count_minus_one = no_of_increases_and_decreases(var)
print(count1)
print(count_minus_one)
d = max(count1, count_minus_one)
print(d)

l = [1,1,1,0,0,1,1,0,0,1,0,1,1,1,0,0,1,1,1,0,0,0,1,0,1,1,1,0,0,1,1,0]
var = bin_count(l)
print(var)
count1, count_minus_one = no_of_increases_and_decreases(var)
print(count1)
print(count_minus_one)
d = max(count1, count_minus_one)
print(d)

s = [2,2,2,5,7,7,9,3,1,4,4]
count1, count_minus_one = no_of_increases_and_decreases(s)
print(count1)
print(count_minus_one)
d = max(count1, count_minus_one)
print(d)

import statistics
s = [5,15,9,1,13,9,4]
m = statistics.median(s)
print(m)

"""5.1.5 Number of Runs Based on the Median"""

import statistics
def no_of_runs_based_on_the_median(l):

  """
  This function  determines the no: of runs that are constructed with respect to the median of the given string s.
  @input: s:string of integers.
  @output: m, s_dash and runs: Median of input string s, Constructs a new sequence of 1s and -1s and determines its number of runs.
  For eg: input: l=[1,0,1,1,0,0,1]
  m = 1, n = 7, l_dash = []
  for 1 in l, if(1<1) which is false, l_dash = [1]
  for 0 in l, if(0<1), which is true, l_dash = [-1]
  ............
  l_dash = [1, -1, 1, 1, -1, -1, 1]
  cur = l_dash[0] = 1, runs = 1,
  for 1 in l_dash, if(1!=1), which is false
  for -1 in l_dash, if(-1!=1), which is true, cur = -1, runs = 2
  likewise till the end of the lst, runs will be calculated..................
  output = runs = 5

  """
  m = statistics.median(l)
  n = len(l)
  l_dash = []
  for x in l:
      if(x < m):
          l_dash.append(-1)
      else:
          l_dash.append(1)
  print(l_dash)

  cur = l_dash[0]
  runs = 1
  for x in l_dash:
      if(x!=cur):
          cur = x
          runs += 1
  return runs

l = [1,1,0,1,0,0,1,1,0,0,1,1,1,0,1,0,1,1,1,0,0,1,0,1,0]
m = statistics.median(l)
print(m)
c = no_of_runs_based_on_the_median(l)
print(c)

l=[1,0,1,1,0,0,1]
m = statistics.median(l)
print(m)
c = no_of_runs_based_on_the_median(l)
print(c)

s = [5,15,12,1,13,9,4]
m = statistics.median(s)
print(m)
c = no_of_runs_based_on_the_median(l)
print(c)

"""5.1.6 Length of Runs Based on Median"""

import statistics
def length_of_runs_based_on_median(l):

  """
  This function  determines the length of the longest run constructed with respect to the median of the given string s.
  @input: s:string of integers.
  @output: m, s_dash and max_count:Median of input string s, Constructs a new sequence of 1s and -1s and determines length of the longest run.
  For eg: input: l=[1,0,1,1,0,0,1]
  m = 1, n = 7, l_dash = []
  for 1 in l, if(1<1) which is false, l_dash = [1]
  for 0 in l, if(0<1), which is true, l_dash = [-1]
  ............
  l_dash = [1, -1, 1, 1, -1, -1, 1]
  a = 7, if a == 1 return 1 , cur_count = max_count = 1
  l_dash[1]!=l_dash[0] so cur_count = 1, max_count = 1
  l_dash[2]!=l_dash[1] which is true so cur = 1 ,max_count = 1,
  .............
  output = max_count = 2, which is the test_statistic.

  """
  m = statistics.median(l)
  n = len(l)
  l_dash = []
  for x in l:
      if(x < m):
          l_dash.append(-1)
      else:
          l_dash.append(1)
  print(l_dash)

  a = len(l_dash)
  if(a == 1):
      return 1
  cur_count = 1
  max_count = 1
  for i in range(1,a):
      max_count = max(max_count, cur_count)
      if(l_dash[i]!=l_dash[i-1]):
         cur_count = 1
      else:
         cur_count += 1
  max_count = max(max_count, cur_count)
  return max_count

l = [1,1,0,1,0,0,1,1,0,0,1,1,1,0,1,0,1,1,1,0,0,1,0,1,0]
m = statistics.median(l)
print(m)
len_of_runs_based_on_median = length_of_runs_based_on_median(l)
print(len_of_runs_based_on_median)

l=[1,0,1,1,0,0,1]
m = statistics.median(l)
print(m)
len_of_runs_based_on_median = length_of_runs_based_on_median(l)
print(len_of_runs_based_on_median)

s = [5,15,12,1,13,9,4]
m = statistics.median(s)
print(m)
y = length_of_runs_based_on_median(s)
print(y)

"""5.1.7 Average Collision Test Statistic"""

def average_collision_test_statistic(deci):

  """

  This function  counts the no: of successive samples in a given string s, until a duplicate is found.
  @input: s : string of integers.
  @output: ans, avg : list of the no: of samples observed to find 2 occurrences of the same value in the input sequence, average of collision of test statistic
  input = l = [1,1,1,0,0,0,1,0,1,1,1,0,0,0,0,1,1,1,1,0,0,0,1,0]
  output of first function(int_con)= a = [226, 225, 226]
  ans = [] = temp
  for 226 in a, if 226 in temp, which is false, append 226 in temp, print it.
  for 225 in a, if 225 in temp, which is false, append 225 in temp, print it.
  for 226 in a, if 226 in temp, which is true, so ans = [3], empty temp and print it.
  average will be calculated.
  output = ans, avg = ([3], 3.0)

  """
  ans = []
  temp = []
  for x in deci:
      if x in temp:
          ans.append(len(temp) + 1)
          temp = []
          print(temp)

      else:
          temp.append(x)
          print(temp)
  avg =  sum(ans)/len(ans)

  return ans, avg


l = [1,1,0,1,0,0,1,1,0,0,1,1,1,0,1,0,1,1,0,1,0,0,1,1,1,1,1,0,0,1,0,1,0,0,1,1,1,0,1,0,0,0,1,1,1,0,1,0]
deci = int_con(l)
print(deci)
avg_col = average_collision_test_statistic(deci)
print(avg_col)

h = [1,1,1,0,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,0,1,1,1,1,0,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,0,1]
deci = int_con(h)
print(deci)
avg_col = average_collision_test_statistic(deci)
print(avg_col)

s = [2,1,1,2,0,1,0,1,1,2]
avg_col = average_collision_test_statistic(s)
print(avg_col)

"""5.1.8 Maximum Collision Test Statistic"""

def maximum_collision_test_statistic(h):

  """
  This function  counts the maximum of no: of successive samples in a given string s, until a duplicate is found.
  @input: s:string of integers.
  @output: ans , max_col:  list of the no:of samples observed to find 2 occurrences of the same value in the input sequence ,maximum of the collision of test statistic
  input = l = [1,1,1,0,0,0,1,0,1,1,1,0,0,0,0,1,1,1,1,0,0,0,1,0,1,1,0,0,0,0,1,1,1,1,0,0,0,0,1,1]
  output of first function(int_con)= a = [226, 225, 226, 195, 195]
  for 226 in a, if 226 in temp, which is false, append 226 in temp, print it.
  .
  .
  for 195 in a, if 195 in temp, which is true, so ans = [3,2], empty temp and print it.
  output = ans, max = ([3,2], 3)

  """

  ans = []
  temp = []
  for x in h:
    print(temp)
    if x in temp:
        ans.append(len(temp) + 1)
        temp = []
    else:
        temp.append(x)
  test_statistic1 = max(ans)
  return ans, test_statistic1

h = [1,0,1,0,0,0,1,1,0,1,1,1,1,0,0,1,1,0,1,0,0,0,1,1,1,0,1,0,0,0,1,1,1,0,1,0,0,0,1,1]
deci = int_con(h)
print(deci)
max_col = maximum_collision_test_statistic(deci)
print(max_col)

l = [1,1,1,0,0,0,1,0,1,1,1,0,0,0,0,1,1,1,1,0,0,0,1,0,1,1,0,0,0,0,1,1,1,1,0,0,0,0,1,1]
deci = int_con(l)
print(deci)
max_col = maximum_collision_test_statistic(deci)
print(max_col)

s = [2,1,1,2,0,1,0,1,1,2]
max_col = maximum_collision_test_statistic(s)
print(max_col)

"""5.1.9 Periodicity Test Statistic"""

def periodicity_test_statistic(var):

  """
  This function  determines the number of periodic structures in the input string s.
  @input: s:string of integers.
  @output: T:Test statistic of the input string s.
  For eg: input = l = [1,0,1,0,1,0,1,1,1,0,0,1,1,0,0,1]
  output from second function(bin_count): [5, 4, 5]
  T = 0, p = 2, L = 3, for 5 in range(1)
  var[0] == var[2] i.e , 5 == 5  ,
  output =  T = 1

  """

  T = 0
  p = 2
  L = len(var)
  for i in range(L-p):
    if var[i] == var[i+p]:
      T+=1
  return T

bin = [1,0,1,1,1,0,1,0,0,1,0,1,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,0,1,0,0,1,0,1,0,1,0,1]
var = bin_count(bin)
print(var)
teststatistic = periodicity_test_statistic(var)
print(teststatistic)

lst = [1,0,0,0,1,1,1,0,1,1,0,1,1,0,1,1,0,0,1,1,1,1,1,1,0,0,0,1,0,1,0,0,1,1,0,0,0,0,0,1,1,1,1,0,1,0,0,1,0,0,0,1,1,1,1,1,1,1,1,0,0,0,1,1,1,0,1,0,1,0,1,0,0,1,1,1,1,1,0,0,0,0,1,1,0,0,0,0,0,0,1,1,1,1,1,0,1,0,0,1]
var = bin_count(lst)
print(var)
teststatistic = periodicity_test_statistic(var)
print(teststatistic)

lst = [1,0,0,0,1,1,1,0,1,1,0,0,1,0,1,1,0,0,1,1,0,1,0,1,1,1,0,0,1,0,1,1,1]
variable = bin_count(lst)
print(variable)
teststatistic = periodicity_test_statistic(variable)
print(teststatistic)

s = (2,1,2,1,0,1,0,1,1,2)
teststatistic = periodicity_test_statistic(s)
print(teststatistic)

"""5.1.10 Covariance Test Statistic"""

def covariance_test_statistic(num):

  """
  This function measures the strength of lagged correlation of string s.
  @input: s:string of integers.
  @output: T:Test statistic of the input string s.
  For eg: input = [1,1,0,0,1,0,1,0,1,1,1,0,0,1,1,0,0,0,1,1,0,1,0,1]
  output from second function(bin_count): num = [4,5,4]
  T = 0, p = 2, L = 3, for 4 in range(1)
  T = 0 + (num[0]*num[2]) = 4*4 = 16 = output = test statistic

  """

  T = 0
  p = 2
  L = len(num)
  for i in range(L-p):
    T = T + (num[i] * num[i+p])
  return T

z = [1,0,0,0,1,1,1,0,1,1,0,1,1,0,1,1,0,0,1,1]
num = bin_count(z)
print(num)
teststatistic1 = covariance_test_statistic(num)
print(teststatistic1)

l = [1,0,0,0,1,1,1,0,1,1,0,1,1,0,1,1,0,0,1,1,1,1,1,1,0,0,0,1,0,1,0,0,1,1,0,0,0,0,0,1,1,1,1,0,1,0,0,1,0,0,0,1,1,1,1,1,1,1,1,0,0,0,1,1,1,0,1,0,1,0,1,0,0,1,1,1,1,1,0,0,0,0,1,1,0,0,0,0,0,0,1,1,1,1,1,0,1,0,0,1]
num = bin_count(l)
print(num)
teststatistic1 = covariance_test_statistic(num)
print(teststatistic1)

s = (5,2,6,10,12,3,1)
teststatistic1 = covariance_test_statistic(s)
print(teststatistic1)

"""Convert List To String"""

def convert_list_to_string(s):

  """

  This function converts list of integers to string.
  @input: s:list of integers
  @output:string_s :converted string from list
  For eg: input: p = [12, 78, 59, 190]
  join the list and covert it to str using map function.
  converted_string = 12 78 59 190

  """

  converted_string = ' '.join(map(str, s))
  return converted_string


s = [14, 66, 98, 2, 4, 56]
string_s = convert_list_to_string(s)
print(string_s)

p = [12, 78, 59, 190]
string_s = convert_list_to_string(p)
print(string_s)

"""Convert String To Bytes"""

def convert_string_to_bytes(string_s):

  """

  This function converts string to bytes.
  @input:string_s :string
  @output: converted_bytes:string converted to bytes.
  For eg: input = 12 78 59 190
  encode the string using utf-8
  output = converted_bytes = b'12 78 59 190'

  """
  converted_bytes = string_s.encode('utf-8')
  return converted_bytes

string_s = "14 66 98 2 4 56"
converted_bytes = convert_string_to_bytes(string_s)
print(converted_bytes)

h = "12 78 59 190"
converted_bytes = convert_string_to_bytes(h)
print(converted_bytes)

"""Compression"""

import bz2
c = bz2.compress(converted_bytes) #compresses the data by using bz2.compress(input_data)
print(len(c)) #for finding length of compressed data
"""
For eg: input: k = b'12 78 59 190'
output: len(k) = 47
"""

"""5.1.11 Compression Test Statistic"""

import bz2
def compression_test_statistic(s):

  """

  This function calculates the length of that data subset after the samples are encoded into a character string and processed by a general-purpose compression algorithm.
  @input: s:list of integers
  @output: length_of_compressed_string:length of the compressed string.
  For eg:
  input = p = [12, 78, 59, 190]
  output of 1st function(convert_list_to_string)= s = 12 78 59 190
  output of 2nd function(convert_string_to_bytes)= y = b'12 78 59 190'
  then bz2.compress(y) will give us the compressed data and its length can be calculated.
  output of the function(compression_test_statistic)(length of compressed data) = 47

  """

  string_s = convert_list_to_string(s)
  converted_bytes = convert_string_to_bytes(string_s)
  d = bz2.compress(converted_bytes)
  return d

s = [14, 66, 98, 2, 4, 56]
d = compression_test_statistic(s)
print(len(d))

d = [234, 89, 456, 345, 77, 89]
f = compression_test_statistic(d)
print(len(f))

"""                                           **END**"""