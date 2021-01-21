from VRP_Model import Model
import Solver
import random

# random.seed(1)
successful = 0
tries = 50
for i in range(tries):

    m = Model()
    m.BuildModel(random.randint(0, 10000000000))

    sol = Solver.Solver(m)
    const_sol = sol.NaiveConstructive(m)

    # if every check is OK the solution is correct
    if sol.NCCheckDuplicates(const_sol) and sol.NCAllCustServiced(const_sol) and sol.NCCountCustomersServiced(const_sol) == 100:
        successful += 1

if successful == tries:
    print("~~~~~~~~~~ SUCCESS ~~~~~~~~~~")
else:
    print("~~~~~~~~~~ FAILED ~~~~~~~~~~")








