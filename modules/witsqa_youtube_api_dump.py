import pandas as pd
from pandas.core.frame import DataFrame
from yt_stats import YTstats

python_engineer_id = 'UCQxK-01l6hi0mZprya9USqg'
channel_id = python_engineer_id

yt = YTstats('AIzaSyAVY1UNekoQN1gpQIx0Jvce2LBRl5JrqQI', channel_id)
extract_raw = yt.get_channel_video_data()
extract_df = DataFrame(extract_raw)

extract_df.to_excel("output.xlsx")
