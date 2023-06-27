import requests
import datetime

OWNER = 'dbsduddn2000'
REPO = 'swego'
API_SERVER_URL = f"https://api.github.com/repos/{OWNER}/{REPO}"

MY_API_KEY = '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'

res = requests.get(f"{API_SERVER_URL}/releases/latest", auth=(OWNER, MY_API_KEY))
if res.status_code != 200:
    #QMessageBox.information(MainWindow, '로그인정보', '컴퓨터 정보저장 완료되었습니다 다시 로그인해주세요' , QMessageBox.Yes)
    print(datetime.datetime.now().strftime("%Y.%m.%d %H:%M:%S"), "업데이트 체크 실패")
print(res.json())