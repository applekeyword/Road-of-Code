#include "helpers.h"

void colorize(int height, int width, RGBTRIPLE image[height][width])
{
    // Change all black pixels to a color of your choosing
    RGBTRIPLE my_color;
    my_color.rgbtBlue = 0x56;
    my_color.rgbtGreen = 0x1d;
    my_color.rgbtRed = 0x12;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            if (image[i][j].rgbtBlue == 0 && image[i][j].rgbtGreen == 0 && image[i][j].rgbtRed == 0)
            {
                image[i][j].rgbtBlue = my_color.rgbtBlue;
                image[i][j].rgbtGreen = my_color.rgbtGreen;
                image[i][j].rgbtRed = my_color.rgbtRed;
            }
        }
    }
}
