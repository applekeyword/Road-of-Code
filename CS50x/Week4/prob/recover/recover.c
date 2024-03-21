#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE\n");
        return 1;
    }

    FILE *input = fopen(argv[1], "rb");
    if (input == NULL)
    {
        printf("Could not open %s\n", argv[1]);
        return 1;
    }

    unsigned char block[512];
    char filename[10];
    int cnt = -1;
    FILE *output = NULL;
    while (fread(block, sizeof(unsigned char), 512, input) == 512)
    {
        if (block[0] == 0xff && block[1] == 0xd8 && block[2] == 0xff && (block[3] >= 0xe0 && block[3] <= 0xef))
        {
            cnt++;
            if (cnt > 0)
            {
                fclose(output);
            }

            sprintf(filename, "%03d.jpg", cnt);
            output = fopen(filename, "wb");
        }

        if (cnt != -1)
        {
            fwrite(block, sizeof(unsigned char), 512, output);
        }
    }

    fclose(output);
    fclose(input);
    return 0;
}