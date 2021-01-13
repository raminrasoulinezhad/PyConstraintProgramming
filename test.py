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
# Example D - I did not understand what is the example
############################################


############################################
# Example D
############################################
'''
You wish to pack chocolates for your mother. 
Your goal is to bring her the sweetest chocolate possible, 
that you can pack in your bag and sneak through security, 
and that wouldn't pass a certain net value for which you'd 
go to prison if you got caught.
Security most likely won't get suspicious if you bring less 
than 3kg. You can fit 1 dm^3 of chocolate in your bag. 
You won't go to jail if you steal less than $300 worth 
of chocolate.
'''

problem = constraint.Problem()
max_price = 30
max_space = 1000
max_weight = 3000

problem.addVariable('A', range(int(max_price//8) + 1))
problem.addVariable('B', range(int(max_price//6.8) + 1))
problem.addVariable('C', range(int(max_price//4) + 1))
problem.addVariable('D', range(int(max_price//3) + 1))

# We have 3kg = 3,000g available
def weight_constraint(a, b, c, d):
    if (a*100 + b*45 + c*10 + d*25) <= max_weight:
        return True

# We have 1dm^3 = 1,000cm^3 available
def volume_constraint(a, b, c, d):
    if (a*8*2.5*0.5 + b*6*2*0.5 * c*2*2*0.5 + d*3*3*0.5) <= max_space:
        return True

# We can't exceed $300
def value_constraint(a, b, c, d):
    if (a*8 + b*6.8 + c*4 + d*3) < max_price:
        return True

problem.addConstraint(weight_constraint, "ABCD")
problem.addConstraint(volume_constraint, "ABCD")
problem.addConstraint(value_constraint, "ABCD")

maximum_sweetness = 0
solution_found = {}
solutions = problem.getSolutions()

for s in solutions:
    current_sweetness = s['A']*10 + s['B']*8 + s['C']*4.5 + s['D']*3.5
    if current_sweetness > maximum_sweetness:
        maximum_sweetness = current_sweetness
        solution_found = s

print("""
The maximum sweetness we can bring is: {}
We'll bring:
{} A Chocolates,
{} B Chocolates,
{} C Chocolates,
{} D Chocolates
""".format(maximum_sweetness, solution_found['A'], solution_found['B'], solution_found['C'], solution_found['D']))


############################################
# Example E - I did not try this case
############################################



############################################
# Example extra example
############################################
'''
Generate all combinations (that have a length equal to the number of keys) of values stored in a dictionary (the order of output doesn't matter). The dictionary is {String : List_of_Strings}. In such a way that every combination has exactly one value from the List_of_Strings of a key.

You don't know the number of keys in the dictionary in advance, nor do you know how long a List_of_String is, every List_of_String can be of different length. I.e. the dictionary is dynamically generated via user input.

Example input: dictionary = {"A" : [1,2], "B" -> [4], "C" -> [5,6,7], "D" -> [8,9]}
Example output: (1,4,5,8), (1,4,5,9), (1,4,6,8), (1,4,6,9), (1,4,7,8)....
'''

# input example
generated_dictionary = {'A' : [1,2], 'B' : [4], 'C' : [5,6,7], 'D' : [8,9]}

problem = constraint.Problem()

for key, value in generated_dictionary.items():
    problem.addVariable(key, value)

solutions = problem.getSolutions()

for solution in solutions:
    print(solution)
