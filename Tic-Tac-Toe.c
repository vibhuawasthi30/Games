#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <time.h>/

char board[3][3];
const char PLAYER = 'X';
const char COMPUTER = 'O';

void resetBoard();
void printBorad();
int checkFreeSpaces();
void playerMove();
void computerMove();
char checkWinner();
void printWinner(char winner);

int main()
{
   char winner = ' ';

   resetBoard();

   while(winner == ' ' && checkFreeSpaces() != 0 )
   {
      printBorad();
      // Player MOVE
      playerMove();
      winner = checkWinner();
      if(winner != ' ' || checkFreeSpaces() == 0)
      {
         break;
      }

       // COmputer MOVE 
       computerMove();
      winner = checkWinner();
      if(winner != ' ' || checkFreeSpaces() == 0)
      {
         break;
      }
   }

   printBorad();
   printWinner(winner);

    return 0;
}

// Reset Board
void resetBoard()
{
   for(int i = 0; i < 3; i++ )
   {
     for(int j = 0; j < 3; j++) 
     {
        board[i][j] = ' ';
     } 
   }
}
// Print Boardd 
void printBorad()
{
   printf(" %c | %c | %c ", board[0][0], board[0][1], board[0][2]);
   printf("\n---|---|---\n");
   // Rows
   printf(" %c | %c | %c ", board[1][0], board[1][1], board[1][2]);
   printf("\n---|---|---\n");
   printf(" %c | %c | %c ", board[2][0], board[2][1], board[2][2]);
   printf("\n");
}
int checkFreeSpaces()
{
   int freeSpaces = 9;

   for(int i = 0; i < 3; i++)
   {
       for(int j = 0; j < 3; j++)
        {
           if(board[i][j] != ' ')
           {
             freeSpaces --;
           }
        }
   }
   return freeSpaces;
}
void playerMove()
{
  int x;
  int y;
  do
  {
     // Ask for row
      printf("Enter row #(1-3): ");
      scanf("%d", &x);
      x--;
     // Ask for colume
       printf("Enter colume #(1-3): ");
       scanf("%d", &y);
       y--;

   if(board[x][y] != ' ')
    {
      printf("Invalid move!\n");
    }
   else
    {
      board[x][x] = PLAYER;
      break;
    }
  } while (board[x][y] != ' ');
  
}
void computerMove()
{
   //creates a seed based on current time
   srand(time(0));
   int x;
   int y;

   if(checkFreeSpaces)
   {
      do
      {
         x = rand() % 3;
         y = rand() % 3;
      } while (board[x][y] != ' ');


      board[x][y] = COMPUTER;
      
   }
   else
   {
      printWinner(' ');
   }
}
char checkWinner()
{
   // check all rows
   for(int i = 0; i < 3; i++)
   {
      if(board[i][0] == board[i][1] && board[i][0] == board[i][2])
      {
         return board[i][0];
      }
   }

   // check all columns
      // check all rows
   for(int j = 0; j < 3; j++)
   {
      if(board[0][j] == board[1][j] && board[0][j] == board[2][j])
      {
         return board[0][j];
      }
   }

   //check diagonals
    if(board[0][0] == board[1][1] && board[0][0] == board[2][2])
      {
         return board[0][0];
      }
      if(board[0][2] == board[1][1] && board[0][2] == board[2][0])
      {
         return board[0][2];
      }

      return ' ';
}
void printWinner(char winner)
{
   if(winner == PLAYER)
   {
      printf("You WIN !!!\n");
   }
   else if( winner == COMPUTER)
   {
      printf("YOU LOSE !!!\n");
   }
   else
   {
      printf("TIE !!!\n");
   }
}
