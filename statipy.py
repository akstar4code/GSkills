import statistics as s
olst = [1,2,3,5,6,9,4,2,10]
elst = [0,1,4,5,6,6,8,6]
print(s.mean(olst))
print(s.mean(elst))
print(s.median(olst))
print(s.median(elst))
print(s.median_low(olst))
print(s.median_high(elst))
print(s.mode(olst),s.mode(elst),sep=' And ')
print(s.stdev(olst),s.stdev(elst))
print(s.variance(olst),s.variance(elst),sep=' And ')
print(s.pvariance(olst),s.pvariance(elst),sep=' And ')
print(s.pstdev(olst),s.pstdev(elst),sep=' And ')