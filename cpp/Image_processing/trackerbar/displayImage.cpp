#include <iostream>
 #include <opencv2/core/core.hpp>
 #include <opencv2/highgui/highgui.hpp>
 #include <opencv2/imgproc.hpp>

using namespace std;
 using namespace cv;

//TrackBar发生改变的回调函数
void onChangeTrackBar(int pos, void* userdata);

//主函数
int main()
 {
     //trackbar的值
    int posTrackBar = 0;
     //trackbar的最大值
    int maxValue = 255;

    //读入图像，以灰度图形式读入
     Mat img = imread("F:\\图片\\timg.jpg", 0);

    //新建窗口
    namedWindow("二值化");
     imshow("二值化", img);

    //创建trackbar，我们把img作为数据传进回调函数中
    createTrackbar("pos", "二值化", &posTrackBar, maxValue, onChangeTrackBar, &img);

    waitKey();

    return 0;
 }

// 回调函数
void onChangeTrackBar(int pos, void* usrdata)
 {
     // 强制类型转换
    Mat src = *(Mat*)(usrdata);
     Mat dst;

    // 二值化
    threshold(src, dst, pos, 255, 0);
     imshow("二值化", dst);
 }