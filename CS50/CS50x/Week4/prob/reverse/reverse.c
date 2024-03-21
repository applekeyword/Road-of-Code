#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#include "wav.h"

int check_format(WAVHEADER header);
int get_block_size(WAVHEADER header);

int main(int argc, char *argv[])
{
    // Ensure proper usage
    // TODO #1
    if (argc != 3)
    {
        printf("Usage: ./reverse input.wav output.wav\n");
        return 1;
    }

    // Open input file for reading
    // TODO #2
    FILE *input = fopen(argv[1], "r");
    if(input == NULL)
    {
        printf("Could not open %s.\n", argv[1]);
        return 1;
    }

    // Read header
    // TODO #3
    WAVHEADER header;
    fread(header.chunkID, sizeof(BYTE), 4, input);
    fread(&header.chunkSize, sizeof(DWORD), 1, input);
    fread(header.format, sizeof(BYTE), 4, input);
    fread(header.subchunk1ID, sizeof(BYTE), 4, input);
    fread(&header.subchunk1Size, sizeof(DWORD), 1, input);
    fread(&header.audioFormat, sizeof(WORD), 1, input);
    fread(&header.numChannels, sizeof(WORD), 1, input);
    fread(&header.sampleRate, sizeof(DWORD), 1, input);
    fread(&header.byteRate, sizeof(DWORD), 1, input);
    fread(&header.blockAlign, sizeof(WORD), 1, input);
    fread(&header.bitsPerSample, sizeof(WORD), 1, input);
    fread(header.subchunk2ID, sizeof(BYTE), 4, input);
    fread(&header.subchunk2Size, sizeof(DWORD), 1, input);

    // Use check_format to ensure WAV format
    // TODO #4
    if (check_format(header) == 0)
    {
        printf("Input is not a WAV file.\n");
        return 1;
    }

    // Open output file for writing
    // TODO #5
    FILE *output = fopen(argv[2], "w");
    if (output == NULL)
    {
        printf("Could not make %s.\n", argv[2]);
        return 1;
    }

    // Write header to file
    // TODO #6
    fwrite(header.chunkID, sizeof(BYTE), 4, output);
    fwrite(&header.chunkSize, sizeof(DWORD), 1, output);
    fwrite(header.format, sizeof(BYTE), 4, output);
    fwrite(header.subchunk1ID, sizeof(BYTE), 4, output);
    fwrite(&header.subchunk1Size, sizeof(DWORD), 1, output);
    fwrite(&header.audioFormat, sizeof(WORD), 1, output);
    fwrite(&header.numChannels, sizeof(WORD), 1, output);
    fwrite(&header.sampleRate, sizeof(DWORD), 1, output);
    fwrite(&header.byteRate, sizeof(DWORD), 1, output);
    fwrite(&header.blockAlign, sizeof(WORD), 1, output);
    fwrite(&header.bitsPerSample, sizeof(WORD), 1, output);
    fwrite(header.subchunk2ID, sizeof(BYTE), 4, output);
    fwrite(&header.subchunk2Size, sizeof(DWORD), 1, output);

    // Use get_block_size to calculate size of block
    // TODO #7
    long block_size = get_block_size(header);

    // Write reversed audio to file
    // TODO #8
    long after_header = ftell(input);
    fseek(input, -1 * block_size, SEEK_END);

    char block[block_size];
    while (ftell(input) >= after_header)
    {
        fread(&block, block_size, 1, input);
        fwrite(&block, block_size, 1, output);
        fseek(input, block_size * (-2), SEEK_CUR);
    }

    fclose(input);
    fclose(output);
    return 0;
}

int check_format(WAVHEADER header)
{
    // TODO #4
    char form[4] = "WAVE";
    for (int i = 0; i < 4; i++)
    {
        if (header.format[i] != form[i])
        {
            return 0;
        }
    }
    return 1;
}

int get_block_size(WAVHEADER header)
{
    // TODO #7
    return header.numChannels * header.bitsPerSample / 8;
}