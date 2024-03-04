# 5-shot
standard_prompt_easy_5shot = '''Find the shortest path from a source node to a target node in an undirected graph.
Input:
In an undirected graph, the nodes are numbered from 0 to 4, and the edges are:
an edge between node 0 and node 3 with distance 2,
an edge between node 1 and node 4 with distance 3,
an edge between node 2 and node 4 with distance 5,
an edge between node 3 and node 4 with distance 3.
Source Node: 0
Target Node: 4

Answer:
The shortest path from the source node to the target node is [0, 3, 4]. The shortest distance is 5.

Input:
In an undirected graph, the nodes are numbered from 0 to 5, and the edges are:
an edge between node 0 and node 1 with distance 5,
an edge between node 1 and node 4 with distance 3,
an edge between node 2 and node 3 with distance 3,
an edge between node 3 and node 4 with distance 4,
an edge between node 3 and node 5 with distance 5,
an edge between node 4 and node 5 with distance 1.
Source Node: 0
Target Node: 5

Answer:
The shortest path from the source node to the target node is [0, 1, 4, 5]. The shortest distance is 9.

Input:
In an undirected graph, the nodes are numbered from 0 to 5, and the edges are:
an edge between node 0 and node 3 with distance 2,
an edge between node 0 and node 2 with distance 2,
an edge between node 1 and node 3 with distance 5,
an edge between node 1 and node 5 with distance 4,
an edge between node 2 and node 3 with distance 2,
an edge between node 2 and node 5 with distance 3,
an edge between node 3 and node 4 with distance 3,
an edge between node 4 and node 5 with distance 4.

Source Node: 0
Target Node: 5

Answer:
The shortest path from the source node to the target node is [0, 2, 5]. The shortest distance is 5.

Input:
In an undirected graph, the nodes are numbered from 0 to 4, and the edges are:
an edge between node 0 and node 2 with distance 5,
an edge between node 1 and node 4 with distance 3,
an edge between node 1 and node 2 with distance 2,
an edge between node 2 and node 4 with distance 1,
an edge between node 3 and node 4 with distance 1.

Source Node: 0
Target Node: 4

Answer:
The shortest path from the source node to the target node is [0, 2, 4]. The shortest distance is 6.

Input:
In an undirected graph, the nodes are numbered from 0 to 8, and the edges are:
an edge between node 0 and node 1 with distance 5,
an edge between node 0 and node 4 with distance 5,
an edge between node 1 and node 4 with distance 2,
an edge between node 1 and node 2 with distance 5,
an edge between node 2 and node 7 with distance 5,
an edge between node 3 and node 7 with distance 2,
an edge between node 3 and node 5 with distance 3,
an edge between node 4 and node 6 with distance 2,
an edge between node 5 and node 8 with distance 3,
an edge between node 6 and node 8 with distance 2,
an edge between node 7 and node 8 with distance 3.

Source Node: 0
Target Node: 8

Answer:
The shortest path from the source node to the target node is [0, 4, 6, 8]. The shortest distance is 9.

Input:
{input}
'''

standard_prompt_easy_1shot = '''Find the shortest path from a source node to a target node in an undirected graph.
Input:
In an undirected graph, the nodes are numbered from 0 to 4, and the edges are:
an edge between node 0 and node 3 with distance 2,
an edge between node 1 and node 4 with distance 3,
an edge between node 2 and node 4 with distance 5,
an edge between node 3 and node 4 with distance 3.

Source Node: 0
Target Node: 4

Answer:
The shortest path from the source node to the target node is [0, 3, 4]. The shortest distance is 5.

Input:
{input}
'''

standard_prompt_easy_zeroshot = '''Find the shortest path from a source node to a target node in an undirected graph.
The format of the input and answer are below:
Input:
In an undirected graph, the nodes are numbered from source node index to target node index, and the edges are represented as:
an edge between node a index and node b index with distance LENGTH,
...,
.

Source Node: source node index
Target Node: target node index

Answer:
The shortest path from the source node to the target node is [source node index, ..., target node index]. The shortest distance is BLANK.

Input:
{input}
'''

# 5-shot
cot_prompt_easy_5shot = '''Find the shortest path from a source node to a target node in an undirected graph.
Input:
In an undirected graph, the nodes are numbered from 0 to 4, and the edges are:
an edge between node 0 and node 3 with distance 2,
an edge between node 1 and node 4 with distance 3,
an edge between node 2 and node 4 with distance 5,
an edge between node 3 and node 4 with distance 3.

Source Node: 0
Target Node: 4

Answer:
Starting from node 0, we arrive at node 3. The distance between these two nodes is 2.
Starting from node 3, we arrive at node 4. The distance between these two nodes is 3.
Thus, the shortest path from the source node to the target node is [0, 3, 4]. The shortest distance is 5.

Input:
In an undirected graph, the nodes are numbered from 0 to 5, and the edges are:
an edge between node 0 and node 1 with distance 5,
an edge between node 1 and node 4 with distance 3,
an edge between node 2 and node 3 with distance 3,
an edge between node 3 and node 4 with distance 4,
an edge between node 3 and node 5 with distance 5,
an edge between node 4 and node 5 with distance 1.

Source Node: 0
Target Node: 5

Answer:
Starting from node 0, we arrive at node 1. The distance between these two nodes is 5.
Starting from node 1, we arrive at node 4. The distance between these two nodes is 3.
Starting from node 4, we arrive at node 5. The distance between these two nodes is 1.
Thus, the shortest path from the source node to the target node is [0, 1, 4, 5]. The shortest distance is 9.

Input:
In an undirected graph, the nodes are numbered from 0 to 5, and the edges are:
an edge between node 0 and node 3 with distance 2,
an edge between node 0 and node 2 with distance 2,
an edge between node 1 and node 3 with distance 5,
an edge between node 1 and node 5 with distance 4,
an edge between node 2 and node 3 with distance 2,
an edge between node 2 and node 5 with distance 3,
an edge between node 3 and node 4 with distance 3,
an edge between node 4 and node 5 with distance 4.

Source Node: 0
Target Node: 5

Answer:
Starting from node 0, we arrive at node 2. The distance between these two nodes is 2.
Starting from node 2, we arrive at node 5. The distance between these two nodes is 3.
Thus, the shortest path from the source node to the target node is [0, 2, 5]. The shortest distance is 5.

Input:
In an undirected graph, the nodes are numbered from 0 to 4, and the edges are:
an edge between node 0 and node 2 with distance 5,
an edge between node 1 and node 4 with distance 3,
an edge between node 1 and node 2 with distance 2,
an edge between node 2 and node 4 with distance 1,
an edge between node 3 and node 4 with distance 1.

Source Node: 0
Target Node: 4

Answer:
Starting from node 0, we arrive at node 2. The distance between these two nodes is 5.
Starting from node 2, we arrive at node 4. The distance between these two nodes is 1.
Thus, the shortest path from the source node to the target node is [0, 2, 4]. The shortest distance is 6.

Input:
In an undirected graph, the nodes are numbered from 0 to 8, and the edges are:
an edge between node 0 and node 1 with distance 5,
an edge between node 0 and node 4 with distance 5,
an edge between node 1 and node 4 with distance 2,
an edge between node 1 and node 2 with distance 5,
an edge between node 2 and node 7 with distance 5,
an edge between node 3 and node 7 with distance 2,
an edge between node 3 and node 5 with distance 3,
an edge between node 4 and node 6 with distance 2,
an edge between node 5 and node 8 with distance 3,
an edge between node 6 and node 8 with distance 2,
an edge between node 7 and node 8 with distance 3.

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

cot_prompt_easy_1shot = '''Find the shortest path from a source node to a target node in an undirected graph.
Input:
In an undirected graph, the nodes are numbered from 0 to 4, and the edges are:
an edge between node 0 and node 3 with distance 2,
an edge between node 1 and node 4 with distance 3,
an edge between node 2 and node 4 with distance 5,
an edge between node 3 and node 4 with distance 3.

Source Node: 0
Target Node: 4

Answer:
Starting from node 0, we arrive at node 3. The distance between these two nodes is 2.
Starting from node 3, we arrive at node 4. The distance between these two nodes is 3.
Thus, the shortest path from the source node to the target node is [0, 3, 4]. The shortest distance is 5.

Input:
{input}
'''

cot_prompt_easy_zeroshot = '''Find the shortest path from a source node to a target node in an undirected graph.
Let's think step by step. The format of the input and answer are below:
Input:
In an undirected graph, the nodes are numbered from source node index to target node index, and the edges are represented as:
an edge between node a index and node b index with distance LENGTH,
...,
.

Source Node: source node index
Target Node: target node index

Answer:
The shortest path from the source node to the target node is [source node index, ..., target node index]. The shortest distance is BLANK.

Input:
{input}
'''

bog_prompt_easy_5shot = '''Find the shortest path from a source node to a target node in an undirected graph.
Input:
In an undirected graph, the nodes are numbered from 0 to 4, and the edges are:
an edge between node 0 and node 3 with distance 2,
an edge between node 1 and node 4 with distance 3,
an edge between node 2 and node 4 with distance 5,
an edge between node 3 and node 4 with distance 3.

Source Node: 0
Target Node: 4

Answer:
Let's construct a graph with the nodes and edges first. The shortest path from the source node to the target node is [0, 3, 4]. The shortest distance is 5.

Input:
In an undirected graph, the nodes are numbered from 0 to 5, and the edges are:
an edge between node 0 and node 1 with distance 5,
an edge between node 1 and node 4 with distance 3,
an edge between node 2 and node 3 with distance 3,
an edge between node 3 and node 4 with distance 4,
an edge between node 3 and node 5 with distance 5,
an edge between node 4 and node 5 with distance 1.

Source Node: 0
Target Node: 5

Answer:
Let's construct a graph with the nodes and edges first. The shortest path from the source node to the target node is [0, 1, 4, 5]. The shortest distance is 9.

Input:
In an undirected graph, the nodes are numbered from 0 to 5, and the edges are:
an edge between node 0 and node 3 with distance 2,
an edge between node 0 and node 2 with distance 2,
an edge between node 1 and node 3 with distance 5,
an edge between node 1 and node 5 with distance 4,
an edge between node 2 and node 3 with distance 2,
an edge between node 2 and node 5 with distance 3,
an edge between node 3 and node 4 with distance 3,
an edge between node 4 and node 5 with distance 4.

Source Node: 0
Target Node: 5

Answer:
Let's construct a graph with the nodes and edges first. The shortest path from the source node to the target node is [0, 2, 5]. The shortest distance is 5.

Input:
In an undirected graph, the nodes are numbered from 0 to 4, and the edges are:
an edge between node 0 and node 2 with distance 5,
an edge between node 1 and node 4 with distance 3,
an edge between node 1 and node 2 with distance 2,
an edge between node 2 and node 4 with distance 1,
an edge between node 3 and node 4 with distance 1.

Source Node: 0
Target Node: 4

Answer:
Let's construct a graph with the nodes and edges first. The shortest path from the source node to the target node is [0, 2, 4]. The shortest distance is 6.

Input:
In an undirected graph, the nodes are numbered from 0 to 8, and the edges are:
an edge between node 0 and node 1 with distance 5,
an edge between node 0 and node 4 with distance 5,
an edge between node 1 and node 4 with distance 2,
an edge between node 1 and node 2 with distance 5,
an edge between node 2 and node 7 with distance 5,
an edge between node 3 and node 7 with distance 2,
an edge between node 3 and node 5 with distance 3,
an edge between node 4 and node 6 with distance 2,
an edge between node 5 and node 8 with distance 3,
an edge between node 6 and node 8 with distance 2,
an edge between node 7 and node 8 with distance 3.

Source Node: 0
Target Node: 8

Answer:
Let's construct a graph with the nodes and edges first. The shortest path from the source node to the target node is [0, 4, 6, 8]. The shortest distance is 9.

Input:
{input}
'''

bog_prompt_easy_1shot = '''Find the shortest path from a source node to a target node in an undirected graph.
Let's construct a graph with the nodes and edges first.
Input:
In an undirected graph, the nodes are numbered from 0 to 4, and the edges are:
an edge between node 0 and node 3 with distance 2,
an edge between node 1 and node 4 with distance 3,
an edge between node 2 and node 4 with distance 5,
an edge between node 3 and node 4 with distance 3.

Source Node: 0
Target Node: 4

Answer:
The shortest path from the source node to the target node is [0, 3, 4]. The shortest distance is 5.

Input:
{input}
'''

bog_prompt_easy_zeroshot = '''Find the shortest path from a source node to a target node in an undirected graph.
Let's construct a graph with the nodes and edges first. The format of the input and answer are below:
Input:
In an undirected graph, the nodes are numbered from source node index to target node index, and the edges are represented as:
an edge between node a index and node b index with distance LENGTH,
...,
.

Source Node: source node index
Target Node: target node index

Answer:
The shortest path from the source node to the target node is [source node index, ..., target node index]. The shortest distance is BLANK.

Input:
{input}
'''


### GoT prompt starts here
neigborhood_propose_prompt = '''Given an input node of an undirected graph, find its neighborhood nodes and save them in a list.

Input:
In an undirected graph, the nodes are numbered from 0 to 4, and the edges are:
an edge between node 0 and node 3,
an edge between node 1 and node 4,
an edge between node 2 and node 4,
an edge between node 3 and node 4.

Input Node: 4

Answer:
The neighborhood node list of the input node is [1, 2, 3].

Input:
In an undirected graph, the nodes are numbered from 0 to 8, and the edges are:
an edge between node 0 and node 1,
an edge between node 0 and node 4,
an edge between node 1 and node 4,
an edge between node 1 and node 2,
an edge between node 2 and node 7,
an edge between node 3 and node 7,
an edge between node 3 and node 5,
an edge between node 4 and node 6,
an edge between node 5 and node 8,
an edge between node 6 and node 8,
an edge between node 7 and node 8.

Input Node: 7

Answer:
The neighborhood node list of the input node is [2, 3, 8].

Input:
In an undirected graph, the nodes are numbered from 0 to 18, and the edges are:
an edge between node 0 and node 5,
an edge between node 1 and node 6,
an edge between node 1 and node 11,
an edge between node 1 and node 14,
an edge between node 2 and node 6,
an edge between node 2 and node 10,
an edge between node 2 and node 11,
an edge between node 3 and node 15,
an edge between node 3 and node 11,
an edge between node 4 and node 18,
an edge between node 4 and node 8,
an edge between node 4 and node 10,
an edge between node 4 and node 11,
an edge between node 4 and node 15,
an edge between node 5 and node 15,
an edge between node 5 and node 8,
an edge between node 5 and node 13,
an edge between node 6 and node 15,
an edge between node 6 and node 14,
an edge between node 7 and node 12,
an edge between node 7 and node 8,
an edge between node 7 and node 15,
an edge between node 8 and node 10,
an edge between node 8 and node 16,
an edge between node 9 and node 17,
an edge between node 9 and node 16,
an edge between node 10 and node 16,
an edge between node 11 and node 18,
an edge between node 11 and node 16,
an edge between node 12 and node 14,
an edge between node 13 and node 14,
an edge between node 14 and node 17,
an edge between node 15 and node 16,
an edge between node 16 and node 18,
an edge between node 17 and node 18.

Input Node: 12

Answer:
The neighborhood node list of the input node is [7, 14].

Input:
In an undirected graph, the nodes are numbered from 0 to 11, and the edges are:
an edge between node 0 and node 2,
an edge between node 1 and node 5,
an edge between node 2 and node 9,
an edge between node 3 and node 7,
an edge between node 3 and node 11,
an edge between node 4 and node 5,
an edge between node 4 and node 6,
an edge between node 5 and node 7,
an edge between node 6 and node 8,
an edge between node 7 and node 11,
an edge between node 8 and node 10,
an edge between node 9 and node 10,
an edge between node 10 and node 11.

Input Node: 11

Answer:
The neighborhood node list of the input node is [3, 7, 10].

Input:
In an undirected graph, the nodes are numbered from 0 to 12, and the edges are:
an edge between node 0 and node 1,
an edge between node 1 and node 9,
an edge between node 1 and node 6,
an edge between node 2 and node 3,
an edge between node 2 and node 7,
an edge between node 2 and node 9,
an edge between node 3 and node 12,
an edge between node 4 and node 7,
an edge between node 5 and node 8,
an edge between node 6 and node 11,
an edge between node 7 and node 11,
an edge between node 8 and node 11,
an edge between node 8 and node 12,
an edge between node 9 and node 10,
an edge between node 10 and node 12,
an edge between node 11 and node 12.

Input Node: 12

Answer:
The neighborhood node list of the input node is [3, 8, 10, 11].

Input:
{input}
'''

# the neighborhood slove prompt is the same as the original one for null problem solving

neighborhood_aggregation_prompt = '''Find the shortest path from a source node to a target node in an undirected graph. The edges in the undirected graph are reversible. We have the hints of one or several intermediate paths from the source node to some intermediate nodes. Please use these hints to find the shortest path from the source node the the target node.

Input:
In an undirected graph, the nodes are numbered from 0 to 4, and the edges are:
an edge between node 0 and node 3 with distance 2,
an edge between node 1 and node 4 with distance 3,
an edge between node 2 and node 4 with distance 5,
an edge between node 3 and node 4 with distance 3.
The hints are:
The shortest path from the source node 0 to the intermediate node 3 is [0, 3]. The shortest distance is 2.
The shortest path from the source node 0 to the intermediate node 1 is [0, 3, 4, 1]. The shortest distance is 8.
The shortest path from the source node 0 to the intermediate node 2 is [0, 3, 4, 2]. The shortest distance is 10.
Use the above hint to find the shortest path from the source node 0 to the target node 4. 

Answer:
Using the above hints, the shortest path from the source node 0 to the target node 4 is [0, 3, 4]. The shortest distance is 5.

Input:
In an undirected graph, the nodes are numbered from 0 to 5, and the edges are:
an edge between node 0 and node 3 with distance 2,
an edge between node 0 and node 2 with distance 2,
an edge between node 1 and node 3 with distance 5,
an edge between node 1 and node 5 with distance 4,
an edge between node 2 and node 3 with distance 2,
an edge between node 2 and node 5 with distance 3,
an edge between node 3 and node 4 with distance 3,
an edge between node 4 and node 5 with distance 4.
The hints are:
The shortest path from the source node 0 to the intermediate node 1 is [0, 3, 1]. The shortest distance is 7.
The shortest path from the source node 0 to the intermediate node 4 is [0, 3, 4]. The shortest distance is 5.
The shortest path from the source node 0 to the intermediate node 2 is [0, 2]. The shortest distance is 2.
Use the above hint to find the shortest path from the source node 0 to the target node 5. 

Answer:
Using the above hints, the shortest path from the source node 0 to the target node 5 is [0, 2, 5]. The shortest distance is 5.

Input:
In an undirected graph, the nodes are numbered from 0 to 5, and the edges are:
an edge between node 0 and node 3 with distance 2,
an edge between node 0 and node 2 with distance 2,
an edge between node 1 and node 3 with distance 5,
an edge between node 1 and node 5 with distance 4,
an edge between node 2 and node 3 with distance 2,
an edge between node 2 and node 5 with distance 3,
an edge between node 3 and node 4 with distance 3,
an edge between node 4 and node 5 with distance 4.
The hints are:
The shortest path from the source node 0 to the intermediate node 1 is [0, 3]. The shortest distance is 2.
The shortest path from the source node 0 to the intermediate node 4 is [0, 2, 5]. The shortest distance is 5.
Use the above hint to find the shortest path from the source node 0 to the target node 4. 

Answer:
Using the above hints, the shortest path from the source node 0 to the target node 4 is [0, 3, 4]. The shortest distance is 5.

Input:
In an undirected graph, the nodes are numbered from 0 to 8, and the edges are:
an edge between node 0 and node 1 with distance 5,
an edge between node 0 and node 4 with distance 5,
an edge between node 1 and node 4 with distance 2,
an edge between node 1 and node 2 with distance 5,
an edge between node 2 and node 7 with distance 5,
an edge between node 3 and node 7 with distance 2,
an edge between node 3 and node 5 with distance 3,
an edge between node 4 and node 6 with distance 2,
an edge between node 5 and node 8 with distance 3,
an edge between node 6 and node 8 with distance 2,
an edge between node 7 and node 8 with distance 3.
The hints are:
The shortest path from the source node 0 to the intermediate node 8 is [0, 1, 2, 7, 8]. The shortest distance is 18.
The shortest path from the source node 0 to the intermediate node 4 is [0, 4]. The shortest distance is 5.
Use the above hint to find the shortest path from the source node 0 to the target node 6. 

Answer:
Using the above hints, the shortest path from the source node 0 to the target node 6 is [0, 4, 6]. The shortest distance is 7.

Input:
In an undirected graph, the nodes are numbered from 0 to 8, and the edges are:
an edge between node 0 and node 1 with distance 5,
an edge between node 0 and node 4 with distance 5,
an edge between node 1 and node 4 with distance 2,
an edge between node 1 and node 2 with distance 5,
an edge between node 2 and node 7 with distance 5,
an edge between node 3 and node 7 with distance 2,
an edge between node 3 and node 5 with distance 3,
an edge between node 4 and node 6 with distance 2,
an edge between node 5 and node 8 with distance 3,
an edge between node 6 and node 8 with distance 2,
an edge between node 7 and node 8 with distance 3.
The hints are:
The shortest path from the source node 0 to the intermediate node 8 is [0, 1, 2]. The shortest distance is 10.
The shortest path from the source node 0 to the intermediate node 4 is [0, 4, 6, 8]. The shortest distance is 9.
Use the above hint to find the shortest path from the source node 0 to the target node 7. 

Answer:
Using the above hints, the shortest path from the source node 0 to the target node 6 is [0, 4, 6, 8, 7]. The shortest distance is 12.

Input:
{input}
'''

readout_prompt = '''Find the shortest path from a source node to a target node in an undirected graph. The edges in the undirected graph are reversible. We have two solution candidates to the shortest path from the source node to the target node. Please verify these two solution candidates and output the better one. If two solutions are the same and both valid, output the first solution. Notice that the shortest distance provided in the hints may be wrong. Check it before use it.

Input:
In an undirected graph, the nodes are numbered from 0 to 5, and the edges are:
an edge between node 0 and node 3 with distance 2,
an edge between node 0 and node 2 with distance 2,
an edge between node 1 and node 3 with distance 5,
an edge between node 1 and node 5 with distance 4,
an edge between node 2 and node 3 with distance 2,
an edge between node 2 and node 5 with distance 3,
an edge between node 3 and node 4 with distance 3,
an edge between node 4 and node 5 with distance 4.

Source Node: 0
Target Node: 5
Solution 1: The shortest path from the source node 0 to the target node 5 is [0, 2, 5]. The shortest distance is 5.
Solution 2: The shortest path from the source node 0 to the target node 5 is [0, 3, 4, 5]. The shortest distance is 9.

Answer:
Solution 1 is valid because it can reach the target node and all the edges in Solution 1 are real edges in the Edge set. Solution 2 is valid because it can reach the target node and all the edges in Solution 2 are real edges in the Edge set. Solution 1 is better than Solution 2 because the path in Solution 1 is shorter than that in Solution 2. So the shortest path from the source node 0 to the target node 5 is [0, 2, 5]. The shortest distance is 5.

Input:
In an undirected graph, the nodes are numbered from 0 to 5, and the edges are:
an edge between node 0 and node 3 with distance 2,
an edge between node 0 and node 2 with distance 2,
an edge between node 1 and node 3 with distance 5,
an edge between node 1 and node 5 with distance 4,
an edge between node 2 and node 3 with distance 2,
an edge between node 2 and node 5 with distance 3,
an edge between node 3 and node 4 with distance 3,
an edge between node 4 and node 5 with distance 4.

Source Node: 0
Target Node: 5
Solution 1: The shortest path from the source node 0 to the target node 5 is [0, 3, 5]. The shortest distance is 3.
Solution 2: The shortest path from the source node 0 to the target node 5 is [0, 2, 5]. The shortest distance is 5.

Answer:
Solution 1 is invalid because the edge [3, 5] in Solution 1 is not a real edge in the Edge Set. Solution 2 is valid because it can reach the target node and all the edges in Solution 2 are real edges in the Edge set. Althought the path in Solution 1 is shorter than that in Solution 2, solution 2 is better than Solution 1 because Solution 1 is an invalid path. So the shortest path from the source node 0 to the target node 5 is [0, 2, 5]. The shortest distance is 5.

Input:
In an undirected graph, the nodes are numbered from 0 to 5, and the edges are:
an edge between node 0 and node 3 with distance 2,
an edge between node 0 and node 2 with distance 2,
an edge between node 1 and node 3 with distance 5,
an edge between node 1 and node 5 with distance 4,
an edge between node 2 and node 3 with distance 2,
an edge between node 2 and node 5 with distance 3,
an edge between node 3 and node 4 with distance 3,
an edge between node 4 and node 5 with distance 4.

Source Node: 0
Target Node: 5
Solution 1: The shortest path from the source node 0 to the target node 5 is [0, 3, 5]. The shortest distance is 5.
Solution 2: The shortest path from the source node 0 to the target node 5 is [0, 3, 5]. The shortest distance is 5.

Answer:
Solution 1 is valid because it can reach the target node and all the edges in Solution 1 are real edges in the Edge set. Solution 2 is valid because it can reach the target node and all the edges in Solution 2 are real edges in the Edge set. Solution 1 and Solution 2 are the same. So the shortest path from the source node 0 to the target node 5 is [0, 3, 5]. The shortest distance is 5.

Input:
In an undirected graph, the nodes are numbered from 0 to 8, and the edges are:
an edge between node 0 and node 1 with distance 5,
an edge between node 0 and node 4 with distance 5,
an edge between node 1 and node 4 with distance 2,
an edge between node 1 and node 2 with distance 5,
an edge between node 2 and node 7 with distance 5,
an edge between node 3 and node 7 with distance 2,
an edge between node 3 and node 5 with distance 3,
an edge between node 4 and node 6 with distance 2,
an edge between node 5 and node 8 with distance 3,
an edge between node 6 and node 8 with distance 2,
an edge between node 7 and node 8 with distance 3.

Source Node: 0
Target Node: 8
Solution 1: The shortest path from the source node 0 to the target node 8 is [0, 1, 2, 7, 8]. The shortest distance is 18.
Solution 2: The shortest path from the source node 0 to the target node 8 is [0, 4, 6, 8]. The shortest distance is 9.

Answer:
Solution 1 is valid because it can reach the target node and all the edges in Solution 1 are real edges in the Edge set. Solution 2 is valid because it can reach the target node and all the edges in Solution 2 are real edges in the Edge set. Solution 2 is better than Solution 1 because the path in Solution 2 is shorter than that in Solution 1. So the shortest path from the source node 0 to the target node 8 is [0, 4, 6, 8]. The shortest distance is 9.

Input:
In an undirected graph, the nodes are numbered from 0 to 8, and the edges are:
an edge between node 0 and node 1 with distance 5,
an edge between node 0 and node 4 with distance 5,
an edge between node 1 and node 4 with distance 2,
an edge between node 1 and node 2 with distance 5,
an edge between node 2 and node 7 with distance 5,
an edge between node 3 and node 7 with distance 2,
an edge between node 3 and node 5 with distance 3,
an edge between node 4 and node 6 with distance 2,
an edge between node 5 and node 8 with distance 3,
an edge between node 6 and node 8 with distance 2,
an edge between node 7 and node 8 with distance 3.

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
In an undirected graph, the nodes are numbered from 0 to 6, and the edges are represented as:
an edge between node 0 and node 1 with distance 2,
an edge between node 0 and node 3 with distance 2,
an edge between node 0 and node 4 with distance 2,
an edge between node 1 and node 4 with distance 3,
an edge between node 2 and node 4 with distance 3,
an edge between node 3 and node 4 with distance 5,
an edge between node 2 and node 5 with distance 4,
an edge between node 2 and node 6 with distance 1.

Input Nodes: [3, 4]
Target Node: 6

Answer:
The most promising one that forms the shortest path to the target node in the input nodes is 4. The shortest path is [4, 2, 6]. The shortest distance is 4.

Input:
In an undirected graph, the nodes are numbered from 0 to 18, and the edges are represented as:
an edge between node 0 and node 5 with distance 4,
an edge between node 1 and node 6 with distance 2,
an edge between node 1 and node 11 with distance 4,
an edge between node 1 and node 14 with distance 2,
an edge between node 2 and node 6 with distance 2,
an edge between node 2 and node 10 with distance 3,
an edge between node 2 and node 11 with distance 2,
an edge between node 3 and node 15 with distance 2,
an edge between node 3 and node 11 with distance 2,
an edge between node 4 and node 18 with distance 5,
an edge between node 4 and node 8 with distance 4,
an edge between node 4 and node 10 with distance 5,
an edge between node 4 and node 11 with distance 5,
an edge between node 4 and node 15 with distance 3,
an edge between node 5 and node 15 with distance 1,
an edge between node 5 and node 8 with distance 1,
an edge between node 5 and node 13 with distance 2,
an edge between node 6 and node 15 with distance 5,
an edge between node 6 and node 14 with distance 1,
an edge between node 7 and node 12 with distance 2,
an edge between node 7 and node 8 with distance 5,
an edge between node 7 and node 15 with distance 4,
an edge between node 8 and node 10 with distance 5,
an edge between node 8 and node 16 with distance 1,
an edge between node 9 and node 17 with distance 1,
an edge between node 9 and node 16 with distance 1,
an edge between node 10 and node 16 with distance 2,
an edge between node 11 and node 18 with distance 1,
an edge between node 11 and node 16 with distance 1,
an edge between node 12 and node 14 with distance 3,
an edge between node 13 and node 14 with distance 2,
an edge between node 14 and node 17 with distance 5,
an edge between node 15 and node 16 with distance 5,
an edge between node 16 and node 18 with distance 2,
an edge between node 17 and node 18 with distance 1.

Input Nodes: [1, 5, 8, 16]
Target Node: 18

Answer:
The most promising one that forms the shortest path to the target node in the input nodes is 16. The shortest path is [16, 18]. The shortest distance is 2.

Input:
In an undirected graph, the nodes are numbered from 0 to 16, and the edges are represented as:
an edge between node 0 and node 12 with distance 5,
an edge between node 1 and node 11 with distance 4,
an edge between node 1 and node 3 with distance 5,
an edge between node 2 and node 4 with distance 1,
an edge between node 2 and node 5 with distance 3,
an edge between node 2 and node 13 with distance 5,
an edge between node 3 and node 6 with distance 3,
an edge between node 3 and node 13 with distance 5,
an edge between node 3 and node 15 with distance 2,
an edge between node 4 and node 8 with distance 2,
an edge between node 4 and node 5 with distance 3,
an edge between node 4 and node 15 with distance 5,
an edge between node 5 and node 12 with distance 5,
an edge between node 6 and node 13 with distance 1,
an edge between node 6 and node 16 with distance 3,
an edge between node 7 and node 10 with distance 2,
an edge between node 7 and node 11 with distance 3,
an edge between node 7 and node 13 with distance 4,
an edge between node 8 and node 9 with distance 4,
an edge between node 9 and node 14 with distance 5,
an edge between node 9 and node 13 with distance 1,
an edge between node 10 and node 11 with distance 1,
an edge between node 10 and node 12 with distance 2,
an edge between node 11 and node 15 with distance 2,
an edge between node 11 and node 13 with distance 3,
an edge between node 12 and node 14 with distance 1,
an edge between node 13 and node 14 with distance 2,
an edge between node 14 and node 15 with distance 1,
an edge between node 15 and node 16 with distance 3.

Input Nodes: [5, 10, 14] 
Target Node: 16

Answer:
The most promising one that forms the shortest path to the target node in the input nodes is 14. The shortest path is [14, 15, 16]. The shortest distance is 4.

Input:
In an undirected graph, the nodes are numbered from 0 to 11, and the edges are represented as:
an edge between node 0 and node 2 with distance 2,
an edge between node 1 and node 5 with distance 2,
an edge between node 2 and node 9 with distance 2,
an edge between node 3 and node 7 with distance 3,
an edge between node 3 and node 11 with distance 5,
an edge between node 4 and node 5 with distance 3,
an edge between node 4 and node 6 with distance 3,
an edge between node 5 and node 7 with distance 5,
an edge between node 6 and node 8 with distance 1,
an edge between node 7 and node 11 with distance 1,
an edge between node 8 and node 10 with distance 5,
an edge between node 9 and node 10 with distance 2,
an edge between node 10 and node 11 with distance 2,

Input Nodes: [2, 7, 8]
Target Node: 11

Answer:
The most promising one that forms the shortest path to the target node in the input nodes is 2. The shortest path is [2, 9, 10, 11]. The shortest distance is 7.

Input:
In an undirected graph, the nodes are numbered from 0 to 12, and the edges are represented as:
an edge between node 0 and node 1 with distance 3,
an edge between node 1 and node 9 with distance 2,
an edge between node 1 and node 6 with distance 3,
an edge between node 2 and node 3 with distance 1,
an edge between node 2 and node 7 with distance 2,
an edge between node 2 and node 9 with distance 5,
an edge between node 3 and node 12 with distance 3,
an edge between node 4 and node 7 with distance 1,
an edge between node 5 and node 8 with distance 5,
an edge between node 6 and node 11 with distance 3,
an edge between node 7 and node 11 with distance 3,
an edge between node 8 and node 11 with distance 1,
an edge between node 8 and node 12 with distance 5,
an edge between node 9 and node 10 with distance 1,
an edge between node 10 and node 12 with distance 5,
an edge between node 11 and node 12 with distance 2.

Input Nodes: [6, 7, 8, 12]
Target Node: 12

Answer:
The most promising one that forms the shortest path to the target node in the input nodes is 12. The shortest path is [12]. The shortest distance is 0.

Input:
{input}
'''


neigborhood_evaluate_prompt_1shot = '''Given several input nodes, evaluate these input nodes and find the most promising one that forms the shortest path to the target node.

Input:
In an undirected graph, the nodes are numbered from 0 to 6, and the edges are represented as:
an edge between node 0 and node 1 with distance 2,
an edge between node 0 and node 3 with distance 2,
an edge between node 0 and node 4 with distance 2,
an edge between node 1 and node 4 with distance 3,
an edge between node 2 and node 4 with distance 3,
an edge between node 3 and node 4 with distance 5,
an edge between node 2 and node 5 with distance 4,
an edge between node 2 and node 6 with distance 1.

Input Nodes: [3, 4]
Target Node: 6

Answer:
The most promising one that forms the shortest path to the target node in the input nodes is 4. The shortest path is [4, 2, 6]. The shortest distance is 4.

Input:
{input}
'''


neigborhood_evaluate_prompt_easy_zeroshot = '''Given several input nodes, evaluate these input nodes and find the most promising one that forms the shortest path to the target node.

Input:
In an undirected graph, the nodes are numbered from source node index to target node index, and the edges are represented as:
an edge between node a index and node b index with distance LENGTH,
...,
.
Input Nodes: []
Target Node: target node index

Answer:
The most promising one that forms the shortest path to the target node in the input nodes is [input node index]. The shortest path is [input node index, ..., target node index]. The shortest distance is BLANK.

Input:
{input}
'''





