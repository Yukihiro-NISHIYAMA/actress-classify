from icrawler.builtin import GoogleImageCrawler

actress_enja = {
    "hashimoto kanna":"橋本環奈",
    "ishihara satomi":"石原さとみ",
    "koshiba fuka":"小芝風花",
    "sano hinako":"佐野ひなこ",
    "sasaki nozomi":"佐々木希",
    "yoshioka riho":"吉岡里帆",
}

for key in actress_enja:
    crawler = GoogleImageCrawler(storage={"root_dir": "./actress-images/train/{}".format(key)})
    crawler.crawl(keyword=actress_enja[key], max_num=300)

for key in actress_enja:
    crawler = GoogleImageCrawler(storage={"root_dir": "./actress-images/validation/{}".format(key)})
    crawler.crawl(keyword=actress_enja[key], max_num=60)

for key in actress_enja:
    crawler = GoogleImageCrawler(storage={"root_dir": "./actress-images/test/{}".format(key)})
    crawler.crawl(keyword=actress_enja[key], max_num=60)