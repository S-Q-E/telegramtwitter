import datetime
import csv
import twint
import nest_asyncio
nest_asyncio.apply()


def get_tweet(keywords_list: list, max_likes: int):
    t = twint.Config()
    for num, word in enumerate(keywords_list):
        t.Search = word
        t.Min_likes = max_likes
        t.Limit = 10
        t.Since = str(datetime.date.today())
        t.Store_csv = True
        t.Output = fr'C:\Users\User\Desktop\tweetertelegrambot\files\{num}_file.csv'
        twint.run.Search(t)

        with open(fr'C:\Users\User\Desktop\tweetertelegrambot\files\{num}_file.csv', 'r', encoding='utf-8') as csv_file:
            lines = csv.DictReader(csv_file)
            all_lines = list(lines)
    return all_lines


# try:
#     with open(r'C:\Users\User\Desktop\tweetertelegrambot\files\file.csv', 'r', encoding='utf-8') as csv_file:
#         csv_reader = csv.DictReader(csv_file)
#         line_count = 0
#         for row in csv_reader:
#             if last_line in row:
#                 print('good')
#             else:
#                 if line_count == 0:
#                     print(f'Columns names are {",".join(row)}')
#                     line_count += 1
#                 print(f"Username: {row['username']}\n"
#                       f"Name: {row['name']}\n"
#                       f"Tweet: {row['tweet']}\n"
#                       f"URL: {row['link']}\n"
#                       f"{'-' * 1000}")
# except Exception as ex:
#     print(ex)
#
#
# def run():
#     schedule.every(1).minutes.do(get_tweet(['Covid', 'Python'], 100))
#     time.sleep(1)





