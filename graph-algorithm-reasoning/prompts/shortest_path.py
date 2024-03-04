# 5-shot
standard_prompt_easy_5shot = '''Find the shortest path from a source node to a target node in a undirected graph. The undirected graph is represented as a node set, a edge set, and a edge distance set.
Input:
Node set: [0, 1, 2, 3, 4]
Edge set: [[0, 3], [1, 4], [2, 4], [3, 4]]
Edge distance set: [2, 3, 5, 3]
Source Node: 0
Target Node: 4

Answer:
The shortest path from the source node to the target node is [0, 3, 4]. The shortest distance is 5.

Input:
Node set: [0, 1, 2, 3, 4, 5]
Edge set: [[0, 1], [1, 4], [2, 3], [3, 4], [3, 5], [4, 5]]
Edge distance set: [5, 3, 3, 4, 5, 1]
Source Node: 0
Target Node: 5

Answer:
The shortest path from the source node to the target node is [0, 1, 4, 5]. The shortest distance is 9.

Input:
Node set: [0, 1, 2, 3, 4, 5]
Edge set: [[0, 3], [0, 2], [1, 3], [1, 5], [2, 3], [2, 5], [3, 4], [4, 5]]
Edge distance set: [2, 2, 5, 4, 2, 3, 3, 4]
Source Node: 0
Target Node: 5

Answer:
The shortest path from the source node to the target node is [0, 2, 5]. The shortest distance is 5.

Input:
Node set: [0, 1, 2, 3, 4]
Edge set: [[0, 2], [1, 4], [1, 2], [2, 4], [3, 4]]
Edge distance set: [5, 3, 2, 1, 1]
Source Node: 0
Target Node: 4

Answer:
The shortest path from the source node to the target node is [0, 2, 4]. The shortest distance is 6.

Input:
Node set: [0, 1, 2, 3, 4, 5, 6, 7, 8]
Edge set: [[0, 1], [0, 4], [1, 4], [1, 2], [2, 7], [3, 7], [3, 5], [4, 6], [5, 8], [6, 8], [7, 8]]
Edge distance set: [5, 5, 2, 5, 5, 2, 3, 2, 3, 2, 3]
Source Node: 0
Target Node: 8

Answer:
The shortest path from the source node to the target node is [0, 4, 6, 8]. The shortest distance is 9.

Input:
{input}
'''

standard_prompt_easy_1shot = '''Find the shortest path from a source node to a target node in a undirected graph. The undirected graph is represented as a node set, a edge set, and a edge distance set.
Input:
Node set: [0, 1, 2, 3, 4]
Edge set: [[0, 3], [1, 4], [2, 4], [3, 4]]
Edge distance set: [2, 3, 5, 3]
Source Node: 0
Target Node: 4

Answer:
The shortest path from the source node to the target node is [0, 3, 4]. The shortest distance is 5.

Input:
{input}
'''

standard_prompt_easy_zeroshot = '''Find the shortest path from a source node to a target node in a undirected graph. The undirected graph is represented as a node set, a edge set, and a edge distance set.
The format of the input and answer are below:
Input:
Node set: []
Edge set: []
Edge distance set: []
Source Node: source node index
Target Node: target node index

Answer:
The shortest path from the source node to the target node is [source node index, ..., target node index]. The shortest distance is BLANK.

Input:
{input}
'''

standard_prompt_medium_5shot = '''Find the shortest path from a source node to a target node in a undirected graph. The undirected graph is represented as a node set, a edge set, and a edge distance set.
Input:
Node set: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
Edge set: [[0, 5], [1, 6], [1, 11], [1, 14], [2, 6], [2, 10], [2, 11], [3, 15], [3, 11], [4, 18], [4, 8], [4, 10], [4, 11], [4, 15], [5, 15], [5, 8], [5, 13], [6, 15], [6, 14], [7, 12], [7, 8], [7, 15], [8, 10], [8, 16], [9, 17], [9, 16], [10, 16], [11, 18], [11, 16], [12, 14], [13, 14], [14, 17], [15, 16], [16, 18], [17, 18]]
Edge distance set: [4, 2, 4, 2, 2, 3, 2, 2, 2, 5, 4, 5, 5, 3, 1, 1, 2, 5, 1, 2, 5, 4, 5, 1, 1, 1, 2, 1, 1, 3, 2, 5, 5, 2, 1]
Source Node: 0
Target Node: 18

Answer:
The shortest path from the source node to the target node is [0, 5, 8, 16, 18]. The shortest distance is 8.

Input:
Node set: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
Edge set: [[0, 12], [1, 11], [1, 3], [2, 4], [2, 5], [2, 13], [3, 6], [3, 13], [3, 15], [4, 8], [4, 5], [4, 15], [5, 12], [6, 13], [6, 16], [7, 10], [7, 11], [7, 13], [8, 9], [9, 14], [9, 13], [10, 11], [10, 12], [11, 15], [11, 13], [12, 14], [13, 14], [14, 15], [15, 16]]
Edge distance set: [5, 4, 5, 1, 3, 5, 3, 5, 2, 2, 3, 5, 5, 1, 3, 2, 3, 4, 4, 5, 1, 1, 2, 2, 3, 1, 2, 1, 3]
Source Node: 0
Target Node: 16

Answer:
The shortest path from the source node to the target node is [0, 12, 14, 15, 16]. The shortest distance is 10.

Input:
Node set: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
Edge set: [[0, 2], [1, 5], [2, 9], [3, 7], [3, 11], [4, 5], [4, 6], [5, 7], [6, 8], [7, 11], [8, 10], [9, 10], [10, 11]]
Edge distance set: [2, 2, 2, 3, 5, 3, 3, 5, 1, 2, 1, 2, 2]
Source Node: 0
Target Node: 11

Answer:
The shortest path from the source node to the target node is [0, 2, 9, 10, 11]. The shortest distance is 9.

Input:
Node set: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
Edge set: [[0, 1], [1, 9], [1, 6], [2, 3], [2, 7], [2, 9], [3, 12], [4, 7], [5, 8], [6, 11], [7, 11], [8, 11], [8, 12], [9, 10], [10, 12], [11, 12]]
Edge distance set: [3, 2, 3, 1, 2, 5, 3, 1, 5, 3, 3, 1, 5, 1, 5, 2]
Source Node: 0
Target Node: 12

Answer:
The shortest path from the source node to the target node is [0, 1, 6, 11, 12]. The shortest distance is 11.

Input:
Node set: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
Edge set: [[0, 10], [0, 8], [1, 17], [1, 6], [1, 14], [2, 5], [3, 6], [4, 16], [4, 13], [5, 14], [5, 9], [5, 10], [5, 12], [6, 17], [7, 18], [8, 13], [8, 9], [8, 11], [8, 16], [9, 11], [9, 13], [9, 14], [10, 13], [10, 14], [11, 17], [12, 17], [13, 15], [14, 15], [14, 16], [15, 18], [16, 17], [17, 18]]
Edge distance set: [4, 3, 5, 4, 1, 4, 4, 1, 5, 1, 4, 3, 5, 2, 3, 3, 5, 5, 5, 3, 1, 5, 4, 3, 3, 4, 3, 1, 2, 3, 3, 5]
Source Node: 0
Target Node: 18

Answer:
The shortest path from the source node to the target node is [0, 10, 14, 15, 18]. The shortest distance is 11.

Input:
{input}
'''

standard_prompt_medium_1shot = '''Find the shortest path from a source node to a target node in a undirected graph. The undirected graph is represented as a node set, a edge set, and a edge distance set.
Input:
Node set: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
Edge set: [[0, 5], [1, 6], [1, 11], [1, 14], [2, 6], [2, 10], [2, 11], [3, 15], [3, 11], [4, 18], [4, 8], [4, 10], [4, 11], [4, 15], [5, 15], [5, 8], [5, 13], [6, 15], [6, 14], [7, 12], [7, 8], [7, 15], [8, 10], [8, 16], [9, 17], [9, 16], [10, 16], [11, 18], [11, 16], [12, 14], [13, 14], [14, 17], [15, 16], [16, 18], [17, 18]]
Edge distance set: [4, 2, 4, 2, 2, 3, 2, 2, 2, 5, 4, 5, 5, 3, 1, 1, 2, 5, 1, 2, 5, 4, 5, 1, 1, 1, 2, 1, 1, 3, 2, 5, 5, 2, 1]
Source Node: 0
Target Node: 18

Answer:
The shortest path from the source node to the target node is [0, 5, 8, 16, 18]. The shortest distance is 8.

Input:
{input}
'''

standard_prompt_medium_zeroshot = '''Find the shortest path from a source node to a target node in a undirected graph. The undirected graph is represented as a node set, a edge set, and a edge distance set.
The format of the input and answer are below:
Input:
Node set: []
Edge set: []
Edge distance set: []
Source Node: source node index
Target Node: target node index

Answer:
The shortest path from the source node to the target node is [source node index, ..., target node index]. The shortest distance is BLANK.

Input:
{input}
'''

standard_prompt_hard = '''Find the shortest path from a source node to a target node in a undirected graph. The undirected graph is represented as a node set, a edge set, and a edge distance set.
Input:
Node set: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
Edge set: [[0, 15], [0, 11], [0, 12], [1, 18], [1, 2], [1, 3], [1, 4], [1, 22], [2, 7], [2, 3], [2, 6], [2, 16], [2, 21], [3, 6], [3, 9], [3, 19], [4, 16], [4, 9], [4, 14], [4, 24], [5, 14], [5, 10], [5, 12], [6, 16], [6, 13], [7, 9], [7, 24], [8, 13], [9, 24], [9, 15], [10, 22], [10, 11], [10, 12], [10, 14], [11, 15], [11, 18], [12, 13], [13, 17], [13, 19], [14, 20], [14, 17], [14, 24], [15, 17], [15, 19], [16, 20], [17, 21], [18, 19], [19, 20], [20, 22], [21, 24], [22, 23], [23, 24]]
Edge distance set: [5, 1, 1, 1, 2, 5, 5, 5, 5, 3, 1, 3, 2, 4, 2, 2, 1, 5, 5, 1, 3, 4, 1, 3, 2, 1, 4, 4, 2, 4, 1, 1, 5, 5, 3, 1, 1, 3, 4, 3, 3, 4, 4, 1, 1, 4, 2, 2, 1, 4, 5, 3]
Source Node: 0
Target Node: 24

Answer:
The shortest path from the source node to the target node is [0, 11, 10, 22, 20, 16, 4, 24]. The shortest distance is 7.

Input:
Node set: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
Edge set: [[0, 13], [1, 7], [1, 15], [1, 22], [2, 19], [2, 8], [3, 17], [3, 11], [3, 12], [4, 9], [4, 10], [4, 14], [5, 19], [5, 8], [6, 11], [6, 7], [7, 14], [7, 15], [8, 20], [8, 12], [9, 16], [9, 11], [10, 13], [11, 18], [11, 12], [12, 22], [13, 14], [14, 19], [15, 19], [15, 21], [16, 18], [17, 19], [17, 20], [18, 19], [19, 21], [20, 22], [21, 22]]
Edge distance set: [4, 5, 1, 5, 2, 3, 5, 1, 3, 2, 4, 5, 3, 2, 4, 2, 5, 4, 2, 5, 2, 2, 3, 4, 2, 2, 4, 2, 3, 4, 3, 4, 5, 1, 5, 1, 5]
Source Node: 0
Target Node: 22

Answer:
The shortest path from the source node to the target node is [0, 13, 14, 19, 2, 8, 20, 22]. The shortest distance is 18.

Input:
Node set: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
Edge set: [[0, 10], [1, 14], [2, 5], [2, 9], [3, 11], [3, 10], [3, 13], [4, 20], [4, 11], [5, 10], [5, 6], [5, 12], [5, 17], [5, 19], [6, 17], [6, 8], [6, 13], [6, 20], [7, 14], [7, 12], [8, 15], [9, 14], [9, 11], [10, 11], [11, 12], [12, 19], [12, 14], [13, 14], [14, 19], [14, 17], [15, 17], [16, 20], [17, 18], [18, 20], [19, 20]]
Edge distance set: [5, 3, 4, 5, 1, 3, 5, 5, 5, 4, 5, 3, 2, 4, 4, 1, 4, 5, 2, 2, 5, 3, 3, 2, 1, 5, 1, 3, 5, 1, 1, 2, 1, 1, 5]
Source Node: 0
Target Node: 20

Answer:
The shortest path from the source node to the target node is [0, 10, 11, 12, 14, 17, 18, 20]. The shortest distance is 12.

Input:
Node set: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
Edge set: [[0, 10], [1, 22], [1, 2], [1, 20], [2, 23], [2, 3], [2, 14], [3, 22], [3, 17], [4, 12], [4, 7], [5, 11], [5, 21], [6, 10], [7, 14], [7, 11], [7, 19], [8, 16], [8, 14], [9, 14], [9, 11], [10, 18], [11, 16], [12, 14], [12, 22], [12, 23], [13, 16], [14, 21], [14, 17], [15, 23], [16, 23], [17, 23], [18, 19], [18, 20], [19, 21], [20, 21], [21, 22], [22, 23]]
Edge distance set: [2, 4, 3, 1, 4, 4, 2, 4, 1, 5, 1, 1, 1, 2, 1, 1, 2, 4, 4, 1, 2, 4, 1, 5, 3, 5, 2, 2, 1, 3, 4, 3, 1, 1, 2, 4, 5, 5]
Source Node: 0
Target Node: 23

Answer:
The shortest path from the source node to the target node is [0, 10, 18, 19, 7, 14, 17, 23]. The shortest distance is 14.

Input:
Node set: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
Edge set: [[0, 9], [1, 13], [1, 4], [1, 10], [2, 8], [2, 23], [3, 18], [4, 16], [5, 16], [5, 12], [5, 20], [5, 22], [6, 12], [6, 7], [7, 13], [7, 16], [7, 25], [8, 11], [9, 21], [10, 25], [11, 17], [11, 25], [12, 20], [13, 24], [13, 17], [14, 15], [14, 17], [14, 18], [14, 22], [15, 16], [16, 17], [16, 23], [17, 19], [18, 25], [19, 22], [20, 21], [21, 22], [22, 24], [23, 25], [24, 25]]
Edge distance set: [3, 5, 3, 5, 4, 5, 5, 1, 1, 3, 1, 3, 3, 5, 1, 4, 4, 4, 3, 1, 4, 3, 2, 1, 5, 4, 4, 5, 4, 1, 3, 1, 3, 1, 2, 3, 3, 5, 3, 2]
Source Node: 0
Target Node: 25

Answer:
The shortest path from the source node to the target node is [0, 9, 21, 20, 5, 16, 23, 25]. The shortest distance is 15.

Input:
{input}
'''

# 5-shot
cot_prompt_easy_5shot = '''Find the shortest path from a source node to a target node in a undirected graph. The undirected graph is represented as a node set, a edge set, and a edge distance set.
Input:
Node set: [0, 1, 2, 3, 4]
Edge set: [[0, 3], [1, 4], [2, 4], [3, 4]]
Edge distance set: [2, 3, 5, 3]
Source Node: 0
Target Node: 4

Answer:
Starting from node 0, we arrive at node 3. The distance between these two nodes is 2.
Starting from node 3, we arrive at node 4. The distance between these two nodes is 3.
Thus, the shortest path from the source node to the target node is [0, 3, 4]. The shortest distance is 5.

Input:
Node set: [0, 1, 2, 3, 4, 5]
Edge set: [[0, 1], [1, 4], [2, 3], [3, 4], [3, 5], [4, 5]]
Edge distance set: [5, 3, 3, 4, 5, 1]
Source Node: 0
Target Node: 5

Answer:
Starting from node 0, we arrive at node 1. The distance between these two nodes is 5.
Starting from node 1, we arrive at node 4. The distance between these two nodes is 3.
Starting from node 4, we arrive at node 5. The distance between these two nodes is 1.
Thus, the shortest path from the source node to the target node is [0, 1, 4, 5]. The shortest distance is 9.

Input:
Node set: [0, 1, 2, 3, 4, 5]
Edge set: [[0, 3], [0, 2], [1, 3], [1, 5], [2, 3], [2, 5], [3, 4], [4, 5]]
Edge distance set: [2, 2, 5, 4, 2, 3, 3, 4]
Source Node: 0
Target Node: 5

Answer:
Starting from node 0, we arrive at node 2. The distance between these two nodes is 2.
Starting from node 2, we arrive at node 5. The distance between these two nodes is 3.
Thus, the shortest path from the source node to the target node is [0, 2, 5]. The shortest distance is 5.

Input:
Node set: [0, 1, 2, 3, 4]
Edge set: [[0, 2], [1, 4], [1, 2], [2, 4], [3, 4]]
Edge distance set: [5, 3, 2, 1, 1]
Source Node: 0
Target Node: 4

Answer:
Starting from node 0, we arrive at node 2. The distance between these two nodes is 5.
Starting from node 2, we arrive at node 4. The distance between these two nodes is 1.
Thus, the shortest path from the source node to the target node is [0, 2, 4]. The shortest distance is 6.

Input:
Node set: [0, 1, 2, 3, 4, 5, 6, 7, 8]
Edge set: [[0, 1], [0, 4], [1, 4], [1, 2], [2, 7], [3, 7], [3, 5], [4, 6], [5, 8], [6, 8], [7, 8]]
Edge distance set: [5, 5, 2, 5, 5, 2, 3, 2, 3, 2, 3]
Source Node: 0
Target Node: 8

Answer:
Starting from node 0, we arrive at node 4. The distance between these two nodes is 5.
Starting from node 4, we arrive at node 6. The distance between these two nodes is 2.
Starting from node 6, we arrive at node 8. The distance between these two nodes is 2.
Thus, the shortest path from the source node to the target node is [0, 4, 6, 8]. The shortest distance is 9.

Input:
{input}
'''

cot_prompt_easy_1shot = '''Find the shortest path from a source node to a target node in a undirected graph. The undirected graph is represented as a node set, a edge set, and a edge distance set.
Input:
Node set: [0, 1, 2, 3, 4]
Edge set: [[0, 3], [1, 4], [2, 4], [3, 4]]
Edge distance set: [2, 3, 5, 3]
Source Node: 0
Target Node: 4

Answer:
Starting from node 0, we arrive at node 3. The distance between these two nodes is 2.
Starting from node 3, we arrive at node 4. The distance between these two nodes is 3.
Thus, the shortest path from the source node to the target node is [0, 3, 4]. The shortest distance is 5.

Input:
{input}
'''

cot_prompt_easy_zeroshot = '''Find the shortest path from a source node to a target node in a undirected graph. The undirected graph is represented as a node set, a edge set, and a edge distance set.
Let's think step by step. The format of the input and answer are below:
Input:
Node set: []
Edge set: []
Edge distance set: []
Source Node: source node index
Target Node: target node index

Answer:
The shortest path from the source node to the target node is [source node index, ..., target node index]. The shortest distance is BLANK.

Input:
{input}
'''

cot_prompt_medium = '''Find the shortest path from a source node to a target node in a undirected graph. The undirected graph is represented as a node set, a edge set, and a edge distance set.
Input:
Node set: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
Edge set: [[0, 5], [1, 6], [1, 11], [1, 14], [2, 6], [2, 10], [2, 11], [3, 15], [3, 11], [4, 18], [4, 8], [4, 10], [4, 11], [4, 15], [5, 15], [5, 8], [5, 13], [6, 15], [6, 14], [7, 12], [7, 8], [7, 15], [8, 10], [8, 16], [9, 17], [9, 16], [10, 16], [11, 18], [11, 16], [12, 14], [13, 14], [14, 17], [15, 16], [16, 18], [17, 18]]
Edge distance set: [4, 2, 4, 2, 2, 3, 2, 2, 2, 5, 4, 5, 5, 3, 1, 1, 2, 5, 1, 2, 5, 4, 5, 1, 1, 1, 2, 1, 1, 3, 2, 5, 5, 2, 1]
Source Node: 0
Target Node: 18

Answer:
Starting from node 0, we arrive at node 5. The distance between these two nodes is 4.
Starting from node 5, we arrive at node 8. The distance between these two nodes is 1.
Starting from node 8, we arrive at node 16. The distance between these two nodes is 1.
Starting from node 16, we arrive at node 18. The distance between these two nodes is 2.
Thus, the shortest path from the source node to the target node is [0, 5, 8, 16, 18]. The shortest distance is 8.

Input:
Node set: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
Edge set: [[0, 12], [1, 11], [1, 3], [2, 4], [2, 5], [2, 13], [3, 6], [3, 13], [3, 15], [4, 8], [4, 5], [4, 15], [5, 12], [6, 13], [6, 16], [7, 10], [7, 11], [7, 13], [8, 9], [9, 14], [9, 13], [10, 11], [10, 12], [11, 15], [11, 13], [12, 14], [13, 14], [14, 15], [15, 16]]
Edge distance set: [5, 4, 5, 1, 3, 5, 3, 5, 2, 2, 3, 5, 5, 1, 3, 2, 3, 4, 4, 5, 1, 1, 2, 2, 3, 1, 2, 1, 3]
Source Node: 0
Target Node: 16

Answer:
Starting from node 0, we arrive at node 12. The distance between these two nodes is 5.
Starting from node 12, we arrive at node 14. The distance between these two nodes is 1.
Starting from node 14, we arrive at node 15. The distance between these two nodes is 1.
Starting from node 15, we arrive at node 16. The distance between these two nodes is 3.
Thus, the shortest path from the source node to the target node is [0, 12, 14, 15, 16]. The shortest distance is 10.

Input:
Node set: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
Edge set: [[0, 2], [1, 5], [2, 9], [3, 7], [3, 11], [4, 5], [4, 6], [5, 7], [6, 8], [7, 11], [8, 10], [9, 10], [10, 11]]
Edge distance set: [2, 2, 2, 3, 5, 3, 3, 5, 1, 2, 1, 2, 2]
Source Node: 0
Target Node: 11

Answer:
Starting from node 0, we arrive at node 2. The distance between these two nodes is 2.
Starting from node 2, we arrive at node 9. The distance between these two nodes is 2.
Starting from node 9, we arrive at node 10. The distance between these two nodes is 2.
Starting from node 10, we arrive at node 11. The distance between these two nodes is 2.
Thus, the shortest path from the source node to the target node is [0, 2, 9, 10, 11]. The shortest distance is 8.

Input:
Node set: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
Edge set: [[0, 1], [1, 9], [1, 6], [2, 3], [2, 7], [2, 9], [3, 12], [4, 7], [5, 8], [6, 11], [7, 11], [8, 11], [8, 12], [9, 10], [10, 12], [11, 12]]
Edge distance set: [3, 2, 3, 1, 2, 5, 3, 1, 5, 3, 3, 1, 5, 1, 5, 2]
Source Node: 0
Target Node: 12

Answer:
Starting from node 0, we arrive at node 1. The distance between these two nodes is 3.
Starting from node 1, we arrive at node 6. The distance between these two nodes is 3.
Starting from node 6, we arrive at node 11. The distance between these two nodes is 3.
Starting from node 11, we arrive at node 12. The distance between these two nodes is 2.
Thus, the shortest path from the source node to the target node is [0, 1, 6, 11, 12]. The shortest distance is 11.

Input:
Node set: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
Edge set: [[0, 10], [0, 8], [1, 17], [1, 6], [1, 14], [2, 5], [3, 6], [4, 16], [4, 13], [5, 14], [5, 9], [5, 10], [5, 12], [6, 17], [7, 18], [8, 13], [8, 9], [8, 11], [8, 16], [9, 11], [9, 13], [9, 14], [10, 13], [10, 14], [11, 17], [12, 17], [13, 15], [14, 15], [14, 16], [15, 18], [16, 17], [17, 18]]
Edge distance set: [4, 3, 5, 4, 1, 4, 4, 1, 5, 1, 4, 3, 5, 2, 3, 3, 5, 5, 5, 3, 1, 5, 4, 3, 3, 4, 3, 1, 2, 3, 3, 5]
Source Node: 0
Target Node: 18

Answer:
Starting from node 0, we arrive at node 10. The distance between these two nodes is 4.
Starting from node 10, we arrive at node 14. The distance between these two nodes is 3.
Starting from node 14, we arrive at node 15. The distance between these two nodes is 1.
Starting from node 15, we arrive at node 18. The distance between these two nodes is 3.
The shortest path from the source node to the target node is [0, 10, 14, 15, 18]. The shortest distance is 11.

Input:
{input}
'''

cot_prompt_hard = '''Find the shortest path from a source node to a target node in a undirected graph. The undirected graph is represented as a node set, a edge set, and a edge distance set.
Input:
Node set: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
Edge set: [[0, 15], [0, 11], [0, 12], [1, 18], [1, 2], [1, 3], [1, 4], [1, 22], [2, 7], [2, 3], [2, 6], [2, 16], [2, 21], [3, 6], [3, 9], [3, 19], [4, 16], [4, 9], [4, 14], [4, 24], [5, 14], [5, 10], [5, 12], [6, 16], [6, 13], [7, 9], [7, 24], [8, 13], [9, 24], [9, 15], [10, 22], [10, 11], [10, 12], [10, 14], [11, 15], [11, 18], [12, 13], [13, 17], [13, 19], [14, 20], [14, 17], [14, 24], [15, 17], [15, 19], [16, 20], [17, 21], [18, 19], [19, 20], [20, 22], [21, 24], [22, 23], [23, 24]]
Edge distance set: [5, 1, 1, 1, 2, 5, 5, 5, 5, 3, 1, 3, 2, 4, 2, 2, 1, 5, 5, 1, 3, 4, 1, 3, 2, 1, 4, 4, 2, 4, 1, 1, 5, 5, 3, 1, 1, 3, 4, 3, 3, 4, 4, 1, 1, 4, 2, 2, 1, 4, 5, 3]
Source Node: 0
Target Node: 24

Answer:
The shortest path from the source node to the target node is [0, 11, 10, 22, 20, 16, 4, 24]. The shortest distance is 7.

Input:
Node set: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
Edge set: [[0, 13], [1, 7], [1, 15], [1, 22], [2, 19], [2, 8], [3, 17], [3, 11], [3, 12], [4, 9], [4, 10], [4, 14], [5, 19], [5, 8], [6, 11], [6, 7], [7, 14], [7, 15], [8, 20], [8, 12], [9, 16], [9, 11], [10, 13], [11, 18], [11, 12], [12, 22], [13, 14], [14, 19], [15, 19], [15, 21], [16, 18], [17, 19], [17, 20], [18, 19], [19, 21], [20, 22], [21, 22]]
Edge distance set: [4, 5, 1, 5, 2, 3, 5, 1, 3, 2, 4, 5, 3, 2, 4, 2, 5, 4, 2, 5, 2, 2, 3, 4, 2, 2, 4, 2, 3, 4, 3, 4, 5, 1, 5, 1, 5]
Source Node: 0
Target Node: 22

Answer:
The shortest path from the source node to the target node is [0, 13, 14, 19, 2, 8, 20, 22]. The shortest distance is 18.

Input:
Node set: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
Edge set: [[0, 10], [1, 14], [2, 5], [2, 9], [3, 11], [3, 10], [3, 13], [4, 20], [4, 11], [5, 10], [5, 6], [5, 12], [5, 17], [5, 19], [6, 17], [6, 8], [6, 13], [6, 20], [7, 14], [7, 12], [8, 15], [9, 14], [9, 11], [10, 11], [11, 12], [12, 19], [12, 14], [13, 14], [14, 19], [14, 17], [15, 17], [16, 20], [17, 18], [18, 20], [19, 20]]
Edge distance set: [5, 3, 4, 5, 1, 3, 5, 5, 5, 4, 5, 3, 2, 4, 4, 1, 4, 5, 2, 2, 5, 3, 3, 2, 1, 5, 1, 3, 5, 1, 1, 2, 1, 1, 5]
Source Node: 0
Target Node: 20

Answer:
The shortest path from the source node to the target node is [0, 10, 11, 12, 14, 17, 18, 20]. The shortest distance is 12.

Input:
Node set: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
Edge set: [[0, 10], [1, 22], [1, 2], [1, 20], [2, 23], [2, 3], [2, 14], [3, 22], [3, 17], [4, 12], [4, 7], [5, 11], [5, 21], [6, 10], [7, 14], [7, 11], [7, 19], [8, 16], [8, 14], [9, 14], [9, 11], [10, 18], [11, 16], [12, 14], [12, 22], [12, 23], [13, 16], [14, 21], [14, 17], [15, 23], [16, 23], [17, 23], [18, 19], [18, 20], [19, 21], [20, 21], [21, 22], [22, 23]]
Edge distance set: [2, 4, 3, 1, 4, 4, 2, 4, 1, 5, 1, 1, 1, 2, 1, 1, 2, 4, 4, 1, 2, 4, 1, 5, 3, 5, 2, 2, 1, 3, 4, 3, 1, 1, 2, 4, 5, 5]
Source Node: 0
Target Node: 23

Answer:
The shortest path from the source node to the target node is [0, 10, 18, 19, 7, 14, 17, 23]. The shortest distance is 14.

Input:
Node set: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
Edge set: [[0, 9], [1, 13], [1, 4], [1, 10], [2, 8], [2, 23], [3, 18], [4, 16], [5, 16], [5, 12], [5, 20], [5, 22], [6, 12], [6, 7], [7, 13], [7, 16], [7, 25], [8, 11], [9, 21], [10, 25], [11, 17], [11, 25], [12, 20], [13, 24], [13, 17], [14, 15], [14, 17], [14, 18], [14, 22], [15, 16], [16, 17], [16, 23], [17, 19], [18, 25], [19, 22], [20, 21], [21, 22], [22, 24], [23, 25], [24, 25]]
Edge distance set: [3, 5, 3, 5, 4, 5, 5, 1, 1, 3, 1, 3, 3, 5, 1, 4, 4, 4, 3, 1, 4, 3, 2, 1, 5, 4, 4, 5, 4, 1, 3, 1, 3, 1, 2, 3, 3, 5, 3, 2]
Source Node: 0
Target Node: 25

Answer:
The shortest path from the source node to the target node is [0, 9, 21, 20, 5, 16, 23, 25]. The shortest distance is 15.

Input:
{input}
'''










bog_prompt_easy_5shot = '''Find the shortest path from a source node to a target node in a undirected graph. The undirected graph is represented as a node set, a edge set, and a edge distance set.
Input:
Node set: [0, 1, 2, 3, 4]
Edge set: [[0, 3], [1, 4], [2, 4], [3, 4]]
Edge distance set: [2, 3, 5, 3]
Source Node: 0
Target Node: 4

Answer:
Let's construct a graph with the nodes and edges first. The shortest path from the source node to the target node is [0, 3, 4]. The shortest distance is 5.

Input:
Node set: [0, 1, 2, 3, 4, 5]
Edge set: [[0, 1], [1, 4], [2, 3], [3, 4], [3, 5], [4, 5]]
Edge distance set: [5, 3, 3, 4, 5, 1]
Source Node: 0
Target Node: 5

Answer:
Let's construct a graph with the nodes and edges first. The shortest path from the source node to the target node is [0, 1, 4, 5]. The shortest distance is 9.

Input:
Node set: [0, 1, 2, 3, 4, 5]
Edge set: [[0, 3], [0, 2], [1, 3], [1, 5], [2, 3], [2, 5], [3, 4], [4, 5]]
Edge distance set: [2, 2, 5, 4, 2, 3, 3, 4]
Source Node: 0
Target Node: 5

Answer:
Let's construct a graph with the nodes and edges first. The shortest path from the source node to the target node is [0, 2, 5]. The shortest distance is 5.

Input:
Node set: [0, 1, 2, 3, 4]
Edge set: [[0, 2], [1, 4], [1, 2], [2, 4], [3, 4]]
Edge distance set: [5, 3, 2, 1, 1]
Source Node: 0
Target Node: 4

Answer:
Let's construct a graph with the nodes and edges first. The shortest path from the source node to the target node is [0, 2, 4]. The shortest distance is 6.

Input:
Node set: [0, 1, 2, 3, 4, 5, 6, 7, 8]
Edge set: [[0, 1], [0, 4], [1, 4], [1, 2], [2, 7], [3, 7], [3, 5], [4, 6], [5, 8], [6, 8], [7, 8]]
Edge distance set: [5, 5, 2, 5, 5, 2, 3, 2, 3, 2, 3]
Source Node: 0
Target Node: 8

Answer:
Let's construct a graph with the nodes and edges first. The shortest path from the source node to the target node is [0, 4, 6, 8]. The shortest distance is 9.

Input:
{input}
'''

bog_prompt_easy_1shot = '''Find the shortest path from a source node to a target node in a undirected graph. The undirected graph is represented as a node set, a edge set, and a edge distance set.
Let's construct a graph with the nodes and edges first.
Input:
Node set: [0, 1, 2, 3, 4]
Edge set: [[0, 3], [1, 4], [2, 4], [3, 4]]
Edge distance set: [2, 3, 5, 3]
Source Node: 0
Target Node: 4

Answer:
The shortest path from the source node to the target node is [0, 3, 4]. The shortest distance is 5.

Input:
{input}
'''

bog_prompt_easy_zeroshot = '''Find the shortest path from a source node to a target node in a undirected graph. The undirected graph is represented as a node set, a edge set, and a edge distance set.
Let's construct a graph with the nodes and edges first. The format of the input and answer are below:
Input:
Node set: []
Edge set: []
Edge distance set: []
Source Node: source node index
Target Node: target node index

Answer:
The shortest path from the source node to the target node is [source node index, ..., target node index]. The shortest distance is BLANK.

Input:
{input}
'''

boglg_prompt_easy_1shot = '''Find the shortest path from a source node to a target node in a undirected graph. The undirected graph is represented as a node set, a edge set, and a edge distance set.
Let's use dijkstra algorithm to solve this problem.
Input:
Node set: [0, 1, 2, 3, 4]
Edge set: [[0, 3], [1, 4], [2, 4], [3, 4]]
Edge distance set: [2, 3, 5, 3]
Source Node: 0
Target Node: 4

Answer:
The shortest path from the source node to the target node is [0, 3, 4]. The shortest distance is 5.

Input:
{input}
'''

boglg_prompt_easy_zeroshot = '''Find the shortest path from a source node to a target node in a undirected graph. The undirected graph is represented as a node set, a edge set, and a edge distance set.
Let's use dijkstra algorithm to solve this problem. The format of the input and answer are below:
Input:
Node set: []
Edge set: []
Edge distance set: []
Source Node: source node index
Target Node: target node index

Answer:
The shortest path from the source node to the target node is [source node index, ..., target node index]. The shortest distance is BLANK.

Input:
{input}
'''



bog_prompt_medium = '''Find the shortest path from a source node to a target node in a undirected graph. The undirected graph is represented as a node set, a edge set, and a edge distance set.
Input:
Node set: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
Edge set: [[0, 5], [1, 6], [1, 11], [1, 14], [2, 6], [2, 10], [2, 11], [3, 15], [3, 11], [4, 18], [4, 8], [4, 10], [4, 11], [4, 15], [5, 15], [5, 8], [5, 13], [6, 15], [6, 14], [7, 12], [7, 8], [7, 15], [8, 10], [8, 16], [9, 17], [9, 16], [10, 16], [11, 18], [11, 16], [12, 14], [13, 14], [14, 17], [15, 16], [16, 18], [17, 18]]
Edge distance set: [4, 2, 4, 2, 2, 3, 2, 2, 2, 5, 4, 5, 5, 3, 1, 1, 2, 5, 1, 2, 5, 4, 5, 1, 1, 1, 2, 1, 1, 3, 2, 5, 5, 2, 1]
Source Node: 0
Target Node: 18

Answer:
Let's construct a graph with the nodes and edges first. The shortest path from the source node to the target node is [0, 5, 8, 16, 18]. The shortest distance is 8.

Input:
Node set: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
Edge set: [[0, 12], [1, 11], [1, 3], [2, 4], [2, 5], [2, 13], [3, 6], [3, 13], [3, 15], [4, 8], [4, 5], [4, 15], [5, 12], [6, 13], [6, 16], [7, 10], [7, 11], [7, 13], [8, 9], [9, 14], [9, 13], [10, 11], [10, 12], [11, 15], [11, 13], [12, 14], [13, 14], [14, 15], [15, 16]]
Edge distance set: [5, 4, 5, 1, 3, 5, 3, 5, 2, 2, 3, 5, 5, 1, 3, 2, 3, 4, 4, 5, 1, 1, 2, 2, 3, 1, 2, 1, 3]
Source Node: 0
Target Node: 16

Answer:
Let's construct a graph with the nodes and edges first. Let's construct a graph with the nodes and edges first. The shortest path from the source node to the target node is [0, 12, 14, 15, 16]. The shortest distance is 10.

Input:
Node set: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
Edge set: [[0, 2], [1, 5], [2, 9], [3, 7], [3, 11], [4, 5], [4, 6], [5, 7], [6, 8], [7, 11], [8, 10], [9, 10], [10, 11]]
Edge distance set: [2, 2, 2, 3, 5, 3, 3, 5, 1, 2, 1, 2, 2]
Source Node: 0
Target Node: 11

Answer:
Let's construct a graph with the nodes and edges first. The shortest path from the source node to the target node is [0, 2, 9, 10, 11]. The shortest distance is 9.

Input:
Node set: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
Edge set: [[0, 1], [1, 9], [1, 6], [2, 3], [2, 7], [2, 9], [3, 12], [4, 7], [5, 8], [6, 11], [7, 11], [8, 11], [8, 12], [9, 10], [10, 12], [11, 12]]
Edge distance set: [3, 2, 3, 1, 2, 5, 3, 1, 5, 3, 3, 1, 5, 1, 5, 2]
Source Node: 0
Target Node: 12

Answer:
Let's construct a graph with the nodes and edges first. The shortest path from the source node to the target node is [0, 1, 6, 11, 12]. The shortest distance is 11.

Input:
Node set: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
Edge set: [[0, 10], [0, 8], [1, 17], [1, 6], [1, 14], [2, 5], [3, 6], [4, 16], [4, 13], [5, 14], [5, 9], [5, 10], [5, 12], [6, 17], [7, 18], [8, 13], [8, 9], [8, 11], [8, 16], [9, 11], [9, 13], [9, 14], [10, 13], [10, 14], [11, 17], [12, 17], [13, 15], [14, 15], [14, 16], [15, 18], [16, 17], [17, 18]]
Edge distance set: [4, 3, 5, 4, 1, 4, 4, 1, 5, 1, 4, 3, 5, 2, 3, 3, 5, 5, 5, 3, 1, 5, 4, 3, 3, 4, 3, 1, 2, 3, 3, 5]
Source Node: 0
Target Node: 18

Answer:
Let's construct a graph with the nodes and edges first. The shortest path from the source node to the target node is [0, 10, 14, 15, 18]. The shortest distance is 11.

Input:
{input}
'''







### GoT prompt starts here
neigborhood_propose_prompt = '''The undirected graph is represented as a node set, a edge set. Given an input node, find its neighborhood nodes and save them in a list.

Input:
Node set: [0, 1, 2, 3, 4]
Edge set: [[0, 3], [1, 4], [2, 4], [3, 4]]
Input Node: 4

Answer:
The neighborhood node list of the input node is [1, 2, 3].

Input:
Node set: [0, 1, 2, 3, 4, 5, 6, 7, 8]
Edge set: [[0, 1], [0, 4], [1, 4], [1, 2], [2, 7], [3, 7], [3, 5], [4, 6], [5, 8], [6, 8], [7, 8]]
Input Node: 7

Answer:
The neighborhood node list of the input node is [2, 3, 8].

Input:
Node set: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
Edge set: [[0, 5], [1, 6], [1, 11], [1, 14], [2, 6], [2, 10], [2, 11], [3, 15], [3, 11], [4, 18], [4, 8], [4, 10], [4, 11], [4, 15], [5, 15], [5, 8], [5, 13], [6, 15], [6, 14], [7, 12], [7, 8], [7, 15], [8, 10], [8, 16], [9, 17], [9, 16], [10, 16], [11, 18], [11, 16], [12, 14], [13, 14], [14, 17], [15, 16], [16, 18], [17, 18]]
Input Node: 12

Answer:
The neighborhood node list of the input node is [7, 14].

Input:
Node set: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
Edge set: [[0, 2], [1, 5], [2, 9], [3, 7], [3, 11], [4, 5], [4, 6], [5, 7], [6, 8], [7, 11], [8, 10], [9, 10], [10, 11]]
Input Node: 11

Answer:
The neighborhood node list of the input node is [3, 7, 10].

Input:
Node set: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
Edge set: [[0, 1], [1, 9], [1, 6], [2, 3], [2, 7], [2, 9], [3, 12], [4, 7], [5, 8], [6, 11], [7, 11], [8, 11], [8, 12], [9, 10], [10, 12], [11, 12]]
Input Node: 12

Answer:
The neighborhood node list of the input node is [3, 8, 10, 11].

Input:
{input}
'''

# the neighborhood slove prompt is the same as the original one for null problem solving

neighborhood_aggregation_prompt = '''The undirected graph is represented as a node set, a edge set and a edge distance set. The edges in the edge set are reversible. We have the hints of one or several intermediate paths from the source node to some intermediate nodes. Please use these hints to find the shortest path from the source node the the target node.

Input:
Node set: [0, 1, 2, 3, 4]
Edge set: [[0, 3], [1, 4], [2, 4], [3, 4]]
Edge distance set: [2, 3, 5, 3]
The hints are:
The shortest path from the source node 0 to the intermediate node 3 is [0, 3]. The shortest distance is 2.
The shortest path from the source node 0 to the intermediate node 1 is [0, 3, 4, 1]. The shortest distance is 8.
The shortest path from the source node 0 to the intermediate node 2 is [0, 3, 4, 2]. The shortest distance is 10.
Use the above hint to find the shortest path from the source node 0 to the target node 4. 

Answer:
Using the above hints, the shortest path from the source node 0 to the target node 4 is [0, 3, 4]. The shortest distance is 5.

Input:
Node set: [0, 1, 2, 3, 4, 5]
Edge set: [[0, 3], [0, 2], [1, 3], [1, 5], [2, 3], [2, 5], [3, 4], [4, 5]]
Edge distance set: [2, 2, 5, 4, 2, 3, 3, 4]
The hints are:
The shortest path from the source node 0 to the intermediate node 1 is [0, 3, 1]. The shortest distance is 7.
The shortest path from the source node 0 to the intermediate node 4 is [0, 3, 4]. The shortest distance is 5.
The shortest path from the source node 0 to the intermediate node 2 is [0, 2]. The shortest distance is 2.
Use the above hint to find the shortest path from the source node 0 to the target node 5. 

Answer:
Using the above hints, the shortest path from the source node 0 to the target node 5 is [0, 2, 5]. The shortest distance is 5.

Input:
Node set: [0, 1, 2, 3, 4, 5]
Edge set: [[0, 3], [0, 2], [1, 3], [1, 5], [2, 3], [2, 5], [3, 4], [4, 5]]
Edge distance set: [2, 2, 5, 4, 2, 3, 3, 4]
The hints are:
The shortest path from the source node 0 to the intermediate node 1 is [0, 3]. The shortest distance is 2.
The shortest path from the source node 0 to the intermediate node 4 is [0, 2, 5]. The shortest distance is 5.
Use the above hint to find the shortest path from the source node 0 to the target node 4. 

Answer:
Using the above hints, the shortest path from the source node 0 to the target node 4 is [0, 3, 4]. The shortest distance is 5.

Input:
Node set: [0, 1, 2, 3, 4, 5, 6, 7, 8]
Edge set: [[0, 1], [0, 4], [1, 4], [1, 2], [2, 7], [3, 7], [3, 5], [4, 6], [5, 8], [6, 8], [7, 8]]
Edge distance set: [5, 5, 2, 5, 5, 2, 3, 2, 3, 2, 3]
The hints are:
The shortest path from the source node 0 to the intermediate node 8 is [0, 1, 2, 7, 8]. The shortest distance is 18.
The shortest path from the source node 0 to the intermediate node 4 is [0, 4]. The shortest distance is 5.
Use the above hint to find the shortest path from the source node 0 to the target node 6. 

Answer:
Using the above hints, the shortest path from the source node 0 to the target node 6 is [0, 4, 6]. The shortest distance is 7.

Input:
Node set: [0, 1, 2, 3, 4, 5, 6, 7, 8]
Edge set: [[0, 1], [0, 4], [1, 4], [1, 2], [2, 7], [3, 7], [3, 5], [4, 6], [5, 8], [6, 8], [7, 8]]
Edge distance set: [5, 5, 2, 5, 5, 2, 3, 2, 3, 2, 3]
The hints are:
The shortest path from the source node 0 to the intermediate node 8 is [0, 1, 2]. The shortest distance is 10.
The shortest path from the source node 0 to the intermediate node 4 is [0, 4, 6, 8]. The shortest distance is 9.
Use the above hint to find the shortest path from the source node 0 to the target node 7. 

Answer:
Using the above hints, the shortest path from the source node 0 to the target node 6 is [0, 4, 6, 8, 7]. The shortest distance is 12.

Input:
{input}
'''

readout_prompt = '''The undirected graph is represented as a node set, a edge set and a edge distance set. The edges in the edge set are reversible. We have two solution candidates to the shortest path from the source node to the target node. Please verify these two solution candidates and output the better one. If two solutions are the same and both valid, output the first solution. Notice that the shortest distance provided in the hints may be wrong. Check it before use it.

Input:
Node set: [0, 1, 2, 3, 4, 5]
Edge set: [[0, 3], [0, 2], [1, 3], [1, 5], [2, 3], [2, 5], [3, 4], [4, 5]]
Edge distance set: [2, 2, 5, 4, 2, 3, 3, 4]
Source Node: 0
Target Node: 5
Solution 1: The shortest path from the source node 0 to the target node 5 is [0, 2, 5]. The shortest distance is 5.
Solution 2: The shortest path from the source node 0 to the target node 5 is [0, 3, 4, 5]. The shortest distance is 9.

Answer:
Solution 1 is valid because it can reach the target node and all the edges in Solution 1 are real edges in the Edge set. Solution 2 is valid because it can reach the target node and all the edges in Solution 2 are real edges in the Edge set. Solution 1 is better than Solution 2 because the path in Solution 1 is shorter than that in Solution 2. So the shortest path from the source node 0 to the target node 5 is [0, 2, 5]. The shortest distance is 5.

Input:
Node set: [0, 1, 2, 3, 4, 5]
Edge set: [[0, 3], [0, 2], [1, 3], [1, 5], [2, 3], [2, 5], [3, 4], [4, 5]]
Edge distance set: [2, 2, 5, 4, 2, 3, 3, 4]
Source Node: 0
Target Node: 5
Solution 1: The shortest path from the source node 0 to the target node 5 is [0, 3, 5]. The shortest distance is 3.
Solution 2: The shortest path from the source node 0 to the target node 5 is [0, 2, 5]. The shortest distance is 5.

Answer:
Solution 1 is invalid because the edge [3, 5] in Solution 1 is not a real edge in the Edge Set. Solution 2 is valid because it can reach the target node and all the edges in Solution 2 are real edges in the Edge set. Althought the path in Solution 1 is shorter than that in Solution 2, solution 2 is better than Solution 1 because Solution 1 is an invalid path. So the shortest path from the source node 0 to the target node 5 is [0, 2, 5]. The shortest distance is 5.

Input:
Node set: [0, 1, 2, 3, 4, 5]
Edge set: [[0, 3], [0, 2], [1, 3], [1, 5], [2, 3], [2, 5], [3, 4], [4, 5]]
Edge distance set: [2, 2, 5, 4, 2, 3, 3, 4]
Source Node: 0
Target Node: 5
Solution 1: The shortest path from the source node 0 to the target node 5 is [0, 3, 5]. The shortest distance is 5.
Solution 2: The shortest path from the source node 0 to the target node 5 is [0, 3, 5]. The shortest distance is 5.

Answer:
Solution 1 is valid because it can reach the target node and all the edges in Solution 1 are real edges in the Edge set. Solution 2 is valid because it can reach the target node and all the edges in Solution 2 are real edges in the Edge set. Solution 1 and Solution 2 are the same. So the shortest path from the source node 0 to the target node 5 is [0, 3, 5]. The shortest distance is 5.

Input:
Node set: [0, 1, 2, 3, 4, 5, 6, 7, 8]
Edge set: [[0, 1], [0, 4], [1, 4], [1, 2], [2, 7], [3, 7], [3, 5], [4, 6], [5, 8], [6, 8], [7, 8]]
Edge distance set: [5, 5, 2, 5, 5, 2, 3, 2, 3, 2, 3]
Source Node: 0
Target Node: 8
Solution 1: The shortest path from the source node 0 to the target node 8 is [0, 1, 2, 7, 8]. The shortest distance is 18.
Solution 2: The shortest path from the source node 0 to the target node 8 is [0, 4, 6, 8]. The shortest distance is 9.

Answer:
Solution 1 is valid because it can reach the target node and all the edges in Solution 1 are real edges in the Edge set. Solution 2 is valid because it can reach the target node and all the edges in Solution 2 are real edges in the Edge set. Solution 2 is better than Solution 1 because the path in Solution 2 is shorter than that in Solution 1. So the shortest path from the source node 0 to the target node 8 is [0, 4, 6, 8]. The shortest distance is 9.

Input:
Node set: [0, 1, 2, 3, 4, 5, 6, 7, 8]
Edge set: [[0, 1], [0, 4], [1, 4], [1, 2], [2, 7], [3, 7], [3, 5], [4, 6], [5, 8], [6, 8], [7, 8]]
Edge distance set: [5, 5, 2, 5, 5, 2, 3, 2, 3, 2, 3]
Source Node: 0
Target Node: 8
Solution 1: The shortest path from the source node 0 to the target node 8 is [0, 1, 4]. The shortest distance is 7.
Solution 2: The shortest path from the source node 0 to the target node 8 is [0, 4, 6, 8]. The shortest distance is 9.

Answer:
Solution 1 is invalid because it cannot reach the target node. Solution 2 is valid because it can reach the target node and all the edges in Solution 2 are real edges in the Edge set. Althought the path in Solution 1 is shorter than that in Solution 2, Solution 2 is better than Solution 1 because Solution 2 can reach the target node. So the shortest path from the source node 0 to the target node 8 is [0, 4, 6, 8]. The shortest distance is 9.

Input:
{input}
'''

neighborhood_one_by_one_aggregation_prompt_solve = '''The undirected graph is represented as a node set, a edge set and a edge distance set. The edges in the edge set are reversible. We have the hints of one or several intermediate paths from the source node to some intermediate nodes.

Input:
{input}

Here is a hint of a shortest path from the source node 0 to an intermediate node:
{neighborhood}

Please use the above hint to find a shortest path from the {source_node_placeholder_1} to the {target_node_placeholder_1}. Your answer should go after 'Answer:' and follow the below format.

Answer:
Using the above hints, the shortest path from the {source_node_placeholder_2} to the {target_node_placeholder_2} is [source node index, ..., target node index]. The shortest distance is BLANK.
'''

# one-by-one score-evaluation in the aggregation part

neighborhood_one_by_one_aggregation_prompt_eval_1 = '''We have several candidate solutions on the shortest path from the source node to the target node in an undirected graph. The undirected graph is represented as a node set, a edge set and a edge distance set. The edges in the edge set are reversible. Please find the best solution from the candidate solutions. Analyze each candidate solution and conclude the best solution with "The best solution is {s}", where s the integer id of the choice.
'''

neighborhood_one_by_one_aggregation_prompt_eval_2 = '''
Input graph:
{input}

Source Node:
{source_node}

Target Node:
{target_node}

Candidate solutions on the shortest path from the source node to the target node:
{candidate_solutions}
'''


neigborhood_evaluate_prompt_5shot = '''Given several input nodes, evaluate these input nodes and find the most promising one that forms the shortest path to the target node.

Input:
Node set: [0, 1, 2, 3, 4, 5, 6]
Edge set: [[0, 1], [0, 3], [0, 4], [1, 4], [2, 4], [3, 4], [2, 5], [2, 6]]
Edge distance set: [2, 2, 2, 3, 3, 5, 4, 1]
Input Nodes: [3, 4]
Target Node: 6

Answer:
The most promising one that forms the shortest path to the target node in the input nodes is 4. The shortest path is [4, 2, 6]. The shortest distance is 4.

Input:
Node set: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
Edge set: [[0, 5], [1, 6], [1, 11], [1, 14], [2, 6], [2, 10], [2, 11], [3, 15], [3, 11], [4, 18], [4, 8], [4, 10], [4, 11], [4, 15], [5, 15], [5, 8], [5, 13], [6, 15], [6, 14], [7, 12], [7, 8], [7, 15], [8, 10], [8, 16], [9, 17], [9, 16], [10, 16], [11, 18], [11, 16], [12, 14], [13, 14], [14, 17], [15, 16], [16, 18], [17, 18]]
Edge distance set: [4, 2, 4, 2, 2, 3, 2, 2, 2, 5, 4, 5, 5, 3, 1, 1, 2, 5, 1, 2, 5, 4, 5, 1, 1, 1, 2, 1, 1, 3, 2, 5, 5, 2, 1]
Input Nodes: [1, 5, 8, 16]
Target Node: 18

Answer:
The most promising one that forms the shortest path to the target node in the input nodes is 16. The shortest path is [16, 18]. The shortest distance is 2.

Input:
Node set: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
Edge set: [[0, 12], [1, 11], [1, 3], [2, 4], [2, 5], [2, 13], [3, 6], [3, 13], [3, 15], [4, 8], [4, 5], [4, 15], [5, 12], [6, 13], [6, 16], [7, 10], [7, 11], [7, 13], [8, 9], [9, 14], [9, 13], [10, 11], [10, 12], [11, 15], [11, 13], [12, 14], [13, 14], [14, 15], [15, 16]]
Edge distance set: [5, 4, 5, 1, 3, 5, 3, 5, 2, 2, 3, 5, 5, 1, 3, 2, 3, 4, 4, 5, 1, 1, 2, 2, 3, 1, 2, 1, 3]
Input Nodes: [5, 10, 14] 
Target Node: 16

Answer:
The most promising one that forms the shortest path to the target node in the input nodes is 14. The shortest path is [14, 15, 16]. The shortest distance is 4.

Input:
Node set: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
Edge set: [[0, 2], [1, 5], [2, 9], [3, 7], [3, 11], [4, 5], [4, 6], [5, 7], [6, 8], [7, 11], [8, 10], [9, 10], [10, 11]]
Edge distance set: [2, 2, 2, 3, 5, 3, 3, 5, 1, 100, 50, 2, 2]
Input Nodes: [2, 7, 8]
Target Node: 11

Answer:
The most promising one that forms the shortest path to the target node in the input nodes is 2. The shortest path is [2, 9, 10, 11]. The shortest distance is 7.

Input:
Node set: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
Edge set: [[0, 1], [1, 9], [1, 6], [2, 3], [2, 7], [2, 9], [3, 12], [4, 7], [5, 8], [6, 11], [7, 11], [8, 11], [8, 12], [9, 10], [10, 12], [11, 12]]
Edge distance set: [3, 2, 3, 1, 2, 5, 3, 1, 5, 3, 3, 1, 5, 1, 5, 2]
Input Nodes: [6, 7, 8, 12]
Target Node: 12

Answer:
The most promising one that forms the shortest path to the target node in the input nodes is 12. The shortest path is [12]. The shortest distance is 0.

Input:
{input}
'''


neigborhood_evaluate_prompt_1shot = '''Given several input nodes, evaluate these input nodes and find the most promising one that forms the shortest path to the target node.

Input:
Node set: [0, 1, 2, 3, 4, 5, 6]
Edge set: [[0, 1], [0, 3], [0, 4], [1, 4], [2, 4], [3, 4], [2, 5], [2, 6]]
Edge distance set: [2, 2, 2, 3, 3, 5, 4, 1]
Input Nodes: [3, 4]
Target Node: 6

Answer:
The most promising one that forms the shortest path to the target node in the input nodes is 4. The shortest path is [4, 2, 6]. The shortest distance is 4.

Input:
{input}
'''

neigborhood_evaluate_prompt_easy_zeroshot = '''Given several input nodes, evaluate these input nodes and find the most promising one that forms the shortest path to the target node.

Input:
Node set: []
Edge set: []
Edge distance set: []
Input Nodes: []
Target Node: target node index

Answer:
The most promising one that forms the shortest path to the target node in the input nodes is [input node index]. The shortest path is [input node index, ..., target node index]. The shortest distance is BLANK.

Input:
{input}
'''