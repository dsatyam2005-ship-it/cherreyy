import urllib.request
import os

media = {
    'fight': {
        'video': 'https://v1.pinimg.com/videos/iht/expMp4/3d/81/5f/3d815fec27307aa43ace6f73d2979b5f_720w.mp4',
        'poster': 'https://i.pinimg.com/736x/04/bf/90/04bf90d011b3bb302b06e51845b1f840.jpg'
    },
    'miss': {
        'video': 'https://v1.pinimg.com/videos/iht/expMp4/d4/c1/3e/d4c13e1ccf18bd66e7e31e1b5dcbb056_720w.mp4',
        'poster': 'https://i.pinimg.com/600x315/73/53/42/735342919f84667ed00057a06c0e242a.jpg'
    },
    'sad': {
        'video': 'https://v1.pinimg.com/videos/iht/expMp4/8d/34/2f/8d342f469e34ff26e74bb8b06f7e9d13_720w_t2.mp4',
        'poster': 'https://i.pinimg.com/736x/31/2d/78/312d78ac55b461997fd49d74da36446a.jpg'
    },
    'hug': {
        'video': 'https://v1.pinimg.com/videos/iht/expMp4/c8/30/52/c830522a955e7dfc05c9789d8fc2360e_720w.mp4',
        'poster': 'https://i.pinimg.com/736x/b2/63/52/b26352fa530dbcec4fafa994c9236090.jpg'
    },
    'happy': {
        'video': 'https://v1.pinimg.com/videos/iht/expMp4/17/ba/be/17babe92c574124540998008b939361d_720w.mp4',
        'poster': 'https://i.pinimg.com/600x315/c9/d9/7d/c9d97dcecde665d36e2c37be213ac888.jpg'
    }
}

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

for name, item in media.items():
    for mtype, url in item.items():
        ext = '.mp4' if mtype == 'video' else '.jpg'
        fname = f"{name}_{mtype}{ext}"
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req) as resp, open(fname, 'wb') as f:
                f.write(resp.read())
            print(f"Downloaded {fname} ({os.path.getsize(fname)} bytes)")
        except Exception as e:
            print(f"Failed {fname}: {e}")
