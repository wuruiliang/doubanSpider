## 豆瓣小组数据查询程序

### 目的：
方便从各种小组发布信息中找到自己需要信息，减少肉眼过滤关键字的工作；

### 使用方式：
1. 首先需要安装python和scrapy环境, 参考：`https://docs.scrapy.org/en/latest/intro/install.html`；
2. 项目目录下执行命令：
   `scrapy crawl douban -a start_url=http://www.douban.com/group/xxxxx/discussion -a max_page=30 -a search_strs='XXX,XX' -a proxy='http://xxx.xxx.xxx.xxx:xxxx'`
   其中`proxy`参数可选, `start_url`为豆瓣小组第一页的路径，注意一定是带有页码的第一页，`max_size`为最多查询的页数， `search_strs`为过滤的关键字，以`,`隔开，强烈建议配置`proxy`以防IP被封禁；
3. 运行结束后同一目录下会生成一个`output.html`文件，使用浏览器打开即可。   