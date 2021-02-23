from scrapy import cmdline

name = 'douban'
start_url = 'http://www.douban.com/group/26926/discussion'
max_page = '2'
search_strs = '十里堡,地铁'
proxy = 'http://61.191.84.224:4227'
cmd = 'scrapy crawl {0} -a start_url={1} -a max_page={2} -a search_strs={3} -a proxy={4}'.format(name, start_url, max_page, search_strs, proxy)
cmdline.execute(cmd.split())