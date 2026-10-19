import urllib.request
import re

url = 'https://pin.it/7m5a4nRnw'
opener = urllib.request.build_opener(urllib.request.HTTPRedirectHandler)
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
resp = opener.open(req)
html = resp.read().decode('utf-8', errors='ignore')

# Extract all video urls
vids = re.findall(r'https://v1\.pinimg\.com/videos/[^\s"\'<>]+', html)
print("Found video links:", len(vids))
for v in set(vids):
    print(v)
    try:
        req_v = urllib.request.Request(v, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req_v) as r:
            data = r.read()
            if len(data) > 1000:
                print(f"SUCCESS {v} ({len(data)} bytes)")
                with open('sad_video.mp4', 'wb') as out:
                    out.write(data)
                break
    except Exception as e:
        print(f"Err {v}: {e}")
