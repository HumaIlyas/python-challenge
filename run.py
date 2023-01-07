
## zero_after_one, count how many zeros in the list are after 1

def zero_after_one(mylist):
  counter = 0
  start = mylist.index(1, 0)
  mylist = mylist[start+1:]
  print(mylist)
  if 1 in mylist:
    for zero in mylist:
      if zero == 0:
          counter += 1
      else:
          break
    return counter
  else:
    return 0


assert zero_after_one([]) == 0
assert zero_after_one([1, 2, 3]) == 0
assert zero_after_one([0, 1, 2]) == 0
assert zero_after_one([0, 0, 0, 0]) == 0
assert zero_after_one([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
assert zero_after_one([1, 0]) == 1
assert zero_after_one([0, 1, 0]) == 1
assert zero_after_one([0, 1, 0, 0, 0, 0, 0]) == 5

print("Everything is correct")

