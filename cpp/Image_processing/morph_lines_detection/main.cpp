
#include <opencv2/core.hpp>
#include <opencv2/imgproc.hpp>
#include <opencv2/highgui.hpp>

#include <iostream>

using namespace std;
using namespace cv;

void show_wait_destroy(const char* winname, cv::Mat img);

int main(int argc, char **argv)
{
    Mat src=imread("src.png");
    imshow("src", src);

    Mat gray;
    if (src.channels()==3)
    {
        cvtColor(src, gray, COLOR_BGR2GRAY);
    }
    else
    {
        gray = src;
    }

    show_wait_destroy("gray", gray);

    // apply adaptiveThreshold at the bitwise_not of gray
    Mat bw;
    adaptiveThreshold(~gray, bw, 255, ADAPTIVE_THRESH_MEAN_C, THRESH_BINARY, 15, -2);

    show_wait_destroy("binary", bw);

    Mat horizontal = bw.clone();
    Mat vertical = bw.clone();


    // create horizontal
    int horizontal_size = horizontal.cols / 30;
    Mat horizontalStructure = getStructuringElement(MORPH_RECT, Size(horizontal_size, 1));

    erode(horizontal, horizontal, horizontalStructure, Point(-1, -1));
    dilate(horizontal, horizontal, horizontalStructure, Point(-1, -1));

    show_wait_destroy("horizontal", horizontal);


    // create vertical
    int vertical_size = vertical.rows / 30;
    Mat verticalStructure = getStructuringElement(MORPH_RECT, Size(vertical_size, 1));

    erode(vertical, vertical, verticalStructure, Point(-1, -1));
    dilate(vertical, vertical, verticalStructure, Point(-1, -1));

    show_wait_destroy("vertical", vertical);

    // inverse vertical image
    bitwise_not(vertical, vertical);
    show_wait_destroy("vertical_bit", vertical);

    // extract edges and smooth image according to the logic
    // 1. extract edges
    // 2. dilate (edges)
    // 3. src.copyto(smooth)
    // 4. blur smooth img
    // 5. smooth.copyto(src, edges)

    // step 1
    Mat edges;
    adaptiveThreshold(vertical, edges, 255, ADAPTIVE_THRESH_MEAN_C, THRESH_BINARY, 3, -2);
    show_wait_destroy("edges", edges);

    // step 2
    Mat kernel = Mat::ones(2,2,CV_8UC1);
    dilate(edges, edges, kernel);
    show_wait_destroy("dilate", edges);

    // step 3
    Mat smooth;
    vertical.copyTo(smooth);

    // step 4
    blur(smooth, smooth, Size(2, 2));

    // step 5
    smooth.copyTo(vertical, edges);


    // show final result
    show_wait_destroy("smooth - final", vertical);

    return 0;
}

void show_wait_destroy(const char*winname, cv::Mat img){
    imshow(winname, img);
    moveWindow(winname, 500, 0);
    waitKey(0);
    destroyWindow(winname);
}