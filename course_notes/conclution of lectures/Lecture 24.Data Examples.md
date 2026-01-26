## Using Built-In Functions and Comprehensions on Iterators
1. what are the indices of all elements in a list s that have the smallest absolute value
```
def abs(num: int):
	if num >= 0:
		return num
	else: 
		return -num

def smallestIndices(s):
	return [i for i in range(len(s)) if s[i] == min(map(abs, s))
```
2. what's the largest sum of two adjacent elments in a list s?(assume len(s) > 1)
```
def maxAdjacentSum(s):
	assert len(s) > 1
	return max((s[i] + s[i+1]) for i in range(len(s) - 1))
```
>[!info] another method using zip:
>```
>return max(a + b for a, b in zip(s[:-1], s[1:]))
>```
3. create a dictionary mapping each digit d to the lists of elements in s that end with d
```
def dicCreater(s):
	dic = {}
	for i in range(10):
		lst = [num for num in s if num % 10 == i]
		if lst:
			dic[i] = lst 
	return dic
```
a better way to avoid this is not purely loop on 10, instead, use the list itself
>[!info]
>```
>last_digits = [x % 10 for x in s]
>return {d: [x for x in s if x % 10 == d] for d in range(10) if d in last_digits}
>```
4. does every element equal some other element in s?
```
def equalChecker(s):
	ans = 1
	for i in range(len(s)):
		ans *= (s[i] in (s[:i] + s[i+1:]))
	return bool(ans)
```
the idea is correct, but not simple enough
>[!info]
>all() is a built-in function that check if all the values in a list are true
>```
>return all(s[i] in s[:i]+s[i+1:] for i in range(len(s)))
>```

## Linked List Exercises
```
class Link:
	empty = None
	
	def __init__(self, value, rest):
		self.val = value
		self.rest = rest
		assert rest is None or is_instance(rest, Link)
		
	def checkOrder(self, func=lambda x: x):
		if not self or not self.rest:
			return True
		return func(self.val) <= func(self.rest.val) and checkOrder(self.rest)	
		
		
def merge(s, t):
	if s is Link.empty:
		return t
	elif t is Link.empty:
		return s
	elif s.first <= t.first:
		return Link(s.first, merge(s.rest, t))
	else:
		return Link(t.first, merge(s, t.rest))

def merge_in_rest(s, t):
"""Instead of creating new Links, this directly modify s"""
	if s is Link.empty:
		return t
	elif t is Link.empty:
		return s
	elif s.first <= t.first:
		s.rest = merge_in_place(s.rest, t)
		return s
	else:
		t.rest = merge_in_place(s, t.rest)
		return t
```