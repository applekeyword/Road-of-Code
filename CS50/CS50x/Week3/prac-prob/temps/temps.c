// Practice working with structs
// Practice applying sorting algorithms

#include <cs50.h>
#include <stdio.h>

#define NUM_CITIES 10

typedef struct
{
    string city;
    int temp;
} avg_temp;

avg_temp temps[NUM_CITIES];

void sort_cities(void);

int main(void)
{
    temps[0].city = "Austin";
    temps[0].temp = 97;

    temps[1].city = "Boston";
    temps[1].temp = 82;

    temps[2].city = "Chicago";
    temps[2].temp = 85;

    temps[3].city = "Denver";
    temps[3].temp = 90;

    temps[4].city = "Las Vegas";
    temps[4].temp = 105;

    temps[5].city = "Los Angeles";
    temps[5].temp = 82;

    temps[6].city = "Miami";
    temps[6].temp = 97;

    temps[7].city = "New York";
    temps[7].temp = 85;

    temps[8].city = "Phoenix";
    temps[8].temp = 107;

    temps[9].city = "San Francisco";
    temps[9].temp = 66;

    sort_cities();

    printf("\nAverage July Temperatures by City\n\n");

    for (int i = 0; i < NUM_CITIES; i++)
    {
        printf("%s: %i\n", temps[i].city, temps[i].temp);
    }
}

// TODO: Sort cities by temperature in descending order
void sort_cities(void)
{
    // Add your code here
    // // 1.Section sort
    // avg_temp tmp;
    // int index;
    // for (int i = 0; i < NUM_CITIES - 1; i++)
    // {
    //     tmp.city = temps[i].city;
    //     tmp.temp = temps[i].temp;
    //     index = i;
    //     for (int j = i + 1; j < NUM_CITIES; j++)
    //     {
    //         if (tmp.temp < temps[j].temp)
    //         {
    //             tmp.city = temps[j].city;
    //             tmp.temp = temps[j].temp;
    //             index = j;
    //         }
    //     }
    //     temps[index].city = temps[i].city;
    //     temps[index].temp = temps[i].temp;
    //     temps[i].city = tmp.city;
    //     temps[i].temp = tmp.temp;
    // }

    // // 2.Insertion sort
    // avg_temp tmp;
    // for (int i = 1; i < NUM_CITIES; i++)
    // {
    //     tmp.city = temps[i].city;
    //     tmp.temp = temps[i].temp;
    //     int j = i - 1;
    //     while (j >= 0 && temps[j].temp < tmp.temp)
    //     {
    //         temps[j + 1].city = temps[j].city;
    //         temps[j + 1].temp = temps[j].temp;
    //         j--;
    //     }
    //     temps[j + 1].city = tmp.city;
    //     temps[j + 1].temp = tmp.temp;
    // }

    // 3.Bubble sort
    avg_temp tmp;
    int status;
    for (int i = 0; i < NUM_CITIES; i++)
    {
        status = 0;
        for (int j = 0; j < NUM_CITIES - 1; j++)
        {
            if (temps[j].temp < temps[j + 1].temp)
            {
                tmp.city = temps[j].city;
                tmp.temp = temps[j].temp;
                temps[j].city = temps[j + 1].city;
                temps[j].temp = temps[j + 1].temp;
                temps[j + 1].city = tmp.city;
                temps[j + 1].temp = tmp.temp;
                status++;
            }
        }
        if (status == 0)
        {
            break;
        }
    }
}