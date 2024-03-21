// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 1000;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    node *trav = table[hash(word)];
    while (trav != NULL)
    {
        if (strcasecmp(trav->word, word) == 0)
        {
            return true;
        }
        trav = trav->next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    // return toupper(word[0]) - 'A';
    unsigned int sum = 0;
    for (int i = 0; word[i] != '\0'; i++)
    {
        sum += toupper(word[i]);
    }
    return sum % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    // initialize all header pointer to NULL
    for (int i = 0; i < N; i++)
    {
        table[i] = NULL;
    }

    // open dictionary file
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        return false;
    }

    // assume that the longest word in dictionary is no longer than LENGTH
    char line[LENGTH + 2];
    while (fgets(line, LENGTH + 3, file) != NULL)
    {
        // replace '\n' with '\0'
        line[strlen(line) - 1] = '\0';

        // create node
        node *new = malloc(sizeof(node));
        if (new == NULL)
        {
            return false;
        }
        strcpy(new->word, line);
        new->next = NULL;

        // find which bucket to insert
        unsigned int hash_value = hash(line);
        new->next = table[hash_value];
        table[hash_value] = new;
    }

    fclose(file);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    unsigned int sum = 0;
    node *trav;
    for (int i = 0; i < N; i++)
    {
        trav = table[i];
        while (trav != NULL)
        {
            sum++;
            trav = trav->next;
        }
    }
    return sum;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    node *trav;
    for (int i = 0; i < N; i++)
    {
        trav = table[i];
        while (trav != NULL)
        {
            trav = trav->next;
            free(table[i]);
            table[i] = trav;
        }
    }
    for (int i = 0; i < N; i++)
    {
        if (table[i] != NULL)
        {
            return false;
        }
    }
    return true;
}
