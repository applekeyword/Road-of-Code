#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    int avg;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            avg = round((image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue) / 3.0);
            image[i][j].rgbtRed = avg;
            image[i][j].rgbtGreen = avg;
            image[i][j].rgbtBlue = avg;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE tmp;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width / 2; j++)
        {
            tmp = image[i][j];
            image[i][j] = image[i][width - j - 1];
            image[i][width - j - 1] = tmp;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE copy[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j] = image[i][j];
        }
    }

    double sum;
    double sumRed, sumGreen, sumBlue;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            sum = 0;
            sumRed = 0;
            sumGreen = 0;
            sumBlue = 0;

            // count nine spots
            for (int row = -1; row <= 1; row++)
            {
                for (int col = -1; col <= 1; col++)
                {
                    if ((row + i) >= 0 && (row + i) < height && (col + j) >= 0 && (col + j) < width)
                    {
                        sumRed += copy[row + i][col + j].rgbtRed;
                        sumGreen += copy[row + i][col + j].rgbtGreen;
                        sumBlue += copy[row + i][col + j].rgbtBlue;
                        sum++;
                    }
                }
            }
            image[i][j].rgbtRed = round(sumRed / sum);
            image[i][j].rgbtGreen = round(sumGreen / sum);
            image[i][j].rgbtBlue = round(sumBlue / sum);
        }
    }
    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE copy[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j] = image[i][j];
        }
    }

    int Gx[3][3] = {{-1, 0, 1}, {-2, 0, 2},{ -1, 0, 1}};
    int Gy[3][3] = {{-1, -2, -1}, {0, 0, 0}, {1, 2, 1}};

    double GxRed, GxGreen, GxBlue;
    double GyRed, GyGreen, GyBlue;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            GxRed = 0;
            GyRed = 0;
            GxGreen = 0;
            GyGreen = 0;
            GxBlue = 0;
            GyBlue = 0;
            for (int row = -1; row <= 1; row++)
            {
                for (int col = -1; col <= 1; col++)
                {
                    if ((row + i) >= 0 && (row + i) < height && (col + j) >=0 && (col + j) < width)
                    {
                        GxRed += Gx[row + 1][col + 1] * copy[row + i][col + j].rgbtRed;
                        GyRed += Gy[row + 1][col + 1] * copy[row + i][col + j].rgbtRed;
                        GxGreen += Gx[row + 1][col + 1] * copy[row + i][col + j].rgbtGreen;
                        GyGreen += Gy[row + 1][col + 1] * copy[row + i][col + j].rgbtGreen;
                        GxBlue += Gx[row + 1][col + 1] * copy[row + i][col + j].rgbtBlue;
                        GyBlue += Gy[row + 1][col + 1] * copy[row + i][col + j].rgbtBlue;

                    }
                }
            }
            // uint8_t will overflow if result is greater than 255
            copy[i][j].rgbtRed = round(sqrt(pow(GxRed, 2) + pow(GyRed, 2))) > 255 ? 255 : round(sqrt(pow(GxRed, 2) + pow(GyRed, 2)));
            copy[i][j].rgbtGreen = round(sqrt(pow(GxGreen, 2) + pow(GyGreen, 2))) > 255 ? 255 : round(sqrt(pow(GxGreen, 2) + pow(GyGreen, 2)));
            copy[i][j].rgbtBlue = round(sqrt(pow(GxBlue, 2) + pow(GyBlue, 2))) > 255 ? 255 : round(sqrt(pow(GxBlue, 2) + pow(GyBlue, 2)));

            // the following is not gonna work unless you add additional variable to store variable
            // image[i][j].rgbtRed = round(sqrt(pow(GxRed, 2) + pow(GyRed, 2)));
            // image[i][j].rgbtGreen = round(sqrt(pow(GxGreen, 2) + pow(GyGreen, 2)));
            // image[i][j].rgbtBlue = round(sqrt(pow(GxBlue, 2) + pow(GyBlue, 2)));
            // if (image[i][j].rgbtRed > 255)
            // {
            //     image[i][j].rgbtRed = 255;
            // }
            // if (image[i][j].rgbtGreen > 255)
            // {
            //     image[i][j].rgbtGreen = 255;
            // }
            // if (image[i][j].rgbtBlue > 255)
            // {
            //     image[i][j].rgbtBlue = 255;
            // }
        }
    }
    return;
}
