
## zero_after_one, count how many zeros in the list are after 1

def zero_after_one(list):
  counter = 0
  start = list.i(1)
  list = []

  for zero in list:
    if i == 0:
        i += 1
    else:
        break
  return counter


assert zero_after_one([]) == 0
assert zero_after_one([1, 2, 3]) == 0
assert zero_after_one([0, 1, 2]) == 0
assert zero_after_one([0, 0, 0, 0]) == 0
assert zero_after_one([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
assert zero_after_one([1, 0]) == 1
assert zero_after_one([0, 1, 0]) == 1
assert zero_after_one([0, 1, 0, 0, 0, 0, 0]) == 5

print("Everything is correct")

