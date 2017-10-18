import sys


def wx_news():
    from wxpy import Bot
    print('wx_news starts!')

    bot = Bot()

    news_group = bot.groups().search('快兰斯')[0]

    @bot.register(news_group)
    def print_news(msg):
        # msg.forward(bot.file_helper, prefix='新闻')
        print(msg.text)

    bot.join()


def ts_news():
    import datetime
    import tushare as ts
    import time

    print('ts_news starts!')
    url_list = []
    df = ts.get_latest_news(top=20)
    url_list.extend(list(df['url']))
    s = ts_series_from_url(df, url_list[0])
    print("=" * 10 + s.time[6:] + '   ' + s.title + "=" * 10)
    content = ts.latest_content(s.url)
    print(content + '\n')

    while True:
        url_list_new = []
        time.sleep(30)
        df_new = ts.get_latest_news(top=10)
        url_list_new = list(df_new['url'])
        for url in url_list_new:
            if url in url_list:
                continue
            else:
                try:
                    s = ts_series_from_url(df, url)
                    print(s)
                    # print("=" * 10 + s.time[6:] + '   ' + s.title + "=" * 10)
                    content = ts.latest_content(url)
                    print(content)
                except TypeError:
                    continue
                finally:
                    print("\n")


def ts_series_from_url(df, url):
    series = df[df['url'] == url].squeeze()
    return series


if __name__ == '__main__':
    if 'wx' in sys.argv:
        wx_news()
    elif 'ts' in sys.argv:
        ts_news()
