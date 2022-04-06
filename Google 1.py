Keyboard
shortcuts(Ctrl + Shift + K)
Interview in progress
1
# Bob loves cake. He wants to have 2 cakes per day
2
# [10:00 11:42 15:24] minimim between 10:00 and 11:42 -> the answer 102 mins
3
​
4
# Minimum time span will always have to do with adjacent values if the list is sorted
5
# O(nlogn) to account for the sorting
6
# [10:00 11:42 15:24 16:00] 09:42 instead of 9:42
7
# We will have to variables that keep track of the currentTimeSpan (currentTime-preTime)
8
# For each iteration we will take the minimum of the currentTimeSpan and the globalMinimumTimeSpan
9
# ont thinking abt 23:59 to 0:01 yet
10
​
11
# 10:00
12
# 11:42
13
​
14


def MinimumTimeSpan(times):
    15


# sort by hour and then sort by minute in ascending order
16
# example
17
# hour, min = str.split(':')
18
# hour = "10"
19
# min = "42"
20
timesInMin = []
21
for i in range(len(times)):
    22
hour, min = times[i].split(':')
23
# lets assume hour and min are now int, # int(hour) -> int
24
newtime = hour * 60 + min
25
timesInMin.apppend(newtime)
26
timesInMin.sort()
27
minTimeSpan = 0
28
# we want to look at each time along with its preceeding time starting with the 2nd time in the list
29
for i in range(1, len(timesInMin)):
    30
currentTime = timesInMin[i]
31
prevTime = timesInMin[i - 1]
32
currentTimeSpan = currentTime - prevTime
33
minTimeSpan = min(currentTimeSpan, minTimeSpan)
34
return minTimeSpan
35
​
36
#       10:00         11:42
37
# -----------------------------------
38
​
39
​
40
​
41
## making the sorting better
42
timesInMin[newtime] = newtime
43
timeline = []
44
for i in range(60 * 24):
    45
timeline[i] = False
46
for i in range(len(times)):
    47
hour, min = times[i].split(':')
48
# lets assume hour and min are now int, # int(hour) -> int
49
newtime = hour * 60 + min
50
timeline[newtime] = True
51
minTimeSpan = 0
52
# we want to look at each time along with its preceeding time starting with the 2nd time in the list
53
# this would be O(n)
54
for i in range(1, len(timeline)):
    55
if time[]
    56
currentTime = timesInMin[i]
57
prevTime = timesInMin[i - 1]
58
currentTimeSpan = currentTime - prevTime
59
minTimeSpan = min(currentTimeSpan, minTimeSpan)
60
return minTimeSpan
61

