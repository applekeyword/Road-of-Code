#include <cs50.h>
#include <stdio.h>
#include <string.h>

const int BITS_IN_BYTE = 8;

void print_bulb(int bit);
int *dec_to_bit(int num);

int main(void)
{
    string message = get_string("Message: ");
    int *bits;
    for (int i = 0, n = strlen(message); i < n; i++)
    {
        bits = dec_to_bit(message[i]);
        for (int j = 0; j < 8; j++)
        {
            print_bulb(bits[j]);
        }
        printf("\n");
    }
}

void print_bulb(int bit)
{
    if (bit == 0)
    {
        // Dark emoji
        printf("\U000026AB");
    }
    else if (bit == 1)
    {
        // Light emoji
        printf("\U0001F7E1");
    }
}

int *dec_to_bit(int num)
{
    static int bit[8];
    for (int i = 7; i >= 0; i--)
    {
        bit[i] = num % 2;
        num /= 2;
    }
    return bit;
}