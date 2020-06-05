#include<iostream>
#include<opencv2/core.hpp>
#include<opencv2/imgproc.hpp>
#include<opencv2/highgui.hpp>


// Hit-or-Miss theory
using namespace cv;

int main()
{
    Mat img_input = (Mat_<uchar>(8, 8) <<
        0, 0, 0, 0, 0, 0, 0, 0,
        0, 255, 255, 255, 0, 0, 0, 255,
        0, 255, 255, 255, 0, 0, 0, 0,
        0, 255, 255, 255, 0, 255, 0, 0,
        0, 0, 255, 0, 0, 0, 0, 0,
        0, 0, 255, 0, 0, 255, 255, 0,
        0, 255, 0, 255, 0, 0, 255, 0,
        0, 255, 255, 255, 0, 0, 0, 0);


    Mat kernel = (Mat_<int>(3, 3) <<
        0, 1, 0,
        1, -1, 1,
        0, 1, 0);

    Mat img_output;
    morphologyEx(img_input, img_output, MORPH_HITMISS, kernel);

    const int rate=50;
    kernel=(kernel+1)*127;
    kernel.convertTo(kernel, CV_8U);

    resize(kernel, kernel, Size(), rate, rate, INTER_NEAREST);
    imshow("kernel", kernel);
    moveWindow("kernel", 0, 0);

    resize(img_input, img_input, Size(), rate, rate, INTER_NEAREST);
    imshow("Original", img_input);
    moveWindow("Original", 0, 200);

    resize(img_output, img_output, Size(), rate, rate, INTER_NEAREST);
    imshow("Hit or miss", img_output);
    moveWindow("Hit or miss", 500, 200);

    waitKey(0);
    return 0;
}