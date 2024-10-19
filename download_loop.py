import requests
import time
import json


def download_file(url, speed_MB):
    response = requests.get(url, stream=True)
    total_length = response.headers.get('content-length')

    if total_length is None:  # no content length header
        print("No content length header")
        return

    total_length = int(total_length)
    downloaded = 0
    start_time = time.time()

    speed = speed_MB * 1024 * 1024  # Convert MB/s to Bytes/s

    for data in response.iter_content(chunk_size=4096):
        downloaded += len(data)
        if speed > 0:
            elapsed_time = time.time() - start_time
            if elapsed_time > 0:
                current_speed = downloaded / elapsed_time
                if current_speed > speed:
                    time.sleep((downloaded / speed) - elapsed_time)
    global fuckjdnum
    fuckjdnum = fuckjdnum +1
    print("\n下载完成"+str(fuckjdnum)+"次")

def main():
    with open('config.json', 'r') as f:
        config = json.load(f)

    url = config['url']
    loop_count = config['loop_count']
    download_speed_MB = config.get('download_speed_MB', 0)

    for _ in range(loop_count):
        download_file(url, download_speed_MB)
        print("已清理，继续运行...\n")

if __name__ == "__main__":
    fuckjdnum = 0
    print("正在运行...")
    main()
    print("已达到设定次数")
    input()
