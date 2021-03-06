
# What's up on a field? 

## Description
It is time to learn to see the result (or lack thereof) of the game. In this stage, you should analyze a Tic-Tac-Toe field.  

Is the winner already known or is the game not over yet?  Is it a draw or an impossible combination of moves?  Let's find out!

**Note:** In this stage either 'X' or 'O' can start the game.

## Objective
In this stage, your program should:

    1. Fill the field from the input and print it as in the previous stage.
    2. Find the state in which the game is at the moment and print it. Possible states:

   - ```"Game not finished"``` - when no side has a three in a row but the field has empty cells;
   - ```"Draw"``` - when no side has a three in a row and the field has no empty cells;
   - ```"X wins"``` - when the field has three X in a row;
   - ```"O wins"``` - when the field has three O in a row;
   - ```"Impossible"``` - when the field has three X in a row as well as three O in a row. Or the field has a lot more X's that O's or vice versa (if the difference is 2 or more, should be 1 or 0). For this stage, consider that the game can be started both as X's or as O's. 

Also, you can use ```' '``` or ```'_'``` to print empty cells - it's up to you.

## Example
The examples below show outputs for some predefined states. Your program should work in the same way. 
The greater-than symbol followed by space (```> ```) represents the user input. Notice that it's not the part of the input.
##### Example 1
```
Enter cells: > XXXOO__O_
---------
| X X X |
| O O _ |
| _ O _ |
---------
X wins
```
##### Example 2
```
Enter cells: > XOXOXOXXO
---------
| X O X |
| O X O |
| X X O |
---------
X wins
```

##### Example 3
```
Enter cells: > XOOOXOXXO
---------
| X O O |
| O X O |
| X X O |
---------
O wins
```
##### Example 4
```
Enter cells: > XOXOOXXXO
---------
| X O X |
| O O X |
| X X O |
---------
Draw
```
##### Example 5
```
Enter cells: > XO_OOX_X_
---------
| X O   |
| O O X |
|   X   |
---------
Game not finished
```
##### Example 6
```
Enter cells: > XO_XO_XOX
---------
| X O _ |
| X O _ |
| X O X |
---------
Impossible
```
##### Example 7
```
Enter cells: > _O_X__X_X
---------
|   O   |
| X     |
| X   X |
---------
Impossible
```
##### Example 8
```
Enter cells: > _OOOO_X_X
---------
|   O O |
| O O   |
| X   X |
---------
Impossible
```

