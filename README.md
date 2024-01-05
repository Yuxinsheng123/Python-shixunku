# Douban Top 250 电影数据爬虫

## 项目介绍
本项目包含一个用于爬取Douban（豆瓣）Top 250 电影排名的Python脚本，豆瓣是一个在中国流行的社交网络服务网站，其中包括用户评论和评分。该脚本针对电影标题、评分、评论数量、电影详情URL、图片URL和摘要等具体细节。它通过线程池执行器实现并发网络请求以优化爬取过程。

###使用方法
要运行此爬虫，请按照以下步骤操作：
1. 确认系统已安装Python。
2. 安装必要的Python包：使用`pip install requests`安装`requests`处理HTTP请求，使用`pip install beautifulsoup4`安装`bs4`包中的`BeautifulSoup`解析HTML内容，使用标准库模块`csv`导出数据。
3. 从终端或命令提示符执行脚本。

#### 依赖库
- **requests** - 安装命令：`pip install requests`
- **BeautifulSoup**（`bs4`包的一部分） - 安装命令：`pip install beautifulsoup4`
- **csv** - 标准库模块，用于CSV文件处理。
- **ThreadPoolExecutor**（`concurrent.futures`模块的一部分） - 标准库模块，用于并发执行。

##### 代码运行
执行脚本时，将执行以下操作：
1. 使用`requests.Session()`开启会话，保持跨请求的持久性参数。
2. 使用`ThreadPoolExecutor`创建线程池执行器以管理爬虫线程。
3. 通过改变URL参数`start`，迭代Douban Top 250电影列表页面。
4. 使用`executor.submit()`在不同的线程中并发获取和处理每个页面的电影数据。
5. 将所有电影收集到一个名为`top250_movies`的单一列表中，通过展平结果列表实现。
6. 调用`save_to_csv()`将数据写入命名为"Douban Top250 Movies.csv"的CSV文件中。
7. 计算总执行时间并输出。

输出是包含电影详细信息的CSV文件，可用于分析、数据挖掘或简单地作为个人参考。

###### 结果
脚本会输出一个包含以下列的CSV文件：
- 电影详细信息URL
- 图片URL
- 中文标题
- 外文标题
- 评分
- 评价人数
- 摘要
- 其他信息（包括导演、年份等）

脚本执行结束后，将打印出爬虫过程的预期持续时间，即所有线程完成执行后的时间。CSV文件将位于脚本相同的目录中。
