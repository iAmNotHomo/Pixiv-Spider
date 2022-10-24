# Pixiv-Spider
P站爬虫。

10月初以来，AI作图大行其道，我也没能免俗。为了让AI在我的XP上作图，我编写了这个脚本用来爬取P站插画，作为训练集。（完成脚本后向同学显摆，被问到为什么不直接下载画师合集，我懵逼了。我是真没想到还有那种办法。）

## 特性
支持下载关注列表中指定数量的更新，支持下载画师在指定日期内上传的插画，支持对关注列表中所有画师进行批量下载。

分画师保存图片，如路径中已存在同名文件则跳过下载，每次遇到网络波动会尝试重连最多10次。

没有实现模拟登录，而是通过手动输入cookie与uid来获取用户的登录信息。

自用脚本，几乎没有健壮性。不要输入奇奇怪怪的参数！

注：由于Windows文件命名限制，若画师用户名中含有`/` `\` `<` `>` `|` `"` `?` `*` `:`，会被统一替换为`-`进行保存。

又注：由于这是我写的第一个超过30行的py程序，所以函数定义有点不规范。脚本完成后我才知道py也能规定参数类型与返回值类型。

## 环境要求
- python 3（开发使用3.10）
- 安装`requests`与`lxml`库
- 科学上网（笑）

## 食用方法

### 1. 填写全局变量
下载PixivSpider.py，根据你的情况填写第6-9行的变量的值。

其中`cookie`与`userAgent`需要抓包分析。`xUserId`就是你的p站账号的uid。`file_root_path`是下载文件的保存目录。

#### Chrome浏览器抓包速通
1. 右击页面
2. 选择检查->网络
3. 勾选保留日志，过滤选项选择`Fetch/XHR`
4. 点击一个p站链接
5. 随便点一个捕获到的数据包，检查它的请求标头
6. 如果包里没有`cookie`数据就换个数据包看，直到在数据包的请求标头里找到`cookie`数据
7. 找到`cookie`与`userAgent`项，右键选择复制值，粘贴到PixivSpider.py的相应变量中

![image](https://user-images.githubusercontent.com/108179220/197403710-d0eb522c-40be-49cd-8ca6-b238a5b0fa2d.png)

#### 示例
这是我自用的脚本中填写的变量值。

![image](https://user-images.githubusercontent.com/108179220/197404175-01b79216-314d-451e-9e32-e9348ebe986d.png)

注意！
- 它们都是字符串
- 文件保存路径中的反斜杠需要转义为`"\\"`
- 不要漏了路径最后的那个反斜杠

### 2. 创建保存目录
以我的参数为例，需要手动创建好`E:\pixiv`文件夹。脚本会自动创建每个画师的子文件夹。

保存效果：

![image](https://user-images.githubusercontent.com/108179220/197404638-93e5224c-ac98-4bc8-a4dd-a0b2d4772e0b.png)

### 3. 运行！
爬虫有3种运行模式：
- 扫荡关注列表中的所有画师的最新20（参数定义在源文件211行，可以自行修改扫荡范围）张插画
  + （可选）指定单个画师的最大下载量
- 指定画师进行下载
  + （可选）指定最大下载量（以单张图片计数，(下载量达到设定值 且 当前pid下载完成)后 终止。例：设定最多下载3张图片，但画师的最新更新有5p，则将更新中的5p全部下载后终止）
  + （可选）指定上传日期（闭区间，精确到月）
- 指定下载量（以单次更新计数），下载更新列表中最新的插画。

依照程序提示输入参数即可使用。轻松加写意！
