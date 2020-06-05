#include <opencv2/opencv.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/imgproc.hpp>
#include <iostream>
using namespace cv;
using namespace std;

Mat src, erosion_dst, dilation_dst;

int erosion_elem = 0;
int erosion_size = 0;
int dilation_elem = 0;
int dilation_size = 0;
int const max_elem = 2;
int const max_kernel_size = 21;

void Erosion( int, void*);
void Dilation( int, void*);


// Morphological operators: Erosion and Dilation;
// 形态算子：Erosion / 侵蚀 和 膨胀


int main(int argc, char** argv )
{

     src = imread( "car.jpg");

    // namedWindow("Origin Demo", WINDOW_AUTOSIZE);
    namedWindow("Erosion Demo", WINDOW_AUTOSIZE);
    namedWindow("Dilation Demo", WINDOW_AUTOSIZE);
    moveWindow("Dilation Demo", src.cols, 0);
   

    createTrackbar( "Element:\n 0: Rect \n 1: Cross \n 2: Ellipse", "Erosion Demo",
              &erosion_elem, max_elem,
              Erosion );
    createTrackbar( "Kernel size:\n 2n +1", "Erosion Demo",
              &erosion_size, max_kernel_size,
              Erosion );
    createTrackbar( "Element:\n 0: Rect \n 1: Cross \n 2: Ellipse", "Dilation Demo",
              &dilation_elem, max_elem,
              Dilation );
    createTrackbar( "Kernel size:\n 2n +1", "Dilation Demo",
              &dilation_size, max_kernel_size,
              Dilation );

    Erosion(0,0);
    Dilation(0,0);

    waitKey();

    return 0;
}


void Erosion(int, void*)
{
    int erosion_type = 0;
    if(erosion_elem==0){erosion_type=MORPH_RECT;}
    else if(erosion_elem==1){erosion_type=MORPH_CROSS;}
    else if(erosion_elem==2){erosion_type=MORPH_ELLIPSE;}

    erosion_type=MORPH_ELLIPSE;

    Mat element = getStructuringElement( erosion_type,
        Size( 2*erosion_size+1, 2*erosion_size+1),
        Point( erosion_size, erosion_size));
        Point( erosion_size, erosion_size));

    erode(src, erosion_dst, element);
    imshow("Erosion Demo", erosion_dst);
}

// Dilation: The value of the output pixel
//           is the maximum value of all the pixels
//           that fall within the structuring element's size and shape.
//           For example in a binary image, if any of the pixels of
//           the input image falling within the range of the kernel is set to the value 1,
//           the corresponding pixel of the output image will be set to 1 as well.
//           The latter applies to any type of image (e.g. grayscale, bgr, etc).
void Dilation( int, void*)
{
    int dilation_type = 0;
    if(dilation_elem==0) {dilation_type = MORPH_RECT;}
    else if(dilation_elem==1) {dilation_type = MORPH_CROSS;}
    else if(dilation_elem==2) {dilation_type = MORPH_ELLIPSE;}

    dilation_type = MORPH_ELLIPSE;

    Mat element = getStructuringElement( dilation_type,
                Size(2*dilation_size+1, 2*dilation_size+1),
                Point(dilation_size, dilation_size));
    dilate(src, dilation_dst, element);
    imshow("Dilation Demo", dilation_dst);
}