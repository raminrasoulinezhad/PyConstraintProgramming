############################################
# Sample A
############################################

# Find all (x,y) where x ∈ {1,2,3} and 0 <= y < 10, and x + y >= 5


import constraint

problem = constraint.Problem()

problem.addVariable('x', [1,2,3])
problem.addVariable('y', range(10))

def our_constraint(x, y):
	if x + y >= 5:
		return True
	# else result is 'None'

problem.addConstraint(our_constraint, ['x','y'])

# if we want to exclude the cases where 'x' == 'y'
#problem.addConstraint(constraint.AllDifferentConstraint())
# the list for all built-in constraints are here in 'https://stackabuse.com/constraint-programming-with-python-constraint/#listofbuiltinconstraints'

solutions = problem.getSolutions()


# Easier way to print and see all solutions
# for solution in solutions:
#    print(solution)

# Prettier way to print and see all solutions
length = len(solutions)
print("(x,y) ∈ {", end="")
for index, solution in enumerate(solutions):
	if index == length - 1:
		print("\n\t\t({},{})".format(solution['x'], solution['y']), end="")
	else:
		print("\n\t\t({},{}),".format(solution['x'], solution['y']), end="")
print("\n\t}")


############################################
# Example B
############################################

problem = constraint.Problem()

# We're using .addVariables() this time since we're adding
# multiple variables that have the same interval.
# Since Strings are arrays of characters we can write
# "TF" instead of ['T','F'].
problem.addVariables("TF", range(1, 10))
problem.addVariables("WOUR", range(10))

# Telling Python that we need TWO + TWO = FOUR
def sum_constraint(t, w, o, f, u, r):
	if 2*(t*100 + w*10 + o) == f*1000 + o*100 + u*10 + r:
		return True

# Adding our custom constraint. The
# order of variables is important!
problem.addConstraint(sum_constraint, "TWOFUR")

# All the characters must represent different digits,
# there's a built-in constraint for that
problem.addConstraint(constraint.AllDifferentConstraint())

solutions = problem.getSolutions()
print("Number of solutions found: {}\n".format(len(solutions)))

# .getSolutions() returns a dictionary
for s in solutions:
	print("T = {}, W = {}, O = {}, F = {}, U = {}, R = {}"
		.format(s['T'], s['W'], s['O'], s['F'], s['U'], s['R']))


############################################
# Example C
############################################

problem = constraint.Problem()

# The maximum amount of each coin type can't be more than 60
# (coin_value*num_of_coints) <= 60
total_val = 60
number_of_coins = 10

problem.addVariable("1 cent", range(total_val + 1))
problem.addVariable("3 cent", range(total_val // 3 + 1))
problem.addVariable("5 cent", range(total_val // 5 + 1))
problem.addVariable("10 cent", range(total_val // 10 + 1))
problem.addVariable("20 cent", range(total_val // 20 + 1))

problem.addConstraint(
	constraint.ExactSumConstraint(60,[1,3,5,10,20]),
	["1 cent", "3 cent", "5 cent","10 cent", "20 cent"]
)

# to force the solutions be less than 10 coins
problem.addConstraint(
	constraint.MaxSumConstraint(number_of_coins),
	["1 cent", "3 cent", "5 cent","10 cent", "20 cent"]
)



def sum_constraint(one, two, five, ten, twenty):
	return one + two + five + ten + twenty

# Where we explicitly give the order in which the weights should be allocated

# We could've used a custom constraint instead, BUT in this case the program will
# run slightly slower - this is because built-in functions are optimized and
# they find the solution more quickly
# def custom_constraint(a, b, c, d, e):
#     if a + 3*b + 5*c + 10*d + 20*e == 60:
#         return True
#     problem.addConstraint(o, ["1 cent", "3 cent", "5 cent","10 cent", "20 cent"])


# A function that prints out the amount of each coin
# in every acceptable combination
def print_solutions(solutions):
	for s in solutions:
		print("---")
		print("""
		1 cent: {0:d}
		3 cent: {1:d}
		5 cent: {2:d}
		10 cent: {3:d}
		20 cent: {4:d}""".format(s["1 cent"], s["3 cent"], s["5 cent"], s["10 cent"], s["20 cent"]))
		# If we wanted to we could check whether the sum was really 60
		# print("Total:", s["1 cent"] + s["3 cent"]*3 + s["5 cent"]*5 + s["10 cent"]*10 + s["20 cent"]*20)
		# print("---")

solutions = problem.getSolutions()
print_solutions(solutions)
print("Total number of ways: {}".format(len(solutions)))


############################################
# Example D
############################################




