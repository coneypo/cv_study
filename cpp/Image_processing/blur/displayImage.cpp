#include <stdio.h>
#include <opencv2/opencv.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/video.hpp>
#include <opencv2/imgproc.hpp>
#include <iostream>
using namespace cv;


// blurring/smoothing
// to reduce noise
// 1. normalized box filter
// 2. gaussian filter 高斯滤波
// 3. median filter 中值滤波
// 4. bilateral filter 双边滤波器
int main(int argc, char** argv )
{

    // Mat img_cv2_Mat = imread( argv[1], 1 );
    // Mat img_cv2_Mat = imread( "lena.pgm");
    Mat img_cv2_Mat = imread( "lena.pgm");


    // Gaussian Blur
    Mat img_cv2_blur_gaussian;
    img_cv2_blur_gaussian = img_cv2_Mat.clone();

    for (int i=1; i<31; i=i+2)
    {
        GaussianBlur(img_cv2_Mat, img_cv2_blur_gaussian, Size(i, i), 0, 0);
    }

    // Median Blur
    Mat img_cv2_blur_median;
    img_cv2_blur_median = img_cv2_Mat.clone();
    for (int i=1; i< 31; i=i+2)
    {
        medianBlur(img_cv2_Mat, img_cv2_blur_median, i);
    }

    // Bilateral Blur
    Mat img_cv2_blur_bilateral;
    img_cv2_blur_bilateral = img_cv2_Mat.clone();
    for (int i=1; i< 31; i=i+2)
    {
        bilateralFilter(img_cv2_Mat, img_cv2_blur_bilateral, i, i*2, i/2);
    }

    namedWindow("Display Image", WINDOW_AUTOSIZE );
    imshow("Display Image", img_cv2_blur_median);

    waitKey(0);

    return 0;
}
