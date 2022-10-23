# Pixiv-Spider
P站爬虫。
支持下载关注列表中的指定数量的更新，支持下载画师在指定日期内上传的插画，支持对关注列表中所有画师进行批量下载。
能够自动跳过已下载的插画，遇到网络问题时会自动重试最多10次。

## 食用方法

### 1. 填写变量
下载PixivSpider.py，根据自己的情况填写第6-9行的变量。
其中'''cookie'''与'''userAgent'''需要抓包分析。'''xUserId'''就是你的p站账号的uid。'''file_root_path'''是保存目录。
chrome浏览器抓包速通：右击页面，选择检查->网络，勾选保留日志，过滤选项选择XHR/Fetch，然后点击一个p站链接，随便点一个捕获到的数据包检查请求标头。如果包里没有cookie数据就换个数据包看。在数据包的请求标头里找到cookie与userAgent后，右键选择复制值，粘贴到PixivSpider.py的相应变量中。
![image](https://user-images.githubusercontent.com/108179220/197403710-d0eb522c-40be-49cd-8ca6-b238a5b0fa2d.png)
这是我自用的脚本中填写的变量值，注意它们都是字符串变量，注意文件保存路径中的"\"需要转义为'''"\\"'''。
![image](https://user-images.githubusercontent.com/108179220/197404175-01b79216-314d-451e-9e32-e9348ebe986d.png)
