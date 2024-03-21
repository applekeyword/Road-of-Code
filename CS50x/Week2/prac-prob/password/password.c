// Check that a password has at least one lowercase letter, uppercase letter, number and symbol
// Practice iterating through a string
// Practice using the ctype library

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

bool valid(string password);

int main(void)
{
    string password = get_string("Enter your password: ");
    if (valid(password))
    {
        printf("Your password is valid!\n");
    }
    else
    {
        printf("Your password needs at least one uppercase letter, lowercase letter, number and symbol\n");
    }
}

// TODO: Complete the Boolean function below
bool valid(string password)
{
    bool status[4];
    for (int i = 0; i < 4; i++)
    {
        status[i] = false;
    }
    for (int i = 0, n = strlen(password); i < n; i++)
    {
        if (isupper(password[i]))
        {
            status[0] = true;
        }
        else if (islower(password[i]))
        {
            status[1] = true;
        }
        else if (isdigit(password[i]))
        {
            status[2] = true;
        }
        else if (isgraph(password[i]))
        {
            status[3] = true;
        }
    }
    bool valid = status[0] && status[1] && status[2] && status[3];
    return valid;
}
