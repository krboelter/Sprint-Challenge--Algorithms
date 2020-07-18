#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) this would be O(n). I put this answer because depending on what n is, the runtime of the while loop depends on what n is.


b) this would be O(n log n). This is because depending on the size of n, the for loop runtime will vary, but becuase the while loop is incremented by it's double, the while loop will exponentially get closer to becoming False.


c) this would be O(n). It is this way beause this function is recursive, and depending on how many bunnies you put in is how many times this function would run.

## Exercise II

make a function that takes 1 parameter (num_stories)
	variable half = divide the num_stories by 2, round up
	
	drop the egg from that story,
	if the egg breaks, then set variable half to the max value
		drop the egg again.
	if the egg does not break from that story, set the minimum story to variable half
		drop the egg again
	
	f will equal the value of the last story the above function when it can no longer calculate i.e. when the lowest story surpasses the max story, the value before that is f

This runtime complexity is O(log n) because it is a binary search tree, that allows you to evaluate only half of an array or value, then depending on the outcome, will allow you to split the evaluated array or value in half again.
