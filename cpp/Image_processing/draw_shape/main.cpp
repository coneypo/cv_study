#include <stdio.h>
#include <opencv2/opencv.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/video.hpp>
#include <opencv2/imgproc.hpp>
using namespace cv;


int main( int argc, char** argv )
{

    // 1. Create a blank image
    Mat image(500,500, CV_8UC3, cv::Scalar(0,0,0));

    // 2. Draw line
    Point p1(100,100), p2(200,100);
    Scalar colorLine(0,255,0); // Green
    int thicknessLine = 2;
    
    line(image, p1, p2, colorLine, thicknessLine);

    // 2. Draw circle with unfilled
    Point centerCircle1(250,250);
    int radiusCircle = 30;
    Scalar colorCircle1(0,0,255);
    int thicknessCircle1 = 2;

    circle(image, centerCircle1, radiusCircle, colorCircle1, thicknessCircle1);

    // 3. Draw circle with filled
    Point centerCircle2(400,100);
    Scalar colorCircle2(0,100,0);

    circle(image, centerCircle2, radiusCircle, colorCircle2, FILLED);

    // 4. Draw rectangle with unfilled
    Point p3(400,400), p4(450,450);
    Scalar colorRectangle1(0,0,255);
    int thicknessRectangle1 = 3;

    rectangle(image, p3, p4, colorRectangle1,thicknessRectangle1);

    // 5. Draw rectangle with filled
    Point p5(100,400), p6(150,450);
    Scalar colorRectangle2(255,0,255);

    rectangle(image, p5, p6, colorRectangle2, FILLED);

    
    namedWindow( "Display window", WINDOW_AUTOSIZE );
    imshow( "Display window", image );

    imwrite("shapes.png", image);

    waitKey(0);
    return 0;
}
