#include<stdio.h>

int sort(int array[], int length) 
{
    int temp, i, j;

    for(i = 0; i < length; i++)
    {
        for(j = 0; j < (length - 1); j++)
        {
            if(array[j]>array[j + 1])
            {
                temp = array[j];
                array[j] = array[j + 1];
                array[j + 1] = temp;
            }
        }
    }

    printf("\n");
    
    for(i = 0; i < length; i++)
    {
        printf("array[%d] = %d\n", i, array[i]);
    }
}

int main() 
{
    int length, i, sorted;

    printf("enter length of the array: ");
    scanf("%d", &length); 

    int array[length];

    for(i = 0; i < length; i++)
    {
        printf("array[%d] = ", i);
        scanf("%d", &array[i]);
    }

    sort(array, length);

    return 0;
}