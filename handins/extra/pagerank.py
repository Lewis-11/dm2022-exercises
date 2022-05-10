import numpy as np

adjacencyMatrix = [
    [0, 1, 0, 0, 0],
    [1, 0, 1, 1, 1],
    [0, 1, 0, 1, 1],
    [0, 1, 1, 0, 1],
    [0, 1, 1, 1, 0],
]

outDegreeMatrix = [
    [1, 0, 0, 0, 0],
    [0, 4, 0, 0, 0],
    [0, 0, 3, 0, 0],
    [0, 0, 0, 3, 0],
    [0, 0, 0, 0, 3],
]

n_nodes = len(adjacencyMatrix)

r0 = np.array(
    [
        1 / n_nodes,
    ]
    * n_nodes
)
r = [r0]

adjacencyMatrix = np.array(adjacencyMatrix)
outDegreeMatrix = np.array(outDegreeMatrix)


M = np.dot(adjacencyMatrix.T, np.linalg.inv(outDegreeMatrix))
print(M)
print()
# for i in range(30):
#     r.append(np.dot(M, r[-1]))


# # Print r iteration by iteration
# for i in range(len(r)):
#     print(f"[i] Iteration {i}:")

#     for j in range(len(r[i])):
#         print(f"{r[i][j]}\t", end="")
#     print("\n")

iterations = 30
M_raised = np.linalg.matrix_power(M, iterations)
final_result = np.dot(M_raised, r0)

for i in range(1, 10):
    print(np.linalg.matrix_power(M, i))
    print()
