#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

bool only_digits(string prompt);
char rotate(char c, int k);

int main(int argc, string argv[])
{
    if (argc != 2 || only_digits(argv[1]) == 0)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    int key = atoi(argv[1]);
    string plaintext = get_string("plaintext:  ");
    printf("ciphertext: ");
    char c;
    for (int i = 0, n = strlen(plaintext); i < n; i++)
    {
        c = rotate(plaintext[i], key);
        printf("%c", c);
    }
    printf("\n");
}

bool only_digits(string prompt)
{
    for (int i = 0, n = strlen(prompt); i < n; i++)
    {
        if (isdigit(prompt[i]) == 0)
        {
            return false;
        }
    }
    return true;
}

char rotate(char c, int k)
{
    if (islower(c))
    {
        char rot_char = (c - 97 + k) % 26 + 97;
        return rot_char;
    }
    else if (isupper(c))
    {
        char rot_char = (c - 65 + k) % 26 + 65;
        return rot_char;
    }
    else
    {
        return c;
    }
}