import requests
from datetime import datetime
import pytz

current_utc_time = datetime.utcnow()
taipei_timezone = pytz.timezone('Asia/Taipei')
current_taipei_time = current_utc_time.replace(tzinfo=pytz.utc).astimezone(taipei_timezone)
current_taipei_time = current_taipei_time.strftime('%Y/%m/%d %H:%M:%S')

url = "http://www.ntu.org.tw/webs/index.php"
r = requests.get(url)
message = ""
if r.status_code != 200:
    message = f"{current_taipei_time} 網站出現問題！"
    token = "6948820173:AAHR8IEhZ4GHJmllH5vd18W_TkHIxUCTcgw"
    chat_id = "5740033148"
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
    requests.get(url)
