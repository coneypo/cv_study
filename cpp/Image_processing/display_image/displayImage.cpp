#include <stdio.h>
#include <opencv2/opencv.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/video.hpp>
#include <opencv2/imgproc.hpp>

#include <dlib/image_processing.h>
#include <dlib/opencv/cv_image.h>

#include <iostream>
using namespace dlib;

using namespace cv;

int main(int argc, char** argv )
{

    // Mat img_cv2_Mat = imread( argv[1], 1 );
    // Mat img_cv2_Mat = imread( "lena.pgm");
    Mat img_cv2_Mat = imread( "lena.pgm");

    IplImage* img_ipl = cvCloneImage(&(IplImage)img_cv2_Mat);

    // Mat img_cv2_Mat(500,500, CV_8UC3, cv::Scalar(0,0,0));
    Point p1(10, 10), p2(200, 200);
    Scalar colorline(0, 255, 0);
    //img_cv2_Mat = line(img_cv2_Mat,Point(10,10), Point(20,30), cv::Scalar(0, 255, 0), 1, cv::LINE_AA);
    line(img_cv2_Mat, p1, p2, colorline, 2);


    // create dlib array2d image
    array2d<rgb_pixel> img_dlib_array2d;

    // Mat to cv_image
    cv_image<bgr_pixel> image(img_ipl);

    // cv_image to array2d
    matrix<rgb_pixel> matrix;
    assign_image(matrix, image);



    namedWindow("Display Image", WINDOW_AUTOSIZE );
    imshow("Display Image", img_cv2_Mat);

    waitKey(0);

    return 0;
}
