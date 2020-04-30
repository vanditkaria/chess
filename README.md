# chess


![](https://github.com/vanditkaria/chess/blob/master/chess/1_fTWDdJ2m3L72X6rqce9_tQ.gif)


### Introduction:
This project is entirely for learning the basics of AI such as minimax, alpha-beta pruning, etc.

We use Alpha Beta Pruning on MiniMax Alogirthm where we create a search tree from which the algorithm can choose the best move. This is done by using the Minimax algorithm.

In this algorithm, the recursive tree of all possible moves is explored to a given depth, and the position is evaluated at the ending “leaves” of the tree.

After that, we return either the smallest or the largest value of the child to the parent node, depending on whether it’s a white or black to move. (That is, we try to either minimize or maximize the outcome at each level.)


### Alpha Beta Pruning:
Alpha-beta pruning is an optimization method to the minimax algorithm that allows us to disregard some branches in the search tree. This helps us evaluate the minimax search tree much deeper, while using the same resources.

The alpha-beta pruning is based on the situation where we can stop evaluating a part of the search tree if we find a move that leads to a worse situation than a previously discovered move.

The alpha-beta pruning does not influence the outcome of the minimax algorithm — it only makes it faster.

The alpha-beta algorithm also is more efficient if we happen to visit first those paths that lead to good moves.


### Pre Requisites

Python3: 
Linux (step by step guide) : https://docs.python-guide.org/starting/install3/linux/

Tkinter python: apt-get install python-tk

Chess GUI Python : sudo pip3 install python-chess


### License
This project is licensed under the MIT License - see the LICENSE file for details


### Understanding the Alogirthm:
https://www.youtube.com/watch?v=STjW3eH0Cik
Prof. Patrick Winston has explained the Algotihms very well, from why using to how using it transformed the way games are played by the computer, He further explains how the world-class chess algorithms have gained the benefit from the algorithms. 



