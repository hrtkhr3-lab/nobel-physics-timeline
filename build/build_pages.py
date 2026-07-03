# -*- coding: utf-8 -*-
"""歴代ノーベル物理学賞 個別ページ生成器.
共通シェル(CSS/レイアウト)を一元管理し、各ページは中身(3ブロック+図解)だけ記述する。
出力先: ../laureates/  (プロジェクト内)。既存の 01,02,03,06 は手書き済みなので生成対象外。
前/次ナビは NAV(全45件・年代順) から自動導出 → リンク切れを防ぐ。
"""
import os

OUT = os.path.join(os.path.dirname(__file__), "..", "laureates")
OUT = os.path.abspath(os.path.join(
    r"c:\Users\PowerSystemLab\OneDrive - 国立大学法人福井大学\堀\github\歴代ノーベル賞", "laureates"))

THEME = {
    "radiation": ("#c2410c", "#fdeee5", "#7c2d12"),
    "quantum":   ("#7c3aed", "#f1ebff", "#4c1d95"),
    "particle":  ("#0d9488", "#e2f5f2", "#115e59"),
    "cosmos":    ("#2563eb", "#e8f0fe", "#1e3a8a"),
    "matter":    ("#16a34a", "#e6f6ec", "#14532d"),
}

# 全45件・年代順: (file, "YEAR 短縮名")  ← 前/次ナビ用
NAV = [
 ("01_1901_roentgen.html",       "1901 レントゲン"),
 ("02_1903_curie.html",          "1903 キュリー夫妻"),
 ("03_1906_thomson.html",        "1906 J.J.トムソン"),
 ("04_1907_michelson.html",      "1907 マイケルソン"),
 ("05_1918_planck.html",         "1918 プランク"),
 ("06_1921_einstein.html",       "1921 アインシュタイン"),
 ("07_1922_bohr.html",           "1922 ボーア"),
 ("08_1923_millikan.html",       "1923 ミリカン"),
 ("09_1927_compton.html",        "1927 コンプトン"),
 ("10_1929_de_broglie.html",     "1929 ド・ブロイ"),
 ("11_1932_heisenberg.html",     "1932 ハイゼンベルク"),
 ("12_1933_schrodinger_dirac.html","1933 シュレディンガー／ディラック"),
 ("13_1935_chadwick.html",       "1935 チャドウィック"),
 ("14_1938_fermi.html",          "1938 フェルミ"),
 ("15_1945_pauli.html",          "1945 パウリ"),
 ("16_1949_yukawa.html",         "1949 湯川秀樹"),
 ("17_1956_transistor.html",     "1956 トランジスタ"),
 ("18_1957_lee_yang.html",       "1957 リー／ヤン"),
 ("19_1962_landau.html",         "1962 ランダウ"),
 ("20_1964_townes.html",         "1964 タウンズ"),
 ("21_1965_tomonaga.html",       "1965 朝永振一郎"),
 ("22_1972_bcs.html",            "1972 BCS理論"),
 ("23_1974_pulsar.html",         "1974 パルサー"),
 ("24_1978_cmb.html",            "1978 宇宙背景放射"),
 ("25_1979_electroweak.html",    "1979 電弱統一"),
 ("26_1983_chandrasekhar.html",  "1983 チャンドラセカール"),
 ("27_1986_stm.html",            "1986 走査トンネル顕微鏡"),
 ("28_1988_neutrino.html",       "1988 ニュートリノ"),
 ("29_2002_koshiba.html",        "2002 小柴昌俊"),
 ("30_2008_nambu.html",          "2008 南部／小林／益川"),
 ("31_2009_fiber.html",          "2009 光ファイバー"),
 ("32_2010_graphene.html",       "2010 グラフェン"),
 ("33_2011_dark_energy.html",    "2011 加速膨張"),
 ("34_2013_higgs.html",          "2013 ヒッグス"),
 ("35_2014_blue_led.html",       "2014 青色LED"),
 ("36_2015_kajita.html",         "2015 梶田隆章"),
 ("37_2016_topology.html",       "2016 トポロジカル相"),
 ("38_2017_ligo.html",           "2017 重力波"),
 ("39_2018_laser_tools.html",    "2018 レーザー技術"),
 ("40_2019_exoplanet.html",      "2019 系外惑星"),
 ("41_2020_black_hole.html",     "2020 ブラックホール"),
 ("42_2021_manabe.html",         "2021 真鍋淑郎"),
 ("43_2022_entanglement.html",   "2022 量子もつれ"),
 ("44_2023_attosecond.html",     "2023 アト秒"),
 ("45_2024_ml.html",             "2024 機械学習"),
]
IDX = {f: i for i, (f, _) in enumerate(NAV)}

TEMPLATE = r'''<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>@@TITLE@@</title>
<style>
  :root{--bg:#f5f4ef;--card:#fff;--ink:#20242e;--muted:#5b6472;--line:#e6e3d9;--accent:@@ACCENT@@;--accent-soft:@@SOFT@@;--hero:@@HERO@@;}
  *{box-sizing:border-box}
  body{margin:0;font-family:"Yu Gothic","Yu Gothic UI","Hiragino Kaku Gothic ProN","Meiryo",sans-serif;background:var(--bg);color:var(--ink);line-height:1.8;-webkit-font-smoothing:antialiased}
  a{color:var(--accent);text-decoration:none}
  .wrap{max-width:860px;margin:0 auto;padding:0 20px 80px}
  .topnav{max-width:860px;margin:0 auto;padding:16px 20px;display:flex;justify-content:space-between;align-items:center;font-size:.9rem}
  .topnav a{color:var(--muted)} .topnav a:hover{color:var(--accent)}
  .hero{background:linear-gradient(135deg,var(--accent),var(--hero));color:#fff;border-radius:20px;padding:34px 30px;margin-top:6px;box-shadow:0 12px 30px rgba(0,0,0,.12)}
  .year{display:inline-block;background:rgba(255,255,255,.22);padding:3px 14px;border-radius:999px;font-weight:700;letter-spacing:.05em;font-size:.9rem}
  .hero h1{margin:14px 0 6px;font-size:2rem;line-height:1.3}
  .hero .who{font-size:1.05rem;opacity:.95}
  .cite{margin-top:16px;padding:12px 16px;background:rgba(255,255,255,.14);border-radius:12px;font-size:.95rem}
  section.block{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:24px 26px;margin-top:22px}
  section.block h2{margin:0 0 10px;font-size:1.15rem;display:flex;align-items:center;gap:10px}
  section.block h2 .no{width:28px;height:28px;border-radius:50%;background:var(--accent-soft);color:var(--accent);display:grid;place-items:center;font-size:.9rem;font-weight:800;flex:none}
  p{margin:.5em 0}
  .term{border-bottom:2px dotted var(--accent);cursor:help;position:relative}
  .term:hover::after{content:attr(data-tip);position:absolute;left:0;bottom:135%;width:250px;background:#20242e;color:#fff;font-size:.8rem;line-height:1.6;padding:10px 12px;border-radius:10px;box-shadow:0 8px 20px rgba(0,0,0,.25);z-index:5}
  .term:hover::before{content:"";position:absolute;left:14px;bottom:125%;border:6px solid transparent;border-top-color:#20242e;z-index:5}
  .demo{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:24px 26px;margin-top:22px}
  .demo h2{margin:0 0 4px;font-size:1.15rem}
  .demo .hint{color:var(--muted);font-size:.9rem;margin-bottom:16px}
  .xbox{background:#0f1420;border-radius:14px;padding:10px;display:flex;justify-content:center;overflow-x:auto}
  .controls{max-width:460px;margin:18px auto 0}
  .controls label{display:block;font-weight:700;margin:12px 0 6px;font-size:.95rem}
  input[type=range]{width:100%;accent-color:var(--accent)}
  .btns{display:flex;gap:10px;justify-content:center;margin-top:18px;flex-wrap:wrap}
  .btns button{border:2px solid var(--line);background:#fff;border-radius:999px;padding:9px 20px;font-size:1rem;font-weight:700;cursor:pointer;font-family:inherit;color:var(--ink)}
  .btns button.on{background:var(--accent);border-color:var(--accent);color:#fff}
  .readout{text-align:center;margin-top:14px;font-size:.98rem;color:var(--muted)}
  .readout b{color:var(--ink)}
  .status{margin-top:16px;text-align:center;font-size:1rem;padding:12px;border-radius:12px;font-weight:700}
  .status.no{background:#fdecea;color:#b42318}
  .status.yes{background:#e7f8ee;color:#087443}
  .note{font-size:.82rem;color:var(--muted);margin-top:14px;padding-top:12px;border-top:1px dashed var(--line)}
  .pager{display:flex;justify-content:space-between;gap:12px;margin-top:30px}
  .pager a{flex:1;background:var(--card);border:1px solid var(--line);border-radius:12px;padding:14px 16px;color:var(--ink);font-size:.9rem}
  .pager a.next{text-align:right}
  .pager a:hover{border-color:var(--accent);color:var(--accent)}
  .pager span{display:block;font-size:.75rem;color:var(--muted)}
  .src{font-size:.82rem;color:var(--muted);margin-top:24px}
  svg text{font-family:"Yu Gothic","Meiryo",sans-serif}
</style>

<nav class="topnav">
  <a href="../index.html">← 年表一覧へ</a>
  <span>物理学賞の歩み @@NN@@ / 45</span>
</nav>

<div class="wrap">
  <div class="hero">
    <span class="year">@@YEAR@@年</span>
    <h1>@@H1@@</h1>
    <div class="who">@@WHO@@</div>
    <div class="cite"><b>受賞理由：</b>@@CITE@@</div>
  </div>

  <section class="block">
    <h2><span class="no">1</span>背景 ── @@B1H@@</h2>
    @@B1@@
  </section>

  <section class="block">
    <h2><span class="no">2</span>発見 ── @@B2H@@</h2>
    @@B2@@
  </section>

  <!-- INTERACTIVE -->
  <div class="demo">
@@DEMO@@
  </div>

  <section class="block">
    <h2><span class="no">3</span>意義 ── いまへのつながり</h2>
    @@B3@@
  </section>

  <p class="src"><b>主な出典：</b>ノーベル財団 公式サイト（nobelprize.org）@@YEAR@@年物理学賞ページ、一般向け科学史資料。@@SRCX@@</p>

  <div class="pager">
    @@PREV@@
    @@NEXT@@
  </div>
</div>

<script>
@@SCRIPT@@
</script>
'''

PAGES = []  # 各バッチで append される

def page(file, theme, year, h1, who, cite, b1h, b1, b2h, b2, demo, b3, script, srcx=""):
    PAGES.append(dict(file=file, theme=theme, year=year, h1=h1, who=who, cite=cite,
                      b1h=b1h, b1=b1, b2h=b2h, b2=b2, demo=demo, b3=b3, script=script, srcx=srcx))

def build():
    os.makedirs(OUT, exist_ok=True)
    for p in PAGES:
        acc, soft, hero = THEME[p["theme"]]
        i = IDX[p["file"]]
        # prev
        if i == 0:
            prev = '<a class="prev" href="../index.html"><span>もどる</span>年表一覧へ</a>'
        else:
            pf, pl = NAV[i-1]
            prev = '<a class="prev" href="%s"><span>前へ</span>← %s</a>' % (pf, pl)
        # next
        if i == len(NAV)-1:
            nxt = '<a class="next" href="../index.html"><span>このあと</span>年表一覧へ →</a>'
        else:
            nf, nl = NAV[i+1]
            nxt = '<a class="next" href="%s"><span>次へ</span>%s →</a>' % (nf, nl)
        html = TEMPLATE
        topic = p["h1"].split(" ── ")[-1] if " ── " in p["h1"] else p["h1"]
        rep = {
            "@@TITLE@@": "%s — %s" % (NAV[i][1], topic),
            "@@ACCENT@@": acc, "@@SOFT@@": soft, "@@HERO@@": hero,
            "@@NN@@": p["file"][:2], "@@YEAR@@": str(p["year"]),
            "@@H1@@": p["h1"], "@@WHO@@": p["who"], "@@CITE@@": p["cite"],
            "@@B1H@@": p["b1h"], "@@B1@@": p["b1"], "@@B2H@@": p["b2h"], "@@B2@@": p["b2"],
            "@@DEMO@@": p["demo"], "@@B3@@": p["b3"], "@@SCRIPT@@": p["script"],
            "@@PREV@@": prev, "@@NEXT@@": nxt, "@@SRCX@@": p["srcx"],
        }
        for k, v in rep.items():
            html = html.replace(k, v)
        with open(os.path.join(OUT, p["file"]), "w", encoding="utf-8") as f:
            f.write(html)
    print("generated", len(PAGES), "pages")

# ==== ページ定義は pages_*.py から読み込む ====
if __name__ == "__main__":
    import pages_data
    pages_data.register(page)
    build()
