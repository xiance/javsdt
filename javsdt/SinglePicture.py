from Functions.Picture import add_watermark_divulge, crop_poster_youma
from Functions.Picture import check_picture, add_watermark_subtitle

path_poster = "Y:\\adult\\javlibrary\\EMP-002_一ノ瀬アメリ\EMP-002_一ノ瀬アメリ 極上ボディ-cd1-poster.jpg"
path_fanart = "Y:\\adult\\javlibrary\\EMP-002_一ノ瀬アメリ\EMP-002_一ノ瀬アメリ 極上ボディ-cd1-fanart.jpg"
crop_poster_youma(path_fanart, path_poster)
# 中文
# add_watermark_subtitle(path_poster)
# 无码流出
add_watermark_divulge(path_poster)

