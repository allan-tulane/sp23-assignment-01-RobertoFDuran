"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.


def foo(x):
  ### TODO
  if x <= 1:
    return x
  else:
    ra, rb = foo(x - 1), foo(x - 2)
    return ra + rb
  pass


def longest_run(mylist, key):
  ### TODO
  count = 0
  lastcount = 0
  for i in mylist:
    if i == key:
      count += 1
      if count > lastcount:
        lastcount = count
    else:
      count = 0
  return lastcount
  pass


class Result:
  """ done """

  def __init__(self, left_size, right_size, longest_size, is_entire_range):
    self.left_size = left_size  # run on left side of input
    self.right_size = right_size  # run on right side of input
    self.longest_size = longest_size  # longest run in input
    self.is_entire_range = is_entire_range  # True if the entire input matches the key

  def __repr__(self):
    return ('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
            (self.longest_size, self.left_size, self.right_size,
             self.is_entire_range))


recursive_counter = 0
last_recursive_counter = 0
first_run = 0
middle = 0
length = 0
left = []
right = []
is_entire = False


def longest_run_recursive(mylist, key):
  ### TODO
  global recursive_counter
  global last_recursive_counter
  global first_run
  global middle
  global length
  global left
  global right
  global is_entire
  if first_run == 0:
    is_empty = 0
    if len(mylist) == 0:
      return 0
    else:
      first_run = 1
      middle = len(mylist) // 2
      length = len(mylist)
      left.clear()
      right.clear()
      left.append(mylist[:middle])
      right.append(mylist[middle:])
      longest_run_recursive(left, key)
      longest_run_recursive(right, key)
  elif len(mylist) == 0:
    if recursive_counter > last_recursive_counter:
      last_recursive_counter = recursive_counter
    if last_recursive_counter == length:
      is_entire = True
    first_run = 0
    list = Result(mylist[:middle], mylist[middle:], last_recursive_counter,
                  is_entire)
    return list
  else:
    if mylist[0] == key:
      recursive_counter += 1
      left.pop(0)
      right.pop(0)
      longest_run_recursive(left, key)
      longest_run_recursive(right, key)
    else:
      if recursive_counter > last_recursive_counter:
        last_recursive_counter = recursive_counter
      left.pop(0)
      right.pop(0)
      longest_run_recursive(left, key)
      longest_run_recursive(right, key)
  pass


## Feel free to add your own tests here.
def test_longest_run():
  assert longest_run([2, 12, 12, 8, 12, 12, 12, 0, 12, 1], 12) == 3
