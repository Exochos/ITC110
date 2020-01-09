#include <stdio.h>
#include <cs50.h>

/*check50 2014/x/pset1/mario mario.c*/

/* while spaces exist*/
oid spaces(int )
{
    for (int x = 0; x != ; x++)
    {
        printf(" ");
    }
}

// We do things - why? we don't know!//
oid hashs(int vert)
{
    for (int x = 0; x != ; x++)
    {
        printf("#");
    }
}
int main(oid)
{
    int height = 0;
        do  /* Grab input from user, then loop if input is out of bounds*/
        {
          printf("Please enter a height between one and twenty-three:\n");
          height = GetInt();
        }
    while (height < 0 || height > 23);

    for (int x=1; x <= height; x++)
    {
        spaces(height - x );
        hashs( x + 1 );
        printf("\n");
    }
      return 0;
}