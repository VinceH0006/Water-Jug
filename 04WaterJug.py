#  File: waterjug.py
#  Description: This program reads in a file and uses the input data to run through the water jug logic problem and outputs the steps to be taken
#  Student's Name: Vincent Hochstein
#  Student's UT EID: VLH546
#  Course Name: CS 313E 
#  Unique Number: 50597
#
#  Date Created: 10/5/2015
#  Date Last Modified: 10/9/2015

# Full knowledge that my code does not work
# I do not know how to order the code properly so that it executes in a way that creates variation in the order in steps
# Or in other words, I don't know how to go for lateral processing first, rather than depth
# I will attempt to remedy this at a later date

# This function calls to all of the others and acts as the function to be recursively called
def delegation (state, jugs, goal_num, goal_amount, history):

  # If the code reaches 50 steps without success, it terminates (gracefully)
  if (len(history) >= 50):
    print ("There is no solution to this problem within 50 moves.  Have a nice day.")
    exit

  #Checking if goal is achieved before each itteration is performed
  goal_achieved = is_goal (state, goal_num, goal_amount)
  if (goal_achieved == 1):
    return (history)

  # Call to the fill function, references each element (each jug)
  for i in range (len(jugs)):
    fill_state = fill (state, jugs, i)
    history.append(fill_state)
    delegation (fill_state, jugs, goal_num, goal_amount, history)

  # Call to the empty function, same as the fill function
  for i in range (len(jugs)):
    empty_state = empty (state, i)
    delegation (empty_state, jugs, goal_num, goal_amount, history)

  # Transfer function call, slightly more comlicated since you can go, a to b, b to a, a to c, or any of the other many combinations
  for i in range (len(jugs)):
    for j in range (len(jugs)):
      if (i == j):
        continue
      else:
        transfer_state = transfer (state, jugs, i, j)
      delegation (transfer_state, jugs, goal_num, goal_amount, history)

# Fill function
def fill (state, jugs, x):
  state[x] = jugs[x]
  return (state)

# Empty function
def empty (state, x):
  state[x] = 0
  return (state)

# Transfer function
def transfer (state, jugs, x, y):
  if (state[x] <= (jugs[y] - state[y])):
    state[y] = state[y] + state[x]
    state[x] = 0
  else:
    state[y] = jugs[y]
    state[x] = (state[x] + state[y] - jugs[y])
  return (state)

# Goal testing function
def is_goal (state, goal_num, goal_amount):
  if (state[goal_num] == goal_amount):
    return 1
  else:
    return 0

# Main only serves to open and read the data, as well as call to the primary function and print the results
def main():

  in_file = open ("jugdata.txt", "r")

  line1 = in_file.readline()
  line1 = line1.strip()

  jugs_list = line1.split(" ")

  line2 = in_file.readline()
  line2 = line2.strip()
  
  line2_list = line2.split(" ")

  jug_num_goal = int(line2_list[0])
  jug_amount_goal = int(line2_list[1])

  in_file.close()

  jug_state = []

  for i in range (len(jugs_list)):
    jug_state.append(0)
    jugs_list[i] = int(jugs_list[i])

  empty_history = [[]]
  empty_history.append(jug_state)

  history = delegation (jug_state, jugs_list, jug_num_goal, jug_amount_goal, empty_history)

  for i in range (len(history)):
    print (history[[i]])
main()