import numpy as np

def para(start,end,step):
	forward = list(np.arange(start,end,step)
	back = list(np.arange(end,start,step))
	times = forward
	times.append(back)
	return times

def main():
	begin = raw_input('Begining time:\n')
	stop = raw_input('Ending time:\n')
	inc = raw_input('Increment:\n')
	para(begin,stop,inc)
