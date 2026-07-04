# 歴代ノーベル物理学賞 ビジュアル年表

物理学史の節目となったノーベル物理学賞の**受賞研究そのもの**を、一般・高校生向けにやさしく解説する、
**完全オフラインの自己完結型HTMLツール**です。1901年から2024年まで、**45件**を古い順に収録しています。

各ページには、研究内容を直感的につかむための**インタラクティブ図解**が1つずつ付いています。
うち**25件は、物理式に基づく定量シミュレーション**（実単位のスライダーで実験を追体験できる「実験してみよう」型）です。
さらに全45ページに、数式を使った大学初年級レベルの**「発展」セクション**（折りたたみ式）を備えており、
やさしい本文と専門的な解説の2段構えで読めます。外部ネットワークなしでブラウザで動きます。

▶ **オンラインで見る**: https://hrtkhr3-lab.github.io/nobel-physics-timeline/

## リンク

- ▶ **[オンラインで開く（GitHub Pages）](https://hrtkhr3-lab.github.io/nobel-physics-timeline/)** ← クリックでそのまま動きます
- 各受賞の個別ページは下の[収録リスト](#収録リスト45件古い順)からリンクで開けます
- ⚙️ 生成スクリプト: [build/build_pages.py](build/build_pages.py) ／ [build/pages_data.py](build/pages_data.py) ／ [build/patch_index.py](build/patch_index.py)

> オンライン版（上のリンク）は GitHub Pages でそのまま動きます。ローカルで使う場合は、リポジトリをダウンロードして `index.html` をブラウザで開いてください（`file://` 直開きOK）。

---

## 使い方

1. **`index.html`** をダブルクリックして開きます（ブラウザの `file://` で直接開けます。サーバー不要）。
2. 年代順に並んだカードから、見たい受賞をクリックすると個別ページへ移動します。
3. 個別ページでは次のことができます。
   - 受賞年・受賞者・**受賞理由（やさしい和訳）**を読む
   - **背景 → 発見 → 意義** の3ステップで研究内容を理解する
   - **図解を操作**して現象を体験する（各ページ1つ）。体験型シミュレーションのページでは、
     管電圧・温度・散乱角・質量などの**実単位のパラメータ**を動かして物理式どおりの応答をグラフで確かめられます
   - **「発展 ── もっと詳しく知りたい人へ（数式あり）」**を開くと、数式・導出の考え方・現代とのつながりが読めます
   - 難しい用語は**点線の語**にマウスを乗せると意味が出ます（ふりがな・補足）
   - ページ下部の **前へ／次へ／年表一覧へ** で移動する
4. 一覧ページでは、**キーワード検索**（例：湯川、レーザー、1965）や、**分野フィルタ**（放射線・量子・素粒子・宇宙・物性）で絞り込めます。

> オフライン（機内モード相当）でも、すべてのページ・図解・リンクが動作します。
> 外部CDN・外部画像・外部フォント・`fetch()` は一切使っていません。日本語フォントはシステム標準（Yu Gothic 等）を指定しています。

---

## ファイル構成

```
歴代ノーベル賞/
├── index.html            … 年代順タイムライン一覧（全45件を埋め込み・検索/フィルタ付き）
├── README.md             … このファイル
├── laureates/            … 受賞ごとの個別ページ（自己完結HTML・45ファイル）
│   ├── 01_1901_roentgen.html
│   ├── 02_1903_curie.html
│   ├── …
│   └── 45_2024_ml.html
└── build/                … 生成用スクリプト（再生成・メンテ用。閲覧には不要）
    ├── build_pages.py    … 共通レイアウト雛形＋生成エンジン
    ├── pages_data.py     … 各ページの本文・図解の定義（全45件）
    ├── sims_data.py      … 定量シミュレーション25件（図解を差し替える）
    ├── advanced_data.py  … 「発展」セクション45件（数式・専門解説）
    └── patch_index.py    … index.html のリンク張り替え
```

各個別HTMLは **CSS・JavaScript・データをすべて内部に埋め込んだ自己完結ファイル**です。
1ファイルだけ他所へコピーしても単体で開けます（前後ページ・一覧へのリンクは相対パス）。
ファイル名は `連番_受賞年_内容.html`（連番＝年代順の通し番号）。

---

## 収録リスト（45件・古い順）

| # | 年 | 受賞（テーマ） | 分野 |
|---|---|---|---|
| 01 | 1901 | [レントゲン（X線）](https://hrtkhr3-lab.github.io/nobel-physics-timeline/laureates/01_1901_roentgen.html) | 放射線・原子 |
| 02 | 1903 | [ベクレル／キュリー夫妻（放射能）](https://hrtkhr3-lab.github.io/nobel-physics-timeline/laureates/02_1903_curie.html) | 放射線・原子 |
| 03 | 1906 | [J.J.トムソン（電子の発見）](https://hrtkhr3-lab.github.io/nobel-physics-timeline/laureates/03_1906_thomson.html) | 放射線・原子 |
| 04 | 1907 | [マイケルソン（干渉計）](https://hrtkhr3-lab.github.io/nobel-physics-timeline/laureates/04_1907_michelson.html) | 物性・応用 |
| 05 | 1918 | [プランク（エネルギー量子）](https://hrtkhr3-lab.github.io/nobel-physics-timeline/laureates/05_1918_planck.html) | 量子力学 |
| 06 | 1921 | [アインシュタイン（光電効果）](https://hrtkhr3-lab.github.io/nobel-physics-timeline/laureates/06_1921_einstein.html) | 量子力学 |
| 07 | 1922 | [ボーア（原子模型）](https://hrtkhr3-lab.github.io/nobel-physics-timeline/laureates/07_1922_bohr.html) | 量子力学 |
| 08 | 1923 | [ミリカン（電気素量）](https://hrtkhr3-lab.github.io/nobel-physics-timeline/laureates/08_1923_millikan.html) | 放射線・原子 |
| 09 | 1927 | [コンプトン（コンプトン効果）](https://hrtkhr3-lab.github.io/nobel-physics-timeline/laureates/09_1927_compton.html) | 量子力学 |
| 10 | 1929 | [ド・ブロイ（物質波）](https://hrtkhr3-lab.github.io/nobel-physics-timeline/laureates/10_1929_de_broglie.html) | 量子力学 |
| 11 | 1932 | [ハイゼンベルク（不確定性原理）](https://hrtkhr3-lab.github.io/nobel-physics-timeline/laureates/11_1932_heisenberg.html) | 量子力学 |
| 12 | 1933 | [シュレディンガー／ディラック（波動力学・反物質）](https://hrtkhr3-lab.github.io/nobel-physics-timeline/laureates/12_1933_schrodinger_dirac.html) | 量子力学 |
| 13 | 1935 | [チャドウィック（中性子）](https://hrtkhr3-lab.github.io/nobel-physics-timeline/laureates/13_1935_chadwick.html) | 素粒子・核 |
| 14 | 1938 | [フェルミ（遅い中性子・核反応）](https://hrtkhr3-lab.github.io/nobel-physics-timeline/laureates/14_1938_fermi.html) | 素粒子・核 |
| 15 | 1945 | [パウリ（排他原理）](https://hrtkhr3-lab.github.io/nobel-physics-timeline/laureates/15_1945_pauli.html) | 量子力学 |
| 16 | 1949 | [**湯川秀樹**（中間子の予言）](https://hrtkhr3-lab.github.io/nobel-physics-timeline/laureates/16_1949_yukawa.html) | 素粒子・核 |
| 17 | 1956 | [ショックレー他（トランジスタ）](https://hrtkhr3-lab.github.io/nobel-physics-timeline/laureates/17_1956_transistor.html) | 物性・応用 |
| 18 | 1957 | [リー／ヤン（パリティの破れ）](https://hrtkhr3-lab.github.io/nobel-physics-timeline/laureates/18_1957_lee_yang.html) | 素粒子・核 |
| 19 | 1962 | [ランダウ（超流動）](https://hrtkhr3-lab.github.io/nobel-physics-timeline/laureates/19_1962_landau.html) | 物性・応用 |
| 20 | 1964 | [タウンズ他（メーザー・レーザー）](https://hrtkhr3-lab.github.io/nobel-physics-timeline/laureates/20_1964_townes.html) | 物性・応用 |
| 21 | 1965 | [**朝永振一郎**他（量子電磁力学 QED）](https://hrtkhr3-lab.github.io/nobel-physics-timeline/laureates/21_1965_tomonaga.html) | 量子力学 |
| 22 | 1972 | [バーディーン他（超伝導 BCS理論）](https://hrtkhr3-lab.github.io/nobel-physics-timeline/laureates/22_1972_bcs.html) | 物性・応用 |
| 23 | 1974 | [ライル／ヒューイッシュ（パルサー）](https://hrtkhr3-lab.github.io/nobel-physics-timeline/laureates/23_1974_pulsar.html) | 宇宙・天文 |
| 24 | 1978 | [ペンジアス／ウィルソン（宇宙背景放射）](https://hrtkhr3-lab.github.io/nobel-physics-timeline/laureates/24_1978_cmb.html) | 宇宙・天文 |
| 25 | 1979 | [ワインバーグ他（電弱統一）](https://hrtkhr3-lab.github.io/nobel-physics-timeline/laureates/25_1979_electroweak.html) | 素粒子・核 |
| 26 | 1983 | [チャンドラセカール（星の進化・限界質量）](https://hrtkhr3-lab.github.io/nobel-physics-timeline/laureates/26_1983_chandrasekhar.html) | 宇宙・天文 |
| 27 | 1986 | [ビニッヒ他（走査トンネル顕微鏡）](https://hrtkhr3-lab.github.io/nobel-physics-timeline/laureates/27_1986_stm.html) | 物性・応用 |
| 28 | 1988 | [レーダーマン他（ニュートリノ）](https://hrtkhr3-lab.github.io/nobel-physics-timeline/laureates/28_1988_neutrino.html) | 素粒子・核 |
| 29 | 2002 | [**小柴昌俊**他（ニュートリノ天文学）](https://hrtkhr3-lab.github.io/nobel-physics-timeline/laureates/29_2002_koshiba.html) | 宇宙・天文 |
| 30 | 2008 | [**南部・小林・益川**（対称性の破れ）](https://hrtkhr3-lab.github.io/nobel-physics-timeline/laureates/30_2008_nambu.html) | 素粒子・核 |
| 31 | 2009 | [高錕（光ファイバー）](https://hrtkhr3-lab.github.io/nobel-physics-timeline/laureates/31_2009_fiber.html) | 物性・応用 |
| 32 | 2010 | [ガイム／ノボセロフ（グラフェン）](https://hrtkhr3-lab.github.io/nobel-physics-timeline/laureates/32_2010_graphene.html) | 物性・応用 |
| 33 | 2011 | [パールマッター他（宇宙の加速膨張）](https://hrtkhr3-lab.github.io/nobel-physics-timeline/laureates/33_2011_dark_energy.html) | 宇宙・天文 |
| 34 | 2013 | [アングレール／ヒッグス（ヒッグス機構）](https://hrtkhr3-lab.github.io/nobel-physics-timeline/laureates/34_2013_higgs.html) | 素粒子・核 |
| 35 | 2014 | [**赤﨑・天野・中村**（青色LED）](https://hrtkhr3-lab.github.io/nobel-physics-timeline/laureates/35_2014_blue_led.html) | 物性・応用 |
| 36 | 2015 | [**梶田隆章**他（ニュートリノ振動）](https://hrtkhr3-lab.github.io/nobel-physics-timeline/laureates/36_2015_kajita.html) | 宇宙・天文 |
| 37 | 2016 | [サウレス他（トポロジカル相）](https://hrtkhr3-lab.github.io/nobel-physics-timeline/laureates/37_2016_topology.html) | 物性・応用 |
| 38 | 2017 | [ワイス他（重力波 LIGO）](https://hrtkhr3-lab.github.io/nobel-physics-timeline/laureates/38_2017_ligo.html) | 宇宙・天文 |
| 39 | 2018 | [アシュキン他（レーザー技術）](https://hrtkhr3-lab.github.io/nobel-physics-timeline/laureates/39_2018_laser_tools.html) | 物性・応用 |
| 40 | 2019 | [ピーブルス他（宇宙論・系外惑星）](https://hrtkhr3-lab.github.io/nobel-physics-timeline/laureates/40_2019_exoplanet.html) | 宇宙・天文 |
| 41 | 2020 | [ペンローズ他（ブラックホール）](https://hrtkhr3-lab.github.io/nobel-physics-timeline/laureates/41_2020_black_hole.html) | 宇宙・天文 |
| 42 | 2021 | [**真鍋淑郎**他（気候モデル・複雑系）](https://hrtkhr3-lab.github.io/nobel-physics-timeline/laureates/42_2021_manabe.html) | 宇宙・天文 |
| 43 | 2022 | [アスペ他（量子もつれ）](https://hrtkhr3-lab.github.io/nobel-physics-timeline/laureates/43_2022_entanglement.html) | 量子力学 |
| 44 | 2023 | [アゴスティーニ他（アト秒）](https://hrtkhr3-lab.github.io/nobel-physics-timeline/laureates/44_2023_attosecond.html) | 物性・応用 |
| 45 | 2024 | [ホップフィールド／ヒントン（機械学習の基礎）](https://hrtkhr3-lab.github.io/nobel-physics-timeline/laureates/45_2024_ml.html) | 物性・応用 |

太字は日本人（または日本出身）の受賞者。

**体験型シミュレーション搭載（25件）**: 01〜10, 12, 13, 23, 24, 26, 27, 31, 33, 35, 36, 38, 40, 42, 43, 45
（理論中心の残り20件は模式図のまま。発展セクションは全45件にあります）

---

## 図解と2段構えの方針

- 図解は2種類あります。
  - **体験型シミュレーション（25件）** … クレイマースの式・プランクの法則・コンプトンの式・
    ニュートリノ振動の生存確率・重力波のチャープ波形など、**物理式に基づく実単位の計算**です。
    スライダー2〜4本（管電圧 kV、温度 K、散乱角° など）を操作すると、応答が定量的にグラフへ反映されます。
    簡略化した点（近似・規格化など）は各図の注記に明記しています。
  - **模式図（20件・理論中心の回）** … 従来どおり「模式図＋軽い操作」。誇張は注記で断っています。
- **本文は2段構え**です。やさしい本文（背景→発見→意義、数式なし）は従来どおり残し、
  各ページ末尾の折りたたみ**「発展 ── もっと詳しく知りたい人へ（数式あり）」**に、
  大学初年級レベルの数式・導出の考え方・他の受賞とのつながりをまとめています。
- すべて軽量なSVG／Canvasと少量のJavaScriptで、外部ライブラリは使っていません（数式もHTML/CSSで組版）。

## 出典方針

- 事実（受賞年・受賞者・共同受賞者・受賞理由・研究内容）は、**ノーベル財団公式サイト（nobelprize.org）**の
  各年の受賞者ページと、一般向けの科学史資料に基づいています。
- 受賞理由は原文（英語 citation）の**平易な和訳・要約**です。逐語訳ではありません。
- 各ページ末尾に主な出典を簡潔に記しています（学術的な引用形式までは採用していません）。
- 分野の色分けや通し番号は、本ツール独自の整理です。

## 分野の色分け

放射線・原子＝橙／量子力学＝紫／素粒子・核＝青緑／宇宙・天文＝青／物性・応用＝緑

---

## 再生成のしかた（メンテナンス用）

本ページ群は `build/` のスクリプトで生成しています。編集する場所は内容によって変わります。

- やさしい本文・模式図 → `build/pages_data.py`
- 体験型シミュレーション → `build/sims_data.py`（`SIM[ファイル名] = (図解HTML, スクリプトJS)`）
- 「発展」セクション → `build/advanced_data.py`（`ADV[ファイル名] = HTML`）

編集後、次を実行すると `laureates/` が作り直されます。

```
python build/build_pages.py     # 個別ページ45件を生成（SIM/ADV を自動で合流）
python build/patch_index.py     # index.html のカードに個別ページのリンクを張り直す
```

- 共通デザイン（配色・レイアウト・数式や操作パネルのCSS）は `build/build_pages.py` の `TEMPLATE` を編集します。
- 前へ／次へのリンクは `build/build_pages.py` の `NAV`（年代順リスト）から自動生成されます。
  順番の変更は `NAV` の並べ替えだけで反映されます。
- スクリプトを使わず、個別HTMLを直接手で編集してもかまいません（各ファイルは自己完結です）。
