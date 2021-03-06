import csv
import re
dates = []
retweets = []
likes=[]
 
with open('DaleSteyn62_tweets.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        dates.append(row[1])
        retweets.append(row[3])
	likes.append(row[4])
dates = dates[0:700]
retweets = retweets[1:700]
likes = likes[1:700]
retweets = [int(numeric_string) for numeric_string in retweets]
likes = [int(numeric_string) for numeric_string in likes]
#print retweets
count = []
str2 = ''.join(dates)
sepdays = re.findall(r'2017-09-\d{1,2}',str2)
augdays = re.findall(r'2017-08-\d{1,2}',str2)
juldays = re.findall(r'2017-07-\d{1,2}',str2)
jundays = re.findall(r'2017-06-\d{1,2}',str2)
maydays = re.findall(r'2017-05-\d{1,2}',str2)
aprdays = re.findall(r'2017-04-\d{1,2}',str2)
mardays = re.findall(r'2017-03-\d{1,2}',str2)
febdays = re.findall(r'2017-02-\d{1,2}',str2)
jandays = re.findall(r'2017-01-\d{1,2}',str2)
dec16days = re.findall(r'2016-12-\d{1,2}',str2)
nov16days = re.findall(r'2016-11-\d{1,2}',str2)
oct16days = re.findall(r'2016-10-\d{1,2}',str2)
sep16days = re.findall(r'2016-09-\d{1,2}',str2)
aug16days = re.findall(r'2016-08-\d{1,2}',str2)
jul16days = re.findall(r'2016-07-\d{1,2}',str2)
jun16days = re.findall(r'2016-06-\d{1,2}',str2)
may16days  =re.findall(r'2016-05-\d{1,2}',str2)
apr16days =re.findall(r'2016-04-\d{1,2}',str2)
mar16days = re.findall(r'2016-03-\d{1,2}',str2)
feb16days  =re.findall(r'2016-02-\d{1,2}',str2)
jan16days  =re.findall(r'2016-01-\d{1,2}',str2)
a = []
a.extend([len(jan16days),len(feb16days),len(mar16days),len(apr16days),len(may16days),len(jun16days),len(jul16days),len(aug16days),len(sep16days),len(oct16days),len(nov16days),len(dec16days),len(jandays),len(febdays),len(mardays),len(aprdays),len(maydays),len(jundays),len(juldays),len(augdays),len(sepdays)])
print a #a stores the number of tweets monthwise in a list
num = []
for i in range(0,len(a)):
	num.append(i+1)
cumulative = []
print num
i=0
j=0
x=0
counter = 0
while i<len(a):
	j=0
	x=0
	while j<=i:
		x=x+a[j]
		j+=1
	cumulative.append(x) #cumulative stores the cumulative no of tweets, month wise in a list
	i+=1
print cumulative


for x in range(0,cumulative[1]):
	counter = counter + retweets[x]
count.append(counter) 
i=0
while i < len(a)-1:	
	counter = 0	
	for x in range(cumulative[i],cumulative[i+1]):
		counter = counter + retweets[x]#count stores the number of retweets monthwise in a list
	count.append(counter)
	i+=1

print count

likecount =[]
counter = 0
for x in range(0,cumulative[1]):
	counter = counter + likes[x]
likecount.append(counter) 
i=0
while i < len(a)-1:	
	counter = 0	
	for x in range(cumulative[i],cumulative[i+1]):
		counter = counter + likes[x]#likecount stores the number of likes monthwise in a list
	likecount.append(counter)
	i+=1

print likecount

i=0
avgcount = [] #avgcount stores the avg no of retweets in a list
while i<len(a):
	j=0
	x=0
	while j<=i:
		x=x+count[j]
		j+=1
	avgcount.append(x)
	i+=1
print avgcount
i=0

i=0
avglikecount = [] #avgcount stores the avg no of retweets in a list
while i<len(a):
	j=0
	x=0
	while j<=i:
		x=x+likecount[j]
		j+=1
	avglikecount.append(x)
	i+=1
print avglikecount
import pandas as pd

my_df = pd.DataFrame(a)
my_df.to_csv('DaleSteyntweetsmonthwise.csv', index=False, header=False) #first col is monthwise the no of tweets
my_df = pd.DataFrame(count)
my_df.to_csv('DaleSteynretweetsmonthwise.csv', index=False, header=False) #first col is monthwise the no of tweets
my_df = pd.DataFrame(likecount)
my_df.to_csv('DaleSteynlikesmonthwise.csv', index=False, header=False) #first col is monthwise the no of tweets


import matplotlib.pyplot as plt
plt.bar(num,a,align = 'center',color = 'red')
plt.ylabel("Number of tweets posted in each month")
plt.xlabel("Month 1 = Jan16, 2 = Feb16, 3= Mar....")
plt.show()
plt.bar(num,cumulative,align = 'center',color = 'magenta')
plt.xlabel("Month number")
plt.ylabel("Cumulative no of tweets")
plt.show()
plt.bar(num,count,align = 'center',color = 'yellow')
plt.xlabel("Month number")
plt.ylabel("Number of retweets per month")
plt.show()
plt.bar(num,avgcount,align = 'center',color = 'purple')
plt.xlabel("Month number")
plt.ylabel("Cumulative Number of retweets per month")
plt.show()
plt.bar(num,likecount,align = 'center',color = 'indigo')
plt.xlabel("Month number")
plt.ylabel("No of likes each month")
plt.show()
plt.bar(num,avglikecount,align='center',color = 'orange')
plt.xlabel("Month number")
plt.ylabel("Average likes per month");
plt.show()
#print(dates)
#print(scores)
