import re, sys, zipfile, io
z = zipfile.ZipFile('/tmp/confirm2_p7/bundle.zip')
def show(member, rx, width=60, maxn=6, mask=True):
    data = z.read(member)
    try:
        t = data.decode('utf-8')
    except UnicodeDecodeError:
        t = data.decode('latin-1')
    n = 0
    for m in re.finditer(rx, t):
        s = max(0, m.start()-width); e = min(len(t), m.end()+width)
        before = t[s:m.start()].replace('\n',' ')
        after = t[m.end():e].replace('\n',' ')
        mid = '<<%s:len%d>>' % ('HIT', len(m.group(0))) if mask else m.group(0)
        print(f'  [{member.split("art5-harmos-audit/")[-1]}] ...{before}{mid}{after}...')
        n += 1
        if n >= maxn: break
if __name__ == '__main__':
    pass
