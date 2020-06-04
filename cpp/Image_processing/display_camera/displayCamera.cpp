#include <stdio.h>
#include <opencv2/opencv.hpp>


std::string get_tegra_pipeline(int width, int height, int fps) {
    // return "nvcamerasrc ! "
    // 
    return "nvarguscamerasrc ! video/x-raw(memory:NVMM), width=(int)" + std::to_string(width) + ", height=(int)" +
           std::to_string(height) + ", format=(string)NV12, framerate=(fraction)" + std::to_string(fps) +
           "/1 ! nvvidconv flip-method=0 ! video/x-raw, format=(string)BGRx ! videoconvert ! video/x-raw, format=(string)BGR ! appsink";
}


int main(int argc, char** argv )
{

    // std::string pipeline = get_tegra_pipeline(1280, 720, 60);
    cv::VideoCapture cap(0);
    cap.set(cv::CAP_PROP_FRAME_WIDTH,640);
    cap.set(cv::CAP_PROP_FRAME_HEIGHT,480);
    cv::Mat frame;
    while (1)
    {
	    cap >> frame;
	    cv::imshow("Display camera", frame);
	    cv::waitKey(1);
    }

    return 0;
}
