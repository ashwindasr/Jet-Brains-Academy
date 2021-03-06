#  Menu, please
## Description
We're almost done!

Let's add more flavor to the game by adding a suggestion to replay after the current game session ends.

## Objective

   1. The game starts with a menu where a player can choose to either play or exit.
   2. Print ```Type "play" to play the game, "exit" to quit: ```and ask again if the player inputs something else.
   3. If the user chooses to play, the game starts.

Please, make sure that your program's output formatting precisely follows the example output formatting. Pay attention to the empty lines between tries and in the end.
## Example
The greater-than symbol followed by space (```> ```) represents the user input. Notice that it's not the part of the input.
```
H A N G M A N
Type "play" to play the game, "exit" to quit: > play
 
----------
Input a letter: > a
 
-a-a------
Input a letter: > i
 
-a-a---i--
Input a letter: > o
No such letter in the word
 
-a-a---i--
Input a letter: > o
You already typed this letter
 
-a-a---i--
Input a letter: > p
 
-a-a---ip-
Input a letter: > p
You already typed this letter
 
-a-a---ip-
Input a letter: > h
No such letter in the word
 
-a-a---ip-
Input a letter: > k
No such letter in the word
 
-a-a---ip-
Input a letter: > a
You already typed this letter
 
-a-a---ip-
Input a letter: > z
No such letter in the word
 
-a-a---ipt
Input a letter: > t
 
-a-a---ipt
Input a letter: > x
No such letter in the word
 
-a-a---ipt
Input a letter: > b
No such letter in the word
 
-a-a---ipt
Input a letter: > d
No such letter in the word
 
-a-a---ipt
Input a letter: > w
No such letter in the word
You are hanged!
 
Type "play" to play the game, "exit" to quit: > exit
```
