"""Pixel sprites for 소 잃고 외양간 고친다 — single source of truth.
The cows are the same herd as in 소 귀에 경 읽기 (cows_from_sogwi.json, exported from that game's art).
Writes sprites.json (embedded into the game) and exports .aseprite + .png into ../assets/."""
import json, os
from PIL import Image
from aseprite import write_aseprite
here = os.path.dirname(os.path.abspath(__file__))

PAL = {
    'k': '#2a1a12', 'h': '#3a2a24', 'f': '#efc49a', 'e': '#1b1418', 'm': '#8b2b2b', 's': '#4c6b8a',
    'p': '#5a4030', 'y': '#e8c86a', 'R': '#b8382e', 'w': '#f1ece0', 'g': '#9aa3ad', 'b': '#9a6a3a',
    'c': '#f1ece0',
}
SPR = {
    'farmer': ['...kkkk...', '..kyyyyk..', 'kkyyyyyykk', 'kyyyyyyyyk', '.kkffffkk.', '.kfeffefk.', '.kffmmffk.',
               '..kffffk..', '.kssssssk.', 'ksssssssk.', 'kfssssssfk', 'kfssssssfk', '.kssssssk.', '.kppppppk.',
               '.kppkkppk.', '.kpk..kpk.', '.kpk..kpk.', 'kkkk..kkkk'],
    'hammer': ['kkkk....', 'kggkbbbb', 'kkkk....'],
    'plank': ['kkkkkkkk', 'kbbbbbbk', 'kbgbbgbk', 'kbbbbbbk', 'kbbbbbbk', 'kbgbbgbk', 'kbbbbbbk', 'kkkkkkkk'],
    'barn': ['....k....', '...kRk...', '..kRRRk..', '.kRRRRRk.', 'kRRwwwRRk', 'kRRwRwRRk', 'kRRwwwRRk', 'kkkkkkkkk'],
    'drum': ['.kkkkkk.', 'kccccccK'.replace('K', 'k'), 'kggggggk', 'kRRyyRRk', 'kRRRRRRk', 'kRyRRyRk', 'kRRRRRRk', '.kkkkkk.'],
    'person': ['..kkkk..', '.khhhhk.', '.kfefek.', '.kfmmfk.', '..kffk..', '.kssssk.', 'kfssssfk', 'kfssssfk',
               '.kssssk.', '.kppppk.', '.kpkkpk.', '.kk..kk.'],
    'heart': ['.kk.kk.', 'kRRkRRk', 'kRRRRRk', '.kRRRk.', '..kRk..', '...k...'],
    'flag': ['kkkkkkk.', 'kyyyyyyk', 'kyyyyyyk', 'kkkkkkk.', 'k.......', 'k.......', 'k.......', 'k.......', 'k.......', 'k.......'],
}
COWS = json.load(open(os.path.join(here, 'cows_from_sogwi.json')))
for k, rows in COWS['rows'].items(): SPR['cow_' + k] = rows
CPAL = COWS['pal']          # cow sprites use their own palette (same colours as 소 귀에 경 읽기)

def img(name):
    rows = SPR[name]; pal = CPAL if name.startswith('cow_') else PAL
    im = Image.new('RGBA', (len(rows[0]), len(rows)))
    for y, r in enumerate(rows):
        for x, ch in enumerate(r):
            if ch == '.': continue
            h = pal[ch]; im.putpixel((x, y), tuple(int(h[i:i + 2], 16) for i in (1, 3, 5)) + (255,))
    return im

if __name__ == '__main__':
    for n, rows in SPR.items(): assert len(set(map(len, rows))) == 1, (n, [len(r) for r in rows])
    json.dump({'pal': PAL, 'cpal': CPAL, 'spr': SPR}, open(os.path.join(here, 'sprites.json'), 'w'), ensure_ascii=False)
    out = os.path.join(here, '..', 'assets'); os.makedirs(out + '/aseprite', exist_ok=True); os.makedirs(out + '/png', exist_ok=True)
    pal = [tuple(int(h[i:i + 2], 16) for i in (1, 3, 5)) + (255,) for h in list(PAL.values()) + list(CPAL.values())]
    for n in SPR:
        if n.startswith('cow_'): continue
        im = img(n); write_aseprite(f'{out}/aseprite/{n}.aseprite', [im], palette=pal)
        im.resize((im.width * 4, im.height * 4), Image.NEAREST).save(f'{out}/png/{n}_x4.png')
    cows = [n for n in SPR if n.startswith('cow_')]
    frames = []
    for n in cows: f = Image.new('RGBA', (24, 24)); f.paste(img(n), (0, 24 - len(SPR[n]))); frames.append(f)
    write_aseprite(f'{out}/aseprite/herd.aseprite', frames, [200] * len(frames), [(n[4:], i, i) for i, n in enumerate(cows)], pal)
    sheet = Image.new('RGBA', (24 * len(frames), 24)); [sheet.paste(f, (24 * i, 0)) for i, f in enumerate(frames)]
    sheet.resize((sheet.width * 4, 96), Image.NEAREST).save(f'{out}/png/herd_sheet_x4.png')
    print('sprites ok', len(SPR))
