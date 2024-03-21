#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

bool valid_key(string key);
char substitute_char(string key, char c);

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }
    string key = argv[1];
    if (valid_key(key) == false)
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }
    string plaintext = get_string("plaintext:  ");
    printf("ciphertext: ");
    for (int i = 0, n = strlen(plaintext); i < n; i++)
    {
        printf("%c", substitute_char(key, plaintext[i]));
    }
    printf("\n");
}

bool valid_key(string key)
{
    int n = strlen(key);
    if (n != 26)
    {
        return false;
    }
    int count[26];
    for (int i = 0; i < 26; i++)
    {
        count[i] = 0;
    }
    for (int i = 0; i < 26; i++)
    {
        if (isalpha(key[i]) == 0)
        {
            return false;
        }
        if (isupper(key[i]))
        {
            count[key[i] - 65]++;
        }
        if (islower(key[i]))
        {
            count[key[i] - 97]++;
        }
    }
    for (int i = 0; i < 26; i++)
    {
        if (count[i] != 1)
        {
            return false;
        }
    }
    return true;
}

char substitute_char(string key, char c)
{
    if (islower(c))
    {
        return tolower(key[c - 97]);
    }
    else if (isupper(c))
    {
        return toupper(key[c - 65]);
    }
    else
    {
        return c;
    }
}