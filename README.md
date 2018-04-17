# webcrawl
爬虫的实践

#使用shell行来运行爬虫
scrapy shell '地址'

#在顶层目录运行爬虫
scrapy crawl "爬虫的名字"

#将爬取的数据写入
scrapy crawl "爬虫的名字" -o data.json
scrapy crawl "爬虫的名字" -o data.jl

###scrapy的命令行的使用
创建项目scrapy startproject myproject 【project_dir] 如果未指定project_dir,就将与my project一样
控制项目
scrapy genspider <name> <domain>
name是spider的name<domain>参数用来设置allowed_domains和start_urls
scrapy genspider mydomain mydomain.com

#查看所有的可用命令
scrapy -h

crawl
#开始使用Spider爬取
scrapy crawl <spider>
check
#运行约定检查
scrapy check [-l] <spider>
#列出当前项目所有可用的Spider
scrapy list

#使用editor环境变量中定义的编辑器编辑给定的spider
scrapy edit <spider>

#使用Scrapy下载器下载给定的url并将内容写到标准输出
scrapy fetch <url>

#在浏览器中打开给定的URL，就像Scrapy Spider看到的那样
scrapy view <url>

#为指定的URL启动scrapy shell
scrapy shell

#获取给定url
scrapy parse <url> [options]

#获取Scrapy的设置值
scrapy settings [option]

#运行一个包含在Python文件中的Spider，而不必创建项目
scrapy runspider <spider_file.py>

#打印Scrapy版本，如果与-v一起使用
scrapy version [-v]

#运行一个快速基准测试
scrapy bench

还可以使用commands_modules设置来添加自定义项目命令
eg:COMMANDS_MODULE=‘mybot.commands',
#使用crawl命令-a选项传递spider参数
scrapy crawl myspider -a category=electronics