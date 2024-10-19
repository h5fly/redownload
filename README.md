# redownload
是用newbing生成的基于python的重复下载测试工具，用于测试网络下行速率。
## windows版本
默认下载地址为空，根据需要在config.json里设置下载地址

### config.json是配置文件：
url是下载地址，
oop_count是下载次数，
download_speed_MB是下载速率，单位是MB/s,0为不限速。

download_loop.exe是主程序，运行后直接开跑，可以在任务管理器中检查当前网速


## linux版本
首先确保系统安装了wget

脚本中，i<=69978900 这里是循环次数，更改等于号后边的数值
limit-rate=20M 这里是下载速率，单位是MB/s

https这里是下载地址，根据需要修改
