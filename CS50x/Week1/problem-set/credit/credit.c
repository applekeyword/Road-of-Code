#include <cs50.h>
#include <math.h>
#include <stdio.h>

int num_of_digits(long number);
char struct_is_valid(long number);
int get_sum_digits(long num);
bool luhn_is_valid(long number);

int main(void)
{
    // get the number
    long number = get_long("Number: ");

    // judge its validation
    char first_letter = struct_is_valid(number);
    // printf("%c", first_letter);
    bool indicator = luhn_is_valid(number);

    // classify and print the information
    if (indicator)
    {
        switch (first_letter)
        {
            case 'v':
                printf("VISA\n");
                break;

            case 'a':
                printf("AMEX\n");
                break;

            case 'm':
                printf("MASTERCARD\n");
                break;

            default:
                printf("INVALID\n");
                break;
        }
    }
    else
    {
        printf("INVALID\n");
    }
}

int num_of_digits(long number)
{
    int n = 0;
    do
    {
        number /= 10;
        n++;
    }
    while (number > 0);
    return n;
}

char struct_is_valid(long number)
{
    int n = num_of_digits(number);
    int first_one = number / (long) pow(10, n - 1);
    int first_two = number / (long) pow(10, n - 2);
    if (first_one == 4 && (n == 13 || n == 16))
    {
        return 'v';
    }
    else if ((first_two == 34 || first_two == 37) && n == 15)
    {
        return 'a';
    }
    else if ((first_two == 51 || first_two == 52 || first_two == 53 || first_two == 54 || first_two == 55) && n == 16)
    {
        return 'm';
    }
    else
    {
        return 'i';
    }
}

int get_sum_digits(long num)
{
    int sum = 0;
    while (num > 0)
    {
        sum += (num % 10);
        num /= 10;
    }
    return sum;
}

bool luhn_is_valid(long number)
{
    int sum_prod_digits = 0;
    long number_copy = number;
    while (number > 0)
    {
        sum_prod_digits += get_sum_digits(((number % 100) / 10) * 2);
        number /= 100;
    }
    int sum_not_prod_digits = (number_copy % 10);
    number_copy /= 10;
    while (number_copy > 0)
    {
        sum_not_prod_digits += (number_copy % 100) / 10;
        number_copy /= 100;
    }
    int sum_all_digits = sum_prod_digits + sum_not_prod_digits;
    if (sum_all_digits % 10 == 0)
    {
        return true;
    }
    else
    {
        return false;
    }
}