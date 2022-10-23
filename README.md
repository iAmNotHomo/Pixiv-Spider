# Pixiv-Spider
P站爬虫。

支持下载关注列表中的指定数量的更新，支持下载画师在指定日期内上传的插画，支持对关注列表中所有画师进行批量下载。

能够自动跳过已下载的插画，遇到网络问题时会自动重试最多10次。

注：若画师用户名中含有`/` `\` `<` `>` `|` `"` `?` `*` `:`等特殊符号，将会被替换为`-`进行保存。

## 食用方法

### 1. 填写全局变量
下载PixivSpider.py，根据自己的情况填写第6-9行的变量。

其中`cookie`与`userAgent`需要抓包分析。`xUserId`就是你的p站账号的uid。`file_root_path`是下载文件的保存目录。

#### Chrome浏览器抓包速通
1. 右击页面
2. 选择检查->网络
3. 勾选保留日志，过滤选项选择Fetch/XHR
4. 点击一个p站链接
5. 随便点一个捕获到的数据包检查请求标头
6. 如果包里没有cookie数据就换个数据包看，直到在数据包的请求标头里找到cookie数据
7. 找到cookie与userAgent项，右键选择复制值，粘贴到PixivSpider.py的相应变量中

![image](https://user-images.githubusercontent.com/108179220/197403710-d0eb522c-40be-49cd-8ca6-b238a5b0fa2d.png)

#### 示例
这是我自用的脚本中填写的变量值，注意它们都是字符串，注意文件保存路径中的反斜杠需要转义为`"\\"`。

![image](https://user-images.githubusercontent.com/108179220/197404175-01b79216-314d-451e-9e32-e9348ebe986d.png)

保存效果：

![image](https://user-images.githubusercontent.com/108179220/197404638-93e5224c-ac98-4bc8-a4dd-a0b2d4772e0b.png)

### 2. 运行模式
爬虫有3种运行模式。
- 扫荡关注列表中的所有画师
  + （可选）指定单个画师的最大下载量
- 指定画师进行下载
  + （可选）指定最大下载量（以单张图片计数，(下载量达到设定值 且 当前pid下载完成)后 终止。例：设定最多下载3张图片，但画师的最新更新有5p，则将更新中的5p全部下载后终止）
  + （可选）指定上传日期（闭区间，精确到月）
- 指定下载量（以单次更新计数），下载更新列表中最新的插画。
依照程序提示输入参数即可使用。
