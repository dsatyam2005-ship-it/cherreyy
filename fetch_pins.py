import urllib.request
import re
import json

urls = {
    'fight': 'https://pin.it/61EDOcExl',
    'miss': 'https://pin.it/2tvmyzl9g',
    'sad': 'https://pin.it/7m5a4nRnw',
    'hug': 'https://pin.it/26in3BBOk',
    'happy': 'https://pin.it/7efMPYY9l'
}

opener = urllib.request.build_opener(urllib.request.HTTPRedirectHandler)
opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')]

results = {}

for k, u in urls.items():
    try:
        req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        resp = opener.open(req)
        final_url = resp.geturl()
        html = resp.read().decode('utf-8', errors='ignore')
        og_img = re.findall(r'<meta property=["\']og:image["\'] content=["\']([^"\']+)["\']', html)
        og_video = re.findall(r'<meta property=["\']og:video:[^"\']*["\'] content=["\']([^"\']+)["\']', html)
        canonical = re.findall(r'<link rel=["\']canonical["\'] href=["\']([^"\']+)["\']', html)
        
        # Also check for 736x or originals pin images or 720p videos
        pins_images = re.findall(r'https://i\.pinimg\.com/[^"\'\s<>]+', html)
        pins_videos = re.findall(r'https://v1\.pinimg\.com/[^"\'\s<>]+', html)
        
        results[k] = {
            'final_url': final_url,
            'canonical': canonical[:1],
            'og_image': og_img[:2],
            'og_video': og_video[:2],
            'pins_images': list(set(pins_images))[:5],
            'pins_videos': list(set(pins_videos))[:5],
        }
        print(f"Done {k}")
    except Exception as e:
        results[k] = {'error': str(e)}
        print(f"Error {k}: {e}")

with open('pin_results.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=2)
print("Saved pin_results.json")
