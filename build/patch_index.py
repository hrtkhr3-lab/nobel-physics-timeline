# -*- coding: utf-8 -*-
"""index.html の DATA 各エントリに正しい h:（個別ページへのリンク）を付け直す。"""
import re, os
from build_pages import NAV

IDX = r"c:\Users\PowerSystemLab\OneDrive - 国立大学法人福井大学\堀\github\歴代ノーベル賞\index.html"
with open(IDX, encoding="utf-8") as f:
    txt = f.read()

lines = txt.split("\n")
i = 0
out = []
for ln in lines:
    m = re.match(r'^(\s*)\{y:(\d{4}),', ln)
    if m:
        # 既存の ,h:"..." を除去
        body = re.sub(r',h:"[^"]*"', '', ln)
        # 末尾の } の直前に h を挿入
        href = 'laureates/' + NAV[i][0]
        body = body.rstrip()
        tail = '},' if body.endswith('},') else '}'
        assert body.endswith(tail), body
        body = body[:-len(tail)] + ',h:"' + href + '"' + tail
        out.append(m.group(1) + body.lstrip())
        i += 1
    else:
        out.append(ln)

assert i == len(NAV), "entries %d != NAV %d" % (i, len(NAV))
with open(IDX, "w", encoding="utf-8") as f:
    f.write("\n".join(out))
print("patched", i, "entries")
