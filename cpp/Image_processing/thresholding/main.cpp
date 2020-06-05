#include <opencv2/core.hpp>
#include <opencv2/imgproc.hpp>
#include <opencv2/highgui.hpp>
#include <iostream>

using namespace cv;
using namespace std;

Mat src, src_gray, dst;

const char* trackbar_type = "Type: \n 0: Binary \n 1: Binary Inverted \n 2: Truncate \n 3: To Zero \n 4: To Zero Inverted";
const char* trackbar_value = "Value";

int threshold_value = 0;
int threshold_type = 3;

static void Threshold_Demo(int, void*)
{
    threshold( src_gray, dst, threshold_value, 255, threshold_type);
    imshow("demo", dst);
}

int main()
{

    // thresholding
    // 1. threshold binary:             maxVal when > thresh, 0 when otherwise
    // 2. threshold binary inverted:    0 when > thresh, maxVal otherwise
    // 3. Truncate:                     threshold when > thresh, src(x,y) otherwise
    // 4. Threshold to zero:            src(x,y) when > thresh, 0 otherwise
    // 5. Threshold to zero inverted:   0 when > thresh, src(x,y) otherwise

    Mat src = imread("all.png");

    cvtColor(src, src_gray, COLOR_BGR2GRAY);

    namedWindow("demo",  WINDOW_AUTOSIZE);

    createTrackbar(trackbar_type, "demo", &threshold_type, 4, Threshold_Demo);
    createTrackbar(trackbar_value, "demo", &threshold_value, 255, Threshold_Demo);

    //threshold(src_gray, dst, threshold_value, 255, threshold_type);
    Threshold_Demo (0,0);
    waitKey();
    return 0;
}