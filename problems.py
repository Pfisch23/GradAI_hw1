################################################################################
# Check if a given partial assignment is consistent with the cnf
# Input: formula is a CNF encoded as described in the problem set.
#        assignments is a dictionary of assignments.
# Output: Whether there is a clause that is false in the formula.
################################################################################
def check(formula, assignments):
    index_list = []
    for assignment in assignments:
        index_list.append(assignment[1])
    #print(index_list)
    for clause in formula:
        lit_check =False
        no_index = False
        for lit in clause:
            for asg in assignments:
                if lit[1] == asg[1] and lit[0]+asg[0]==1:
                    #print(lit)
                    lit_check = True
                elif lit[1] == asg[1] and (lit[0]+asg[0]) in (0,2) and not lit_check:
                    #print(lit,asg, lit[0]+asg[0])
                    lit_check = False
                elif lit[1] not in index_list and not lit_check:
                     #print(lit,lit[1])
                     no_index = True   
            # if lit in assignments:
            #     #print(lit)
            #     lit_check = True
            # elif lit[1] not in index_list:
            #     #print(lit,lit[1])
            #     no_index = True
        #print (lit_check,no_index)
        if not lit_check and not no_index:
            #print(clause)
            return False
    return True

################################################################################
# Simple Sat Problem Solver
# Input: n is the number of variables (numbered 0, ..., n-1).
#        formula is CNF
# Output: An assignment that satisfies the formula
#         A count of how many variable assignments were tried
################################################################################
def simpleSolver(n, formula):
    assignments = [(0,0)]
    i=0
    j=0
    while i<=n-1:
        check_bool = check(formula,assignments)
        #print(check_bool,i)
        #print(i)
        #j+=1
        if not check_bool:
            # print(assignments)
            assignments.pop()
            assignments.append((1,i))
            check_bool = check(formula,assignments)
            #print(check_bool)
            j+=1
            #print(assignments)
            #print(i)
            while not check_bool:
                print(assignments)
                assignments.pop()
                assignments.pop()
                i -= 1
                assignments.append((1,i))
                j += 1
                # print(i)
                check_bool = check(formula,assignments)
            #assignments.append((1,i))
            # print(assignments)
                if i<0:
                    return(False,j)
        if check_bool:
            i+=1
            j+=1
            if i<=n-1:
                assignments.append((0,i))
    #print(i)
    result = {}
    for asgn in assignments:
        result[asgn[1]] = asgn[0]
    return (result, j)

################################################################################
# Simple Sat Problem Solver with unit propagation
# Input: n is the number of variables (numbered 0, ..., n-1).
#        formula is CNF
# Output: An assignment that satisfies the formula
#         A count of how many variable assignments were tried
################################################################################
def unitSolver(n, formula):
    return False, 0

################################################################################
# Clause Learning SAT Problem Solver                      
# Input: n is the number of variables (numbered 0, ..., n-1).
#        formula is CNF
# Output: An assignment that satisfies the formula
#         A count of how many variable assignments where tried
#         A list of all conflict-induced clauses that were found
################################################################################
def clauseLearningSolver(n, formula):
    return False, 0, []

################################################################################
# Conflict-directed backjumping with clause learning SAT Problem Solver                      
# Input: n is the number of variables (numbered 0, ..., n-1).
#        formula is CNF
# Output: An assignment that satisfies the formula
#         A count of how many variable assignments where tried
################################################################################
def backjumpSolver(n, formula):
    return False, 0, []


def sanityCheck():
    # Some simple sanity checks.
    # Feel free to edit this part.
    # The autograder does not touch it.
    
    numvar = 3

    # (x0 | ~x1) & (x1 | x2) & (x1 | ~x2)
    # satisfying assignment: x0 = 1, x1 = 1, x2 = 0
    formula = [[(0,0), (1, 1)], [(0, 1), (0, 2)], [(0, 1), (1, 2)]]
    assignments = dict()

    def checkEqual(val, expected):
        print("EXPECTED:", expected)
        print("GOT:     ", val)
        if expected == val:
            print("\033[0;32mOK\033[0m")
            print()
        else:
            print("\033[0;31mMISMATCH\033[0m")
            print()

    # check
    checkEqual(simpleSolver(numvar, formula), ({0: 1, 1: 1, 2: 0}, 11))
    # checkEqual(unitSolver(numvar, formula), ({0: 1, 1: 1, 2: 0}, 5))
    # checkEqual(clauseLearningSolver(numvar, formula), ({0: 1, 1: 1, 2: 0}, 5, [[(0, 1)], [(0, 1)]]))
    # checkEqual(backjumpSolver(numvar, formula), ({0: 1, 1: 1, 2: 0}, 2))

    formula_2 = [[(1,0), (1, 1)],[(1, 0), (0, 2)],[(1,2), (1,3)], [(0, 1), (0, 3), (0, 4)], 
                    [(1, 4), (0, 5), (1, 6)], [(0, 1), (0, 6), (0, 7)], [(1, 7), (1, 8)], [(1, 7), (0, 9)],
                    [(0, 8), (1, 9), (0, 10)], [(1, 9), (1, 11)], [(0, 10), (0, 11)]]

    # check
    checkEqual(simpleSolver(12, formula_2), ({0: 0, 1: 0, 2: 0, 3: 0, 4: 1, 5: 1, 6: 1, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0}, 37))
    # checkEqual(unitSolver(12, formula_2), ({0: 0, 1: 0, 2: 0, 3: 0, 4: 1, 5: 1, 6: 1, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0}, 13))
    # checkEqual(clauseLearningSolver(12, formula_2), ({0: 0, 1: 0, 2: 0, 3: 0, 4: 1, 5: 1, 6: 1, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0}, 13, [[(1, 7)], [(1, 7)]]))
    # checkEqual(backjumpSolver(12, formula_2), ({0: 0, 1: 0, 2: 0, 3: 0, 4: 1, 5: 1, 6: 1, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0}, 9))

# if __name__ == "__main__":
#     sanityCheck()
formula = [[(0,0), (1, 1)], [(0, 1), (0, 2)], [(0, 1), (1, 2)]]
assignments = [(1,0),(1,1),(0,2)]
test = check(formula,assignments)
print(test)