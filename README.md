# TDT4173-MachineLearning
Introduction to the principles and methods for automatic learning in computer systems


## Notes from book

### chapter 1

The program needs only to learn how to choose the best move from among a set of legal moves, e.g. a manufactoring plant may know all the available manifacturing steps, but not the best strategy for sequencing them. 

It is often useful to reduce the problem of improving performance P at task T to the problem of learning some particular function such as ``ChooseMove`` in the checkers example.

In the case of checkers, we use a target function V(b) (V is any legal board state from set b) which gives 100 whenever a board is won, -100 when lost, 0 when draw, and V(b)=V(b') (b' is the best final state that can be achieved starting from b and playing optimally until the end of the game). The last case (case 4) is a nonoperational definition, as it has to calculate all possible moves untill the very end. The goal of learning in this case is to discover an operational description of V; i.e. that can be used by the program to evaluate states and select moves within a realistic time bounds.

Choosing a simple target function