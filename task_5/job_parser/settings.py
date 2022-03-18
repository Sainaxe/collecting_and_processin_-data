BOT_NAME = 'job_parser'

SPIDER_MODULES = ['job_parser.spiders']
NEWSPIDER_MODULE = 'job_parser.spiders'

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'

ROBOTSTXT_OBEY = False

ITEM_PIPELINES = {
    'job_parser.pipelines.JobParserPipeline': 300,
}
