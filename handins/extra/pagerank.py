import numpy as np

adjacencyMatrix = [
    [0, 0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 0],
]

outDegreeMatrix = [
    [3, 0, 0, 0, 0, 0, 0],
    [0, 3, 0, 0, 0, 0, 0],
    [0, 0, 3, 0, 0, 0, 0],
    [0, 0, 0, 3, 0, 0, 0],
    [0, 0, 0, 0, 4, 0, 0],
    [0, 0, 0, 0, 0, 4, 0],
    [0, 0, 0, 0, 0, 0, 4],
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

for i in range(10):
    r.append(np.dot(M, r[-1]))


# Print r iteration by iteration
for i in range(len(r)):
    print(f"`[i] Iteration {i}:`\n")
    print('<span style="color:orange">**', end="")
    for j in range(len(r[i])):
        print(f"{r[i][j]:.3f}" + "&nbsp;" * 4, end="")
    print("**</span>\n")
