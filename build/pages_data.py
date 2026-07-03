# -*- coding: utf-8 -*-
"""各ページの中身(3ブロック+図解)。register(page) で build_pages.page() に流し込む。"""

def register(page):

    # ===== 04 マイケルソン 1907 =====
    page("04_1907_michelson.html", "matter", 1907,
      "光の波を重ねて長さを測る ── 干渉計",
      "アルバート・マイケルソン（アメリカ）",
      "精密な光学機器の開発と、それを用いた分光学・長さの基準づくりの研究に対して。",
      "光は波、でも波長はとても短い",
      r'''<p>光が<b>波</b>であることは分かっていましたが、その波の間隔（<span class="term" data-tip="波の山から次の山までの長さ。可視光では1mmの千分の一ほどしかありません。">波長</span>）は、髪の毛よりずっと細かい長さです。これを普通のものさしで測るのは不可能でした。</p>''',
      "2つに分けて、また重ねる",
      r'''<p>マイケルソンは、1本の光を鏡で2手に分け、別々の鏡ではね返してもう一度<b>重ね合わせる</b>装置（<span class="term" data-tip="光を2つの道に分けて反射させ、再び重ねて明暗の縞を作る精密測定器。マイケルソンが完成させました。">干渉計</span>）を作りました。2つの道のりの差（<span class="term" data-tip="分かれた2つの光が進む距離の差。これが波長の整数倍か半端かで、重ねた光の明暗が決まります。">光路差</span>）が波長の整数倍なら山と山が重なって<b>明るく</b>、半波長ずれると山と谷が打ち消して<b>暗く</b>なります。鏡をほんの少し動かすだけで明暗が入れかわるので、<b>光の波長そのものをものさし</b>にした超精密な測定ができたのです。</p>''',
      r'''    <h2>やってみよう ── 2つの波を重ねる</h2>
    <div class="hint">スライダーで片方の鏡を動かすと2つの波の「ずれ」が変わり、重ねた光（検出器）が明るくなったり暗くなったりします。</div>
    <div class="xbox">
      <svg id="mi" width="520" height="210" viewBox="0 0 520 210" role="img" aria-label="光の干渉">
        <path id="wA" fill="none" stroke="#ff9a8a" stroke-width="3"/>
        <path id="wB" fill="none" stroke="#8ab6ff" stroke-width="3"/>
        <text x="10" y="20" fill="#ff9a8a" font-size="12">波A（基準の光）</text>
        <text x="130" y="20" fill="#8ab6ff" font-size="12">波B（動く鏡からの光）</text>
        <circle id="lamp" cx="440" cy="150" r="26" fill="#ffd257"/>
        <circle cx="440" cy="150" r="26" fill="none" stroke="#3a4356" stroke-width="2"/>
        <text x="440" y="196" fill="#8b93a7" font-size="12" text-anchor="middle">検出器</text>
      </svg>
    </div>
    <div class="controls">
      <label for="ph">動く鏡の位置（光路差）</label>
      <input id="ph" type="range" min="0" max="100" value="0">
    </div>
    <div class="status yes" id="st">山と山が重なって明るい（強め合い）</div>
    <div class="note">※ 2つの波の山どうしが重なると明るく、山と谷が重なると打ち消して暗くなります。この明暗の周期が「光の波長ものさし」です。仕組みをつかむための模式図です。</div>''',
      r'''<p>この干渉の技術は、長さの世界基準を光の波長で定める道を開き、いまも精密計測の土台です。さらにマイケルソンは「光の速さは地球の動きによらず一定らしい」という有名な実験（マイケルソン・モーリーの実験）も行い、これがのちの<b>アインシュタインの相対性理論</b>につながりました。2017年に受賞した<b>重力波望遠鏡LIGO</b>も、じつは巨大な干渉計そのものです。</p>''',
      r'''var ph=document.getElementById('ph'), wA=document.getElementById('wA'),
    wB=document.getElementById('wB'), lamp=document.getElementById('lamp'), st=document.getElementById('st');
function sine(shift,yc){var d='M',i;for(i=0;i<=500;i+=4){var y=yc-30*Math.sin((i/40)+shift);d+=(i===0?'':'L')+(10+i)+','+y.toFixed(1)+' ';}return d;}
function render(){
  var t=+ph.value/100, shift=t*4*Math.PI;         // 鏡を動かす → 位相ずれ
  wA.setAttribute('d',sine(0,70)); wB.setAttribute('d',sine(shift,70));
  var b=Math.cos(shift/2)*Math.cos(shift/2);       // 明るさ 0..1
  lamp.setAttribute('fill','rgba(255,210,87,'+(0.12+0.88*b).toFixed(2)+')');
  if(b>0.7){st.className='status yes';st.textContent='山と山が重なって明るい（強め合い）';}
  else if(b<0.15){st.className='status no';st.textContent='山と谷が打ち消して暗い（弱め合い）';}
  else{st.className='status';st.style.background='#fff7e6';st.style.color='#8a5a00';st.textContent='中間の明るさ（少しずれている）';}
}
ph.addEventListener('input',render); render();''')

    # ===== 05 プランク 1918 =====
    page("05_1918_planck.html", "quantum", 1918,
      "エネルギーは飛び飛び ── 量子の発見",
      "マックス・プランク（ドイツ）",
      "エネルギー量子の発見によって物理学の進歩に大きく貢献したことに対して。",
      "熱い物体の色が説明できなかった",
      r'''<p>熱した鉄が赤→オレンジ→白と光る「<span class="term" data-tip="熱を持った物体が出す光。温度によって色（波長の分布）が変わります。">熱放射</span>」の色の分布を、当時の理論（エネルギーは連続的にいくらでも細かく分けられるという考え）で計算すると、短い波長側で値が無限大になり、実験とまるで合いませんでした。</p>''',
      "エネルギーを「かたまり」で数える",
      r'''<p>プランクは思いきって「光のエネルギーは、ある<b>最小のかたまり（<span class="term" data-tip="エネルギーのそれ以上分けられない最小単位。連続ではなく、この単位の整数倍しか取れないと考えます。">量子</span>）</b>の整数倍しか取れない」と仮定しました。なだらかな坂道ではなく、<b>階段のようにとびとび</b>。すると計算が実験にぴたりと合ったのです。このかたまりの大きさを決める数が<span class="term" data-tip="量子の世界の大きさを決める基本定数。とても小さな値で、これがゼロなら世界は連続的（古典的）に見えます。">プランク定数</span>で、量子の世界の“最小通貨”です。</p>''',
      r'''    <h2>やってみよう ── エネルギーの階段</h2>
    <div class="hint">スライダーでエネルギーを増やしても、ボールは「階段の段」にしか止まれません。点線（昔の考え＝なめらかな坂）と比べてみましょう。</div>
    <div class="xbox">
      <svg id="pl" width="440" height="250" viewBox="0 0 440 250" role="img" aria-label="エネルギーの量子化">
        <line x1="70" y1="220" x2="380" y2="60" stroke="#4b5563" stroke-width="2" stroke-dasharray="5 5"/>
        <text x="300" y="70" fill="#8b93a7" font-size="11">昔の考え＝連続の坂</text>
        <g id="rungs" stroke="#2a3446" stroke-width="2"></g>
        <circle id="ball" cx="150" cy="220" r="13" fill="#c4b5fd"/>
      </svg>
    </div>
    <div class="controls">
      <label for="en">与えるエネルギー</label>
      <input id="en" type="range" min="0" max="100" value="0">
      <div class="readout" id="msg">いまは <b>レベル 0</b></div>
    </div>
    <div class="note">※ エネルギーは「量子」という段の高さの整数倍しか取れません。段の間の高さには止まれない――これが量子化です。模式図です。</div>''',
      r'''<p>「とびとび（量子）」という発想は、光電効果（1921）・ボーアの原子模型（1922）・量子力学（1932）へと受けつがれ、20世紀物理学の出発点になりました。<b>半導体・レーザー・LED</b>など、いまの電子技術はすべて、この量子の考えの上に成り立っています。</p>''',
      r'''var en=document.getElementById('en'), ball=document.getElementById('ball'),
    rungs=document.getElementById('rungs'), msg=document.getElementById('msg');
var N=5, x0=110, x1=250, base=220, step=32;
for(var k=0;k<=N;k++){var y=base-k*step;
  var ln=document.createElementNS('http://www.w3.org/2000/svg','line');
  ln.setAttribute('x1',x0);ln.setAttribute('y1',y);ln.setAttribute('x2',x1);ln.setAttribute('y2',y);
  rungs.appendChild(ln);
  var t=document.createElementNS('http://www.w3.org/2000/svg','text');
  t.setAttribute('x',x1+8);t.setAttribute('y',y+4);t.setAttribute('fill','#8b93a7');t.setAttribute('font-size','11');
  t.textContent='レベル '+k; rungs.appendChild(t);}
function render(){var lvl=Math.round(+en.value/100*N);
  ball.setAttribute('cy',base-lvl*step); ball.setAttribute('cx',(x0+x1)/2);
  msg.innerHTML='いまは <b>レベル '+lvl+'</b>（この段の高さだけ）';}
en.addEventListener('input',render); render();''')

    # ===== 07 ボーア 1922 =====
    page("07_1922_bohr.html", "quantum", 1922,
      "電子は決まった軌道にいる ── 原子模型",
      "ニールス・ボーア（デンマーク）",
      "原子の構造と、原子から出る光（放射）についての研究に対して。",
      "なぜ原子はつぶれないのか",
      r'''<p>電子が原子核のまわりを回っているなら、電磁気の法則では光を出してだんだん失速し、すぐ核に落ちて原子はつぶれてしまうはずでした。ところが原子は安定で、しかも元素ごとに<b>決まった色の光</b>（<span class="term" data-tip="原子が出す光を色（波長）ごとに分けると、とびとびの決まった線として現れるもの。元素ごとに違う“指紋”です。">線スペクトル</span>）しか出さない、という謎がありました。</p>''',
      "軌道はとびとび、移るときに光を出す",
      r'''<p>ボーアは「電子は<b>とびとびの決まった軌道</b>（<span class="term" data-tip="電子が取れるとびとびのエネルギーの段。内側ほど低く、外側ほど高いエネルギーです。">エネルギー準位</span>）にだけいられて、そこでは光を出さない」と考えました。電子が外側の軌道から内側へ飛び移るとき、その差のぶんを<span class="term" data-tip="光のエネルギーの最小のつぶ。差が大きいほど紫っぽく、小さいほど赤っぽい光になります。">光子</span>1粒として放ちます。差が大きいほど青〜紫、小さいほど赤い光。元素ごとの線スペクトルがこうして説明できました。</p>''',
      r'''    <h2>やってみよう ── 電子を飛び移らせる</h2>
    <div class="hint">ボタンで電子の軌道を選びます。外側から内側へ移ると、その差のぶんだけ色のついた光が飛び出します。</div>
    <div class="xbox">
      <svg id="atom" width="360" height="240" viewBox="0 0 360 240" role="img" aria-label="ボーアの原子模型">
        <circle cx="140" cy="120" r="38" fill="none" stroke="#3a4356"/>
        <circle cx="140" cy="120" r="68" fill="none" stroke="#3a4356"/>
        <circle cx="140" cy="120" r="98" fill="none" stroke="#3a4356"/>
        <circle cx="140" cy="120" r="10" fill="#ff8a8a"/>
        <text x="140" y="228" fill="#8b93a7" font-size="11" text-anchor="middle">原子核</text>
        <circle id="elec" cx="140" cy="52" r="8" fill="#c4b5fd"/>
        <circle id="photon" cx="0" cy="0" r="7" opacity="0"/>
      </svg>
    </div>
    <div class="btns">
      <button data-n="1">内側 n=1</button>
      <button data-n="2">n=2</button>
      <button data-n="3">外側 n=3</button>
    </div>
    <div class="readout" id="msg">電子はいま <b>n=3</b> にいます</div>
    <div class="note">※ 外側→内側で光を出し（放出）、内側→外側は光を吸って移ります（吸収）。落差が大きいほど紫、小さいほど赤い光。模式図です。</div>''',
      r'''<p>この「エネルギー準位」の考えは、<b>蛍光灯・LED・レーザー・ネオンサイン</b>の発光や、星や銀河の成分を光の色で見分ける方法（分光）まで、光と物質のかかわりすべての基礎になりました。のちに量子力学によって、より正確な姿へと磨かれていきます。</p>''',
      r'''var elec=document.getElementById('elec'), photon=document.getElementById('photon'), msg=document.getElementById('msg');
var btns=document.querySelectorAll('.btns button');
var R={1:38,2:68,3:98}, cx=140, cy=120, cur=3;
function hueFor(gap){return Math.max(0,Math.min(285,(gap-0.1)/0.8*285));}
function setElec(n){elec.setAttribute('cy',cy-R[n]);}
var anim=null;
function go(n){
  btns.forEach(function(b){b.classList.toggle('on',+b.dataset.n===n);});
  if(n<cur){ // 放出
    var gap=(1/(n*n))-(1/(cur*cur)); var col='hsl('+hueFor(gap)+',85%,62%)';
    msg.innerHTML='<b>n='+cur+' → n='+n+'</b>：光を放出！（'+(gap>0.5?'青〜紫':'赤っぽい')+'光）';
    if(anim)cancelAnimationFrame(anim); var px=cx, t0=null;
    photon.setAttribute('fill',col); photon.setAttribute('cy',cy); photon.setAttribute('opacity','1');
    function step(){px+=5; photon.setAttribute('cx',px);
      photon.setAttribute('opacity',Math.max(0,1-(px-cx)/220).toFixed(2));
      if(px<cx+220)anim=requestAnimationFrame(step); }
    photon.setAttribute('cx',cx); step();
  }else if(n>cur){ msg.innerHTML='<b>n='+cur+' → n='+n+'</b>：光を吸って外側へ（吸収）'; photon.setAttribute('opacity','0');
  }else{ msg.innerHTML='電子はいま <b>n='+n+'</b> にいます'; }
  cur=n; setElec(n);
}
btns.forEach(function(b){b.addEventListener('click',function(){go(+b.dataset.n);});});
setElec(3);''')

    # ===== 08 ミリカン 1923 =====
    page("08_1923_millikan.html", "radiation", 1923,
      "電気の最小単位を測る ── 油滴の実験",
      "ロバート・ミリカン（アメリカ）",
      "電気素量（電気のいちばん小さな単位）の測定と、光電効果に関する研究に対して。",
      "電気に「最小のかたまり」はある？",
      r'''<p>電子が見つかっても、電気の量そのものに「これ以上分けられない最小単位」があるのかは、まだ確かめられていませんでした。もし最小単位があるなら、どんな電気の量もその<b>整数倍</b>になるはずです。</p>''',
      "宙に浮かぶ油の粒で数える",
      r'''<p>ミリカンは霧吹きでつくった小さな<span class="term" data-tip="霧吹きで作った油の微粒子。とても軽いので、電気の力とのつり合いを精密に観察できます。">油滴（ゆてき）</span>を、電気の力で空中にぴたりと静止（<span class="term" data-tip="下向きの重力と、上向きの電気の力がちょうど等しくなり、粒が浮いたまま止まる状態。">つり合い</span>）させ、必要な電圧から粒の電気量を計算しました。すると電気量はいつも決まった値 <b>e の整数倍</b>（1倍・2倍・3倍…）ばかりで、半端な値は出ません。電気は <span class="term" data-tip="電気のいちばん小さな単位。電子1個が持つ電気の量にあたります。記号は e。">e というかたまり</span>で数えられる、と確定したのです。</p>''',
      r'''    <h2>やってみよう ── 油滴をつり合わせる</h2>
    <div class="hint">粒にのった電子の数をボタンで選びます。つり合わせるのに必要な電圧が変わりますが、電気量はいつも e の整数倍です。</div>
    <div class="xbox">
      <svg id="oil" width="420" height="230" viewBox="0 0 420 230" role="img" aria-label="ミリカンの油滴実験">
        <rect x="60" y="30" width="220" height="9" rx="3" fill="#ff8a8a"/><text x="288" y="40" fill="#ff8a8a" font-size="13">＋</text>
        <rect x="60" y="191" width="220" height="9" rx="3" fill="#8ab6ff"/><text x="288" y="202" fill="#8ab6ff" font-size="13">−</text>
        <circle id="drop" cx="170" cy="115" r="16" fill="#ffd257"/>
        <text id="dlab" x="170" y="120" fill="#5b3b00" font-size="11" text-anchor="middle" font-weight="bold">−</text>
        <text x="360" y="60" fill="#8b93a7" font-size="12">電圧</text>
        <rect x="345" y="70" width="20" height="120" rx="4" fill="#26343f"/>
        <rect id="gauge" x="345" y="70" width="20" height="0" rx="4" fill="#7ee787"/>
      </svg>
    </div>
    <div class="btns">
      <button data-n="1">電子1個</button>
      <button data-n="2">2個</button>
      <button data-n="3">3個</button>
      <button data-n="4">4個</button>
    </div>
    <div class="readout" id="msg">ボタンを選んでください</div>
    <div class="note">※ 電子が多い粒ほど、軽い電圧でつり合います。でもどの粒も電気量は必ず e の整数倍――半端はありません。模式図です（電圧の値は相対値）。</div>''',
      r'''<p>こうして測られた<b>電気素量 e</b> は、自然界の基本の数のひとつになりました。電池や回路を流れる電流（＝電子の流れ）から、素粒子1個ずつの電気の測定まで、あらゆる電気の量はこの e を単位にはかられています。</p>''',
      r'''var drop=document.getElementById('drop'), dlab=document.getElementById('dlab'),
    gauge=document.getElementById('gauge'), msg=document.getElementById('msg');
var btns=document.querySelectorAll('.btns button');
function pick(n){
  btns.forEach(function(b){b.classList.toggle('on',+b.dataset.n===n);});
  var V=(12/n);                       // つり合い電圧 ∝ 1/n
  var h=V/12*120;
  gauge.setAttribute('height',h); gauge.setAttribute('y',190-h);
  drop.setAttribute('cy',115); drop.setAttribute('fill','#7ee787');
  dlab.textContent = Array(n+1).join('−');
  dlab.setAttribute('x',170);
  msg.innerHTML='電子 <b>'+n+'</b> 個 → つり合う電圧 <b>'+V.toFixed(1)+'</b>（電気量 = e × '+n+'）';
}
btns.forEach(function(b){b.addEventListener('click',function(){pick(+b.dataset.n);});});''')

    # ===== 09 コンプトン 1927 =====
    page("09_1927_compton.html", "quantum", 1927,
      "光がボールのようにぶつかる ── コンプトン効果",
      "アーサー・コンプトン（アメリカ）",
      "X線が電子にぶつかって進む向きと波長を変える現象（コンプトン効果）の発見に対して。",
      "光は本当に「粒」なのか",
      r'''<p>アインシュタインが「光は粒（光子）でもある」と唱えたあとも、それを目に見える形で確かめる実験が求められていました。もし光が粒なら、電子と<b>ボールどうしのようにぶつかる</b>はずです。</p>''',
      "ぶつかると波長がのびる",
      r'''<p>コンプトンはX線を電子に当て、はね返ったX線を調べました。すると、はね返ったX線は<b>波長が少しのびて（エネルギーが減って）</b>いました。ちょうど、動いていた玉が止まっている玉に当たると勢いを分け与えて遅くなるのと同じ。光の粒が電子に<span class="term" data-tip="動いている物の“勢い”の量。ぶつかったときに相手へ渡せます。光の粒もこれを持っています。">運動量（勢い）</span>を渡した証拠で、これで<b>光が粒である</b>ことがはっきり示されました。</p>''',
      r'''    <h2>やってみよう ── X線と電子の玉つき</h2>
    <div class="hint">スライダーで散乱の角度を変えます。大きく曲がるほど、はね返った光は波長がのびて赤っぽくなります。</div>
    <div class="xbox">
      <svg id="cp" width="480" height="230" viewBox="0 0 480 230" role="img" aria-label="コンプトン散乱">
        <line x1="20" y1="120" x2="230" y2="120" stroke="#c4b5fd" stroke-width="5" stroke-linecap="round"/>
        <text x="30" y="108" fill="#c4b5fd" font-size="12">入ってくるX線</text>
        <circle id="etarget" cx="230" cy="120" r="9" fill="#7ee787"/>
        <text x="230" y="150" fill="#8b93a7" font-size="11" text-anchor="middle">電子</text>
        <line id="outp" x1="230" y1="120" x2="230" y2="120" stroke="#ff9a8a" stroke-width="5" stroke-linecap="round"/>
        <line id="oute" x1="230" y1="120" x2="230" y2="120" stroke="#7ee787" stroke-width="3" stroke-linecap="round" stroke-dasharray="4 4"/>
      </svg>
    </div>
    <div class="controls">
      <label for="ang">散乱の角度</label>
      <input id="ang" type="range" min="10" max="80" value="35">
      <div class="readout" id="msg"></div>
    </div>
    <div class="note">※ 光が電子に勢い（運動量）を渡すぶん、はね返った光はエネルギーが減って波長がのびます。玉つきと同じ考え方でよい、という模式図です。</div>''',
      r'''<p>コンプトン効果は「光は波でもあり粒でもある」という量子の考えを決定づけました。この現象は、<b>レントゲンやCTの画像の見え方</b>、<b>放射線の物質への影響</b>、宇宙から届く高エネルギーの光（ガンマ線）の観測などで、いまも欠かせない基礎になっています。</p>''',
      r'''var ang=document.getElementById('ang'), outp=document.getElementById('outp'),
    oute=document.getElementById('oute'), msg=document.getElementById('msg');
var ex=230, ey=120, L=180;
function render(){
  var th=+ang.value*Math.PI/180;
  outp.setAttribute('x2',ex+L*Math.cos(th)); outp.setAttribute('y2',ey-L*Math.sin(th));
  var pe=th*0.45; oute.setAttribute('x2',ex+120*Math.cos(pe)); oute.setAttribute('y2',ey+120*Math.sin(pe));
  var f=(+ang.value-10)/70;                    // 0..1 曲がるほど赤へ
  var hue=270-f*250;                            // violet -> red
  outp.setAttribute('stroke','hsl('+hue+',85%,65%)');
  msg.innerHTML='散乱角 <b>'+ang.value+'°</b>：はね返った光は波長が'+(f<0.4?'少し':'大きく')+'のびて赤っぽく（電子に勢いを渡した）';
}
ang.addEventListener('input',render); render();''')

    # ===== 10 ド・ブロイ 1929 =====
    page("10_1929_de_broglie.html", "quantum", 1929,
      "電子も波のようにふるまう ── 物質波",
      "ルイ・ド・ブロイ（フランス）",
      "電子など「物」にも波の性質があること（物質波）の発見に対して。",
      "光が波でも粒でもあるなら…",
      r'''<p>光は「波でも粒でもある」と分かってきました。ド・ブロイは逆に、「では電子のような<b>物（粒）にも、波の性質があるのでは</b>？」と考えました。しかもその波の間隔（波長）は、<b>速く動くほど短くなる</b>と予想しました。</p>''',
      "波が「ちょうど整数個」で軌道が決まる",
      r'''<p>この<span class="term" data-tip="電子などの粒が持つ波。速く動くほど波長が短くなります。のちに電子線の実験で本当に波として観測されました。">物質波</span>の考えは、ボーアの謎を解きました。原子の中で電子の波が<b>軌道をちょうど整数個の波でひとまわりする</b>ときだけ、波が自分自身とうまくつながって安定する（<span class="term" data-tip="行って戻ってきた波がぴったり重なり、消えずに保たれる波。弦楽器の音もこれです。">定常波</span>）。だから軌道が「とびとび」に決まるのです。電子の波は、のちに電子線の実験で本当に観測されました。</p>''',
      r'''    <h2>やってみよう ── 波が軌道につながるか</h2>
    <div class="hint">スライダーで電子の波の数を変えます。ちょうど整数個そろうと波がつながって「安定な軌道」になります。</div>
    <div class="xbox">
      <svg id="db" width="360" height="260" viewBox="0 0 360 260" role="img" aria-label="物質波と定常波">
        <circle cx="180" cy="130" r="80" fill="none" stroke="#2a3446" stroke-width="1" stroke-dasharray="3 4"/>
        <path id="wave" fill="none" stroke="#c4b5fd" stroke-width="3"/>
      </svg>
    </div>
    <div class="controls">
      <label for="k">電子の波の数（速さで変わる）</label>
      <input id="k" type="range" min="300" max="800" value="500">
      <div class="status yes" id="st"></div>
    </div>
    <div class="note">※ 波が整数個そろうと自分自身とつながり、消えずに残ります（定常波）。だから原子の軌道はとびとびに決まります。模式図です。</div>''',
      r'''<p>「物にも波がある」というド・ブロイの考えは、シュレディンガーの<b>波動方程式</b>（1933）へと発展し、量子力学の柱になりました。電子の波を利用した<b>電子顕微鏡</b>は、光では見えないウイルスや原子の並びまで映し出し、いまも科学と産業を支えています。</p>''',
      r'''var k=document.getElementById('k'), wave=document.getElementById('wave'), st=document.getElementById('st');
var cx=180, cy=130, R=80;
function render(){
  var kk=+k.value/100;                          // 3.00 .. 8.00
  var d='', i;
  for(i=0;i<=360;i+=2){var a=i*Math.PI/180;
    var rr=R+12*Math.sin(kk*a);
    var x=cx+rr*Math.cos(a-Math.PI/2), y=cy+rr*Math.sin(a-Math.PI/2);
    d+=(i===0?'M':'L')+x.toFixed(1)+','+y.toFixed(1)+' ';}
  wave.setAttribute('d',d);
  var frac=Math.abs(kk-Math.round(kk));
  if(frac<0.06){wave.setAttribute('stroke','#7ee787');st.className='status yes';
    st.textContent='波がぴったり '+Math.round(kk)+' 個つながった！ 安定な軌道';}
  else{wave.setAttribute('stroke','#ff9a8a');st.className='status no';
    st.textContent='端がずれて波がつながらない（この速さは不安定）';}
}
k.addEventListener('input',render); render();''')

    # ===== 11 ハイゼンベルク 1932 =====
    page("11_1932_heisenberg.html", "quantum", 1932,
      "位置と速さは同時に決められない ── 不確定性原理",
      "ヴェルナー・ハイゼンベルク（ドイツ）",
      "量子力学をつくり上げたこと（その応用が水素などの発見にもつながった）に対して。",
      "小さな世界のあいまいさ",
      r'''<p>ハイゼンベルクは、日常の物理とはまるで違う、原子の世界のための新しい理論「<b>量子力学</b>」をつくりました。そこから驚くべき性質が導かれます。粒の<b>位置</b>と<b>速さ（勢い）</b>を、<b>両方同時にきっちり決めることはできない</b>のです。</p>''',
      "片方をはっきりさせると、もう片方がぼやける",
      r'''<p>これが<span class="term" data-tip="位置をはっきりさせるほど速さがぼやけ、逆もまた同じ。量子の世界に必ずある“あいまいさ”で、測り方が下手なせいではありません。">不確定性原理</span>です。「どこにいるか」をはっきり突きとめようとするほど、「どんな速さか」はぼやけて広がってしまう。これは道具が悪いのではなく、<b>自然そのものが持つあいまいさ</b>。小さな世界では、物はキッチリした点ではなく、少しぼんやりした存在なのです。</p>''',
      r'''    <h2>やってみよう ── 位置と速さのシーソー</h2>
    <div class="hint">スライダーで「位置のはっきり度」を上げる（青い幅を狭める）と、そのぶん「速さのぼやけ」（赤い幅）が広がります。</div>
    <div class="xbox">
      <svg id="hb" width="460" height="200" viewBox="0 0 460 200" role="img" aria-label="不確定性">
        <text x="30" y="55" fill="#8ab6ff" font-size="13">位置のぼやけ Δx</text>
        <rect x="30" y="65" width="200" height="20" rx="6" fill="#26343f"/>
        <rect id="bx" x="30" y="65" width="120" height="20" rx="6" fill="#8ab6ff"/>
        <text x="30" y="130" fill="#ff9a8a" font-size="13">速さのぼやけ Δp</text>
        <rect x="30" y="140" width="400" height="20" rx="6" fill="#26343f"/>
        <rect id="bp" x="30" y="140" width="120" height="20" rx="6" fill="#ff9a8a"/>
      </svg>
    </div>
    <div class="controls">
      <label for="dx">位置をどれだけはっきりさせるか</label>
      <input id="dx" type="range" min="20" max="190" value="120">
      <div class="readout" id="msg"></div>
    </div>
    <div class="note">※ 位置の幅と速さの幅は「かけ算するとほぼ一定」。片方を狭めると必ずもう片方が広がります。量子の世界のきまりを表す模式図です。</div>''',
      r'''<p>不確定性原理は、量子の世界が確率で語られることを示し、現代物理の常識になりました。この「あいまいさ」は欠点ではなく、<b>トンネル効果</b>（半導体やSTM、2011年以降の量子技術）や<b>量子コンピュータ</b>など、新しい技術の源にもなっています。</p>''',
      r'''var dx=document.getElementById('dx'), bx=document.getElementById('bx'), bp=document.getElementById('bp'), msg=document.getElementById('msg');
function render(){
  var w=+dx.value; bx.setAttribute('width',w);
  var wp=Math.min(400, 14000/w); bp.setAttribute('width',wp.toFixed(0));
  msg.innerHTML='位置の幅 <b>'+(w<70?'せまい（はっきり）':'広い（あいまい）')+'</b> → 速さの幅 <b>'+(wp>200?'広い（ぼやける）':'せまい')+'</b>';
}
dx.addEventListener('input',render); render();''')

    # ===== 12 シュレディンガー／ディラック 1933 =====
    page("12_1933_schrodinger_dirac.html", "quantum", 1933,
      "波の式と反物質の予言 ── 量子力学の完成へ",
      "エルヴィン・シュレディンガー（オーストリア） ／ ポール・ディラック（イギリス）",
      "原子の理論を新しい形（波動力学）にまとめ上げたことに対して。",
      "電子を「波の式」で表す",
      r'''<p>シュレディンガーは、電子のふるまいを1本の<b>波の式（波動方程式）</b>で表す方法を作りました。電子はきっちりした点ではなく、「ここらへんにいそう」という<span class="term" data-tip="電子がどこにいそうかを表す“もや”。濃いところほど見つかりやすい。点ではなく広がった存在としてあつかいます。">確率の雲</span>として広がっています。この式で原子の姿がきれいに計算できました。</p>''',
      "ディラックの式から現れた「反物質」",
      r'''<p>ディラックは、量子力学と相対性理論を1本の式にまとめました。するとその式は、電子と同じ重さで<b>電気の符号だけ逆の粒</b>（<span class="term" data-tip="ふつうの粒と重さが同じで電気の＋−が逆の粒。電子の反粒子が陽電子。出会うと光になって消えます。">反粒子</span>）の存在を予言したのです。数年後、本当に<b>陽電子（プラスの電子）</b>が見つかりました。エネルギーがあれば、粒と反粒子が<b>ペアで生まれる</b>こともあります。</p>''',
      r'''    <h2>やってみよう ── エネルギーから粒のペアが生まれる</h2>
    <div class="hint">ボタンでエネルギー（光）を注ぐと、電子（−）と反電子＝陽電子（＋）がペアで生まれて飛び出します。</div>
    <div class="xbox">
      <svg id="pair" width="460" height="220" viewBox="0 0 460 220" role="img" aria-label="対生成">
        <line id="gam" x1="20" y1="110" x2="230" y2="110" stroke="#ffe066" stroke-width="5" stroke-linecap="round" opacity="0"/>
        <circle id="pe" cx="230" cy="110" r="13" fill="#8ab6ff" opacity="0"/>
        <text id="pel" x="230" y="115" fill="#04203f" font-size="13" text-anchor="middle" font-weight="bold" opacity="0">−</text>
        <circle id="po" cx="230" cy="110" r="13" fill="#ff9a8a" opacity="0"/>
        <text id="pol" x="230" y="115" fill="#3f0404" font-size="13" text-anchor="middle" font-weight="bold" opacity="0">＋</text>
      </svg>
    </div>
    <div class="btns"><button id="go">エネルギーを注ぐ</button></div>
    <div class="readout" id="msg">ボタンを押してみましょう</div>
    <div class="note">※ E=mc²。じゅうぶんなエネルギーがあると、質量を持つ粒と反粒子がペアで生まれます。逆に出会うと光になって消えます。模式図です。</div>''',
      r'''<p>シュレディンガーの波の式は、いまも化学・材料・電子工学のあらゆる計算の土台です。ディラックが予言した<b>反物質</b>は、医療の<b>PET検査</b>（陽電子を使う体内の画像診断）に実際に使われています。宇宙になぜ物質だけが残ったのか、という大きな謎（2008年の項）にもつながります。</p>''',
      r'''var go=document.getElementById('go'), gam=document.getElementById('gam'), msg=document.getElementById('msg');
var pe=document.getElementById('pe'), pel=document.getElementById('pel'),
    po=document.getElementById('po'), pol=document.getElementById('pol');
var anim=null;
function reset(){['pe','pel','po','pol'].forEach(function(id){document.getElementById(id).setAttribute('opacity','0');});
  gam.setAttribute('opacity','0');pe.setAttribute('cx',230);po.setAttribute('cx',230);pel.setAttribute('x',230);pol.setAttribute('x',230);}
function fire(){ if(anim)cancelAnimationFrame(anim); reset();
  gam.setAttribute('opacity','1'); msg.innerHTML='エネルギー（光）を注入中…';
  var phase=0, t=0;
  function step(){ t++;
    if(t<25){ var gx=20+t*8; gam.setAttribute('x2',Math.min(230,gx)); anim=requestAnimationFrame(step); return; }
    gam.setAttribute('opacity','0');
    ['pe','pel','po','pol'].forEach(function(id){document.getElementById(id).setAttribute('opacity','1');});
    var s=t-25, off=s*3.2, y=110-s*1.2;
    pe.setAttribute('cx',230-off); pe.setAttribute('cy',y); pel.setAttribute('x',230-off); pel.setAttribute('y',y+5);
    po.setAttribute('cx',230+off); po.setAttribute('cy',y); pol.setAttribute('x',230+off); pol.setAttribute('y',y+5);
    msg.innerHTML='<b>電子（−）</b>と<b>陽電子（＋）</b>がペアで誕生！（E=mc²）';
    if(s<45)anim=requestAnimationFrame(step);
  }
  step();
}
go.addEventListener('click',fire);''')

    # ===== 13 チャドウィック 1935 =====
    page("13_1935_chadwick.html", "particle", 1935,
      "電気を持たない粒 ── 中性子の発見",
      "ジェームズ・チャドウィック（イギリス）",
      "中性子（電気を帯びていない、原子核の中の重い粒）の発見に対して。",
      "原子核の重さが合わない",
      r'''<p>原子核はプラスの電気を持つ<b>陽子</b>でできていると考えられていましたが、それだけでは核の<b>重さが足りません</b>。プラスの数（電気）は合うのに重さが2倍近い――核の中には、電気を持たない“見えない重り”が隠れているようでした。</p>''',
      "曲がらないから見つけにくかった",
      r'''<p>チャドウィックは、ある放射線が<b>電気の力でも磁石でも曲がらない</b>のに、重い原子核をはじき飛ばすほどの勢いを持つことを突きとめました。電気を持たない（中性の）重い粒――<span class="term" data-tip="原子核の中にある、電気を帯びていない粒。陽子とほぼ同じ重さ。電気で曲がらないので見つけるのが難しかった。">中性子</span>です。電気がないので電場を素通りしますが、質量はしっかりある。これで原子核の重さの謎が解けました。</p>''',
      r'''    <h2>やってみよう ── 電気の力で曲がる？曲がらない？</h2>
    <div class="hint">3種類の粒をボタンで発射します。電気を持つ粒は曲がり、中性子だけはまっすぐ進みます。</div>
    <div class="xbox">
      <svg id="ch" width="500" height="220" viewBox="0 0 500 220" role="img" aria-label="荷電粒子と中性子">
        <rect x="150" y="34" width="200" height="9" rx="3" fill="#ff8a8a"/><text x="356" y="44" fill="#ff8a8a" font-size="13">＋</text>
        <rect x="150" y="177" width="200" height="9" rx="3" fill="#8ab6ff"/><text x="356" y="187" fill="#8ab6ff" font-size="13">−</text>
        <path id="track" d="" fill="none" stroke="#7ee787" stroke-width="3" stroke-dasharray="5 5" opacity="0.5"/>
        <circle id="pt" cx="30" cy="110" r="10" fill="#7ee787"/>
        <text id="ptl" x="30" y="114" font-size="11" text-anchor="middle" font-weight="bold"></text>
      </svg>
    </div>
    <div class="btns">
      <button data-k="p">陽子（＋）</button>
      <button data-k="e">電子（−）</button>
      <button data-k="n">中性子（0）</button>
    </div>
    <div class="readout" id="msg">粒を選んでください</div>
    <div class="note">※ 中性子は電気を持たないので、電場を素通りしてまっすぐ進みます。だから発見が遅れました。模式図です。</div>''',
      r'''<p>中性子の発見で、原子核の姿（陽子＋中性子）がはっきりしました。電気で反発されない中性子は原子核に入りこみやすく、<b>核分裂</b>の発見（フェルミ、1938年の項）、そして<b>原子力</b>や<b>医療用の放射線</b>へとつながりました。中性子をぶつけて物質の中を調べる「中性子線」は、いまも材料研究の重要な道具です。</p>''',
      r'''var track=document.getElementById('track'), pt=document.getElementById('pt'), ptl=document.getElementById('ptl'), msg=document.getElementById('msg');
var btns=document.querySelectorAll('.btns button');
var col={p:'#ff9a8a',e:'#8ab6ff',n:'#7ee787'}, lab={p:'p',e:'e',n:'n'};
var dir={p:1,e:-1,n:0};                          // ＋は下(−極)へ、−は上(＋極)へ、中性子はまっすぐ
var name={p:'陽子（＋）：−極のほうへ曲がった',e:'電子（−）：＋極のほうへ曲がった',n:'中性子（0）：曲がらずまっすぐ！'};
var anim=null;
function yAt(x,d){var f=Math.max(0,Math.min(1,(x-150)/200)); return 110+d*70*f*f;}
function fire(k){
  btns.forEach(function(b){b.classList.toggle('on',b.dataset.k===k);});
  pt.setAttribute('fill',col[k]); ptl.textContent=lab[k]; ptl.setAttribute('fill','#04203f');
  if(anim)cancelAnimationFrame(anim);
  var d=dir[k], path='M30,110', xx;
  for(xx=150;xx<=490;xx+=10){ path+=' L'+xx+','+yAt(xx,d).toFixed(1); }
  track.setAttribute('d',path);
  var x=30;
  function step(){ x+=5; var y=yAt(x,d);
    pt.setAttribute('cx',x); pt.setAttribute('cy',y); ptl.setAttribute('x',x); ptl.setAttribute('y',y+4);
    if(x<490)anim=requestAnimationFrame(step); else msg.innerHTML='<b>'+name[k]+'</b>'; }
  msg.innerHTML='発射…'; step();
}
btns.forEach(function(b){b.addEventListener('click',function(){fire(b.dataset.k);});});''')

    # ===== 14 フェルミ 1938 =====
    page("14_1938_fermi.html", "particle", 1938,
      "遅い中性子で新しい元素をつくる ── 核反応への道",
      "エンリコ・フェルミ（イタリア）",
      "中性子を当ててつくり出した新しい放射性元素の発見と、遅い中性子による核反応の発見に対して。",
      "電気を持たない中性子は核に近づける",
      r'''<p>中性子（1935年の項）は電気を持たないので、プラスの原子核に反発されず<b>すっと核に近づけます</b>。フェルミは、いろいろな元素に中性子を当てて、それまでにない<b>新しい放射性元素</b>を次々と作り出しました。</p>''',
      "「遅い」中性子ほどよく吸われる",
      r'''<p>さらにフェルミは意外な発見をします。中性子を水やパラフィンでわざと<b>遅くする</b>と、かえって原子核に<b>吸いこまれやすくなる</b>のです（<span class="term" data-tip="中性子が原子核に吸収されて、別の（多くは放射性の）原子核に変わること。ゆっくりした中性子ほど起きやすい。">中性子捕獲</span>）。速い球はすり抜けてしまうが、ゆっくりな球は核に捕まる――このふしぎな性質が、のちの<span class="term" data-tip="重い原子核が中性子を吸って2つに割れ、大きなエネルギーと新たな中性子を出す反応。">核分裂</span>の利用へつながりました。</p>''',
      r'''    <h2>やってみよう ── 速い中性子と遅い中性子</h2>
    <div class="hint">スライダーで中性子の速さを決めて発射します。遅いほど原子核に吸いこまれ、新しい元素に変わります。</div>
    <div class="xbox">
      <svg id="fm" width="480" height="200" viewBox="0 0 480 200" role="img" aria-label="中性子捕獲">
        <circle id="nuc" cx="360" cy="100" r="26" fill="#5c9dff"/>
        <text x="360" y="150" fill="#8b93a7" font-size="11" text-anchor="middle">原子核</text>
        <circle id="neu" cx="30" cy="100" r="9" fill="#7ee787"/>
        <text x="30" y="82" fill="#7ee787" font-size="11" text-anchor="middle">中性子</text>
      </svg>
    </div>
    <div class="controls">
      <label for="sp">中性子の速さ</label>
      <input id="sp" type="range" min="0" max="100" value="20">
      <div class="btns"><button id="shoot">中性子を撃つ</button></div>
      <div class="readout" id="msg">速さを決めて撃ってみましょう</div>
    </div>
    <div class="note">※ 直感に反して、遅い中性子のほうが核に吸われやすいのです。速いと素通りします。模式図です。</div>''',
      r'''<p>フェルミの研究は<b>核分裂</b>の発見に直結し、原子力発電や医療用の放射性物質づくり（がん診断・治療）につながりました。フェルミは世界初の原子炉も動かしています。中性子の科学は、いまも<b>材料の内部を調べる中性子線</b>など幅広く使われています。</p>''',
      r'''var sp=document.getElementById('sp'), shoot=document.getElementById('shoot'),
    neu=document.getElementById('neu'), nuc=document.getElementById('nuc'), msg=document.getElementById('msg');
var anim=null;
function fire(){ if(anim)cancelAnimationFrame(anim);
  var slow=+sp.value<50, v=1.5+ (+sp.value)/100*6, x=30;
  neu.setAttribute('cx',30); nuc.setAttribute('fill','#5c9dff'); nuc.setAttribute('r',26);
  msg.innerHTML=(slow?'遅い':'速い')+'中性子を発射…';
  function step(){ x+=v; neu.setAttribute('cx',x);
    if(x>=334){
      if(slow){ neu.setAttribute('cx',360); nuc.setAttribute('fill','#ffb454'); nuc.setAttribute('r',30);
        msg.innerHTML='<b>吸いこまれた！</b> 核が中性子を捕まえ、新しい元素に変わった'; }
      else if(x>480){ msg.innerHTML='<b>素通り</b>：速すぎて核に捕まらなかった'; return; }
      else { anim=requestAnimationFrame(step); return; }
      return;
    }
    anim=requestAnimationFrame(step);
  }
  step();
}
shoot.addEventListener('click',fire);''')

    # ===== 15 パウリ 1945 =====
    page("15_1945_pauli.html", "quantum", 1945,
      "電子は同じ席に座れない ── 排他原理",
      "ヴォルフガング・パウリ（オーストリア）",
      "排他原理（パウリの原理）と呼ばれる、電子の並び方のきまりの発見に対して。",
      "なぜ元素はいろいろな性質を持つのか",
      r'''<p>原子の中の電子が、みんないちばん低いエネルギーに集まってしまうなら、すべての原子は似たようなものになるはずです。でも実際は、水素・炭素・鉄…と、元素ごとにまるで性質が違います。なぜでしょう。</p>''',
      "1つの席には1個だけ",
      r'''<p>パウリは「電子は<b>まったく同じ状態（席）に2個以上入れない</b>」というきまりを見つけました（<span class="term" data-tip="同じ状態には電子は1個しか入れないというきまり。原子の電子配置や、物質の硬さの理由になっています。">排他原理</span>）。だから電子は下の席から順に<b>一つずつ埋めて</b>いき、下が満席になると上の席へ。この「席の埋まり方」の違いが、元素ごとの個性（周期表）を生みます。電子の<span class="term" data-tip="電子が持つ小さな自転のような性質。上向き・下向きの2種類があり、1つの軌道に2個まで座れます。">スピン</span>には上向き・下向きがあり、1つの軌道に2個までです。</p>''',
      r'''    <h2>やってみよう ── 電子で席を埋める</h2>
    <div class="hint">ボタンで電子を1個ずつ入れます。下のエネルギーの席から順に埋まり、同じ席には2個（上向き・下向き）まで。</div>
    <div class="xbox">
      <svg id="pa" width="360" height="240" viewBox="0 0 360 240" role="img" aria-label="排他原理"></svg>
    </div>
    <div class="btns">
      <button id="add">電子を入れる ＋</button>
      <button id="rem">取り出す −</button>
    </div>
    <div class="readout" id="msg">電子 0 個</div>
    <div class="note">※ 同じ席（状態）には電子は入れないので、下から順に埋まっていきます。これが元素の個性と物質の硬さのもと。模式図です。</div>''',
      r'''<p>排他原理は、周期表のしくみ、物質が押しても縮まない硬さ、そして白色矮星や中性子星が自分の重さでつぶれずにいられる理由（1983年の項）まで説明します。半導体の電子のふるまいなど、現代技術の理解にも欠かせません。</p>''',
      r'''var svg=document.getElementById('pa'), addB=document.getElementById('add'),
    remB=document.getElementById('rem'), msg=document.getElementById('msg');
var NS='http://www.w3.org/2000/svg', levels=4, seatsPer=2, n=0;
var seatXY=[];
for(var L=0;L<levels;L++){var y=210-L*46;
  var ln=document.createElementNS(NS,'line');
  ln.setAttribute('x1',110);ln.setAttribute('y1',y);ln.setAttribute('x2',250);ln.setAttribute('y2',y);
  ln.setAttribute('stroke','#2a3446');ln.setAttribute('stroke-width','2');svg.appendChild(ln);
  var t=document.createElementNS(NS,'text');t.setAttribute('x',258);t.setAttribute('y',y+4);
  t.setAttribute('fill','#8b93a7');t.setAttribute('font-size','11');t.textContent='席 '+(L+1);svg.appendChild(t);
  seatXY.push([150,y-9]); seatXY.push([210,y-9]);
}
function draw(){
  Array.prototype.slice.call(svg.querySelectorAll('.e')).forEach(function(el){el.remove();});
  for(var i=0;i<n && i<seatXY.length;i++){var p=seatXY[i];
    var c=document.createElementNS(NS,'circle');c.setAttribute('class','e');
    c.setAttribute('cx',p[0]);c.setAttribute('cy',p[1]);c.setAttribute('r',9);c.setAttribute('fill','#c4b5fd');svg.appendChild(c);
    var a=document.createElementNS(NS,'text');a.setAttribute('class','e');a.setAttribute('x',p[0]);a.setAttribute('y',p[1]+4);
    a.setAttribute('text-anchor','middle');a.setAttribute('font-size','12');a.setAttribute('fill','#20242e');
    a.textContent=(i%2===0)?'↑':'↓';svg.appendChild(a);
  }
  msg.innerHTML='電子 <b>'+n+'</b> 個'+(n>=seatXY.length?'（満席）':'');
}
addB.addEventListener('click',function(){if(n<seatXY.length){n++;draw();}});
remB.addEventListener('click',function(){if(n>0){n--;draw();}});
draw();''')

    # ===== 16 湯川秀樹 1949 =====
    page("16_1949_yukawa.html", "particle", 1949,
      "核をまとめる力の正体 ── 中間子の予言",
      "湯川秀樹（日本）",
      "原子核の中で働く力についての理論研究にもとづく、中間子の存在の予言に対して。",
      "プラスどうしなのに、なぜ核はまとまる？",
      r'''<p>原子核はプラスの陽子がぎゅっと集まっています。同じプラスどうしは反発するはずなのに、核はバラバラになりません。反発をおさえて核をまとめる、電気とは別の<b>強い力</b>があるはず――でもその正体は謎でした。</p>''',
      "粒をキャッチボールして力が生まれる",
      r'''<p>湯川は「陽子と中性子が、ある<b>粒をキャッチボール</b>することで引き合う」と考えました。その未知の粒が<span class="term" data-tip="陽子や中性子の間でやりとりされ、核をまとめる力を伝える粒。重さが電子と陽子の中くらいなので“中間子”。湯川が予言し、のちに発見されました。">中間子（ちゅうかんし）</span>です。重さが電子と陽子の中くらいなのでこの名前に。しかもこの力は<b>核の中だけに届く近距離の力</b>だと予言しました。数年後、中間子は宇宙線の中から本当に見つかり、<b>日本人初のノーベル賞</b>となりました。</p>''',
      r'''    <h2>やってみよう ── 中間子のキャッチボール</h2>
    <div class="hint">ボタンを押すと、陽子と中性子が中間子を投げ合います。このやりとりが、核をまとめる「強い力」です。</div>
    <div class="xbox">
      <svg id="yu" width="460" height="180" viewBox="0 0 460 180" role="img" aria-label="中間子交換">
        <circle cx="120" cy="90" r="26" fill="#ff9a8a"/><text x="120" y="95" text-anchor="middle" font-size="13" fill="#3f0404" font-weight="bold">p</text>
        <text x="120" y="150" fill="#8b93a7" font-size="11" text-anchor="middle">陽子</text>
        <circle cx="340" cy="90" r="26" fill="#8ab6ff"/><text x="340" y="95" text-anchor="middle" font-size="13" fill="#04203f" font-weight="bold">n</text>
        <text x="340" y="150" fill="#8b93a7" font-size="11" text-anchor="middle">中性子</text>
        <circle id="pion" cx="120" cy="90" r="10" fill="#c4b5fd" opacity="0"/>
      </svg>
    </div>
    <div class="btns"><button id="toggle">力を働かせる（開始）</button></div>
    <div class="readout" id="msg">ボタンで中間子のやりとりを始めます</div>
    <div class="note">※ 粒を投げ合うことで力が伝わる、というのが現代物理の「力」の見方です。強い力は核の中だけに届く近距離の力。模式図です。</div>''',
      r'''<p>「力は粒のやりとりで伝わる」という湯川の考え方は、その後の<b>素粒子物理学</b>の基本になりました。電磁気の力は光子、弱い力・強い力もそれぞれの粒のやりとり――という現代の描像（1965・1979・2013年の項）はここから続いています。日本の物理学が世界に認められる出発点にもなりました。</p>''',
      r'''var pion=document.getElementById('pion'), toggle=document.getElementById('toggle'), msg=document.getElementById('msg');
var on=false, anim=null, t=0;
function loop(){ t+=0.03; var s=(Math.sin(t)+1)/2;   // 0..1 往復
  var x=120+(340-120)*s, y=90-40*Math.sin(s*Math.PI);
  pion.setAttribute('cx',x); pion.setAttribute('cy',y);
  anim=requestAnimationFrame(loop);
}
toggle.addEventListener('click',function(){
  on=!on;
  if(on){ pion.setAttribute('opacity','1'); toggle.textContent='止める'; toggle.classList.add('on');
    msg.innerHTML='中間子を<b>キャッチボール</b>中 ── これが核をまとめる力'; loop(); }
  else{ if(anim)cancelAnimationFrame(anim); pion.setAttribute('opacity','0'); toggle.textContent='力を働かせる（開始）'; toggle.classList.remove('on');
    msg.innerHTML='止めました'; }
});''')

    # ===== 17 トランジスタ 1956 =====
    page("17_1956_transistor.html", "matter", 1956,
      "電気を操る小さなスイッチ ── トランジスタの発明",
      "ショックレー ／ バーディーン ／ ブラッテン（アメリカ）",
      "半導体の研究と、トランジスタ効果（小さな信号で大きな電流を操るしくみ）の発見に対して。",
      "大きくて熱い「真空管」の時代",
      r'''<p>電気の流れを操る部品として、当時は<b>真空管</b>が使われていました。しかし大きく、熱く、こわれやすく、電気も食います。もっと小さく丈夫な“電気のスイッチ”が求められていました。</p>''',
      "半導体で、小さな力が大きな流れを操る",
      r'''<p>3人は<span class="term" data-tip="電気を通しやすい金属と、通さない絶縁体の中間の物質。シリコンなど。条件しだいで流れをオン・オフでき、電子技術の主役です。">半導体</span>を使い、<b>ごく小さな信号で大きな電流をオン・オフしたり増幅したりできる</b>部品＝<span class="term" data-tip="半導体でできた、電気のスイッチ兼増幅器。小さな入力で大きな出力を操れます。コンピュータの基本部品。">トランジスタ</span>を作りました。水道の蛇口を軽くひねるだけで大量の水を出したり止めたりできるのと同じ。真空管よりずっと小さく、丈夫で、省エネでした。</p>''',
      r'''    <h2>やってみよう ── 小さな操作で大きな流れ</h2>
    <div class="hint">スライダー（ゲート＝小さな信号）を動かすと、下の太い電流が増えたり止まったりします。ランプの明るさで確かめて。</div>
    <div class="xbox">
      <svg id="tr" width="480" height="200" viewBox="0 0 480 200" role="img" aria-label="トランジスタ">
        <rect x="40" y="120" width="360" height="24" rx="6" fill="#26343f"/>
        <text x="20" y="137" fill="#8b93a7" font-size="11">入</text>
        <rect id="gate" x="210" y="70" width="20" height="50" fill="#16a34a"/>
        <text x="220" y="60" fill="#66bb6a" font-size="11" text-anchor="middle">ゲート</text>
        <circle id="lamp" cx="440" cy="132" r="22" fill="#26343f"/>
        <text x="440" y="176" fill="#8b93a7" font-size="11" text-anchor="middle">出力ランプ</text>
      </svg>
    </div>
    <div class="controls">
      <label for="g">ゲート（小さな信号）</label>
      <input id="g" type="range" min="0" max="100" value="0">
      <div class="readout" id="msg">スイッチ OFF</div>
    </div>
    <div class="note">※ 小さな信号が“蛇口”になって大きな電流を操ります。オン・オフはコンピュータの0と1、増幅はスピーカーや電波に使われます。模式図です。</div>''',
      r'''<p>トランジスタは電子機器を一気に小さくし、やがて何十億個も1枚のチップに詰めこむ<b>集積回路（IC）</b>へ。コンピュータ・スマホ・インターネット・あらゆる家電――現代のデジタル社会は、この小さなスイッチの上に成り立っています。20世紀最大の発明のひとつです。</p>''',
      r'''var g=document.getElementById('g'), gate=document.getElementById('gate'),
    lamp=document.getElementById('lamp'), msg=document.getElementById('msg'), svg=document.getElementById('tr');
var NS='http://www.w3.org/2000/svg', dots=[];
for(var i=0;i<10;i++){var c=document.createElementNS(NS,'circle');
  c.setAttribute('r',5);c.setAttribute('cy',132);c.setAttribute('fill','#7ee787');c.setAttribute('cx',40+i*36);
  svg.appendChild(c);dots.push({el:c,x:40+i*36});}
var t=+g.value;
function frame(){ var open=+g.value/100;
  gate.setAttribute('y',120-50*open); gate.setAttribute('height',24+50*open>50?50:24+50*open);
  gate.setAttribute('height',20+30*open);
  lamp.setAttribute('fill','rgba(126,231,135,'+(0.15+0.85*open).toFixed(2)+')');
  dots.forEach(function(d){ d.x+=1+open*6; if(d.x>400)d.x=40; d.el.setAttribute('cx',d.x);
    d.el.setAttribute('opacity', open>0.02?1:0.12); });
  msg.innerHTML = open<0.02?'スイッチ <b>OFF</b>（流れない）': open<0.6?'少し流れる（絞った蛇口）':'<b>ON</b>：大きく流れる';
  requestAnimationFrame(frame);
}
g.addEventListener('input',function(){});
frame();''')

    # ===== 18 リー／ヤン 1957 =====
    page("18_1957_lee_yang.html", "particle", 1957,
      "自然は左右対称ではなかった ── パリティの破れ",
      "李政道（リー） ／ 楊振寧（ヤン）（中国→アメリカ）",
      "左右の対称性（パリティ保存）についての鋭い研究が、素粒子の重要な発見につながったことに対して。",
      "鏡の中と同じはず、という思いこみ",
      r'''<p>物理の法則は<b>鏡に映しても同じ</b>――左右をひっくり返しても自然のふるまいは変わらない、と長く信じられていました（<span class="term" data-tip="左右（鏡像）を入れかえても物理法則は同じ、という考え。長く当然と思われていました。">パリティ保存</span>）。ボールの運動も電気の現象も、鏡の中でちゃんと成り立ちます。</p>''',
      "弱い力は「左右」を区別していた",
      r'''<p>リーとヤンは、原子核がこわれる<span class="term" data-tip="原子核が電子などを放って別の核に変わる現象。これを起こすのが自然界の“弱い力”です。">弱い力</span>の現象では、これが確かめられていないと見抜きました。実験（ウー夫人による）で、放射性の原子核から出る電子は<b>特定の向きにかたよって</b>飛び、その鏡像は自然界に<b>起こらない</b>ことが分かりました。弱い力は<b>左右を区別していた</b>のです。「当たり前」が崩れた衝撃的な発見でした。</p>''',
      r'''    <h2>やってみよう ── 現実と、鏡の中</h2>
    <div class="hint">ボタンで「現実」と「鏡の中」を切りかえます。弱い力では、鏡の中の向きは自然界に起こりません。</div>
    <div class="xbox">
      <svg id="pv" width="420" height="220" viewBox="0 0 420 220" role="img" aria-label="パリティの破れ">
        <line x1="210" y1="10" x2="210" y2="210" stroke="#3a4356" stroke-dasharray="4 4"/>
        <circle id="nuc" cx="210" cy="110" r="24" fill="#0d9488"/>
        <path id="spin" d="" fill="none" stroke="#5eead4" stroke-width="3" marker-end="url(#ah)"/>
        <defs><marker id="ah" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#5eead4"/></marker></defs>
        <path id="emit" d="" fill="none" stroke="#ffd257" stroke-width="0" stroke-linecap="round"/>
        <text id="dir" x="210" y="200" fill="#e8edf3" font-size="12" text-anchor="middle"></text>
      </svg>
    </div>
    <div class="btns">
      <button id="real" class="on">現実</button>
      <button id="mir">鏡の中</button>
    </div>
    <div class="status yes" id="st">現実：電子はスピンと逆向き（下）に多く飛ぶ</div>
    <div class="note">※ 弱い力では、現実に起きる向きと、その鏡像が別物です。つまり自然は左右を区別している――模式図です。</div>''',
      r'''<p>「対称性は破れることがある」という発見は、その後の素粒子物理の大きなテーマになりました。物質と反物質の非対称（2008年の南部・小林・益川）や、宇宙になぜ物質だけが残ったのかという謎にもつながる、深い問いの始まりでした。</p>''',
      r'''var spin=document.getElementById('spin'), emit=document.getElementById('emit'),
    dir=document.getElementById('dir'), st=document.getElementById('st');
var realB=document.getElementById('real'), mirB=document.getElementById('mir');
function drawEmit(down,thickDown){
  // 上向き・下向きの矢印を太さで表現（多い向きを太く）
  emit.setAttribute('d','M210,110 L210,60');   // up
  emit.setAttribute('stroke','#ffd257');
}
function show(mirror){
  realB.classList.toggle('on',!mirror); mirB.classList.toggle('on',mirror);
  // スピン回転の向き（円弧）
  spin.setAttribute('d', mirror ? 'M186,96 A26,26 0 1 0 186,124' : 'M234,96 A26,26 0 1 1 234,124');
  if(!mirror){ st.className='status yes'; st.textContent='現実：電子はスピンと逆向き（下）に多く飛ぶ'; dir.textContent='↓ 多い　↑ 少ない'; }
  else{ st.className='status no'; st.textContent='鏡の中：向きが反転…でも自然界ではこの向きは起こらない！'; dir.textContent='↑ 多い（現実には起きない）'; }
}
realB.addEventListener('click',function(){show(false);});
mirB.addEventListener('click',function(){show(true);});
show(false);''')

    # ===== 19 ランダウ 1962 =====
    page("19_1962_landau.html", "matter", 1962,
      "抵抗ゼロで流れ続ける液体 ── 超流動の理論",
      "レフ・ランダウ（ソ連）",
      "液体ヘリウムなど、凝縮した物質のふるまいを説明する先駆的な理論に対して。",
      "冷やしきったヘリウムの不思議",
      r'''<p>ヘリウムを絶対零度近くまで冷やすと、ふつうの液体ではありえないことが起こります。<b>抵抗（粘り）がまったくなく流れ続け</b>、細いすき間をすり抜け、容器のかべをはい上がってこぼれ出すことさえある――この状態を<span class="term" data-tip="極低温でヘリウムなどが示す、粘りがゼロで永遠に流れ続ける状態。量子の性質が目に見える大きさで現れます。">超流動（ちょうりゅうどう）</span>といいます。</p>''',
      "量子のふるまいが目に見える大きさで現れる",
      r'''<p>ランダウは、こうした低温の物質を数式で説明する理論を築きました。ふつうはミクロな原子1個で起きる<b>量子の性質</b>が、超流動では<b>液体全体でそろって</b>現れます。だから摩擦を生む“ひっかかり”がなくなり、いつまでも流れ続けるのです。彼の理論は、極低温の物理を理解する共通の言葉になりました。</p>''',
      r'''    <h2>やってみよう ── 温度を下げると流れが変わる</h2>
    <div class="hint">スライダーで温度を下げてみましょう。ある温度より下がると、液体は抵抗ゼロで流れ続けます。</div>
    <div class="xbox">
      <svg id="lg" width="460" height="160" viewBox="0 0 460 160" role="img" aria-label="超流動"></svg>
    </div>
    <div class="controls">
      <label for="tp">温度（右へ動かすと下がる）　高温 ← → 極低温</label>
      <input id="tp" type="range" min="0" max="100" value="10">
      <div class="status no" id="st"></div>
    </div>
    <div class="note">※ ある温度（転移点）より下では粘りがゼロになり、液体はいつまでも止まりません。量子の性質が“大きな世界”に現れた例。模式図です。</div>''',
      r'''<p>超流動やそれと似た現象の理解は、<b>超伝導</b>（1972年の項）や、レーザーで原子を極低温にして作る新しい物質の状態など、現代の低温物理・量子技術の土台になりました。ランダウの理論は物性物理学の“古典”として、いまも教科書で学ばれています。</p>''',
      r'''var tp=document.getElementById('tp'), st=document.getElementById('st'), svg=document.getElementById('lg');
var NS='http://www.w3.org/2000/svg', dots=[];
var pipe=document.createElementNS(NS,'rect');
pipe.setAttribute('x',20);pipe.setAttribute('y',66);pipe.setAttribute('width',420);pipe.setAttribute('height',28);
pipe.setAttribute('rx',14);pipe.setAttribute('fill','#0b1220');pipe.setAttribute('stroke','#2a3446');svg.appendChild(pipe);
for(var i=0;i<9;i++){var c=document.createElementNS(NS,'circle');
  c.setAttribute('r',7);c.setAttribute('cy',80);c.setAttribute('cx',40+i*44);svg.appendChild(c);
  dots.push({el:c,x:40+i*44});}
function frame(){ var cold=+tp.value>50;
  dots.forEach(function(d,i){ var v=cold?3.2:(0.5+Math.sin(Date.now()/300+i)*0.4);
    d.x+=v; if(d.x>430)d.x=25; d.el.setAttribute('cx',d.x);
    d.el.setAttribute('fill',cold?'#5eead4':'#ff9a8a'); });
  if(cold){st.className='status yes';st.textContent='超流動：抵抗ゼロで永遠に流れ続ける';}
  else{st.className='status no';st.textContent='ふつうの液体：摩擦があってすぐ止まる';}
  requestAnimationFrame(frame);
}
frame();''')

    # ===== 20 タウンズ 1964 =====
    page("20_1964_townes.html", "matter", 1964,
      "そろった光をつくる ── メーザーとレーザー",
      "タウンズ ／ バソフ ／ プロホロフ（アメリカ・ソ連）",
      "メーザーやレーザーを生み出した、量子エレクトロニクスの基礎研究に対して。",
      "ふつうの光はバラバラ",
      r'''<p>電球や太陽の光は、いろいろな色・向き・タイミングの波が<b>バラバラに混ざって</b>います。もし波の山をぜんぶ<b>そろえた光</b>が作れたら、まっすぐ遠くまで届き、1点に強く集められるはず――でもどうやって？</p>''',
      "1粒の光が、そっくりな光を次々生む",
      r'''<p>カギは<span class="term" data-tip="エネルギーの高い状態にある原子に光が当たると、それと“うり二つ”の光（同じ色・向き・タイミング）を放って自分も下がる現象。レーザーの心臓部です。">誘導放出（ゆうどうほうしゅつ）</span>です。エネルギーを蓄えた原子に光が1粒当たると、<b>まったく同じ光をもう1粒</b>放ちます。それがまた次の原子を刺激して…と<b>そっくりな光がなだれのように増え</b>、山のそろった強い光＝<span class="term" data-tip="色・向き・波の山がそろった光。まっすぐ進み、1点に集められます。">レーザー</span>になります（電波でやると<b>メーザー</b>）。</p>''',
      r'''    <h2>やってみよう ── そろった光のなだれ</h2>
    <div class="hint">「光を1粒入れる」を押すと、エネルギーを蓄えた原子（★）が次々と同じ光を放ち、そろったビームになります。</div>
    <div class="xbox">
      <svg id="ls" width="480" height="170" viewBox="0 0 480 170" role="img" aria-label="レーザー"></svg>
    </div>
    <div class="btns"><button id="seed">光を1粒入れる</button><button id="reset2">元にもどす</button></div>
    <div class="readout" id="msg">原子はエネルギーを蓄えた状態（★）です</div>
    <div class="note">※ 1粒の光が引き金になり、同じ色・同じ向きの光がそろって増えます。これがレーザーの原理。模式図です。</div>''',
      r'''<p>レーザーはいまや<b>光通信・DVD/バーコード・手術・金属加工・距離の計測・スマホの顔認証</b>まで、数えきれない場面で活躍しています。2017年の重力波観測や2018年の光ピンセットなど、後のノーベル賞の道具にもなりました。「そろった光」は現代文明の必需品です。</p>''',
      r'''var svg=document.getElementById('ls'), seed=document.getElementById('seed'),
    reset2=document.getElementById('reset2'), msg=document.getElementById('msg');
var NS='http://www.w3.org/2000/svg', atoms=[], photons=[], N=7, running=false;
function build(){ svg.innerHTML=''; atoms=[]; photons=[];
  for(var i=0;i<N;i++){var x=70+i*54;
    var c=document.createElementNS(NS,'circle');c.setAttribute('cx',x);c.setAttribute('cy',85);
    c.setAttribute('r',15);c.setAttribute('fill','#3b2f66');c.setAttribute('stroke','#c4b5fd');svg.appendChild(c);
    var s=document.createElementNS(NS,'text');s.setAttribute('x',x);s.setAttribute('y',90);
    s.setAttribute('text-anchor','middle');s.setAttribute('font-size','14');s.setAttribute('fill','#ffd257');s.textContent='★';svg.appendChild(s);
    atoms.push({x:x,excited:true,star:s,body:c});}
}
function frame(){ if(!running){return;}
  for(var i=photons.length-1;i>=0;i--){var p=photons[i]; p.x+=5; p.el.setAttribute('cx',p.x);
    atoms.forEach(function(a){ if(a.excited && Math.abs(p.x-a.x)<4){ a.excited=false; a.star.textContent='';
        a.body.setAttribute('fill','#26343f'); a.body.setAttribute('stroke','#3a4356');
        addPhoton(a.x,58); } });
    if(p.x>480){}
  }
  if(atoms.every(function(a){return !a.excited;})) msg.innerHTML='<b>そろった光（レーザー）が飛び出した！</b> 全部そっくりな光';
  requestAnimationFrame(frame);
}
function addPhoton(x,y){var e=document.createElementNS(NS,'circle');e.setAttribute('cx',x);e.setAttribute('cy',y||85);
  e.setAttribute('r',5);e.setAttribute('fill','#ffe066');svg.appendChild(e);photons.push({x:x,el:e});}
seed.addEventListener('click',function(){ if(!running){running=true;frame();} addPhoton(20,85);
  msg.innerHTML='光が原子を刺激して、同じ光が増えていく…'; });
reset2.addEventListener('click',function(){running=false;build();msg.innerHTML='原子はエネルギーを蓄えた状態（★）です';});
build();''')

    # ===== 21 朝永振一郎 1965 =====
    page("21_1965_tomonaga.html", "quantum", 1965,
      "光と電子の理論を完成させる ── 量子電磁力学(QED)",
      "朝永振一郎（日本） ／ シュウィンガー ／ ファインマン（アメリカ）",
      "素粒子の物理に深い影響を与えた、量子電磁力学の基礎研究に対して。",
      "計算すると答えが無限大になってしまう",
      r'''<p>電子と光（電磁気）を量子力学できちんと扱おうとすると、計算のとちゅうで答えが<b>無限大</b>になって破綻してしまう、という深刻な問題がありました。理論はあるのに、まともな数字が出せなかったのです。</p>''',
      "電子は「光の雲」をまとっている",
      r'''<p>電子は、絶えず生まれては消える<span class="term" data-tip="ごく短い時間だけ現れて消える光や粒。直接は見えませんが、電子のふるまいに影響します。">仮想的な光（虚光子）</span>の雲をまとっている――3人はこの効果を正しく計算する方法（<span class="term" data-tip="無限大が出る部分を、実際に測れる電子の質量や電気の値にうまく含めて処理する手法。これで有限のまともな答えが得られます。">くりこみ</span>）を独立に完成させました。これが<span class="term" data-tip="光と電子（電磁気）を量子力学で扱う理論。自然界でもっとも精密に検証された理論です。">量子電磁力学(QED)</span>です。予言は実験と<b>小数第10位以上まで</b>一致し、「もっとも正確な理論」と呼ばれます。</p>''',
      r'''    <h2>やってみよう ── 電子をぐっと拡大する</h2>
    <div class="hint">スライダーで電子を拡大すると、まわりに現れては消える「光の雲」が見えてきます。QEDはこの雲まで計算します。</div>
    <div class="xbox">
      <svg id="qe" width="360" height="240" viewBox="0 0 360 240" role="img" aria-label="QEDの光の雲">
        <circle cx="180" cy="120" r="14" fill="#c4b5fd"/>
        <text x="180" y="125" text-anchor="middle" font-size="12" fill="#20242e" font-weight="bold">e</text>
        <g id="cloud"></g>
      </svg>
    </div>
    <div class="controls">
      <label for="zoom">拡大（近づいて見る）</label>
      <input id="zoom" type="range" min="0" max="100" value="20">
      <div class="readout" id="msg"></div>
    </div>
    <div class="note">※ 電子は絶えず光をやりとりする“雲”をまとっています。この効果まで計算するのがQED。模式図です。</div>''',
      r'''<p>QEDは、その後に自然界の力を統一的に理解する<b>場の量子論</b>のお手本になりました。弱い力・強い力の理論（1979・2013年の項）も、この考え方の上に築かれています。朝永は湯川に続く日本人2人目のノーベル物理学賞受賞者で、日本の理論物理を世界水準に押し上げました。</p>''',
      r'''var zoom=document.getElementById('zoom'), cloud=document.getElementById('cloud'), msg=document.getElementById('msg');
var NS='http://www.w3.org/2000/svg';
function frame(){ var z=+zoom.value/100; var nn=Math.round(z*14);
  cloud.innerHTML='';
  for(var i=0;i<nn;i++){ var a=Math.random()*6.28, r=24+Math.random()*(30+z*60);
    var x=180+r*Math.cos(a), y=120+r*Math.sin(a);
    var c=document.createElementNS(NS,'circle');c.setAttribute('cx',x);c.setAttribute('cy',y);
    c.setAttribute('r',2+Math.random()*3);c.setAttribute('fill','#ffe066');
    c.setAttribute('opacity',(0.3+Math.random()*0.6).toFixed(2));cloud.appendChild(c);}
  msg.innerHTML = z<0.15?'遠目には、電子はただの点':'まわりに<b>現れては消える光の雲</b>が見える';
  requestAnimationFrame(frame);
}
frame();''')

    # ===== 22 BCS理論 1972 =====
    page("22_1972_bcs.html", "matter", 1972,
      "電子がペアを組んで抵抗ゼロに ── 超伝導のBCS理論",
      "バーディーン ／ クーパー ／ シュリーファー（アメリカ）",
      "電子が対をつくることで説明される、超伝導の理論（BCS理論）に対して。",
      "冷やすと電気抵抗が突然ゼロになる",
      r'''<p>ある金属をとても低い温度まで冷やすと、電気<b>抵抗が突然ゼロ</b>になり、電流が減らずに流れ続けます（<span class="term" data-tip="低温で電気抵抗がゼロになる現象。電流が永遠に流れ、強い磁石を浮かせられます。">超伝導</span>）。40年以上も理由が分からない大きな謎でした。</p>''',
      "電子2個がそっと手をつなぐ",
      r'''<p>ふだん電子は金属の中の原子にぶつかって進みにくく、それが抵抗になります。3人は、低温では電子が2個1組の<span class="term" data-tip="低温で電子2個がゆるく引き合ってできるペア。ペアはそろって動くので原子にぶつからず、抵抗が消えます。">クーパー対（つい）</span>を組み、ペアたちが<b>足並みをそろえて</b>動くため、原子にぶつからずスルスル流れる――と説明しました（BCS理論）。名前は3人の頭文字です。</p>''',
      r'''    <h2>やってみよう ── ぶつかる電子、ペアを組む電子</h2>
    <div class="hint">スライダーで温度を下げると、電子が2個ずつペアを組み、原子にぶつからずまっすぐ流れます（抵抗ゼロ）。</div>
    <div class="xbox">
      <svg id="bc" width="480" height="170" viewBox="0 0 480 170" role="img" aria-label="超伝導"></svg>
    </div>
    <div class="controls">
      <label for="tc">温度　高温 ← → 極低温</label>
      <input id="tc" type="range" min="0" max="100" value="10">
      <div class="status no" id="st"></div>
    </div>
    <div class="note">※ 高温では電子が原子にぶつかってジグザグ（抵抗あり）。低温ではペアがそろって直進（抵抗ゼロ）。模式図です。</div>''',
      r'''<p>超伝導は、<b>MRI（病院の強力な磁石）</b>、<b>リニアモーターカーの浮上</b>、<b>電力を損なわず送る電線</b>、<b>量子コンピュータ</b>などに使われています。より高い温度で超伝導になる材料の探索は、いまも物理学の大きなテーマです。</p>''',
      r'''var tc=document.getElementById('tc'), st=document.getElementById('st'), svg=document.getElementById('bc');
var NS='http://www.w3.org/2000/svg', ions=[], es=[];
for(var r=0;r<3;r++)for(var c=0;c<8;c++){var ix=45+c*54, iy=45+r*40;
  var p=document.createElementNS(NS,'circle');p.setAttribute('cx',ix);p.setAttribute('cy',iy);
  p.setAttribute('r',5);p.setAttribute('fill','#3a4356');svg.appendChild(p);ions.push([ix,iy]);}
for(var i=0;i<6;i++){var e=document.createElementNS(NS,'circle');e.setAttribute('r',7);e.setAttribute('fill','#5eead4');
  svg.appendChild(e);es.push({el:e,x:20+i*70,y:85,ph:Math.random()*6.28});}
function frame(){ var cold=+tc.value>50;
  es.forEach(function(e,i){ e.x+=cold?3:2.2;
    if(cold){ e.y=85+((i%2)?6:-6); }                 // ペアで直進
    else{ e.y=85+Math.sin(e.x/16+e.ph)*26; }          // ジグザグ
    if(e.x>470)e.x=15; e.el.setAttribute('cx',e.x); e.el.setAttribute('cy',e.y);
    e.el.setAttribute('fill',cold?'#5eead4':'#ff9a8a'); });
  if(cold){st.className='status yes';st.textContent='超伝導：ペアがそろって直進 → 電気抵抗ゼロ';}
  else{st.className='status no';st.textContent='ふつうの金属：原子にぶつかりジグザグ → 抵抗あり';}
  requestAnimationFrame(frame);
}
frame();''')

    # ===== 23 パルサー 1974 =====
    page("23_1974_pulsar.html", "cosmos", 1974,
      "宇宙の灯台 ── 電波天文学とパルサーの発見",
      "ライル ／ ヒューイッシュ（イギリス）",
      "電波天文学の先駆的な研究（ライル）と、パルサーの発見での決定的な役割（ヒューイッシュ）に対して。",
      "目ではなく電波で宇宙を見る",
      r'''<p>宇宙からは、目に見える光だけでなく<b>電波</b>も届いています。ライルたちは複数のアンテナを組み合わせて、電波で宇宙を精密に“見る”技術（<span class="term" data-tip="離れた複数のアンテナを組み合わせ、巨大な望遠鏡1台ぶんの解像度を得る技術。">電波干渉計</span>）を発展させました。</p>''',
      "きっかり規則正しく明滅する謎の星",
      r'''<p>その観測中、<b>1秒ほどの間隔できっちり明滅する</b>電波源が見つかりました（発見者は大学院生ジョスリン・ベル）。あまりに正確なので一時は宇宙人の信号かと騒がれましたが、正体は高速で自転する<span class="term" data-tip="太陽ほどの質量が都市サイズにぎゅっと詰まった超高密度の星。ティースプーン1杯で数億トン。">中性子星</span>でした。電波を一方向に出しながら回転し、ビームが地球を向くたびに“点滅”して見える――宇宙の灯台<span class="term" data-tip="規則正しい電波のパルスを出す、回転する中性子星。灯台のように光（電波）を振りまきます。">パルサー</span>です。</p>''',
      r'''    <h2>やってみよう ── 回転する宇宙の灯台</h2>
    <div class="hint">スライダーで自転の速さを変えます。ビームが地球（右）を向くたびに、下の記録計にパルスが刻まれます。</div>
    <div class="xbox">
      <svg id="ps" width="480" height="230" viewBox="0 0 480 230" role="img" aria-label="パルサー">
        <circle cx="150" cy="90" r="20" fill="#e8edf3"/>
        <line id="beam" x1="150" y1="90" x2="150" y2="90" stroke="#5c9dff" stroke-width="8" stroke-linecap="round" opacity="0.85"/>
        <line id="beam2" x1="150" y1="90" x2="150" y2="90" stroke="#5c9dff" stroke-width="8" stroke-linecap="round" opacity="0.85"/>
        <circle id="earth" cx="430" cy="90" r="9" fill="#66bb6a"/><text x="430" y="115" fill="#66bb6a" font-size="11" text-anchor="middle">地球</text>
        <rect x="20" y="160" width="440" height="50" rx="6" fill="#0b1220" stroke="#2a3446"/>
        <polyline id="chart" points="" fill="none" stroke="#7ee787" stroke-width="2"/>
      </svg>
    </div>
    <div class="controls">
      <label for="rot">自転の速さ</label>
      <input id="rot" type="range" min="1" max="10" value="4">
      <div class="readout" id="msg"></div>
    </div>
    <div class="note">※ ビームが地球を向いた瞬間だけ強く受信 → 規則正しいパルスになります。星の回転が“時計”のように正確です。模式図です。</div>''',
      r'''<p>パルサーは、極限の高密度・強い磁場・強い重力を調べる宇宙の実験室です。その正確な明滅は<b>宇宙の時計</b>として使われ、のちに連星パルサーの観測は<b>重力波の存在</b>を間接的に証明しました（直接観測は2017年の項）。電波天文学はブラックホールや宇宙背景放射（1978年の項）の研究へと広がりました。</p>''',
      r'''var beam=document.getElementById('beam'), beam2=document.getElementById('beam2'),
    earth=document.getElementById('earth'), chart=document.getElementById('chart'),
    rot=document.getElementById('rot'), msg=document.getElementById('msg');
var ang=0, cx=150, cy=90, L=120, pts=[], hitCount=0;
function frame(){ ang+=(+rot.value)/40;
  var dx=Math.cos(ang), dy=Math.sin(ang);
  beam.setAttribute('x2',cx+L*dx); beam.setAttribute('y2',cy+L*dy);
  beam2.setAttribute('x2',cx-L*dx); beam2.setAttribute('y2',cy-L*dy);
  var toward = dx>0.985;                            // 右（地球）を向いた
  earth.setAttribute('r', toward?14:9);
  earth.setAttribute('fill', toward?'#b6ffcf':'#66bb6a');
  var y = toward?168:205;
  pts.push(y); if(pts.length>220)pts.shift();
  chart.setAttribute('points', pts.map(function(v,i){return (24+i*2)+','+v;}).join(' '));
  if(toward){ msg.innerHTML='<b>パルス受信！</b> ビームが地球を向いた'; }
  requestAnimationFrame(frame);
}
frame();''')

    # ===== 24 宇宙背景放射 1978 =====
    page("24_1978_cmb.html", "cosmos", 1978,
      "ビッグバンの残り火 ── 宇宙マイクロ波背景放射",
      "ペンジアス ／ ウィルソン（アメリカ）",
      "宇宙のあらゆる方向から届く「宇宙マイクロ波背景放射」の発見に対して。",
      "消えない“雑音”の正体",
      r'''<p>2人はアンテナの実験中、どうしても消えない<b>かすかな電波の雑音</b>に悩まされました。アンテナを掃除しても、どの方向へ向けても、昼も夜も、同じ強さで“サーッ”と聞こえ続けます。原因が分かりませんでした。</p>''',
      "宇宙全体を満たす、生まれたての光",
      r'''<p>それは、<b>約138億年前のビッグバン</b>のときの熱い光が、宇宙がふくらむにつれ冷めて<b>電波（マイクロ波）</b>になったもの――<span class="term" data-tip="ビッグバン直後の熱い光が、宇宙の膨張で冷えて今は約−270℃の電波として全天から届くもの。ビッグバンの決定的な証拠です。">宇宙マイクロ波背景放射</span>でした。宇宙のあらゆる方向から、ほぼ同じ温度（<b>約−270℃</b>）で届きます。ビッグバン理論の動かぬ証拠であり、「宇宙にも始まりがあった」ことを告げる光でした。</p>''',
      r'''    <h2>やってみよう ── どの方向を向いても同じ</h2>
    <div class="hint">スライダーでアンテナの向きを変えてみましょう。空のどこを向いても、受信する電波の強さ（温度）は同じです。</div>
    <div class="xbox">
      <svg id="cm" width="440" height="220" viewBox="0 0 440 220" role="img" aria-label="宇宙背景放射">
        <g id="stars"></g>
        <g id="dish" transform="rotate(0 220 200)">
          <line x1="220" y1="200" x2="220" y2="120" stroke="#e8edf3" stroke-width="4"/>
          <path d="M195,120 A40,40 0 0 1 245,120 Z" fill="#9fb2c9"/>
        </g>
        <rect x="150" y="200" width="140" height="12" rx="4" fill="#26343f"/>
      </svg>
    </div>
    <div class="controls">
      <label for="dir">アンテナの向き</label>
      <input id="dir" type="range" min="-70" max="70" value="0">
      <div class="readout" id="msg">受信温度：<b>約 2.7 K（−270℃）</b> ── どこでも同じ</div>
    </div>
    <div class="note">※ 全天からほぼ均一に届くのがこの放射の特徴。だからビッグバンが宇宙全体で起きた証拠になります。模式図です。</div>''',
      r'''<p>この放射のごくわずかな“むら”を精密に測ることで、宇宙の年齢・成分・生い立ちが分かるようになりました（のちのCOBE・WMAP・Planck衛星）。宇宙論は「哲学」から「精密科学」へと変わり、ダークマターやダークエネルギー（2011年の項）の研究へとつながっています。</p>''',
      r'''var dir=document.getElementById('dir'), dish=document.getElementById('dish'), stars=document.getElementById('stars');
var NS='http://www.w3.org/2000/svg';
for(var i=0;i<90;i++){var c=document.createElementNS(NS,'circle');
  c.setAttribute('cx',Math.random()*440);c.setAttribute('cy',Math.random()*180);
  c.setAttribute('r',1+Math.random()*1.5);c.setAttribute('fill','#5c9dff');
  c.setAttribute('opacity',(0.3+Math.random()*0.5).toFixed(2));stars.appendChild(c);}
function render(){ dish.setAttribute('transform','rotate('+dir.value+' 220 200)'); }
dir.addEventListener('input',render); render();''')

    # ===== 25 電弱統一 1979 =====
    page("25_1979_electroweak.html", "particle", 1979,
      "2つの力はもともと1つ ── 電弱統一理論",
      "グラショー ／ サラム ／ ワインバーグ（アメリカ・パキスタン）",
      "電磁気の力と弱い力を1つにまとめる理論（電弱統一）に対して。とくに弱い中性カレントの予言。",
      "まるで似ていない2つの力",
      r'''<p>身のまわりの<b>電磁気の力</b>（電気・磁石・光）と、原子核をこわす<b>弱い力</b>は、強さも届く距離もまるで違います。別々の力に見えました。ところが理論家たちは、両者に深いつながりがあると気づきます。</p>''',
      "高いエネルギーでは1つの力になる",
      r'''<p>3人は、<b>ものすごく高いエネルギー（宇宙のごく初期のような状態）</b>では、電磁気の力と弱い力が区別できない<b>1つの力（電弱力）</b>になる、という理論を作りました。エネルギーが下がって宇宙が冷えると、力を伝える粒のうち<span class="term" data-tip="弱い力を伝える重い粒。重いために弱い力は近距離でしか働きません。のちに実験で発見されました。">W粒子・Z粒子</span>だけが重くなり、身軽な<span class="term" data-tip="電磁気の力（光）を伝える、重さゼロの粒。">光子</span>と枝分かれして、別々の力に“見える”ようになったのです。予言どおりW・Z粒子は実験で見つかりました。</p>''',
      r'''    <h2>やってみよう ── エネルギーを上げて力を1つにする</h2>
    <div class="hint">スライダーでエネルギーを上げると、離れていた「電磁気力」と「弱い力」が近づき、やがて1つの力に溶け合います。</div>
    <div class="xbox">
      <svg id="ew" width="440" height="200" viewBox="0 0 440 200" role="img" aria-label="電弱統一">
        <circle id="cA" cx="120" cy="100" r="40" fill="#2563eb" opacity="0.85"/>
        <text id="tA" x="120" y="105" text-anchor="middle" font-size="13" fill="#fff">電磁気力</text>
        <circle id="cB" cx="320" cy="100" r="40" fill="#0d9488" opacity="0.85"/>
        <text id="tB" x="320" y="105" text-anchor="middle" font-size="13" fill="#fff">弱い力</text>
      </svg>
    </div>
    <div class="controls">
      <label for="en">エネルギー（宇宙初期に近づく）</label>
      <input id="en" type="range" min="0" max="100" value="0">
      <div class="status no" id="st">低エネルギー：2つは別々の力に見える</div>
    </div>
    <div class="note">※ ふだんは別々でも、超高エネルギーでは同じ1つの力。宇宙が冷えて枝分かれした、という考え。模式図です。</div>''',
      r'''<p>電弱統一は、自然界の力をまとめて理解しようとする<b>標準模型</b>の柱になりました。W・Z粒子やヒッグス粒子（2013年の項）の発見でその正しさが確かめられています。さらに「強い力」まで含めて統一する<b>大統一理論</b>の夢は、いまも物理学最前線の課題です。</p>''',
      r'''var en=document.getElementById('en'), cA=document.getElementById('cA'), cB=document.getElementById('cB'),
    tA=document.getElementById('tA'), tB=document.getElementById('tB'), st=document.getElementById('st');
function render(){ var t=+en.value/100;
  var ax=120+t*100, bx=320-t*100;
  cA.setAttribute('cx',ax); tA.setAttribute('x',ax);
  cB.setAttribute('cx',bx); tB.setAttribute('x',bx);
  if(t>0.9){ cA.setAttribute('fill','#7c3aed'); cB.setAttribute('fill','#7c3aed');
    tA.textContent='電弱力'; tB.textContent=''; st.className='status yes'; st.textContent='超高エネルギー：2つが溶け合って1つの力（電弱力）！'; }
  else{ cA.setAttribute('fill','#2563eb'); cB.setAttribute('fill','#0d9488');
    tA.textContent='電磁気力'; tB.textContent='弱い力'; st.className='status no'; st.textContent='低エネルギー：2つは別々の力に見える'; }
}
en.addEventListener('input',render); render();''')

    # ===== 26 チャンドラセカール 1983 =====
    page("26_1983_chandrasekhar.html", "cosmos", 1983,
      "星の最期を決める限界の重さ ── チャンドラセカール限界",
      "チャンドラセカール ／ ファウラー（アメリカ）",
      "星の構造と進化、とくに星の最期に関する理論研究に対して。",
      "燃えつきた星はどうなる？",
      r'''<p>太陽のような星は、燃料を使い果たすと縮んで小さな<span class="term" data-tip="燃えつきた星の残骸。地球ほどの大きさに太陽ほどの質量が詰まった超高密度の星。">白色矮星（はくしょくわいせい）</span>になります。このとき星をつぶさずに支えているのは、電子が「同じ席に入れない」というパウリの原理（1945年の項）による押し返す力です。</p>''',
      "重さに上限があった",
      r'''<p>チャンドラセカールは若干19歳のとき、計算からある結論に達しました。白色矮星の重さには<b>限界（太陽の約1.4倍）</b>があり、それを超えると電子の力では支えきれず、星は一気に<b>つぶれてしまう</b>――。この<span class="term" data-tip="白色矮星が自分を支えられる重さの上限（太陽の約1.4倍）。超えると中性子星やブラックホールへ崩壊します。">チャンドラセカール限界</span>を超えた星は、超新星爆発を起こし、中性子星やブラックホール（2020年の項）になります。当時は大御所に否定されましたが、のちに正しさが認められました。</p>''',
      r'''    <h2>やってみよう ── 星の重さと運命</h2>
    <div class="hint">スライダーで白色矮星の重さを変えます。限界（太陽の1.4倍）を超えると、星は支えきれずに崩壊します。</div>
    <div class="xbox">
      <svg id="ch2" width="360" height="230" viewBox="0 0 360 230" role="img" aria-label="チャンドラセカール限界">
        <circle id="star" cx="180" cy="115" r="70" fill="#ffe066"/>
        <circle id="flash" cx="180" cy="115" r="0" fill="#ff6b6b" opacity="0"/>
      </svg>
    </div>
    <div class="controls">
      <label for="m">星の重さ（太陽の何倍）</label>
      <input id="m" type="range" min="20" max="200" value="60">
      <div class="status yes" id="st"></div>
    </div>
    <div class="note">※ 重いほど強い重力で小さく縮みます。1.4倍を超えると電子の力で支えきれず崩壊――模式図です。</div>''',
      r'''<p>チャンドラセカール限界は、<b>Ia型超新星</b>という“標準の明るさ”の爆発を生み、それが宇宙の距離をはかる「ものさし」になりました。この物差しが、のちに<b>宇宙の加速膨張</b>（2011年の項）の発見を可能にしました。星の一生とブラックホール誕生を理解する、天体物理の基礎です。</p>''',
      r'''var m=document.getElementById('m'), star=document.getElementById('star'), flash=document.getElementById('flash'), st=document.getElementById('st');
function render(){ var mass=+m.value/100;           // 太陽比
  if(mass<=1.4){ var r=80-(mass-0.2)/1.2*46;         // 重いほど小さく
    star.setAttribute('r',r); star.setAttribute('fill','#ffe066'); star.setAttribute('opacity',1);
    flash.setAttribute('opacity',0);
    st.className='status yes'; st.textContent='重さ '+mass.toFixed(2)+' 倍：電子の力で支えて安定（白色矮星）'; }
  else{ star.setAttribute('r',10); star.setAttribute('fill','#5c6470');
    flash.setAttribute('r',95); flash.setAttribute('opacity',0.5);
    st.className='status no'; st.textContent='重さ '+mass.toFixed(2)+' 倍：限界超え！ 支えきれず崩壊（→超新星・中性子星）'; }
}
m.addEventListener('input',render); render();''')

    # ===== 27 走査トンネル顕微鏡 1986 =====
    page("27_1986_stm.html", "matter", 1986,
      "原子を1個ずつ見る ── 走査トンネル顕微鏡",
      "ビニッヒ ／ ローラー ／ ルスカ（ドイツ・スイス）",
      "走査型トンネル顕微鏡の設計（ビニッヒ・ローラー）と、電子顕微鏡の基礎（ルスカ）に対して。",
      "原子は小さすぎて光では見えない",
      r'''<p>原子は光の波長よりずっと小さいので、どんなに良い光学顕微鏡でも<b>原子1個は見えません</b>。「原子を直接見たい」は科学者の長年の夢でした。</p>''',
      "しみ出す電流で表面をなぞる",
      r'''<p>ビニッヒとローラーは、とがった針を試料の表面に<b>触れるか触れないかの距離</b>まで近づけました。すると量子力学の効果で、すき間をこえて電子が<span class="term" data-tip="本来こえられないはずのすき間を、電子がすり抜ける量子力学の効果。距離がほんの少し変わるだけで大きく変化します。">トンネル</span>し、わずかな電流が流れます。この電流は距離にとても敏感なので、針で表面をなぞる（走査する）と<b>原子のデコボコが手に取るように分かり</b>、原子の地図が描けます。ついに人類は原子を“見た”のです。</p>''',
      r'''    <h2>やってみよう ── 針でなぞって原子を描く</h2>
    <div class="hint">スライダーで針を左右に動かします。原子の真上ほどトンネル電流が強くなり、下の線が原子のデコボコを描きます。</div>
    <div class="xbox">
      <svg id="sm" width="480" height="230" viewBox="0 0 480 230" role="img" aria-label="STM">
        <g id="atoms2"></g>
        <path id="tip" d="" fill="#e8edf3"/>
        <text x="20" y="205" fill="#8b93a7" font-size="11">電流の記録 →</text>
        <polyline id="scan" points="" fill="none" stroke="#66bb6a" stroke-width="2"/>
      </svg>
    </div>
    <div class="controls">
      <label for="x">針の位置</label>
      <input id="x" type="range" min="40" max="440" value="40">
      <div class="readout" id="msg"></div>
    </div>
    <div class="note">※ 電子が“しみ出す”トンネル電流は距離に超敏感。だから原子のデコボコが読み取れます。模式図です。</div>''',
      r'''<p>STMは原子を見るだけでなく、針で<b>原子を1個ずつ動かして並べる</b>ことさえできます（原子で文字を書いた例も）。ナノテクノロジーの扉を開き、半導体・新素材・分子機械の研究に不可欠な道具になりました。2010年のグラフェン（原子1枚のシート）など、その後のナノ科学の土台です。</p>''',
      r'''var svg=document.getElementById('sm'), atoms=document.getElementById('atoms2'),
    tip=document.getElementById('tip'), scan=document.getElementById('scan'),
    xr=document.getElementById('x'), msg=document.getElementById('msg');
var NS='http://www.w3.org/2000/svg', centers=[100,170,240,310,380], surfY=150;
centers.forEach(function(cx){var c=document.createElementNS(NS,'circle');
  c.setAttribute('cx',cx);c.setAttribute('cy',surfY);c.setAttribute('r',26);c.setAttribute('fill','#2b3b52');
  c.setAttribute('stroke','#3a4356');atoms.appendChild(c);});
function current(x){var s=0;centers.forEach(function(cx){s+=Math.exp(-((x-cx)*(x-cx))/700);});return Math.min(1,s);}
var trace=[];
function render(){ var x=+xr.value, cur=current(x);
  var ty=70 - cur*30;                              // 電流が強い（原子の上）ほど針が持ち上がる描画
  tip.setAttribute('d','M'+(x-8)+',30 L'+(x+8)+',30 L'+x+','+(ty+18)+' Z');
  trace.push([x, 200 - cur*34]);
  trace.sort(function(a,b){return a[0]-b[0];});
  scan.setAttribute('points', trace.map(function(p){return p[0]+','+p[1];}).join(' '));
  msg.innerHTML = cur>0.6?'原子の真上：トンネル電流<b>強い</b>':'原子のあいだ：電流<b>弱い</b>';
}
xr.addEventListener('input',render); render();''')

    # ===== 28 ニュートリノ 1988 =====
    page("28_1988_neutrino.html", "particle", 1988,
      "すべてを通り抜ける幽霊粒子 ── ニュートリノの研究",
      "レーダーマン ／ シュワルツ ／ シュタインバーガー（アメリカ）",
      "ニュートリノのビームを使った実験と、ニュートリノに複数の種類があることを示したことに対して。",
      "ほとんど何とも反応しない粒",
      r'''<p><span class="term" data-tip="電気を持たず質量もごくわずかな、非常に小さな粒。物質とめったに反応せず、地球さえ簡単に通り抜けます。">ニュートリノ</span>は、電気を持たず、他の粒とめったに反応しません。太陽から毎秒莫大な数が飛んできて、あなたの体も地球も<b>ほぼ素通り</b>していきます。あまりに反応しないので「幽霊粒子」とも呼ばれます。</p>''',
      "ニュートリノにも「種類」があった",
      r'''<p>3人は、加速器で<b>ニュートリノのビーム</b>を作る方法を編み出し、実験を行いました。その結果、ニュートリノには<b>1種類ではなく複数の“型”</b>があることを突きとめました（電子にともなうものと、ミューオンにともなうもの）。この「型（世代）」の考えは、その後の素粒子物理の基本設計図＝<b>標準模型</b>の重要な柱になりました。</p>''',
      r'''    <h2>やってみよう ── 分厚い壁もほとんど素通り</h2>
    <div class="hint">「大量に撃つ」を押すと、たくさんのニュートリノが検出器を通り抜けます。ごくまれに1個だけ反応（光る）します。</div>
    <div class="xbox">
      <svg id="nu" width="480" height="200" viewBox="0 0 480 200" role="img" aria-label="ニュートリノ">
        <rect x="180" y="30" width="120" height="140" rx="8" fill="#12233a" stroke="#2a3446"/>
        <text x="240" y="188" fill="#8b93a7" font-size="11" text-anchor="middle">検出器（分厚い物質）</text>
      </svg>
    </div>
    <div class="btns"><button id="shoot2">ニュートリノを大量に撃つ</button></div>
    <div class="readout" id="msg">通過：0　／　反応：0</div>
    <div class="note">※ ほとんどが素通りし、ごくまれにだけ反応します。だから観測にはとても大きな検出器が要ります（2002・2015年の項へ）。模式図です。</div>''',
      r'''<p>「ほとんど反応しない」ニュートリノを捕まえるため、巨大な地下検出器が作られました。日本の<b>カミオカンデ</b>は太陽や超新星からのニュートリノを観測し（2002年 小柴）、<b>スーパーカミオカンデ</b>はニュートリノに質量がある証拠をつかみました（2015年 梶田）。ニュートリノは宇宙と素粒子をつなぐ最前線です。</p>''',
      r'''var svg=document.getElementById('nu'), shoot=document.getElementById('shoot2'), msg=document.getElementById('msg');
var NS='http://www.w3.org/2000/svg', passed=0, hit=0, running=0;
function beam(){
  for(var k=0;k<24;k++){ (function(delay){ setTimeout(function(){
    var y=40+Math.random()*120;
    var c=document.createElementNS(NS,'circle');c.setAttribute('cx',10);c.setAttribute('cy',y);
    c.setAttribute('r',4);c.setAttribute('fill','#5eead4');svg.appendChild(c);
    var willHit=Math.random()<0.06, x=10;
    function step(){ x+=6; c.setAttribute('cx',x);
      if(willHit && x>=240){ c.setAttribute('r',10); c.setAttribute('fill','#ffd257'); hit++;
        update(); setTimeout(function(){c.remove();},400); return; }
      if(x>480){ c.remove(); passed++; update(); return; }
      requestAnimationFrame(step); }
    step();
  },delay); })(k*70); }
}
function update(){ msg.innerHTML='通過：<b>'+passed+'</b>　／　反応：<b>'+hit+'</b>（ほとんど素通り）'; }
shoot.addEventListener('click',beam);''')

    # ===== 29 小柴昌俊 2002 =====
    page("29_2002_koshiba.html", "cosmos", 2002,
      "ニュートリノで宇宙を見る ── ニュートリノ天文学の誕生",
      "小柴昌俊（日本） ／ デービス（アメリカ） ／ ジャコーニ（アメリカ）",
      "宇宙から来るニュートリノの検出（小柴・デービス）と、宇宙X線の研究（ジャコーニ）に対して。",
      "光では見えない宇宙の奥",
      r'''<p>星の内部や超新星爆発の中心は、光では見えません。しかし、そこからは<b>ほとんど何も通り抜ける</b>ニュートリノ（1988年の項）が飛び出してきます。これを捕まえられれば、光では見えない宇宙の奥をのぞけます。</p>''',
      "水の中の一瞬の光をとらえる",
      r'''<p>小柴は岐阜県の地下深くに大きな水タンク<span class="term" data-tip="小柴が建設した地下の巨大水タンク型ニュートリノ検出器。壁一面の光センサーで、水中の一瞬の光をとらえます。">カミオカンデ</span>を作りました。まれにニュートリノが水中の粒とぶつかると、<b>青白い一瞬の光</b>（チェレンコフ光）が輪のように広がります。1987年、彼らは<b>超新星爆発</b>からのニュートリノを世界で初めてとらえ、<span class="term" data-tip="光ではなくニュートリノを使って星や宇宙を観測する新しい天文学。小柴が開きました。">ニュートリノ天文学</span>という新しい窓を開きました。</p>''',
      r'''    <h2>やってみよう ── ニュートリノ天文台</h2>
    <div class="hint">「ニュートリノが来た」を押すと、まれに水中で反応が起き、壁のセンサーが輪の形に光ります。</div>
    <div class="xbox">
      <svg id="ko" width="380" height="240" viewBox="0 0 380 240" role="img" aria-label="カミオカンデ">
        <rect x="40" y="30" width="300" height="180" rx="10" fill="#0a2540" stroke="#2a3446"/>
        <g id="pmts"></g>
        <circle id="ev" cx="190" cy="120" r="0" fill="#7ec8ff" opacity="0"/>
      </svg>
    </div>
    <div class="btns"><button id="ntr">ニュートリノが来た</button></div>
    <div class="readout" id="msg">検出回数：0（めったに反応しません）</div>
    <div class="note">※ 何度も試すと、たまに反応してリング状の光が出ます。その光から、ニュートリノの来た方向まで分かります。模式図です。</div>''',
      r'''<p>ニュートリノ天文学は、太陽の内部や超新星、宇宙の成り立ちを直接調べる手段になりました。後継の<b>スーパーカミオカンデ</b>はニュートリノに質量がある証拠をつかみ（2015年 梶田）、いまも宇宙のなぞに挑んでいます。日本の“地下の巨大実験”が世界の宇宙物理を牽引しています。</p>''',
      r'''var svg=document.getElementById('ko'), pmts=document.getElementById('pmts'),
    ev=document.getElementById('ev'), ntr=document.getElementById('ntr'), msg=document.getElementById('msg');
var NS='http://www.w3.org/2000/svg', dots=[], cnt=0;
for(var gx=0;gx<10;gx++)for(var gy=0;gy<6;gy++){var x=60+gx*30, y=50+gy*30;
  var c=document.createElementNS(NS,'circle');c.setAttribute('cx',x);c.setAttribute('cy',y);
  c.setAttribute('r',6);c.setAttribute('fill','#16324f');pmts.appendChild(c);dots.push({el:c,x:x,y:y});}
function fire(){ var react=Math.random()<0.45;
  if(!react){ msg.innerHTML='検出回数：<b>'+cnt+'</b> ── 今のは素通り（反応なし）'; return; }
  cnt++; var ex=90+Math.random()*200, ey=70+Math.random()*100;
  ev.setAttribute('cx',ex); ev.setAttribute('cy',ey); ev.setAttribute('r',6); ev.setAttribute('opacity',1);
  var R=55;
  dots.forEach(function(d){ var dist=Math.hypot(d.x-ex,d.y-ey);
    if(Math.abs(dist-R)<16){ d.el.setAttribute('fill','#7ec8ff');
      setTimeout(function(){d.el.setAttribute('fill','#16324f');},700); } });
  setTimeout(function(){ev.setAttribute('opacity',0);},700);
  msg.innerHTML='検出回数：<b>'+cnt+'</b> ── <b>反応！</b> 青い光の輪が広がった';
}
ntr.addEventListener('click',fire);''')

    # ===== 30 南部・小林・益川 2008 =====
    page("30_2008_nambu.html", "particle", 2008,
      "対称性が自発的に破れる ── 物質が残った理由へ",
      "南部陽一郎（日本→アメリカ） ／ 小林誠 ／ 益川敏英（日本）",
      "自発的対称性の破れの発見（南部）と、クォークが3世代あることを予言した対称性の破れの研究（小林・益川）に対して。",
      "対称なはずなのに、かたよる",
      r'''<p>自然の法則は左右や向きについて<b>対称</b>にできています。それなのに現実の世界は、磁石にN極S極ができたり、宇宙に<b>物質だけ</b>が残ったりと、どこか<b>かたよって</b>います。なぜでしょう。</p>''',
      "出発点は対称でも、結果はかたよる",
      r'''<p>南部は「法則は対称でも、<b>安定した状態を選ぶときに対称性が自然に破れる</b>」という考え（<span class="term" data-tip="法則そのものは対称なのに、実際に落ち着く状態が対称でなくなること。磁石や、素粒子の質量の起源にも関わります。">自発的対称性の破れ</span>）を示しました。山の頂上（対称）のボールが、転がり落ちて<b>どれか1方向</b>に決まるイメージです。小林と益川は、粒と反粒子のわずかな性質の違い（<span class="term" data-tip="粒子と反粒子のふるまいがわずかに違うこと。宇宙に物質が残った理由に関わると考えられています。">CP対称性の破れ</span>）を説明するには<b>クォークが3世代（6種類）必要</b>だと予言し、のちに全種類が見つかりました。</p>''',
      r'''    <h2>やってみよう ── 対称な丘からボールが落ちる</h2>
    <div class="hint">「落とす」を押すと、てっぺん（対称な出発点）のボールがどれか1方向へ転がり落ちます。毎回向きが変わります。</div>
    <div class="xbox">
      <svg id="nb" width="360" height="240" viewBox="0 0 360 240" role="img" aria-label="自発的対称性の破れ">
        <ellipse cx="180" cy="150" rx="120" ry="46" fill="none" stroke="#2a3446" stroke-width="2"/>
        <circle cx="180" cy="150" r="4" fill="#3a4356"/>
        <text x="180" y="120" fill="#8b93a7" font-size="11" text-anchor="middle">対称な出発点（てっぺん）</text>
        <circle id="ball" cx="180" cy="150" r="12" fill="#5eead4"/>
      </svg>
    </div>
    <div class="btns"><button id="drop">落とす</button><button id="rs">もどす</button></div>
    <div class="readout" id="msg">ボタンで転がしてみましょう</div>
    <div class="note">※ 法則（丘の形）は完全に対称でも、落ち着く先は1方向にかたよります。これが対称性の破れ。模式図です。</div>''',
      r'''<p>自発的対称性の破れは、素粒子が質量を持つしくみ（<b>ヒッグス機構</b>・2013年の項）の核心でもあります。小林・益川の理論は、日本の加速器実験<b>Belle</b>などで確かめられました。宇宙になぜ物質だけが残り、私たちが存在できるのか――その根本にかかわる研究です。</p>''',
      r'''var ball=document.getElementById('ball'), drop=document.getElementById('drop'),
    rs=document.getElementById('rs'), msg=document.getElementById('msg');
var anim=null;
function roll(){ if(anim)cancelAnimationFrame(anim);
  var a=Math.random()*6.28, tx=180+120*Math.cos(a), ty=150+46*Math.sin(a), t=0;
  msg.innerHTML='転がり落ちて…';
  function step(){ t+=0.05; if(t>1)t=1;
    ball.setAttribute('cx',180+(tx-180)*t); ball.setAttribute('cy',150+(ty-150)*t);
    if(t<1)anim=requestAnimationFrame(step);
    else msg.innerHTML='<b>1方向に決まった！</b>（対称な出発点なのに結果はかたよる）'; }
  step();
}
rs.addEventListener('click',function(){if(anim)cancelAnimationFrame(anim);ball.setAttribute('cx',180);ball.setAttribute('cy',150);msg.innerHTML='てっぺんにもどしました';});
drop.addEventListener('click',roll);''')

    # ===== 31 光ファイバー 2009 =====
    page("31_2009_fiber.html", "matter", 2009,
      "光で情報を運ぶ ── 光ファイバー通信",
      "高錕（チャールズ・カオ） ／ ボイル ／ スミス（イギリス・アメリカ）",
      "光ファイバーによる光通信の画期的な業績（カオ）と、画像センサーCCDの発明（ボイル・スミス）に対して。",
      "電気の信号は遠くで弱ってしまう",
      r'''<p>電話やデータを<b>電気の信号</b>で送ると、遠くへ行くほど弱ってしまいます。もっと大量の情報を、遠くまで、速く送る方法として<b>光</b>が注目されましたが、当時のガラスは光をすぐ吸収してしまい、使いものになりませんでした。</p>''',
      "超すきとおったガラスの糸を光が走る",
      r'''<p>カオは「ガラスの<b>不純物さえ取り除けば</b>、光は何kmも通る」と見抜き、超高純度ガラスの<span class="term" data-tip="髪の毛ほどの細さの超高純度ガラスの糸。光を閉じこめて遠くまで運びます。インターネットの大動脈です。">光ファイバー</span>を実現しました。光はガラスのかべで<span class="term" data-tip="光がガラスと外の境目で全部はね返る現象。おかげで光はもれずにファイバーの中を進み続けます。">全反射</span>をくり返し、もれずに進みます。1本の細い糸に、膨大な情報を光の点滅で乗せて送れるのです。</p>''',
      r'''    <h2>やってみよう ── ガラスの糸を光が走る</h2>
    <div class="hint">スライダーでガラスの純度を上げると、光は弱らずに遠くの受信機まで届きます。純度が低いと途中で消えます。</div>
    <div class="xbox">
      <svg id="fb" width="480" height="150" viewBox="0 0 480 150" role="img" aria-label="光ファイバー">
        <rect x="20" y="55" width="410" height="40" rx="20" fill="#0b1a2a" stroke="#2a3446"/>
        <path id="ray" d="" fill="none" stroke="#ffe066" stroke-width="3"/>
        <circle id="rx" cx="445" cy="75" r="14" fill="#26343f"/>
        <text x="445" y="118" fill="#8b93a7" font-size="11" text-anchor="middle">受信機</text>
      </svg>
    </div>
    <div class="controls">
      <label for="pur">ガラスの純度</label>
      <input id="pur" type="range" min="0" max="100" value="30">
      <div class="status no" id="st"></div>
    </div>
    <div class="note">※ 光はガラスのかべで全反射をくり返して進みます。純度が高いほど遠くまで届く＝大容量の光通信。模式図です。</div>''',
      r'''<p>光ファイバーは、いまや世界中を結ぶ<b>インターネットの大動脈</b>です。海底ケーブルで大陸をつなぎ、動画も通話もこの細いガラスの糸を走る光が運んでいます。同時に受賞したCCDは<b>デジタルカメラの目</b>となり、スマホやハッブル宇宙望遠鏡の撮影を可能にしました。現代の情報社会そのものを支える発明です。</p>''',
      r'''var pur=document.getElementById('pur'), ray=document.getElementById('ray'),
    rx=document.getElementById('rx'), st=document.getElementById('st');
function render(){ var p=+pur.value/100;
  var reach=20+p*425;                              // 純度が高いほど遠くまで
  var d='M20,75', x=20, up=true;
  while(x<reach){ x+=34; up=!up; d+=' L'+Math.min(x,reach)+','+(up?60:90); }
  ray.setAttribute('d',d);
  ray.setAttribute('opacity',(0.35+0.65*p).toFixed(2));
  var ok=reach>=430;
  rx.setAttribute('fill', ok?'#ffe066':'#26343f');
  if(ok){st.className='status yes';st.textContent='高純度：光が受信機まで届いた！ 情報が伝わる';}
  else{st.className='status no';st.textContent='純度が低い：光が途中で消えて届かない';}
}
pur.addEventListener('input',render); render();''')

    # ===== 32 グラフェン 2010 =====
    page("32_2010_graphene.html", "matter", 2010,
      "原子1枚のふしぎなシート ── グラフェン",
      "ガイム ／ ノボセロフ（オランダ・イギリス）",
      "二次元の物質グラフェン（炭素原子1枚のシート）に関する画期的な実験に対して。",
      "鉛筆の芯にひそんでいた素材",
      r'''<p>鉛筆の芯（黒鉛）は、炭素原子のシートが何層も重なったものです。もしこれを<b>たった1枚だけ</b>はがせたら――そんな究極に薄い物質は「理論上は存在できない」とさえ言われていました。</p>''',
      "セロテープではがして生まれた二次元物質",
      r'''<p>2人は、なんと<b>セロハンテープで黒鉛を何度もはがす</b>という素朴な方法で、炭素原子<b>1枚ぶんの厚さ</b>のシート＝<span class="term" data-tip="炭素原子が六角形（ハチの巣状）に並んだ、厚さ原子1個ぶんのシート。世界一薄いのに非常に強く、電気をよく通します。">グラフェン</span>を取り出しました。厚さは原子1個ぶんなのに、<b>鋼鉄より強く、銅より電気をよく通し、透明でよく曲がる</b>という夢のような性質を持っていました。</p>''',
      r'''    <h2>やってみよう ── 何層？ 1枚にすると…</h2>
    <div class="hint">スライダーで層の数を減らしていきます。1枚になったとき、それが「グラフェン」です。</div>
    <div class="xbox">
      <svg id="gr" width="420" height="230" viewBox="0 0 420 230" role="img" aria-label="グラフェン"></svg>
    </div>
    <div class="controls">
      <label for="ly">層の数</label>
      <input id="ly" type="range" min="1" max="6" value="6">
      <div class="status no" id="st"></div>
    </div>
    <div class="note">※ 何層も重なると「黒鉛（鉛筆の芯）」、1枚だけだと「グラフェン」。同じ炭素でも1枚にすると性質が一変します。模式図です。</div>''',
      r'''<p>グラフェンは、折り曲げられる<b>画面やセンサー</b>、超高速の<b>電子部品</b>、軽くて強い<b>複合材料</b>、水をきれいにする<b>フィルター</b>など、幅広い応用が期待されています。「二次元物質」という新分野を切り開き、原子1枚の世界を舞台にした材料研究が世界中で進んでいます。</p>''',
      r'''var svg=document.getElementById('gr'), ly=document.getElementById('ly'), st=document.getElementById('st');
var NS='http://www.w3.org/2000/svg';
function sheet(y,hi){ var g=document.createElementNS(NS,'g');
  for(var i=0;i<7;i++){ var cx=50+i*52;
    var p=document.createElementNS(NS,'polygon');
    var pts=[]; for(var k=0;k<6;k++){var a=Math.PI/6+k*Math.PI/3; pts.push((cx+22*Math.cos(a)).toFixed(1)+','+(y+12*Math.sin(a)).toFixed(1));}
    p.setAttribute('points',pts.join(' ')); p.setAttribute('fill','none');
    p.setAttribute('stroke',hi?'#66bb6a':'#4b5b70'); p.setAttribute('stroke-width',hi?'2.5':'1.5'); g.appendChild(p);
  } return g;
}
function render(){ svg.innerHTML=''; var n=+ly.value;
  for(var L=0;L<n;L++){ var y=60+L*30, hi=(n===1); svg.appendChild(sheet(y,hi)); }
  if(n===1){st.className='status yes';st.textContent='原子1枚 ＝ グラフェン！ 鋼鉄より強く電気をよく通す';}
  else{st.className='status no';st.textContent=n+'層：まだ黒鉛（鉛筆の芯）のなかま';}
}
ly.addEventListener('input',render); render();''')

    # ===== 33 加速膨張 2011 =====
    page("33_2011_dark_energy.html", "cosmos", 2011,
      "宇宙は加速して広がっている ── ダークエネルギー",
      "パールマッター ／ シュミット ／ リース（アメリカ・オーストラリア）",
      "遠くの超新星の観測から、宇宙の膨張が加速していることを発見したことに対して。",
      "膨張はやがて遅くなるはずだった",
      r'''<p>宇宙がビッグバン以来ふくらみ続けているのは分かっていました。物どうしは重力で引き合うので、膨張は<b>だんだん遅くなる</b>はず――誰もがそう思っていました。問題は「どれくらい遅くなるか」を測ることでした。</p>''',
      "遠くの星の明るさが告げた意外な真実",
      r'''<p>研究チームは、決まった明るさで爆発する<span class="term" data-tip="いつもほぼ同じ明るさで爆発する星。見かけの明るさから距離が分かるので、宇宙の“ものさし”になります。">Ia型超新星</span>を宇宙の“ものさし”にして、遠くの宇宙の膨張を測りました。すると予想に反し、膨張は<b>加速していた</b>のです。宇宙を押し広げる正体不明のエネルギー＝<span class="term" data-tip="宇宙を加速膨張させていると考えられる正体不明のエネルギー。宇宙の約7割を占めるとされます。">ダークエネルギー</span>が、宇宙の約7割を占めていることになります。</p>''',
      r'''    <h2>やってみよう ── 広がる宇宙</h2>
    <div class="hint">「時間を進める」を押すと銀河どうしが離れていきます。しかも、離れる速さがどんどん増していきます（加速）。</div>
    <div class="xbox">
      <svg id="de" width="300" height="240" viewBox="0 0 300 240" role="img" aria-label="加速膨張"></svg>
    </div>
    <div class="btns"><button id="play">時間を進める</button><button id="rs3">最初にもどす</button></div>
    <div class="readout" id="msg">銀河どうしの間隔：×1.0</div>
    <div class="note">※ 重力だけなら膨張は減速するはず。実際は加速――だから未知のエネルギーがあると考えます。模式図です。</div>''',
      r'''<p>ダークエネルギーの発見は、宇宙の中身のほとんどが<b>正体不明</b>（ダークエネルギー約7割＋ダークマター約2割半）だという衝撃をもたらしました。宇宙の未来（永遠に薄まっていく？）を左右する大問題であり、その正体解明は現代物理学・宇宙論の最大の謎のひとつです。</p>''',
      r'''var svg=document.getElementById('de'), play=document.getElementById('play'),
    rs3=document.getElementById('rs3'), msg=document.getElementById('msg');
var NS='http://www.w3.org/2000/svg', gal=[], t=0, running=false;
for(var i=0;i<7;i++){ var a=Math.random()*6.28, r=20+Math.random()*90;
  var g=document.createElementNS(NS,'circle'); g.setAttribute('r',5+Math.random()*4);
  g.setAttribute('fill','#5c9dff'); svg.appendChild(g);
  gal.push({el:g, dx:Math.cos(a)*r, dy:Math.sin(a)*r}); }
function place(scale){ gal.forEach(function(gg){ gg.el.setAttribute('cx',150+gg.dx*scale); gg.el.setAttribute('cy',120+gg.dy*scale); }); }
function frame(){ if(!running)return; t+=0.02; var scale=1+0.3*t+0.25*t*t;   // 加速
  place(scale); msg.innerHTML='銀河どうしの間隔：×<b>'+scale.toFixed(2)+'</b>（速さが増していく）';
  if(scale<2.6)requestAnimationFrame(frame); else running=false;
}
play.addEventListener('click',function(){ if(!running){running=true;frame();} });
rs3.addEventListener('click',function(){ running=false;t=0;place(1);msg.innerHTML='銀河どうしの間隔：×1.0'; });
place(1);''')

    # ===== 34 ヒッグス 2013 =====
    page("34_2013_higgs.html", "particle", 2013,
      "質量はどこから来るのか ── ヒッグス機構",
      "アングレール ／ ヒッグス（ベルギー・イギリス）",
      "素粒子が質量を持つしくみ（ヒッグス機構）の理論的な発見に対して。のちにその粒子が実験で確認された。",
      "そもそも「重さ」はなぜあるのか",
      r'''<p>物に重さ（質量）があるのは当たり前に思えます。でも素粒子のレベルでは、「なぜ質量があるのか」はまったく自明ではありませんでした。理論をきれいに作ると、素粒子はどれも<b>質量ゼロ</b>になってしまうのです。</p>''',
      "宇宙を満たす“場”との抵抗が質量になる",
      r'''<p>アングレールとヒッグスは、宇宙全体が目に見えない<span class="term" data-tip="宇宙のどこにでもある見えない場。素粒子はこれとの結びつきの強さに応じて“動きにくさ＝質量”を得ます。">ヒッグス場</span>で満たされていると考えました。素粒子はこの場の中を進むとき、<b>結びつきが強いものほど動きにくくなり</b>、それが<b>質量</b>として現れます。人ごみをかき分けて進む有名人ほど動きにくい、というイメージ。光子は場と結びつかないので質量ゼロで光速です。2012年、その証拠となる<span class="term" data-tip="ヒッグス場のさざ波にあたる粒子。2012年に巨大加速器LHCで見つかり、理論が裏づけられました。">ヒッグス粒子</span>が発見されました。</p>''',
      r'''    <h2>やってみよう ── 場との結びつきが重さになる</h2>
    <div class="hint">スライダーで「ヒッグス場との結びつき」を強くすると、粒子のまわりに場がまとわりつき、動きが重く（遅く）なります。</div>
    <div class="xbox">
      <svg id="hg" width="480" height="160" viewBox="0 0 480 160" role="img" aria-label="ヒッグス機構"></svg>
    </div>
    <div class="controls">
      <label for="cp">ヒッグス場との結びつき</label>
      <input id="cp" type="range" min="0" max="100" value="0">
      <div class="readout" id="msg"></div>
    </div>
    <div class="note">※ 結びつきが強いほど“動きにくさ＝質量”が大きい。光子は結びつかないので質量ゼロ。人ごみをかき分ける有名人のイメージ。模式図です。</div>''',
      r'''<p>ヒッグス機構は、電弱統一理論（1979年の項）を完成させ、素粒子物理の<b>標準模型</b>の最後のピースでした。ヒッグス粒子の発見は、この描像が正しいことの決定的な証拠です。「なぜ物には重さがあるのか」という素朴で根本的な問いに、物理学が出したひとつの答えです。</p>''',
      r'''var svg=document.getElementById('hg'), cp=document.getElementById('cp'), msg=document.getElementById('msg');
var NS='http://www.w3.org/2000/svg', field=[];
for(var i=0;i<48;i++){var d=document.createElementNS(NS,'circle');
  d.setAttribute('cx',20+Math.random()*440);d.setAttribute('cy',20+Math.random()*120);
  d.setAttribute('r',2.5);d.setAttribute('fill','#3a2f66');svg.appendChild(d);field.push(d);}
var part=document.createElementNS(NS,'circle');part.setAttribute('r',12);part.setAttribute('fill','#b388ff');svg.appendChild(part);
var x=20;
function frame(){ var c=+cp.value/100; var v=3.2/(1+c*6); x+=v; if(x>470)x=20;
  part.setAttribute('cx',x); part.setAttribute('cy',80);
  field.forEach(function(d){ var dx=+d.getAttribute('cx')-x, dy=+d.getAttribute('cy')-80;
    var near=Math.hypot(dx,dy)<22+c*20; d.setAttribute('fill', near&&c>0.05?'#ffd257':'#3a2f66'); });
  msg.innerHTML = c<0.05?'結びつきゼロ：<b>質量ゼロ</b>で光速（光子のイメージ）':'結びつき'+(c<0.6?'中':'強')+'：<b>重く</b>なってゆっくり（質量大）';
  requestAnimationFrame(frame);
}
frame();''')

    # ===== 35 青色LED 2014 =====
    page("35_2014_blue_led.html", "matter", 2014,
      "青い光で白色照明を完成 ── 青色発光ダイオード",
      "赤﨑勇 ／ 天野浩 ／ 中村修二（日本）",
      "明るく省エネな白色光源を可能にした、青色発光ダイオード（LED）の発明に対して。",
      "赤と緑はできたのに、青だけが作れない",
      r'''<p>電気を光に変える<span class="term" data-tip="電気を流すと光る半導体。電球より圧倒的に省エネで長持ちします。">LED（発光ダイオード）</span>は、赤と緑は早くから作れていました。しかし<b>青色</b >だけは、材料づくりがとても難しく、世界中の研究者が数十年も挑んで失敗し続けていました。光の三原色（赤・緑・青）がそろわないと<b>白い光</b>が作れません。</p>''',
      "困難な結晶づくりを日本の研究者が突破",
      r'''<p>赤﨑・天野は<span class="term" data-tip="青色LEDの材料となる半導体の結晶。きれいに作るのが非常に難しく、長く実現できませんでした。">窒化ガリウム（GaN）</span>の良質な結晶を作る方法を切り開き、中村は明るく光らせて量産する道を拓きました。ついに<b>青色LED</b>が完成。赤・緑・青がそろい、<b>省エネな白色LED照明</b>が実現しました。</p>''',
      r'''    <h2>やってみよう ── 光の三原色で白をつくる</h2>
    <div class="hint">赤・緑・青のスライダーを動かして光を混ぜます。青を消すと、どうやっても白い光が作れないことを確かめて。</div>
    <div class="xbox">
      <svg id="rgb" width="360" height="200" viewBox="0 0 360 200" role="img" aria-label="光の三原色">
        <circle id="mix" cx="180" cy="100" r="70" fill="#000"/>
        <circle cx="180" cy="100" r="70" fill="none" stroke="#2a3446"/>
      </svg>
    </div>
    <div class="controls">
      <label for="rr">赤</label><input id="rr" type="range" min="0" max="255" value="255">
      <label for="gg">緑</label><input id="gg" type="range" min="0" max="255" value="255">
      <label for="bb">青</label><input id="bb" type="range" min="0" max="255" value="0">
      <div class="status no" id="st"></div>
    </div>
    <div class="note">※ 光の三原色は赤・緑・青。3つそろって初めて白になります。青が最後まで作れなかったのです。模式図です。</div>''',
      r'''<p>白色LEDは、白熱電球の何分の一もの電気で同じ明るさを出し、寿命も長いため、世界中の照明を置きかえて<b>大きな省エネ</b>をもたらしました。スマホやテレビの画面、信号機、植物工場の照明まで、青色LEDなしの現代生活は考えられません。日本発の発明が世界を明るくしました。</p>''',
      r'''var rr=document.getElementById('rr'), gg=document.getElementById('gg'), bb=document.getElementById('bb'),
    mix=document.getElementById('mix'), st=document.getElementById('st');
function render(){ var r=+rr.value, g=+gg.value, b=+bb.value;
  mix.setAttribute('fill','rgb('+r+','+g+','+b+')');
  if(r>200&&g>200&&b>200){st.className='status yes';st.textContent='白色！ 赤・緑・青がそろって白色照明ができた';}
  else if(b<40){st.className='status no';st.textContent='青がないと…どうやっても白い光にならない';}
  else{st.className='status';st.style.background='#fff7e6';st.style.color='#8a5a00';st.textContent='混色中（3色をそろえてみよう）';}
}
[rr,gg,bb].forEach(function(s){s.addEventListener('input',render);}); render();''')

    # ===== 36 梶田隆章 2015 =====
    page("36_2015_kajita.html", "cosmos", 2015,
      "ニュートリノは姿を変える ── ニュートリノ振動",
      "梶田隆章（日本） ／ マクドナルド（カナダ）",
      "ニュートリノが種類を変える現象（ニュートリノ振動）の発見と、それが示すニュートリノの質量に対して。",
      "ニュートリノは質量ゼロと思われていた",
      r'''<p>ニュートリノ（1988年の項）には3つの型があります。長いあいだ、ニュートリノは<b>質量ゼロ</b>（重さがない）と考えられていました。ところが、宇宙から降ってくるニュートリノの数を数えると、なぜか計算より<b>足りない</b>のです。</p>''',
      "飛ぶうちに“型”が入れかわっていた",
      r'''<p>梶田はスーパーカミオカンデで、ニュートリノが飛んでいるあいだに<b>別の型へと姿を変えている</b>ことを突きとめました（<span class="term" data-tip="ニュートリノが飛ぶうちに、電子型・ミュー型・タウ型のあいだで種類を変える現象。質量がないと起こりません。">ニュートリノ振動</span>）。数が足りなく見えたのは、途中で観測しにくい型に変わっていたから。そして<b>姿を変えられるのは、ニュートリノにわずかでも質量があるから</b>――「質量ゼロ」という常識がくつがえりました。</p>''',
      r'''    <h2>やってみよう ── 飛ぶうちに型が変わる</h2>
    <div class="hint">スライダーで飛んだ距離を変えます。ニュートリノの型（色）が、行くほどに入れかわっていきます。</div>
    <div class="xbox">
      <svg id="ko2" width="480" height="150" viewBox="0 0 480 150" role="img" aria-label="ニュートリノ振動">
        <line x1="30" y1="75" x2="450" y2="75" stroke="#2a3446" stroke-dasharray="4 4"/>
        <circle id="nv" cx="30" cy="75" r="14"/>
        <text x="30" y="40" fill="#8b93a7" font-size="11" text-anchor="middle">発生</text>
        <text x="450" y="40" fill="#8b93a7" font-size="11" text-anchor="middle">検出</text>
      </svg>
    </div>
    <div class="controls">
      <label for="dist">飛んだ距離</label>
      <input id="dist" type="range" min="0" max="100" value="0">
      <div class="readout" id="msg"></div>
    </div>
    <div class="note">※ 型が入れかわるのは、ニュートリノに質量がある証拠。距離によって見つかる型の割合が変わります。模式図です。</div>''',
      r'''<p>ニュートリノに質量があるという発見は、素粒子の<b>標準模型を超える</b>新しい物理への入り口です。ニュートリノは宇宙にあふれており、その性質は宇宙に物質が残った謎（2008年の項）にも関わるかもしれません。日本の巨大地下実験が、またも世界の物理を書きかえました。</p>''',
      r'''var dist=document.getElementById('dist'), nv=document.getElementById('nv'), msg=document.getElementById('msg');
function render(){ var d=+dist.value; var x=30+d/100*420; nv.setAttribute('cx',x);
  var ph=d/100*Math.PI*2.2;
  var pMu=Math.cos(ph)*Math.cos(ph);               // ミュー型の割合
  var col = pMu>0.5 ? '#5c9dff' : '#b388ff';
  nv.setAttribute('fill',col);
  msg.innerHTML='今のすがた：<b>'+(pMu>0.66?'ミュー型':pMu<0.34?'タウ型':'混ざった状態')+'</b>（ミュー型 '+Math.round(pMu*100)+'%）';
}
dist.addEventListener('input',render); render();''')

    # ===== 37 トポロジカル相 2016 =====
    page("37_2016_topology.html", "matter", 2016,
      "形のもつ“ゆるがない性質” ── トポロジカル相",
      "サウレス ／ ホールデン ／ コスタリッツ（イギリス→アメリカ）",
      "物質のトポロジカルな相と、その相転移についての理論的な発見に対して。",
      "少し曲げても変わらない性質がある",
      r'''<p>コップとドーナツは形が違いますが、粘土なら<b>穴を1つ持つ仲間</b>として連続的に作り変えられます。この「<span class="term" data-tip="連続的に変形しても変わらない性質を調べる数学。穴の数などがその代表です。">トポロジー</span>（位相幾何）」では、<b>穴の数</b>のように、少しくらい曲げても伸ばしても<b>変わらない（整数の）性質</b>があります。</p>''',
      "物質の性質にも“穴の数”のような整数がある",
      r'''<p>3人は、この考えを物質の中の電子に当てはめました。ある種の物質では、電気の通り方などの性質が<b>ぴたりと整数の段</b>でしか変わらず、少々の乱れや不純物があっても<b>びくともしない</b>ことを説明しました（<span class="term" data-tip="物質の状態を、トポロジーの整数で分類したもの。乱れに強い性質を生みます。">トポロジカル相</span>）。形の“穴の数”のように、物質の状態にも変わりにくい整数がひそんでいたのです。</p>''',
      r'''    <h2>やってみよう ── 変形しても穴の数は整数のまま</h2>
    <div class="hint">スライダーで形を変形しても、穴の数（＝性質を決める整数）は変わりません。ボタンで穴の数を変えると、性質が“段”で飛びます。</div>
    <div class="xbox">
      <svg id="tp" width="360" height="200" viewBox="0 0 360 200" role="img" aria-label="トポロジー">
        <ellipse id="body" cx="180" cy="100" rx="120" ry="60" fill="#2b3b52" stroke="#4b5b70"/>
        <g id="holes"></g>
      </svg>
    </div>
    <div class="controls">
      <label for="def">形を変形する</label>
      <input id="def" type="range" min="40" max="150" value="120">
      <div class="btns"><button data-h="0">穴0</button><button data-h="1" class="on">穴1</button><button data-h="2">穴2</button></div>
      <div class="readout" id="msg"></div>
    </div>
    <div class="note">※ 連続変形では穴の数（整数）は変わらない＝性質が乱れに強い。だから量子ホール効果の伝導度はきっちり整数段になります。模式図です。</div>''',
      r'''<p>トポロジーで守られた性質は<b>乱れに強い</b>ため、正確な電気抵抗の標準や、エラーに強い<b>量子コンピュータ</b>の候補として注目されています。「トポロジカル物質」は物性物理の一大分野になり、新しい電子材料の探索が世界中で進んでいます。</p>''',
      r'''var body=document.getElementById('body'), holes=document.getElementById('holes'),
    def=document.getElementById('def'), msg=document.getElementById('msg');
var NS='http://www.w3.org/2000/svg', nHole=1;
function draw(){ body.setAttribute('rx',def.value);
  holes.innerHTML=''; var rx=+def.value;
  for(var i=0;i<nHole;i++){ var cx=180+(i-(nHole-1)/2)*Math.min(70,rx*0.5);
    var h=document.createElementNS(NS,'ellipse'); h.setAttribute('cx',cx); h.setAttribute('cy',100);
    h.setAttribute('rx',18); h.setAttribute('ry',16); h.setAttribute('fill','#f5f4ef'); holes.appendChild(h); }
  msg.innerHTML='穴の数 = <b>'+nHole+'</b> → 性質（伝導度）= '+nHole+' × 基本値（きっちり整数）';
}
def.addEventListener('input',draw);
document.querySelectorAll('.btns button').forEach(function(b){b.addEventListener('click',function(){
  nHole=+b.dataset.h; document.querySelectorAll('.btns button').forEach(function(x){x.classList.toggle('on',x===b);}); draw();});});
draw();''')

    # ===== 38 重力波 2017 =====
    page("38_2017_ligo.html", "cosmos", 2017,
      "時空のさざ波をとらえる ── 重力波の直接観測",
      "ワイス ／ バリッシュ ／ ソーン（アメリカ）",
      "重力波を検出した観測装置LIGOへの決定的な貢献と、重力波の観測に対して。",
      "アインシュタインが予言した“時空のゆれ”",
      r'''<p>アインシュタインは、重い物が激しく動くと<b>時空そのものがゆれ、さざ波のように広がる</b>と予言していました（<span class="term" data-tip="重い天体が動くときに生じる時空のゆがみの波。空間そのものが伸び縮みします。">重力波</span>）。しかしそのゆれはあまりに小さく、100年間だれも直接とらえられませんでした。</p>''',
      "ブラックホール合体のゆれを検出",
      r'''<p>2015年、LIGO は<b>2つのブラックホールが合体</b>した瞬間の重力波をとらえました。重力波が通ると、空間が<b>片方向に伸び、直角方向に縮む</b>のを交互にくり返します。その伸び縮みは<b>陽子より小さい</b>ほどですが、巨大な<span class="term" data-tip="マイケルソン（1907年の項）と同じしくみの装置を数kmに巨大化したもの。腕の長さの超微小な変化を光でとらえます。">干渉計</span>で検出しました。目に見えない宇宙を“ゆれ”で聴く、新しい天文学の始まりです。</p>''',
      r'''    <h2>やってみよう ── 重力波が通ると空間が伸び縮み</h2>
    <div class="hint">「重力波が来た」を押すと、輪に並んだ点が、たてよこ交互に伸び縮みします（空間そのもののゆれ）。</div>
    <div class="xbox">
      <svg id="gw" width="300" height="240" viewBox="0 0 300 240" role="img" aria-label="重力波">
        <circle cx="150" cy="120" r="80" fill="none" stroke="#2a3446" stroke-dasharray="3 4"/>
        <g id="ring"></g>
      </svg>
    </div>
    <div class="btns"><button id="wave">重力波が来た</button><button id="stopw">止める</button></div>
    <div class="readout" id="msg">静かな時空（ゆれなし）</div>
    <div class="note">※ 重力波は空間を「たて伸び・よこ縮み」→「たて縮み・よこ伸び」と交互にゆらします。実際の伸び縮みは原子より小さい。模式図です。</div>''',
      r'''<p>重力波の観測は、光では見えないブラックホールや中性子星の合体を“聴く”手段になりました。以来、多数の合体が観測され、宇宙のなりたちを探る新しい窓が開きました。数kmの巨大干渉計は、1907年のマイケルソンの発想が現代の宇宙物理へと実を結んだ姿でもあります。</p>''',
      r'''var svg=document.getElementById('gw'), ring=document.getElementById('ring'),
    wave=document.getElementById('wave'), stopw=document.getElementById('stopw'), msg=document.getElementById('msg');
var NS='http://www.w3.org/2000/svg', pts=[], running=false, t=0;
for(var i=0;i<12;i++){var a=i/12*6.283; var c=document.createElementNS(NS,'circle');
  c.setAttribute('r',6);c.setAttribute('fill','#5c9dff');ring.appendChild(c);pts.push({a:a,el:c});}
function place(sx,sy){ pts.forEach(function(p){ p.el.setAttribute('cx',150+80*sx*Math.cos(p.a));
  p.el.setAttribute('cy',120+80*sy*Math.sin(p.a)); }); }
function frame(){ if(!running)return; t+=0.12; var A=0.28*Math.sin(t);
  place(1+A,1-A); msg.innerHTML='<b>重力波が通過中</b>：空間がたて・よこ交互に伸び縮み';
  requestAnimationFrame(frame);
}
wave.addEventListener('click',function(){ if(!running){running=true;frame();} });
stopw.addEventListener('click',function(){ running=false;place(1,1);msg.innerHTML='静かな時空（ゆれなし）'; });
place(1,1);''')

    # ===== 39 レーザー技術 2018 =====
    page("39_2018_laser_tools.html", "matter", 2018,
      "光でモノをつまみ、光を極限まで強くする ── レーザー技術",
      "アシュキン ／ ムル ／ ストリックランド（アメリカ・フランス・カナダ）",
      "光ピンセットの発明（アシュキン）と、極めて短く強いレーザーパルスを作る手法（ムル・ストリックランド）に対して。",
      "光に“力”を持たせる",
      r'''<p>光は物にぶつかると、ごくわずかに<b>押す力</b>を持っています。ふだんは弱すぎて気づきませんが、レーザーで1点に集めれば、この力を道具として使えるのでは――そんな発想から新しい技術が生まれました。</p>''',
      "光のピンセットと、極限の光パルス",
      r'''<p>アシュキンは、強く絞ったレーザーの光で<b>細胞やウイルスを傷つけずにつまんで動かす</b><span class="term" data-tip="強く集めたレーザー光で、細胞や微粒子をつまんで自在に動かす技術。生物研究の必需品です。">光ピンセット</span>を発明しました。いっぽうムルとストリックランドは、レーザーのパルスをいったん引きのばして増幅し、また圧縮する巧妙な方法（<span class="term" data-tip="短いレーザーパルスを一度引きのばして安全に増幅し、再び圧縮して超高強度にする手法。近視の手術などに使われます。">チャープパルス増幅</span>）で、<b>極端に短く強い光</b>を作り出しました。</p>''',
      r'''    <h2>やってみよう ── 光ピンセットで粒をつまむ</h2>
    <div class="hint">スライダーでレーザーの焦点を動かすと、つままれた粒が光についてきます。光がモノをつかんでいます。</div>
    <div class="xbox">
      <svg id="tw" width="440" height="180" viewBox="0 0 440 180" role="img" aria-label="光ピンセット">
        <polygon id="beam" points="" fill="#ffe066" opacity="0.35"/>
        <circle id="bead" cx="220" cy="120" r="13" fill="#7ec8ff"/>
        <text x="220" y="20" fill="#8b93a7" font-size="11" text-anchor="middle">レーザー</text>
      </svg>
    </div>
    <div class="controls">
      <label for="fx">レーザーの焦点の位置</label>
      <input id="fx" type="range" min="40" max="400" value="220">
      <div class="readout" id="msg">光の焦点に粒がとらえられています</div>
    </div>
    <div class="note">※ 強く集めた光は、微小な粒を“つまむ”力を持ちます。粒は焦点についてきます。模式図です。</div>''',
      r'''<p>光ピンセットは、<b>細胞やDNA、細菌を1個ずつ操る</b>生命科学の必需品になりました。チャープパルス増幅は、<b>近視のレーザー手術</b>や精密な金属加工、さらに2023年のアト秒物理（次の時代の光）へとつながります。光は「照らす」だけでなく「操る道具」になったのです。</p>''',
      r'''var fx=document.getElementById('fx'), beam=document.getElementById('beam'), bead=document.getElementById('bead'), msg=document.getElementById('msg');
var bx=220;
function frame(){ var f=+fx.value; bx+=(f-bx)*0.12;
  beam.setAttribute('points',(f-40)+',0 '+(f+40)+',0 '+(f+4)+',120 '+(f-4)+',120');
  bead.setAttribute('cx',bx);
  msg.innerHTML = Math.abs(f-bx)>6?'粒が光の焦点に引かれて移動中…':'粒は光にしっかりつままれています';
  requestAnimationFrame(frame);
}
frame();''')

    # ===== 40 系外惑星 2019 =====
    page("40_2019_exoplanet.html", "cosmos", 2019,
      "太陽系の外にも惑星があった ── 系外惑星の発見",
      "ピーブルス ／ マイヨール ／ ケロー（アメリカ・スイス）",
      "宇宙論への理論的貢献（ピーブルス）と、太陽に似た星をまわる系外惑星の初発見（マイヨール・ケロー）に対して。",
      "惑星は遠すぎて直接は見えない",
      r'''<p>ほかの星をまわる惑星（<span class="term" data-tip="太陽以外の星をまわる惑星。とても暗く星のまぶしさに埋もれるため、直接見るのは困難です。">系外惑星</span>）は、星のまぶしい光にかき消され、直接は見えません。存在するのかどうかさえ、長らく確かめられませんでした。</p>''',
      "星の“ふらつき”が惑星の証拠",
      r'''<p>マイヨールとケローは、惑星ではなく<b>星のわずかなふらつき</b>に注目しました。惑星があると、星もその重力に引かれて小さく揺れます。星が近づくときは光が青く、遠ざかるときは赤く見える（<span class="term" data-tip="近づく光は青っぽく、遠ざかる光は赤っぽくずれる現象。星のふらつきを読み取れます。">ドップラー効果</span>）ずれを精密に測り、1995年、<b>太陽に似た星をまわる惑星</b>を初めて見つけました。</p>''',
      r'''    <h2>やってみよう ── 星のふらつきで惑星を見つける</h2>
    <div class="hint">惑星が星をまわると、星も小さく揺れます。近づくと青、遠ざかると赤――この色ずれが惑星の証拠です。</div>
    <div class="xbox">
      <svg id="ex" width="360" height="240" viewBox="0 0 360 240" role="img" aria-label="系外惑星">
        <circle id="star" cx="180" cy="120" r="26" fill="#ffe066"/>
        <circle id="planet" cx="180" cy="120" r="8" fill="#8ab6ff"/>
        <rect x="120" y="212" width="120" height="16" rx="4" fill="#26343f"/>
        <rect id="dop" x="180" y="212" width="4" height="16" fill="#fff"/>
        <text x="126" y="208" fill="#8ab6ff" font-size="10">青（近づく）</text>
        <text x="196" y="208" fill="#ff9a8a" font-size="10">赤（遠ざかる）</text>
      </svg>
    </div>
    <div class="btns"><button id="play4">動かす</button><button id="stop4">止める</button></div>
    <div class="readout" id="msg">ボタンで惑星をまわしてみましょう</div>
    <div class="note">※ 惑星は見えなくても、星の“揺れ”と光の色ずれから存在が分かります。模式図です。</div>''',
      r'''<p>この発見以来、<b>5000個以上</b>の系外惑星が見つかり、「宇宙に地球のような星はあるのか」「生命はいるのか」という問いが現実の研究テーマになりました。ピーブルスの宇宙論と合わせ、私たちの宇宙観を大きく広げた受賞です。</p>''',
      r'''var star=document.getElementById('star'), planet=document.getElementById('planet'),
    dop=document.getElementById('dop'), play=document.getElementById('play4'),
    stop=document.getElementById('stop4'), msg=document.getElementById('msg');
var ang=0, running=false;
function frame(){ if(!running)return; ang+=0.05;
  var px=180+90*Math.cos(ang), py=120+50*Math.sin(ang);
  planet.setAttribute('cx',px); planet.setAttribute('cy',py);
  var sx=180-10*Math.cos(ang), sy=120-6*Math.sin(ang);       // 星の反対向きの揺れ
  star.setAttribute('cx',sx); star.setAttribute('cy',sy);
  var vx=Math.sin(ang);                                       // 星の視線速度（右=遠ざかる）
  dop.setAttribute('x',180+vx*56);
  dop.setAttribute('fill', vx>0.1?'#ff9a8a':vx<-0.1?'#8ab6ff':'#fff');
  msg.innerHTML = vx>0.1?'星は<b>遠ざかる</b>（光が赤へ）':vx<-0.1?'星は<b>近づく</b>（光が青へ）':'星は真横に移動中';
  requestAnimationFrame(frame);
}
play.addEventListener('click',function(){if(!running){running=true;frame();}});
stop.addEventListener('click',function(){running=false;});''')

    # ===== 41 ブラックホール 2020 =====
    page("41_2020_black_hole.html", "cosmos", 2020,
      "光さえ抜け出せない天体 ── ブラックホール",
      "ペンローズ ／ ゲンツェル ／ ゲズ（イギリス・ドイツ・アメリカ）",
      "ブラックホールが一般相対論の帰結であることの証明（ペンローズ）と、銀河中心の超巨大天体の発見（ゲンツェル・ゲズ）に対して。",
      "重力が強すぎると何が起きる？",
      r'''<p>物が重く小さく集まるほど、そこから抜け出すのに必要な速さは大きくなります。もし<b>光の速さでも抜け出せない</b>ほど重力が強くなったら――そこは光さえ出てこられない<span class="term" data-tip="重力が強すぎて光さえ抜け出せない天体。境界の内側の情報は外に伝わりません。">ブラックホール</span>になります。</p>''',
      "理論の証明と、銀河中心での発見",
      r'''<p>ペンローズは、アインシュタインの<span class="term" data-tip="重力を時空のゆがみとして説明するアインシュタインの理論。ブラックホールや重力波を予言します。">一般相対性理論</span>から、ブラックホールが<b>必ず生まれる</b>ことを数学的に証明しました。ゲンツェルとゲズは、私たちの銀河の中心で<b>星々が目に見えない一点を猛スピードでまわっている</b>のを何年も追跡し、そこに太陽の数百万倍の質量が潜む＝<b>超巨大ブラックホール</b>があることを突きとめました。</p>''',
      r'''    <h2>やってみよう ── 見えない中心をまわる星</h2>
    <div class="hint">「動かす」を押すと、星が見えない一点を高速でまわります。中心に何も見えないのに強い重力＝ブラックホールです。</div>
    <div class="xbox">
      <svg id="bh" width="320" height="240" viewBox="0 0 320 240" role="img" aria-label="ブラックホール">
        <circle id="eh" cx="160" cy="120" r="0" fill="#000" stroke="#7c3aed" stroke-dasharray="3 3"/>
        <circle cx="160" cy="120" r="3" fill="#3a4356"/>
        <circle id="s1" r="7" fill="#ffe066"/>
        <circle id="s2" r="6" fill="#ff9a8a"/>
      </svg>
    </div>
    <div class="btns"><button id="play5">動かす</button><button id="show">境界を表示</button></div>
    <div class="readout" id="msg">中心には何も見えないのに、強い重力がある</div>
    <div class="note">※ 星の速い動きから、見えない中心の重い天体（ブラックホール）が分かります。点線は「これより内は光も出られない」境界。模式図です。</div>''',
      r'''<p>2019年には、ブラックホールの“影”が電波望遠鏡で直接<b>撮影</b>されました。ブラックホールは、重力の極限を調べる究極の実験室であり、銀河の成り立ちにも深く関わります。100年前のアインシュタインの理論が、現代の観測でくり返し裏づけられているのです。</p>''',
      r'''var eh=document.getElementById('eh'), s1=document.getElementById('s1'), s2=document.getElementById('s2'),
    play=document.getElementById('play5'), show=document.getElementById('show'), msg=document.getElementById('msg');
var ang=0, running=false, shown=false;
function frame(){ if(!running)return; ang+=0.045;
  s1.setAttribute('cx',160+95*Math.cos(ang)); s1.setAttribute('cy',120+55*Math.sin(ang));
  var a2=ang*1.7+2; s2.setAttribute('cx',160+55*Math.cos(a2)); s2.setAttribute('cy',120+80*Math.sin(a2));
  requestAnimationFrame(frame);
}
play.addEventListener('click',function(){if(!running){running=true;frame();}});
show.addEventListener('click',function(){shown=!shown; eh.setAttribute('r',shown?26:0);
  msg.innerHTML=shown?'点線の内側＝光も抜け出せない境界（事象の地平面）':'中心には何も見えないのに、強い重力がある';});''')

    # ===== 42 真鍋淑郎 2021 =====
    page("42_2021_manabe.html", "cosmos", 2021,
      "気候を物理で予測する ── 地球温暖化のモデル",
      "真鍋淑郎（日本→アメリカ） ／ ハッセルマン ／ パリシ（ドイツ・イタリア）",
      "地球の気候を物理法則で数値モデル化し、温暖化を予測したこと（真鍋・ハッセルマン）と、複雑系の理論（パリシ）に対して。",
      "複雑な気候を計算できるのか",
      r'''<p>気候は、大気・海・太陽・雲…が絡み合う<b>とても複雑なしくみ</b>です。こんなものを物理法則で計算し、未来を予測するなど無理だと思われていました。</p>''',
      "二酸化炭素が増えると地球は暖まる",
      r'''<p>真鍋は1960年代、地球の大気を<b>物理法則の計算モデル</b>にしました。そして<b>大気中の二酸化炭素（CO₂）が増えると地表の温度が上がる</b>ことを、数値ではっきり示しました。CO₂などの<span class="term" data-tip="地表から宇宙へ逃げる熱（赤外線）を吸収して、地球を暖める気体。二酸化炭素やメタンなど。">温室効果ガス</span>が、地表から逃げる熱をせき止めるからです。半世紀前の予測は、現在の温暖化とよく一致しています。</p>''',
      r'''    <h2>やってみよう ── CO₂と地球の温度</h2>
    <div class="hint">スライダーでCO₂を増やすと、宇宙へ逃げる熱がせき止められ、地球の温度が上がります。</div>
    <div class="xbox">
      <svg id="cl" width="440" height="220" viewBox="0 0 440 220" role="img" aria-label="温室効果">
        <circle cx="150" cy="150" r="55" fill="#3b6ea5"/>
        <path d="M110,150 a40,40 0 0 1 80,0" fill="#4a8a5a"/>
        <rect id="ghg" x="60" y="60" width="200" height="14" rx="7" fill="#c2410c" opacity="0.2"/>
        <text x="160" y="52" fill="#8b93a7" font-size="11" text-anchor="middle">CO₂の層</text>
        <line x1="330" y1="20" x2="210" y2="120" stroke="#ffe066" stroke-width="3"/>
        <g id="ir"></g>
        <rect x="360" y="40" width="26" height="150" rx="13" fill="#26343f"/>
        <rect id="merc" x="360" y="150" width="26" height="40" rx="13" fill="#ff6b6b"/>
      </svg>
    </div>
    <div class="controls">
      <label for="co2">大気中のCO₂</label>
      <input id="co2" type="range" min="0" max="100" value="20">
      <div class="status yes" id="st"></div>
    </div>
    <div class="note">※ CO₂が増えるほど、地表から逃げる熱（赤外線）がせき止められ気温が上がります。真鍋のモデルの核心を簡単にした模式図です。</div>''',
      r'''<p>真鍋の気候モデルは、いまの<b>地球温暖化予測</b>の原型です。気候変動を「政治的な意見」ではなく<b>物理で示せる科学</b>にしたことが評価されました。同時受賞のパリシは、乱れた複雑な系にひそむ規則を見いだす理論で知られます。地球の未来を考えるうえで、欠かせない研究です。</p>''',
      r'''var co2=document.getElementById('co2'), ghg=document.getElementById('ghg'),
    merc=document.getElementById('merc'), ir=document.getElementById('ir'), st=document.getElementById('st');
var NS='http://www.w3.org/2000/svg';
function render(){ var c=+co2.value/100;
  ghg.setAttribute('opacity',(0.15+0.75*c).toFixed(2));
  var h=30+c*120; merc.setAttribute('height',h); merc.setAttribute('y',190-h);
  ir.innerHTML='';
  for(var i=0;i<5;i++){ var x=110+i*20, blocked=(i/5)<c;
    var l=document.createElementNS(NS,'line'); l.setAttribute('x1',x); l.setAttribute('y1',120);
    l.setAttribute('x2',x); l.setAttribute('y2',blocked?74:20);
    l.setAttribute('stroke',blocked?'#c2410c':'#ff9a8a'); l.setAttribute('stroke-width','2');
    l.setAttribute('stroke-dasharray','3 3'); ir.appendChild(l); }
  st.className='status '+(c>0.6?'no':'yes');
  st.textContent='CO₂ '+(c<0.3?'少':c<0.7?'中':'多')+'：地球の温度 '+(c<0.3?'低め':c<0.7?'上昇中':'高い（熱がこもる）');
}
co2.addEventListener('input',render); render();''')

    # ===== 43 量子もつれ 2022 =====
    page("43_2022_entanglement.html", "quantum", 2022,
      "離れていても結びつく2粒子 ── 量子もつれ",
      "アスペ ／ クラウザー ／ ツァイリンガー（フランス・アメリカ・オーストリア）",
      "もつれ合った光子を使った実験でベルの不等式の破れを示し、量子情報科学を開いたことに対して。",
      "アインシュタインも悩んだ“不気味な結びつき”",
      r'''<p>量子力学では、2つの粒子が<span class="term" data-tip="2つの粒子が1つの運命を分け合う状態。片方を測ると、もう片方の状態も瞬時に決まります。">量子もつれ</span>という特別な関係を結べます。すると、どんなに遠く離れても<b>片方を測った瞬間に、もう片方の状態も決まる</b>のです。アインシュタインはこれを「不気味」と呼び、本当は隠れた仕掛けがあるのでは、と疑いました。</p>''',
      "実験が決着をつけた",
      r'''<p>クラウザー、アスペ、ツァイリンガーは、もつれ合った<b>光子</b>のペアで精密な実験を重ね、<span class="term" data-tip="隠れた仕掛け（古典的な事前の取り決め）では説明できない相関の限界を示す式。量子もつれはこれを破ります。">ベルの不等式</span>が<b>破れる</b>ことを示しました。つまり「隠れた仕掛け」では説明できず、<b>量子もつれは本物</b>だと決着したのです。ただし、これを使って光より速く<b>情報を送ることはできません</b>（結果はランダムに見えるため）。</p>''',
      r'''    <h2>やってみよう ── 離れた2粒子を測る</h2>
    <div class="hint">「測定する」を押すと、左右のもつれた粒子の結果が出ます。毎回ランダムですが、2つは必ず逆向き（強く相関）です。</div>
    <div class="xbox">
      <svg id="en2" width="440" height="170" viewBox="0 0 440 170" role="img" aria-label="量子もつれ">
        <line x1="120" y1="85" x2="320" y2="85" stroke="#3a4356" stroke-dasharray="4 4"/>
        <circle cx="60" cy="85" r="24" fill="#3b2f66" stroke="#c4b5fd"/>
        <text id="lft" x="60" y="92" text-anchor="middle" font-size="20" fill="#e8edf3">?</text>
        <circle cx="380" cy="85" r="24" fill="#3b2f66" stroke="#c4b5fd"/>
        <text id="rgt" x="380" y="92" text-anchor="middle" font-size="20" fill="#e8edf3">?</text>
        <text x="60" y="135" fill="#8b93a7" font-size="11" text-anchor="middle">粒子A</text>
        <text x="380" y="135" fill="#8b93a7" font-size="11" text-anchor="middle">粒子B（遠く離れている）</text>
      </svg>
    </div>
    <div class="btns"><button id="meas">測定する</button></div>
    <div class="readout" id="msg">測定回数：0　一致して逆向き：0</div>
    <div class="note">※ 片方が上向きなら、もう片方は必ず下向き――遠く離れても結果は結びついています。ただし通信には使えません。模式図です。</div>''',
      r'''<p>量子もつれは、いまや<b>量子コンピュータ</b>・<b>量子暗号（盗聴を見破る通信）</b>・<b>量子テレポーテーション</b>といった量子情報技術の基盤です。かつては哲学的な論争だった話題が、実験を経て新しい産業技術になりました。「不気味な結びつき」は、これからの情報社会のカギになろうとしています。</p>''',
      r'''var meas=document.getElementById('meas'), lft=document.getElementById('lft'),
    rgt=document.getElementById('rgt'), msg=document.getElementById('msg');
var n=0, corr=0;
meas.addEventListener('click',function(){ n++;
  var up=Math.random()<0.5;
  lft.textContent=up?'↑':'↓'; rgt.textContent=up?'↓':'↑';
  lft.setAttribute('fill',up?'#7ec8ff':'#ff9a8a'); rgt.setAttribute('fill',up?'#ff9a8a':'#7ec8ff');
  corr++;                                          // つねに逆向き
  msg.innerHTML='測定回数：<b>'+n+'</b>　一致して逆向き：<b>'+corr+'</b>（いつも相関している）';
});''')

    # ===== 44 アト秒 2023 =====
    page("44_2023_attosecond.html", "matter", 2023,
      "電子の動きを止めて撮る ── アト秒の光",
      "アゴスティーニ ／ クラウス ／ ルイリエ（フランス・ドイツ・スウェーデン）",
      "物質の中の電子のふるまいを調べるための、アト秒の光パルスを生み出す実験手法に対して。",
      "電子は速すぎて“撮れ”なかった",
      r'''<p>原子の中の電子は、とてつもない速さで動きます。速い動きを撮るには<b>もっと短い一瞬のシャッター</b>が要りますが、電子の動きはあまりに速く、ふつうの光パルスでは<b>ブレて</b>しまって撮れませんでした。</p>''',
      "1秒の100京分の1の光の点滅",
      r'''<p>3人は、<span class="term" data-tip="1アト秒は1秒の100京分の1（0.000000000000000001秒）。電子の動きに追いつける、とてつもなく短い時間です。">アト秒</span>という、想像を絶するほど短い光の点滅を作り出す方法を確立しました。これは超高速の<b>ストロボ写真</b>のようなもの。あまりに短い一瞬なので、それまでブレていた<b>電子の動きを止めて“撮る”</b>ことができるようになりました。</p>''',
      r'''    <h2>やってみよう ── シャッターを短くする</h2>
    <div class="hint">スライダーでシャッター（光パルス）を短くすると、動く電子のブレが消えて、くっきり撮れます。</div>
    <div class="xbox">
      <svg id="at" width="420" height="180" viewBox="0 0 420 180" role="img" aria-label="アト秒撮影">
        <circle cx="210" cy="90" r="70" fill="none" stroke="#2a3446" stroke-dasharray="3 4"/>
        <ellipse id="eblur" cx="280" cy="90" rx="40" ry="12" fill="#66bb6a" opacity="0.85"/>
      </svg>
    </div>
    <div class="controls">
      <label for="sh">シャッターの短さ　長い ← → アト秒</label>
      <input id="sh" type="range" min="0" max="100" value="10">
      <div class="status no" id="st"></div>
    </div>
    <div class="note">※ シャッターが長いと動く電子はブレます。アト秒まで短くすると点として止めて撮れます。模式図です。</div>''',
      r'''<p>アト秒の光は、<b>電子が動く現場</b>そのものを観察する新しい目です。化学反応の瞬間、材料の中の電子の動き、光と物質のやりとりを直接とらえられるようになり、<b>超高速エレクトロニクス</b>や新材料・医療の研究への応用が期待されています。人類の“時間の分解能”が、また一段深くなりました。</p>''',
      r'''var sh=document.getElementById('sh'), eblur=document.getElementById('eblur'), st=document.getElementById('st');
var ang=0;
function frame(){ ang+=0.08; var s=+sh.value/100;
  var cx=210+70*Math.cos(ang), cy=90+70*Math.sin(ang);
  eblur.setAttribute('cx',cx); eblur.setAttribute('cy',cy);
  eblur.setAttribute('rx',6+(1-s)*46);            // 短いほどブレない
  eblur.setAttribute('ry',6+(1-s)*8);
  eblur.setAttribute('opacity',(0.4+0.6*s).toFixed(2));
  st.className='status '+(s>0.6?'yes':'no');
  st.textContent = s<0.3?'シャッターが長い：電子がブレて撮れない':s<0.7?'短くなってきた：少しブレ':'アト秒：電子を止めてくっきり撮れた！';
  requestAnimationFrame(frame);
}
frame();''')

    # ===== 45 機械学習 2024 =====
    page("45_2024_ml.html", "matter", 2024,
      "物理から生まれた“学ぶ機械” ── 機械学習の基礎",
      "ホップフィールド ／ ヒントン（アメリカ・イギリス→カナダ）",
      "人工ニューラルネットワークによる機械学習を可能にした、基礎的な発見と発明に対して。",
      "脳のまねをする計算のしくみ",
      r'''<p>脳は、たくさんの神経細胞がつながり合って学びます。これをまねた計算のしくみ（<span class="term" data-tip="脳の神経細胞のつながりをまねた計算のしくみ。データから自動でパターンを学びます。">ニューラルネットワーク</span>）は古くからありましたが、うまく学習させる方法が分かりませんでした。ここで<b>物理学の考え方</b>が力を発揮します。</p>''',
      "エネルギーが低い方へ“落ち着く”記憶",
      r'''<p>ホップフィールドは、物理でおなじみの「<b>エネルギーが低い状態に落ち着く</b>」という考えを使い、あいまいな入力から正しい記憶を思い出すネットワークを作りました（<span class="term" data-tip="ノイズだらけの入力から、記憶したパターンへと“転がり落ちて”思い出すネットワーク。物理のエネルギー最小化がもとです。">ホップフィールド・ネットワーク</span>）。ヒントンは、これを発展させて<b>データから自動で学ぶ</b>方法を築きました。いまの人工知能（AI）ブームの土台です。</p>''',
      r'''    <h2>やってみよう ── ノイズから記憶を思い出す</h2>
    <div class="hint">「ノイズを加える」で絵を乱し、「思い出す」を押すと、ネットワークが記憶した絵へと“落ち着いて”復元します。</div>
    <div class="xbox">
      <svg id="hp" width="220" height="220" viewBox="0 0 220 220" role="img" aria-label="連想記憶"></svg>
    </div>
    <div class="btns"><button id="noise">ノイズを加える</button><button id="recall">思い出す</button></div>
    <div class="readout" id="msg">記憶した絵を表示中</div>
    <div class="note">※ ノイズだらけの入力から、記憶したパターンへ“転がり落ちて”復元します（エネルギー最小化）。連想記憶の模式図です。</div>''',
      r'''<p>物理から生まれた「学ぶ機械」の考えは、いまや<b>画像認識・音声認識・自動翻訳・生成AI</b>など、社会のあらゆる場面で使われています。物理学賞がAIの基礎に贈られたことは、物理の考え方が分野を超えて世界を変えている証しです。この年表の最新の1ページであり、次の時代への入り口でもあります。</p>''',
      r'''var svg=document.getElementById('hp'), noise=document.getElementById('noise'),
    recall=document.getElementById('recall'), msg=document.getElementById('msg');
var NS='http://www.w3.org/2000/svg', G=7, cell=28, pad=12;
// 記憶パターン（十字）
var mem=[]; for(var y=0;y<G;y++){var row=[];for(var x=0;x<G;x++){ row.push((x===3||y===3)?1:0);} mem.push(row);}
var state=mem.map(function(r){return r.slice();});
var rects=[];
for(var y=0;y<G;y++){rects.push([]);for(var x=0;x<G;x++){
  var r=document.createElementNS(NS,'rect'); r.setAttribute('x',pad+x*cell); r.setAttribute('y',pad+y*cell);
  r.setAttribute('width',cell-3); r.setAttribute('height',cell-3); r.setAttribute('rx',4); svg.appendChild(r); rects[y].push(r);}}
function paint(){ for(var y=0;y<G;y++)for(var x=0;x<G;x++) rects[y][x].setAttribute('fill', state[y][x]?'#b388ff':'#20293a'); }
noise.addEventListener('click',function(){ for(var k=0;k<16;k++){var x=(Math.random()*G)|0,y=(Math.random()*G)|0; state[y][x]=1-state[y][x];}
  paint(); msg.innerHTML='ノイズを加えました（乱れた入力）'; });
var timer=null;
recall.addEventListener('click',function(){ if(timer)clearInterval(timer);
  msg.innerHTML='記憶へ“落ち着いて”いく…';
  timer=setInterval(function(){ var changed=false;
    var x=(Math.random()*G)|0, y=(Math.random()*G)|0;
    if(state[y][x]!==mem[y][x]){ state[y][x]=mem[y][x]; changed=true; }
    paint();
    var done=true; for(var yy=0;yy<G;yy++)for(var xx=0;xx<G;xx++) if(state[yy][xx]!==mem[yy][xx])done=false;
    if(done){ clearInterval(timer); msg.innerHTML='<b>思い出した！</b> 記憶した絵にぴったり復元'; }
  },60);
});
paint();''')

    # ===MORE===
