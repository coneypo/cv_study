// use pyrUp() and pyrDown() to downsample and upsample a given image;

// two kinds of pyramid
// 1. gaussian pyramid
// 2. laplacian pyramid

#include<opencv2/core.hpp>
#include<opencv2/imgproc.hpp>
#include<opencv2/highgui.hpp>
#include "iostream"
#include "stdio.h"
using namespace cv;
using namespace std;
int main()
{
    Mat img_rd = imread("all_face.png");


    for (;;)
    {
        imshow("pyramids demo", img_rd);
        char c = (char)waitKey(0);

        if (c==27)
        {break; }
        else if (c=='i')
        {
            pyrUp(img_rd, img_rd, Size(img_rd.cols*2, img_rd.rows*2));
            cout<<img_rd.cols<<" * "<<img_rd.rows;
            printf("** zoom in: Image x2 \n ");
        }
        else if (c=='o')
        {
            pyrDown(img_rd, img_rd, Size(img_rd.cols/2, img_rd.rows/2));
            cout<<img_rd.cols<<" * "<<img_rd.rows;
            printf("** zoom out: Image x2 \n ");
        }
    }

     return EXIT_SUCCESS;

}
