# -*- coding: utf-8 -*-
"""定量シミュレーション差し替え（25件）。SIM[file] = (demo_html, script_js)。
build_pages.apply_overrides() が pages_data.py の図解をこれで置き換える。
方針: 物理式に基づく実単位の計算（簡略化した点は各ページの .note に明記する）。
完全オフライン: canvas + 素のJSのみ。外部リソースは使わない。"""

SIM = {}

# ===== 01 レントゲン: X線管のスペクトル（クレイマースの式 + 特性X線 + フィルタ減衰） =====
SIM["01_1901_roentgen.html"] = (r'''    <h2>実験してみよう ── X線管でスペクトルを作る</h2>
    <div class="hint">レントゲンの放電管を現代のX線管に置き換えた実験です。<b>管電圧</b>で電子を加速し、タングステンの的にぶつけてX線を作ります。電圧・電流・アルミフィルタを変えると、出てくるX線のスペクトル（横軸：光子エネルギー、縦軸：強さ）がどう変わるでしょうか。</div>
    <div class="xbox"><canvas id="cv" width="640" height="320"></canvas></div>
    <div class="cpanel">
      <div class="ctl"><label>管電圧（加速電圧） <output id="oU">80 kV</output></label><input id="U" type="range" min="30" max="150" value="80"></div>
      <div class="ctl"><label>管電流（電子の数） <output id="oI">10 mA</output></label><input id="I" type="range" min="1" max="20" value="10"></div>
      <div class="ctl"><label>アルミフィルタの厚さ <output id="oD">1.0 mm</output></label><input id="D" type="range" min="0" max="50" value="10"></div>
    </div>
    <div class="rpanel"><span>最大光子エネルギー <b id="rEmax">–</b></span><span>最短波長 <b id="rLmin">–</b></span><span>特性X線 <b id="rChar">–</b></span></div>
    <div class="note">連続X線は<b>クレイマースの式</b> I(E)∝i·(U−E)/E、フィルタ透過は指数減衰 e<sup>−μd</sup> による計算です（タングステン陽極。μのエネルギー依存は簡略化）。電子の運動エネルギー eU がX線光子1個の上限になる（デュエイン・ハントの限界）こと、69.5 kV を超えるとタングステン原子の内殻に由来する<b>特性X線</b>の鋭い山が立つことを確かめてください。</div>''',
r'''var cv=document.getElementById('cv'),g=cv.getContext('2d'),W=cv.width,H=cv.height;
var U=document.getElementById('U'),I=document.getElementById('I'),D=document.getElementById('D');
var PX0=52,PY0=H-38,PW=W-80,PH=H-70;   // plot area
function mu(E){return 0.02+0.28*Math.pow(30/E,3);}      // Al 減衰係数 /mm（近似）
function spec(E,kv,ma,dmm){
  if(E>=kv||E<5)return 0;
  var s=ma*(kv-E)/E;                                    // Kramers
  if(kv>69.5){                                          // W 特性X線 Kα59.3 / Kβ67.2 keV
    var a=ma*22*Math.pow(kv/69.5-1,1.6);
    s+=a*Math.exp(-Math.pow((E-59.3)/1.1,2))+0.45*a*Math.exp(-Math.pow((E-67.2)/1.1,2));
  }
  return s*Math.exp(-mu(E)*dmm);
}
var NORM=0;(function(){for(var E=5;E<150;E+=0.2){var v=spec(E,150,20,0);if(v>NORM)NORM=v;}})();
function render(){
  var kv=+U.value,ma=+I.value,dmm=+D.value/10;
  document.getElementById('oU').textContent=kv+' kV';
  document.getElementById('oI').textContent=ma+' mA';
  document.getElementById('oD').textContent=dmm.toFixed(1)+' mm';
  g.clearRect(0,0,W,H);
  g.strokeStyle='#232b3d';g.lineWidth=1;g.beginPath();
  for(var i=1;i<=7;i++){var gy=PY0-PH*i/7;g.moveTo(PX0,gy);g.lineTo(PX0+PW,gy);}
  for(var e=20;e<=160;e+=20){var gx=PX0+PW*e/160;g.moveTo(gx,PY0);g.lineTo(gx,PY0-PH);}
  g.stroke();
  g.strokeStyle='#8b93a7';g.beginPath();g.moveTo(PX0,PY0-PH);g.moveTo(PX0,PY0);g.lineTo(PX0+PW,PY0);g.stroke();
  g.fillStyle='#8b93a7';g.font='12px sans-serif';
  for(var e2=0;e2<=160;e2+=40)g.fillText(e2,PX0+PW*e2/160-6,PY0+16);
  g.fillText('光子エネルギー (keV)',W/2-56,H-4);
  g.save();g.translate(14,H/2+30);g.rotate(-Math.PI/2);g.fillText('X線の強さ（相対値）',0,0);g.restore();
  // Duane-Hunt limit line
  var xl=PX0+PW*kv/160;
  g.strokeStyle='#5c6470';g.setLineDash([4,4]);g.beginPath();g.moveTo(xl,PY0);g.lineTo(xl,PY0-PH);g.stroke();g.setLineDash([]);
  g.fillStyle='#8b93a7';g.fillText('eU の壁',Math.min(xl+4,W-60),PY0-PH+14);
  // spectrum
  g.strokeStyle='#ffb454';g.lineWidth=2.5;g.beginPath();var started=false;
  for(var px=0;px<=PW;px++){var E=160*px/PW,v=spec(E,kv,ma,dmm)/NORM*3.2;if(v>1)v=1;
    var y=PY0-PH*v;if(E<5){continue;}
    if(!started){g.moveTo(PX0+px,y);started=true;}else g.lineTo(PX0+px,y);}
  g.stroke();
  document.getElementById('rEmax').textContent=kv+' keV';
  document.getElementById('rLmin').textContent=(1239.8/kv).toFixed(1)+' pm';
  document.getElementById('rChar').textContent=kv>69.5?'Kα 59.3 keV / Kβ 67.2 keV が出現':'出ない（69.5 kV 以上で出現）';
}
[U,I,D].forEach(function(s){s.addEventListener('input',render);});render();''')

# ===== 02 キュリー: 放射性崩壊の指数法則（半減期・放射能 A=λN） =====
SIM["02_1903_curie.html"] = (r'''    <h2>実験してみよう ── 半減期と放射能を測る</h2>
    <div class="hint">核種（放射線を出す原子の種類）を選び、時間を進めてみましょう。原子の数 N は半減期 T ごとに半分になり、放射能（1秒あたりの崩壊数）A = λN も同じペースで弱まります。</div>
    <div class="xbox"><canvas id="cv" width="640" height="300"></canvas></div>
    <div class="btns">
      <button data-k="rn" class="on">ラドン222（T=3.82日）</button>
      <button data-k="po">ポロニウム210（T=138日）</button>
      <button data-k="ra">ラジウム226（T=1600年）</button>
    </div>
    <div class="cpanel">
      <div class="ctl"><label>初期の原子数 N₀ <output id="oN">10¹⁶ 個</output></label><input id="N0" type="range" min="12" max="20" value="16"></div>
      <div class="ctl"><label>経過時間 <output id="oT">0</output></label><input id="T" type="range" min="0" max="800" value="0"></div>
    </div>
    <div class="rpanel"><span>残っている原子 <b id="rN">–</b></span><span>放射能 <b id="rA">–</b></span><span>崩壊した割合 <b id="rP">–</b></span></div>
    <div class="note">N(t) = N₀·2<sup>−t/T</sup>、A = λN、λ = ln2/T による正確な計算です。マリー・キュリーの本質的な発見は「放射能は化学状態や温度によらず、<b>原子の種類と数だけで決まる</b>」こと──つまり放射能が原子そのものの性質だという点でした。ポロニウム・ラジウムはいずれも夫妻が発見した元素です。</div>''',
r'''var cv=document.getElementById('cv'),g=cv.getContext('2d'),W=cv.width,H=cv.height;
var N0s=document.getElementById('N0'),Ts=document.getElementById('T');
var NUC={rn:{T:3.82,u:'日',s:3.82*86400},po:{T:138.4,u:'日',s:138.4*86400},ra:{T:1600,u:'年',s:1600*365.25*86400}};
var cur='rn';
var btns=document.querySelectorAll('.btns button');
btns.forEach(function(b){b.addEventListener('click',function(){cur=b.dataset.k;
  btns.forEach(function(x){x.classList.toggle('on',x===b)});render();});});
function fmtN(n){var e=Math.floor(Math.log(n)/Math.LN10);var m=n/Math.pow(10,e);
  return m.toFixed(2)+'×10^'+e;}
function fmtA(a){if(a>1e12)return (a/1e12).toFixed(2)+' 兆 Bq';if(a>1e8)return (a/1e8).toFixed(2)+' 億 Bq';
  if(a>1e4)return (a/1e4).toFixed(2)+' 万 Bq';return a.toFixed(0)+' Bq';}
var PX0=56,PY0=H-36,PW=W-90,PH=H-64;
function render(){
  var nu=NUC[cur],lgN0=+N0s.value,N0=Math.pow(10,lgN0);
  var tT=+Ts.value/100;                      // 半減期の何倍か (0..8)
  var t=tT*nu.T;
  document.getElementById('oN').textContent='10^'+lgN0+' 個';
  document.getElementById('oT').textContent=(nu.T>=1600?t.toFixed(0):t.toFixed(1))+' '+nu.u;
  g.clearRect(0,0,W,H);
  g.strokeStyle='#232b3d';g.beginPath();
  for(var i=1;i<=4;i++){var gy=PY0-PH*i/4;g.moveTo(PX0,gy);g.lineTo(PX0+PW,gy);}
  for(var k=1;k<=8;k++){var gx=PX0+PW*k/8;g.moveTo(gx,PY0);g.lineTo(gx,PY0-PH);}
  g.stroke();
  g.strokeStyle='#8b93a7';g.beginPath();g.moveTo(PX0,PY0);g.lineTo(PX0+PW,PY0);g.stroke();
  g.fillStyle='#8b93a7';g.font='12px sans-serif';
  for(var k2=0;k2<=8;k2+=2)g.fillText((k2*nu.T).toFixed(0)+nu.u,PX0+PW*k2/8-14,PY0+16);
  g.fillText('N/N₀',8,PY0-PH+4);g.fillText('1',PX0-16,PY0-PH+4);g.fillText('1/2',PX0-26,PY0-PH/2+4);g.fillText('0',PX0-14,PY0+4);
  // 半減期の階段（目印）
  g.strokeStyle='#3a4356';g.setLineDash([3,4]);g.beginPath();
  for(var h=1;h<=8;h++){var vy=PY0-PH*Math.pow(0.5,h),vx=PX0+PW*h/8;
    g.moveTo(PX0,vy);g.lineTo(vx,vy);g.lineTo(vx,PY0);}
  g.stroke();g.setLineDash([]);
  // 崩壊曲線
  g.strokeStyle='#7ee787';g.lineWidth=2.5;g.beginPath();
  for(var px=0;px<=PW;px++){var xt=8*px/PW,f=Math.pow(0.5,xt);
    if(px===0)g.moveTo(PX0,PY0-PH*f);else g.lineTo(PX0+px,PY0-PH*f);}
  g.stroke();g.lineWidth=1;
  // マーカー
  var f=Math.pow(0.5,tT),mx=PX0+PW*tT/8,my=PY0-PH*f;
  g.fillStyle='#ffd257';g.beginPath();g.arc(mx,my,6,0,7);g.fill();
  var N=N0*f,lam=Math.LN2/nu.s,A=lam*N;
  document.getElementById('rN').textContent=fmtN(N)+' 個';
  document.getElementById('rA').textContent=fmtA(A);
  document.getElementById('rP').textContent=((1-f)*100).toFixed(1)+' %';
}
[N0s,Ts].forEach(function(s){s.addEventListener('input',render);});render();''')

# ===== 03 トムソン: e/m の測定（電場と磁場のつり合い） =====
SIM["03_1906_thomson.html"] = (r'''    <h2>実験してみよう ── トムソンの方法で e/m を測る</h2>
    <div class="hint">トムソンの実験を3ステップで再現します。<b>①</b> 加速電圧で電子を打ち出す → <b>②</b> 偏向電圧で上に曲げる → <b>③</b> 磁場を強めて、ちょうどまっすぐに戻す。つり合ったとき電子の速さは v = E/B と分かり、そこから e/m（電荷と質量の比）が求まります。</div>
    <div class="xbox"><canvas id="cv" width="640" height="280"></canvas></div>
    <div class="cpanel">
      <div class="ctl"><label>① 加速電圧 <output id="oVa">1500 V</output></label><input id="Va" type="range" min="500" max="3000" value="1500" step="50"></div>
      <div class="ctl"><label>② 偏向板の電圧 <output id="oVd">300 V</output></label><input id="Vd" type="range" min="0" max="600" value="300" step="10"></div>
      <div class="ctl"><label>③ 磁束密度 <output id="oB">0.00 mT</output></label><input id="B" type="range" min="0" max="200" value="0"></div>
    </div>
    <div class="status" id="st">まず ②偏向電圧 で曲げてから、③磁場 でまっすぐに戻しましょう</div>
    <div class="rpanel"><span>電子の速さ v <b id="rV">–</b></span><span>測定された e/m <b id="rEM">–</b></span><span>現代の値 <b>1.759×10¹¹ C/kg</b></span></div>
    <div class="note">偏向板の長さ 10 cm・間隔 2 cm・スクリーンまで 25 cm の装置を想定し、電子の軌道は運動方程式どおりに計算しています（磁気偏向は小角近似）。つり合いから v = E/B、加速の式 eV<sub>a</sub> = ½mv² から e/m = v²/2V<sub>a</sub>。トムソンはこの値が「陰極の材質や気体の種類を変えても同じ」であることから、電子があらゆる原子に共通の部品だと見抜きました。</div>''',
r'''var cv=document.getElementById('cv'),g=cv.getContext('2d'),W=cv.width,H=cv.height;
var Va=document.getElementById('Va'),Vd=document.getElementById('Vd'),Bs=document.getElementById('B'),st=document.getElementById('st');
var EM=1.7588e11,L=0.10,d=0.02,DD=0.25;    // 実寸 (m)
var X0=40,XP1=220,XP2=XP1+180,XS=W-30,YC=H/2,SC=1800;  // 描画: 180px=10cm → 1px≈0.55mm, y倍率SC px/m
function render(){
  var va=+Va.value,vd=+Vd.value,B=+Bs.value/100*1e-3;   // T
  document.getElementById('oVa').textContent=va+' V';
  document.getElementById('oVd').textContent=vd+' V';
  document.getElementById('oB').textContent=(B*1e3).toFixed(2)+' mT';
  var v=Math.sqrt(2*EM*va),E=vd/d;
  // 板の中: 上向き加速度 aE=(e/m)E, 下向き aB=(e/m)vB
  var a=EM*(E-v*B);                       // 正なら上へ
  var t1=L/v,y1=0.5*a*t1*t1,vy=a*t1;      // 板の出口
  var y2=y1+vy*(DD/v);                    // スクリーン
  g.clearRect(0,0,W,H);
  // 管
  g.strokeStyle='#2a3446';g.lineWidth=2;g.strokeRect(20,30,W-46,H-60);
  g.fillStyle='#8b93a7';g.fillRect(26,YC-16,20,32);
  g.font='12px sans-serif';g.fillText('電子銃',24,YC+40);
  // 偏向板
  g.fillStyle='#ff8a8a';g.fillRect(XP1,YC-40,XP2-XP1,8);g.fillText('＋',XP2+6,YC-32);
  g.fillStyle='#8ab6ff';g.fillRect(XP1,YC+32,XP2-XP1,8);g.fillText('−',XP2+6,YC+44);
  // 磁場マーク（紙面の奥向き ×）
  if(B>0){g.fillStyle='#c4b5fd';for(var mx=XP1+20;mx<XP2;mx+=40)for(var my=YC-20;my<=YC+20;my+=40)g.fillText('×',mx,my);}
  // スクリーン
  g.fillStyle='#26343f';g.fillRect(XS-6,40,8,H-80);
  // 軌道: 板内は放物線、板後は直線
  g.strokeStyle='#7ee787';g.lineWidth=3;g.beginPath();g.moveTo(X0,YC);g.lineTo(XP1,YC);
  for(var i=0;i<=30;i++){var frac=i/30,xx=XP1+(XP2-XP1)*frac,tt=t1*frac;
    var yy=0.5*a*tt*tt;g.lineTo(xx,YC-yy*SC);}
  var xrest=(XS-XP2)/ (XP2-XP1)*L;        // 描画x → 実距離換算
  var yEnd=y1+vy*(xrest/v);
  g.lineTo(XS,YC-yEnd*SC);g.stroke();g.lineWidth=1;
  var ys=Math.max(48,Math.min(H-48,YC-yEnd*SC));
  g.fillStyle='#b6ffcf';g.beginPath();g.arc(XS-2,ys,6,0,7);g.fill();
  // 判定
  var rV=document.getElementById('rV'),rEM=document.getElementById('rEM');
  rV.textContent=(v/1e7).toFixed(2)+'×10⁷ m/s';
  if(vd===0){st.className='status';st.style.background='#fff7e6';st.style.color='#8a5a00';
    st.textContent='② 偏向電圧をかけて、ビームを曲げてみましょう';rEM.textContent='–';}
  else if(B===0){st.className='status no';st.textContent='電場で上に曲がった ── ③ 磁場をかけて、まっすぐに戻してみましょう';rEM.textContent='–';}
  else{var bal=Math.abs(E-v*B)/(E);
    if(bal<0.02){var vm=E/B,em=vm*vm/(2*va);st.className='status yes';
      st.textContent='つり合った！ v = E/B = '+(vm/1e7).toFixed(2)+'×10⁷ m/s と測定できた';
      rEM.textContent=(em/1e11).toFixed(3)+'×10¹¹ C/kg（誤差 '+(Math.abs(em-EM)/EM*100).toFixed(1)+'%）';}
    else{st.className='status no';st.textContent=(E>v*B?'まだ電気の力が強い ── 磁場をもう少し強く':'磁気の力が強すぎる ── 磁場を少し弱く');
      rEM.textContent='つり合っていないので測定できない';}}
}
[Va,Vd,Bs].forEach(function(s){s.addEventListener('input',render);});render();''')

# ===== 04 マイケルソン: 干渉計で波長を測る（実波長・実変位） =====
SIM["04_1907_michelson.html"] = (r'''    <h2>実験してみよう ── 干渉計で光の波長を測る</h2>
    <div class="hint">鏡を動かすと光の道のりの差（光路差 = 鏡の移動 × 2）が変わり、検出器が明→暗→明…と点滅します。<b>明暗の回数を数えると波長が測れる</b>のがマイケルソンの発明です。波長を変えて、点滅の間隔がどう変わるかも見てみましょう。</div>
    <div class="xbox"><canvas id="cv" width="640" height="300"></canvas></div>
    <div class="cpanel">
      <div class="ctl"><label>光の波長 λ <output id="oL">550 nm</output></label><input id="L" type="range" min="400" max="700" value="550"></div>
      <div class="ctl"><label>鏡の移動距離 Δd <output id="oD">0 nm</output></label><input id="Dm" type="range" min="0" max="1500" value="0"></div>
    </div>
    <div class="rpanel"><span>光路差 2Δd <b id="rP">0 nm</b></span><span>数えた明暗の回数 m <b id="rM">0</b></span><span>m から逆算した波長 2Δd/m <b id="rW">–</b></span></div>
    <div class="note">明るさは干渉の式 I = I₀cos²(2πΔd/λ) による正確な計算です。鏡を Δd 動かすと光は往復で 2Δd 余分に進むため、<b>2Δd がちょうど波長の整数倍のとき明るく</b>なります。この「明暗を数えて長さを測る」原理は、いまのレーザー測長器や重力波望遠鏡LIGO（2017年のページ参照）とまったく同じです。</div>''',
r'''var cv=document.getElementById('cv'),g=cv.getContext('2d'),W=cv.width,H=cv.height;
var Ls=document.getElementById('L'),Dm=document.getElementById('Dm');
function wl2rgb(w){var r=0,gg=0,b=0;
  if(w<440){r=-(w-440)/60;b=1;}else if(w<490){gg=(w-440)/50;b=1;}
  else if(w<510){gg=1;b=-(w-510)/20;}else if(w<580){r=(w-510)/70;gg=1;}
  else if(w<645){r=1;gg=-(w-645)/65;}else{r=1;}
  return [Math.round(255*r),Math.round(255*gg),Math.round(255*b)];}
function render(){
  var lam=+Ls.value,dd=+Dm.value,path=2*dd;
  var phase=2*Math.PI*path/lam;                 // 位相差
  var I=Math.pow(Math.cos(phase/2),2);          // 検出強度
  var c=wl2rgb(lam),col='rgb('+c[0]+','+c[1]+','+c[2]+')';
  document.getElementById('oL').textContent=lam+' nm';
  document.getElementById('oD').textContent=dd+' nm';
  g.clearRect(0,0,W,H);
  g.font='12px sans-serif';
  // 波A(基準) と 波B(2Δd ずれ) と 合成波
  var y1=64,y2=134,y3=224,amp=26,px2nm=3.5;     // 1px = 3.5nm
  g.fillStyle='#8b93a7';g.fillText('波A（固定鏡から）',16,y1-34);
  g.fillText('波B（動かした鏡から: 2Δd 遅れ）',16,y2-34);
  g.fillText('重ね合わせ（検出器へ）',16,y3-40);
  function wave(yc,shiftNm,a,color,lw){g.strokeStyle=color;g.lineWidth=lw;g.beginPath();
    for(var x=0;x<=W-140;x++){var pos=(x*px2nm-shiftNm)/lam*2*Math.PI;
      var y=yc-a*Math.sin(pos);if(x===0)g.moveTo(16+x,y);else g.lineTo(16+x,y);}g.stroke();}
  wave(y1,0,amp,'rgba('+c[0]+','+c[1]+','+c[2]+',0.95)',2);
  wave(y2,path,amp,'rgba('+c[0]+','+c[1]+','+c[2]+',0.65)',2);
  // 合成
  g.strokeStyle=col;g.lineWidth=2.5;g.beginPath();
  for(var x=0;x<=W-140;x++){var p1=(x*px2nm)/lam*2*Math.PI,p2=(x*px2nm-path)/lam*2*Math.PI;
    var y=y3-amp*0.9*(Math.sin(p1)+Math.sin(p2));if(x===0)g.moveTo(16+x,y);else g.lineTo(16+x,y);}
  g.stroke();g.lineWidth=1;
  // 検出器
  var dx=W-70,dy=H/2;
  g.fillStyle='rgba('+c[0]+','+c[1]+','+c[2]+','+(0.08+0.92*I).toFixed(2)+')';
  g.beginPath();g.arc(dx,dy,30,0,7);g.fill();
  g.strokeStyle='#3a4356';g.beginPath();g.arc(dx,dy,30,0,7);g.stroke();
  g.fillStyle='#8b93a7';g.fillText('検出器',dx-20,dy+52);
  g.fillStyle='#e6e3d9';g.fillText('明るさ '+(I*100).toFixed(0)+'%',dx-26,dy-40);
  var m=Math.floor(path/lam+0.5/1e9);           // 通過した明線の数
  document.getElementById('rP').textContent=path+' nm';
  document.getElementById('rM').textContent=(path/lam).toFixed(2)+' 周期（明線 '+Math.floor(path/lam)+' 回）';
  document.getElementById('rW').textContent=Math.floor(path/lam)>=1?(path/Math.floor(path/lam)).toFixed(0)+' nm（真値 '+lam+' nm）':'明線1回以上動かすと計算できます';
}
[Ls,Dm].forEach(function(s){s.addEventListener('input',render);});render();''')

# ===== 05 プランク: 黒体放射スペクトル（プランクの法則 vs レイリー・ジーンズ） =====
SIM["05_1918_planck.html"] = (r'''    <h2>実験してみよう ── 温度と「光の色」の法則</h2>
    <div class="hint">物体の温度を変えると、出てくる光のスペクトル（波長ごとの強さ）がどう変わるでしょうか。「古典理論」ボタンを押すと、量子を使わない場合の予言（レイリー・ジーンズの式）が重なります──短波長側で無限大に発散する「紫外破綻」を確かめてください。</div>
    <div class="xbox"><canvas id="cv" width="640" height="330"></canvas></div>
    <div class="cpanel">
      <div class="ctl"><label>物体の温度 T <output id="oT">3000 K</output></label><input id="T" type="range" min="500" max="10000" value="3000" step="50"></div>
    </div>
    <div class="btns"><button id="cl">古典理論（レイリー・ジーンズ）を重ねる</button></div>
    <div class="rpanel"><span>ピーク波長（ウィーンの変位則） <b id="rW">–</b></span><span>放射の総量 σT⁴ <b id="rS">–</b></span><span>見た目の色 <b id="rC">–</b></span></div>
    <div class="note">曲線は<b>プランクの法則</b> B(λ,T) = (2hc²/λ⁵)·1/(e<sup>hc/λkT</sup>−1) の正確な計算です（縦軸は曲線ごとに見やすく自動調整。総量は T⁴ で急増する点に注意）。ロウソクの炎（約1800 K）、白熱電球（約2800 K）、太陽表面（5772 K）を再現してみてください。ピーク波長×温度＝一定（2898 μm·K）というウィーンの変位則も読み取れます。</div>''',
r'''var cv=document.getElementById('cv'),g=cv.getContext('2d'),W=cv.width,H=cv.height;
var Ts=document.getElementById('T'),clBtn=document.getElementById('cl'),showCl=false;
clBtn.addEventListener('click',function(){showCl=!showCl;clBtn.classList.toggle('on',showCl);render();});
var PX0=56,PY0=H-40,PW=W-86,PH=H-72,LMAX=3000;   // λ 0..3000nm
function planck(lam,T){var x=1.4388e7/(lam*T);   // hc/kλT (λ in nm)
  return 1/(Math.pow(lam/1000,5)*(Math.exp(x)-1));}
function rj(lam,T){return 2.83e-9*T/Math.pow(lam/1000,4);} // 同スケールに調整した RJ 近似
function bbColor(T){ // 黒体色の近似
  var t=T/100,r,gg,b;
  r=t<=66?255:Math.min(255,Math.max(0,329.7*Math.pow(t-60,-0.133)));
  gg=t<=66?Math.min(255,Math.max(0,99.47*Math.log(t)-161.1)):Math.min(255,Math.max(0,288.1*Math.pow(t-60,-0.0755)));
  b=t>=66?255:(t<=19?0:Math.min(255,Math.max(0,138.5*Math.log(t-10)-305)));
  return 'rgb('+Math.round(r)+','+Math.round(gg)+','+Math.round(b)+')';}
function render(){
  var T=+Ts.value;document.getElementById('oT').textContent=T+' K';
  g.clearRect(0,0,W,H);
  // 可視域の虹
  var vx0=PX0+PW*380/LMAX,vx1=PX0+PW*750/LMAX;
  var grd=g.createLinearGradient(vx0,0,vx1,0);
  ['#7c3aed','#2563eb','#06b6d4','#22c55e','#eab308','#f97316','#dc2626'].forEach(function(c,i,arr){grd.addColorStop(i/(arr.length-1),c);});
  g.fillStyle=grd;g.globalAlpha=0.18;g.fillRect(vx0,PY0-PH,vx1-vx0,PH);g.globalAlpha=1;
  g.fillStyle='#8b93a7';g.font='12px sans-serif';g.fillText('可視光',(vx0+vx1)/2-20,PY0-PH+14);
  // 軸
  g.strokeStyle='#8b93a7';g.beginPath();g.moveTo(PX0,PY0);g.lineTo(PX0+PW,PY0);g.stroke();
  for(var l=0;l<=3000;l+=500)g.fillText(l,PX0+PW*l/LMAX-10,PY0+16);
  g.fillText('波長 (nm)',W/2-24,H-6);
  g.save();g.translate(14,H/2+40);g.rotate(-Math.PI/2);g.fillText('強さ（自動スケール）',0,0);g.restore();
  // プランク曲線（自動スケール）
  var peak=0;for(var px=1;px<=PW;px++){var lam=LMAX*px/PW;var v=planck(lam,T);if(v>peak)peak=v;}
  g.strokeStyle=bbColor(T);g.lineWidth=3;g.beginPath();
  for(px=1;px<=PW;px++){var lam2=LMAX*px/PW,y=PY0-PH*0.92*planck(lam2,T)/peak;
    if(px===1)g.moveTo(PX0+px,y);else g.lineTo(PX0+px,y);}
  g.stroke();g.lineWidth=1;
  // 古典（RJ）: 同じ縦スケールで
  if(showCl){g.strokeStyle='#ff7b72';g.setLineDash([6,5]);g.lineWidth=2;var st2=false;
    g.beginPath();
    for(px=1;px<=PW;px++){var lam3=LMAX*px/PW,y2=PY0-PH*0.92*rj(lam3,T)/peak;
      if(y2<PY0-PH){continue;}
      if(!st2){g.moveTo(PX0+px,y2);st2=true;}else g.lineTo(PX0+px,y2);}
    g.stroke();g.setLineDash([]);g.lineWidth=1;
    g.fillStyle='#ff7b72';g.fillText('古典理論 → 短波長で発散（紫外破綻）',PX0+70,PY0-PH+30);}
  // ウィーンのピーク
  var lmax=2.898e6/T;
  if(lmax<LMAX){var wx=PX0+PW*lmax/LMAX;
    g.strokeStyle='#ffd257';g.setLineDash([4,4]);g.beginPath();g.moveTo(wx,PY0);g.lineTo(wx,PY0-PH*0.95);g.stroke();g.setLineDash([]);
    g.fillStyle='#ffd257';g.fillText('ピーク '+lmax.toFixed(0)+' nm',Math.min(wx+6,W-110),PY0-PH*0.95+12);}
  document.getElementById('rW').textContent=lmax.toFixed(0)+' nm';
  var P=5.67e-8*Math.pow(T,4);
  document.getElementById('rS').textContent=P>1e6?(P/1e6).toFixed(2)+' MW/m²':(P/1000).toFixed(1)+' kW/m²';
  var rc=document.getElementById('rC');rc.textContent='■';rc.style.color=bbColor(T);
}
Ts.addEventListener('input',render);render();''')

# ===== 06 アインシュタイン: 光電効果の定量版（E=hν, Kmax=hν−W） =====
SIM["06_1921_einstein.html"] = (r'''    <h2>実験してみよう ── 光電効果の法則 K = hν − W を確かめる</h2>
    <div class="hint">金属を選び、光の波長と明るさを変えて、飛び出す電子の最大運動エネルギー K<sub>max</sub>（＝阻止電圧×e）を測ります。グラフの横軸は振動数 ν。<b>点が乗る直線の傾きがプランク定数 h</b> になっている──これがアインシュタインの式です。</div>
    <div class="xbox"><canvas id="cv" width="640" height="320"></canvas></div>
    <div class="btns">
      <button data-w="2.28" class="on">ナトリウム（W=2.28 eV）</button>
      <button data-w="4.31">亜鉛（W=4.31 eV）</button>
      <button data-w="5.65">白金（W=5.65 eV）</button>
    </div>
    <div class="cpanel">
      <div class="ctl"><label>光の波長 λ <output id="oL">400 nm</output></label><input id="L" type="range" min="150" max="700" value="400"></div>
      <div class="ctl"><label>明るさ（光子の数） <output id="oB">50 %</output></label><input id="B" type="range" min="10" max="100" value="50"></div>
    </div>
    <div class="status no" id="st">–</div>
    <div class="rpanel"><span>光子1個のエネルギー hν <b id="rE">–</b></span><span>K<sub>max</sub>（阻止電圧） <b id="rK">–</b></span><span>しきい波長 λ₀ <b id="rT">–</b></span><span>光電流 <b id="rI">–</b></span></div>
    <div class="note">hν = 1240/λ[nm] eV、K<sub>max</sub> = hν − W という実式の計算です。<b>明るさを変えても K<sub>max</sub>（グラフの点）は動かず、電流だけが変わる</b>こと、金属を変えると直線が平行移動するだけで<b>傾き（h）は変わらない</b>ことを確かめてください。この直線の傾きから h を精密測定したのが1923年受賞のミリカンです。</div>''',
r'''var cv=document.getElementById('cv'),g=cv.getContext('2d'),W=cv.width,H=cv.height;
var Ls=document.getElementById('L'),Bs=document.getElementById('B'),st=document.getElementById('st');
var Wf=2.28,btns=document.querySelectorAll('.btns button');
btns.forEach(function(b){b.addEventListener('click',function(){Wf=+b.dataset.w;
  btns.forEach(function(x){x.classList.toggle('on',x===b)});render();});});
var PX0=60,PY0=H-42,PW=W-96,PH=H-76,FMAX=2.1,KMAX=5.5;  // ν 0..2.1 PHz, K 0..5.5 eV
function fx(f){return PX0+PW*f/FMAX;} function ky(k){return PY0-PH*k/KMAX;}
function render(){
  var lam=+Ls.value,bri=+Bs.value;
  var f=299.79/lam;         // ν (×10^15 Hz)
  var E=1239.84/lam;        // eV
  var K=E-Wf;
  document.getElementById('oL').textContent=lam+' nm';
  document.getElementById('oB').textContent=bri+' %';
  g.clearRect(0,0,W,H);
  g.font='12px sans-serif';
  // 軸
  g.strokeStyle='#8b93a7';g.beginPath();g.moveTo(PX0,PY0-PH);g.lineTo(PX0,PY0);g.lineTo(PX0+PW,PY0);g.stroke();
  g.fillStyle='#8b93a7';
  for(var i=0;i<=2;i+=0.5)g.fillText(i.toFixed(1),fx(i)-8,PY0+16);
  g.fillText('振動数 ν (×10¹⁵ Hz)',W/2-50,H-6);
  for(var k=0;k<=5;k++){g.fillText(k,PX0-16,ky(k)+4);
    g.strokeStyle='#232b3d';g.beginPath();g.moveTo(PX0,ky(k));g.lineTo(PX0+PW,ky(k));g.stroke();}
  g.save();g.translate(14,H/2+30);g.rotate(-Math.PI/2);g.fillText('Kmax = e×阻止電圧 (eV)',0,0);g.restore();
  // 3金属の直線 K=hν−W（h=4.136 eV/PHz）
  var METALS=[[2.28,'#ffd257','Na'],[4.31,'#79c0ff','Zn'],[5.65,'#d2a8ff','Pt']];
  METALS.forEach(function(mm){var w0=mm[0],f0=w0/4.1357;
    g.strokeStyle=mm[1];g.globalAlpha=(Math.abs(w0-Wf)<0.01?1:0.3);g.lineWidth=(Math.abs(w0-Wf)<0.01?2.5:1.5);
    g.beginPath();g.moveTo(fx(f0),ky(0));
    var fEnd=FMAX,kEnd=4.1357*fEnd-w0;if(kEnd>KMAX){kEnd=KMAX;fEnd=(kEnd+w0)/4.1357;}
    g.lineTo(fx(fEnd),ky(kEnd));g.stroke();
    g.fillStyle=mm[1];g.fillText(mm[2]+' (W='+w0+'eV)',fx(f0)+4,PY0-10);
    g.globalAlpha=1;g.lineWidth=1;});
  g.fillStyle='#8b93a7';g.fillText('傾き = プランク定数 h',PX0+PW-160,ky(KMAX)+18);
  // 現在の測定点
  if(K>0){g.fillStyle='#7ee787';g.beginPath();g.arc(fx(f),ky(Math.min(K,KMAX)),7,0,7);g.fill();}
  else{g.fillStyle='#ff7b72';g.beginPath();g.arc(fx(f),ky(0),7,0,7);g.fill();}
  document.getElementById('rE').textContent=E.toFixed(2)+' eV';
  document.getElementById('rT').textContent=(1239.84/Wf).toFixed(0)+' nm';
  if(K>0){st.className='status yes';
    st.textContent='電子が飛び出す！ 阻止電圧 '+K.toFixed(2)+' V までの電子が観測される';
    document.getElementById('rK').textContent=K.toFixed(2)+' eV（'+K.toFixed(2)+' V）';
    document.getElementById('rI').textContent='明るさに比例（相対値 '+bri+'）';}
  else{st.className='status no';
    st.textContent='hν < W ── どれだけ明るくしても電子は1個も出ない（波の理論では説明不可能）';
    document.getElementById('rK').textContent='0（放出なし）';
    document.getElementById('rI').textContent='0';}
}
[Ls,Bs].forEach(function(s){s.addEventListener('input',render);});render();''')

# ===== 07 ボーア: 水素原子のエネルギー準位とスペクトル系列（リュードベリの式） =====
SIM["07_1922_bohr.html"] = (r'''    <h2>実験してみよう ── 電子を飛び移らせてスペクトルを作る</h2>
    <div class="hint">水素原子で、電子が「出発する準位 n<sub>i</sub>」から「落ち着く準位 n<sub>f</sub>」へ飛び移るときに出る光を計算します。n<sub>f</sub>=2 に落ちる系列（バルマー系列）だけが可視光になることを確かめましょう。</div>
    <div class="xbox"><canvas id="cv" width="640" height="330"></canvas></div>
    <div class="cpanel">
      <div class="ctl"><label>出発の準位 n<sub>i</sub> <output id="oNi">3</output></label><input id="Ni" type="range" min="2" max="7" value="3"></div>
      <div class="ctl"><label>落ち着く準位 n<sub>f</sub> <output id="oNf">2</output></label><input id="Nf" type="range" min="1" max="4" value="2"></div>
    </div>
    <div class="rpanel"><span>エネルギー差 ΔE <b id="rE">–</b></span><span>光の波長 λ <b id="rL">–</b></span><span>系列 <b id="rS">–</b></span></div>
    <div class="note">E<sub>n</sub> = −13.6/n² eV、1/λ = R(1/n<sub>f</sub>² − 1/n<sub>i</sub>²) という水素原子の実式です。n<sub>f</sub>=1 はライマン系列（紫外線）、n<sub>f</sub>=2 はバルマー系列（可視光：Hα 656 nm の赤い線など）、n<sub>f</sub>=3 はパッシェン系列（赤外線）。実際の水素放電管のスペクトルがこの式と小数点以下まで一致したことが、ボーア模型の勝利でした。</div>''',
r'''var cv=document.getElementById('cv'),g=cv.getContext('2d'),W=cv.width,H=cv.height;
var Ni=document.getElementById('Ni'),Nf=document.getElementById('Nf');
function eLev(n){return -13.6/(n*n);}
function eY(E){return 40+(H-120)*(E-(-13.6))/13.6*(-1)+(H-120);} // map: E=0→y=40, E=-13.6→y=H-80
function levY(E){return 40+(0-E)/13.6*(H-120);}
function wl2rgb(w){var r=0,gg=0,b=0;
  if(w<380)return [150,150,170];
  if(w<440){r=-(w-440)/60;b=1;}else if(w<490){gg=(w-440)/50;b=1;}
  else if(w<510){gg=1;b=-(w-510)/20;}else if(w<580){r=(w-510)/70;gg=1;}
  else if(w<645){r=1;gg=-(w-645)/65;}else if(w<=780){r=1;}
  else return [180,140,140];
  return [Math.round(255*r),Math.round(255*gg),Math.round(255*b)];}
function render(){
  var ni=+Ni.value,nf=+Nf.value;
  document.getElementById('oNi').textContent=ni;document.getElementById('oNf').textContent=nf;
  g.clearRect(0,0,W,H);g.font='12px sans-serif';
  if(nf>=ni){g.fillStyle='#ffd257';g.fillText('n(f) は n(i) より小さくしてください（外→内 に落ちるとき光が出ます）',60,H/2);
    document.getElementById('rE').textContent='–';document.getElementById('rL').textContent='–';
    document.getElementById('rS').textContent='–';return;}
  // 左: 準位図
  var LX0=60,LX1=280;
  for(var n=1;n<=7;n++){var y=levY(eLev(n));
    g.strokeStyle=(n===ni||n===nf)?'#ffd257':'#3a4356';g.lineWidth=(n===ni||n===nf)?2.5:1.5;
    g.beginPath();g.moveTo(LX0,y);g.lineTo(LX1,y);g.stroke();
    g.fillStyle='#8b93a7';g.fillText('n='+n+'  ('+eLev(n).toFixed(2)+' eV)',LX1+6,y+4);}
  g.lineWidth=1;
  var dE=eLev(ni)-eLev(nf),lam=1239.84/dE;
  var c=wl2rgb(lam),col='rgb('+c[0]+','+c[1]+','+c[2]+')';
  // 矢印
  var ax=(LX0+LX1)/2,y1=levY(eLev(ni)),y2=levY(eLev(nf));
  g.strokeStyle=col;g.lineWidth=3;g.beginPath();g.moveTo(ax,y1);g.lineTo(ax,y2-8);g.stroke();
  g.beginPath();g.moveTo(ax,y2);g.lineTo(ax-6,y2-10);g.lineTo(ax+6,y2-10);g.closePath();g.fillStyle=col;g.fill();
  // 波線の光子
  g.strokeStyle=col;g.lineWidth=2;g.beginPath();
  for(var i=0;i<=40;i++){var px=ax+20+i*1.8,py=(y1+y2)/2-14*Math.sin(i/3);
    if(i===0)g.moveTo(px,py);else g.lineTo(px,py);}
  g.stroke();g.lineWidth=1;
  // 右下: スペクトル帯 (対数 90..2000nm)
  var SX0=60,SW=W-120,SY=H-46;
  var l0=Math.log(90),l1=Math.log(2000);
  function sx(l){return SX0+SW*(Math.log(l)-l0)/(l1-l0);}
  for(var px2=0;px2<=SW;px2++){var lam2=Math.exp(l0+(l1-l0)*px2/SW);
    var cc=wl2rgb(lam2);g.fillStyle=(lam2<380||lam2>780)?'#20242e':'rgb('+cc[0]+','+cc[1]+','+cc[2]+')';
    g.fillRect(SX0+px2,SY,1.5,20);}
  g.fillStyle='#8b93a7';
  [100,200,400,700,1000,2000].forEach(function(l){g.fillText(l,sx(l)-10,SY+34);});
  g.fillText('紫外線',sx(150)-16,SY-6);g.fillText('可視光',sx(520)-16,SY-6);g.fillText('赤外線',sx(1300)-16,SY-6);
  g.fillText('波長 (nm・対数目盛)',SX0+SW-120,SY+34);
  var lx=sx(Math.max(90,Math.min(2000,lam)));
  g.strokeStyle=col;g.lineWidth=3;g.beginPath();g.moveTo(lx,SY-4);g.lineTo(lx,SY+24);g.stroke();g.lineWidth=1;
  document.getElementById('rE').textContent=dE.toFixed(2)+' eV';
  document.getElementById('rL').textContent=lam.toFixed(0)+' nm';
  var ser=nf===1?'ライマン系列（紫外線）':nf===2?'バルマー系列（可視光）':nf===3?'パッシェン系列（赤外線）':'ブラケット系列（赤外線）';
  document.getElementById('rS').textContent=ser;
}
[Ni,Nf].forEach(function(s){s.addEventListener('input',render);});render();''')

# ===== 08 ミリカン: 油滴実験（電圧でつり合わせ、電荷の量子化を発見する） =====
SIM["08_1923_millikan.html"] = (r'''    <h2>実験してみよう ── 油滴を浮かせて電気素量 e を測る</h2>
    <div class="hint">帯電した油滴が極板の間に浮かんでいます。<b>電圧を調節して油滴を空中で静止</b>させると、電気の力 qV/d と重力 mg のつり合いから電荷 q が求まります。「記録」してから「新しい油滴」で何滴も測ると……右のグラフに<b>階段</b>が見えてきます。</div>
    <div class="xbox"><canvas id="cv" width="640" height="300"></canvas></div>
    <div class="cpanel">
      <div class="ctl"><label>極板の電圧 <output id="oV">0 V</output></label><input id="V" type="range" min="0" max="600" value="0"></div>
    </div>
    <div class="btns"><button id="rec">この油滴を記録する</button><button id="new">新しい油滴に替える</button></div>
    <div class="status no" id="st">電圧を上げて油滴を静止させましょう</div>
    <div class="rpanel"><span>油滴の半径（顕微鏡で測定済み） <b id="rR">–</b></span><span>この油滴の電荷 q <b id="rQ">–</b></span><span>記録から推定した e <b id="rE">–</b></span></div>
    <div class="note">つり合いの式 q = mgd/V（極板間隔 d=5 mm、油の密度 886 kg/m³）による計算で、油滴の動きはストークスの空気抵抗を含めて再現しています（速度は見やすく拡大）。測った q が必ず <b>1.6×10⁻¹⁹ C の整数倍</b>になる──電気には最小単位 e があり、それより細かく分けられないことを、ミリカンはこの方法で示しました。</div>''',
r'''var cv=document.getElementById('cv'),g=cv.getContext('2d'),W=cv.width,H=cv.height;
var Vs=document.getElementById('V'),st=document.getElementById('st');
var E0=1.602e-19,RHO=886,GRAV=9.81,DGAP=0.005,ETA=1.82e-5;
var drop,recs=[];
function newDrop(){drop={r:(0.45+Math.random()*0.35)*1e-6,n:1+Math.floor(Math.random()*4),y:80};render();}
document.getElementById('new').addEventListener('click',newDrop);
document.getElementById('rec').addEventListener('click',function(){
  var V=+Vs.value;if(V<=0)return;
  var m=4/3*Math.PI*Math.pow(drop.r,3)*RHO;
  var qTrue=drop.n*E0,Fe=qTrue*V/DGAP,Fg=m*GRAV;
  if(Math.abs(Fe-Fg)/Fg>0.03){st.className='status no';st.textContent='まだ動いています ── 静止させてから記録しましょう';return;}
  var qMeas=m*GRAV*DGAP/V;recs.push(qMeas);newDrop();
  st.className='status yes';st.textContent='記録しました（'+recs.length+' 滴目）── 新しい油滴で続けましょう';});
var vy=0;
function loop(){
  var V=+Vs.value;document.getElementById('oV').textContent=V+' V';
  var m=4/3*Math.PI*Math.pow(drop.r,3)*RHO;
  var q=drop.n*E0,F=q*V/DGAP-m*GRAV;
  var vterm=F/(6*Math.PI*ETA*drop.r);       // 終端速度 (上向き正)
  drop.y-=vterm*4e5*0.016;                  // 表示は拡大
  if(drop.y<44)drop.y=44; if(drop.y>H-64)drop.y=H-64;
  render();
  var bal=Math.abs(F)/(m*GRAV);
  if(V===0){st.className='status no';st.textContent='電圧ゼロ ── 油滴は落ちていく（電圧を上げてみましょう）';}
  else if(bal<0.03){st.className='status yes';st.textContent='静止した！ つり合いから q = mgd/V が求まる ──「記録」を押そう';}
  else if(F>0){st.className='status no';st.textContent='電気の力が強すぎて上昇中 ── 電圧を下げる';}
  else{st.className='status no';st.textContent='まだ重力が勝って落下中 ── 電圧を上げる';}
  requestAnimationFrame(loop);
}
function render(){
  g.clearRect(0,0,W,H);g.font='12px sans-serif';
  // 左: 実験箱
  g.fillStyle='#ff8a8a';g.fillRect(30,34,330,8);g.fillStyle='#8ab6ff';g.fillRect(30,H-52,330,8);
  g.fillStyle='#8b93a7';g.fillText('＋極板',34,30);g.fillText('−極板（間隔 d=5mm）',34,H-32);
  g.fillStyle='#ffd257';g.beginPath();g.arc(195,drop.y,Math.max(4,drop.r*1e7),0,7);g.fill();
  g.fillStyle='#8b93a7';g.fillText('油滴',210,drop.y+4);
  document.getElementById('rR').textContent=(drop.r*1e6).toFixed(2)+' μm';
  var V=+Vs.value,m=4/3*Math.PI*Math.pow(drop.r,3)*RHO;
  var bal=V>0?Math.abs(drop.n*E0*V/DGAP-m*GRAV)/(m*GRAV):1;
  document.getElementById('rQ').textContent=(V>0&&bal<0.03)?(m*GRAV*DGAP/V/1e-19).toFixed(2)+'×10⁻¹⁹ C':'（静止させると測定できる）';
  // 右: 記録チャート
  var CX0=400,CW=W-CX0-60,CY0=H-50,CH=H-90;
  g.strokeStyle='#8b93a7';g.beginPath();g.moveTo(CX0,CY0-CH);g.lineTo(CX0,CY0);g.lineTo(CX0+CW,CY0);g.stroke();
  g.fillStyle='#8b93a7';g.fillText('測った電荷 q (×10⁻¹⁹C)',CX0-6,CY0-CH-8);g.fillText('油滴の番号',CX0+CW-60,CY0+16);
  var QMAX=8e-19;
  for(var k=1;k<=4;k++){var yy=CY0-CH*(k*E0)/QMAX;
    g.strokeStyle='#3a4356';g.setLineDash([3,4]);g.beginPath();g.moveTo(CX0,yy);g.lineTo(CX0+CW,yy);g.stroke();g.setLineDash([]);
    g.fillStyle='#5c6470';g.fillText(k+'e',CX0+CW+4,yy+4);}
  recs.forEach(function(q,i){var xx=CX0+14+i*16,yy=CY0-CH*q/QMAX;
    g.fillStyle='#7ee787';g.beginPath();g.arc(xx,yy,4,0,7);g.fill();});
  if(recs.length>=2){var eEst=0,cnt=0;
    recs.forEach(function(q){var n=Math.round(q/E0);if(n>0){eEst+=q/n;cnt++;}});
    eEst/=cnt;
    document.getElementById('rE').textContent=(eEst/1e-19).toFixed(3)+'×10⁻¹⁹ C（真値 1.602）';}
  else document.getElementById('rE').textContent='2滴以上記録すると計算されます';
}
Vs.addEventListener('input',function(){});newDrop();loop();''')

# ===== 09 コンプトン: 散乱角と波長シフト（Δλ = λc(1−cosθ)） =====
SIM["09_1927_compton.html"] = (r'''    <h2>実験してみよう ── X線を電子にぶつけて「粒」を確かめる</h2>
    <div class="hint">X線の光子を電子に当てて、散乱角 θ を変えながら散乱後の波長を測ります。光が波なら波長は変わらないはず。でも粒（光子）なら、ビリヤードのように電子へエネルギーを渡すぶん<b>波長が伸びる</b>はずです。</div>
    <div class="xbox"><canvas id="cv" width="640" height="300"></canvas></div>
    <div class="cpanel">
      <div class="ctl"><label>散乱角 θ <output id="oA">90°</output></label><input id="A" type="range" min="0" max="180" value="90"></div>
      <div class="ctl"><label>入射X線の波長 λ <output id="oL">7.1 pm</output></label><input id="L" type="range" min="20" max="200" value="71"></div>
    </div>
    <div class="rpanel"><span>波長ののび Δλ <b id="rD">–</b></span><span>散乱後の波長 λ′ <b id="rL2">–</b></span><span>光子のエネルギー <b id="rE">–</b></span><span>電子がもらう運動エネルギー <b id="rT">–</b></span></div>
    <div class="note">コンプトンの式 <b>Δλ = (h/m<sub>e</sub>c)(1−cosθ)</b> の正確な計算です。h/m<sub>e</sub>c = 2.43 pm（コンプトン波長）は光子・電子の相対論的な衝突運動学だけから決まり、入射波長にはよりません。θ=90°でちょうど 2.43 pm 伸びること、λ=7.1 pm（モリブデンKα線）はコンプトンが実際に使った値であることも試してみてください。電子の向きは運動量保存から計算しています。</div>''',
r'''var cv=document.getElementById('cv'),g=cv.getContext('2d'),W=cv.width,H=cv.height;
var As=document.getElementById('A'),Ls=document.getElementById('L');
var LC=2.4263;  // pm
function render(){
  var th=+As.value*Math.PI/180,lam=+Ls.value/10;
  document.getElementById('oA').textContent=As.value+'°';
  document.getElementById('oL').textContent=lam.toFixed(1)+' pm';
  var dl=LC*(1-Math.cos(th)),lam2=lam+dl;
  var E=1239.84/lam,E2=1239.84/lam2;            // keV (hc=1239.84 keV·pm)
  g.clearRect(0,0,W,H);g.font='12px sans-serif';
  // 左: 散乱のベクトル図
  var ox=170,oy=H/2;
  g.strokeStyle='#3a4356';g.beginPath();g.arc(ox,oy,8,0,7);g.stroke();
  g.fillStyle='#8ab6ff';g.beginPath();g.arc(ox,oy,6,0,7);g.fill();
  g.fillStyle='#8b93a7';g.fillText('電子',ox-12,oy+24);
  // 入射光子
  g.strokeStyle='#d2a8ff';g.lineWidth=3;g.beginPath();g.moveTo(30,oy);g.lineTo(ox-10,oy);g.stroke();
  g.fillStyle='#d2a8ff';g.fillText('入射X線 '+E.toFixed(0)+' keV',30,oy-12);
  // 散乱光子 (長さ∝運動量 1/λ)
  var Lin=110,Lout=Lin*lam/lam2;
  var sx=ox+Lout*Math.cos(th),sy=oy-Lout*Math.sin(th);
  g.strokeStyle='#ff9a8a';g.beginPath();g.moveTo(ox,oy);g.lineTo(sx,sy);g.stroke();
  g.fillStyle='#ff9a8a';g.fillText('散乱X線 '+E2.toFixed(0)+' keV',sx-30,sy-10);
  // 電子の反跳（運動量保存: p_e = p_in − p_out）
  var pex=Lin-Lout*Math.cos(th),pey=Lout*Math.sin(th);
  var pl=Math.sqrt(pex*pex+pey*pey);
  if(pl>2){g.strokeStyle='#7ee787';g.beginPath();g.moveTo(ox,oy);g.lineTo(ox+pex,oy+pey);g.stroke();
    g.fillStyle='#7ee787';g.fillText('反跳電子',ox+pex-16,oy+pey+16);}
  g.lineWidth=1;
  // 角度弧
  g.strokeStyle='#8b93a7';g.beginPath();g.arc(ox,oy,26,0,-th,true);g.stroke();
  g.fillStyle='#8b93a7';g.fillText('θ',ox+32*Math.cos(th/2),oy-32*Math.sin(th/2)+4);
  // 右: Δλ vs θ 曲線
  var PX0=400,PW=W-PX0-40,PY0=H-40,PH=H-80;
  g.strokeStyle='#8b93a7';g.beginPath();g.moveTo(PX0,PY0-PH);g.lineTo(PX0,PY0);g.lineTo(PX0+PW,PY0);g.stroke();
  g.fillStyle='#8b93a7';g.fillText('Δλ (pm)',PX0-4,PY0-PH-8);g.fillText('θ',PX0+PW+8,PY0+4);
  g.fillText('0°',PX0-6,PY0+16);g.fillText('90°',PX0+PW/2-8,PY0+16);g.fillText('180°',PX0+PW-14,PY0+16);
  [LC,2*LC].forEach(function(v,i){var yy=PY0-PH*v/(2*LC*1.1);
    g.strokeStyle='#3a4356';g.setLineDash([3,4]);g.beginPath();g.moveTo(PX0,yy);g.lineTo(PX0+PW,yy);g.stroke();g.setLineDash([]);
    g.fillStyle='#5c6470';g.fillText((i+1)+'×2.43',PX0+PW-40,yy-4);});
  g.strokeStyle='#ffb454';g.lineWidth=2.5;g.beginPath();
  for(var px=0;px<=PW;px++){var t2=Math.PI*px/PW,v=LC*(1-Math.cos(t2));
    var yy2=PY0-PH*v/(2*LC*1.1);if(px===0)g.moveTo(PX0,yy2);else g.lineTo(PX0+px,yy2);}
  g.stroke();g.lineWidth=1;
  var mx=PX0+PW*(+As.value)/180,my=PY0-PH*dl/(2*LC*1.1);
  g.fillStyle='#ffd257';g.beginPath();g.arc(mx,my,6,0,7);g.fill();
  document.getElementById('rD').textContent=dl.toFixed(2)+' pm';
  document.getElementById('rL2').textContent=lam2.toFixed(2)+' pm';
  document.getElementById('rE').textContent=E.toFixed(0)+' keV → '+E2.toFixed(0)+' keV';
  document.getElementById('rT').textContent=(E-E2).toFixed(1)+' keV';
}
[As,Ls].forEach(function(s){s.addEventListener('input',render);});render();''')

# ===== 10 ド・ブロイ: 物質波の波長と電子回折（λ = h/√(2meV)） =====
SIM["10_1929_de_broglie.html"] = (r'''    <h2>実験してみよう ── 電子を波として回折させる</h2>
    <div class="hint">電子を加速して薄い黒鉛（グラファイト）の膜に当てると、蛍光スクリーンに<b>回折リング</b>が現れます──電子が波だからです。加速電圧を変えると波長 λ = h/√(2meV) が変わり、リングの大きさが変わります。</div>
    <div class="xbox"><canvas id="cv" width="640" height="300"></canvas></div>
    <div class="cpanel">
      <div class="ctl"><label>加速電圧 <output id="oV">4000 V</output></label><input id="V" type="range" min="500" max="10000" value="4000" step="100"></div>
    </div>
    <div class="btns"><button id="be" class="on">電子</button><button id="bp">陽子（質量1836倍）</button></div>
    <div class="rpanel"><span>ド・ブロイ波長 λ <b id="rL">–</b></span><span>第1リングの半径 <b id="rR">–</b></span><span>比較：黒鉛の面間隔 <b>d=213 pm</b></span></div>
    <div class="note">λ = h/√(2mqV)（非相対論）とブラッグの条件 2d sinθ = λ による計算です（膜からスクリーンまで 13.5 cm、黒鉛の面間隔 d₁=213 pm, d₂=123 pm）。<b>電圧を上げるほど波長が短くなりリングが縮む</b>のは波の証拠。同じ電圧でも質量の大きい陽子では波長が数十分の一になり、リングがほぼ点につぶれることも確かめてください。この実験（G.P.トムソン、デイヴィソン＝ガーマー：1937年受賞）がド・ブロイの理論を裏づけました。</div>''',
r'''var cv=document.getElementById('cv'),g=cv.getContext('2d'),W=cv.width,H=cv.height;
var Vs=document.getElementById('V'),be=document.getElementById('be'),bp=document.getElementById('bp');
var mass=1;  // 1=電子, 1836=陽子
be.addEventListener('click',function(){mass=1;be.classList.add('on');bp.classList.remove('on');render();});
bp.addEventListener('click',function(){mass=1836;bp.classList.add('on');be.classList.remove('on');render();});
var D1=213,D2=123,LSCR=0.135;  // pm, m
function render(){
  var V=+Vs.value;document.getElementById('oV').textContent=V+' V';
  var lam=1226.4/Math.sqrt(mass*V);   // pm
  g.clearRect(0,0,W,H);g.font='12px sans-serif';
  // 左: 装置図
  g.fillStyle='#8b93a7';g.fillRect(24,H/2-14,18,28);g.fillText('電子銃',18,H/2+34);
  g.strokeStyle='#7ee787';g.lineWidth=2;
  // 波として描くビーム（波長に応じた波々）
  var per=Math.max(3,lam/2);
  g.beginPath();for(var x=44;x<=170;x++){var y=H/2+5*Math.sin((x-44)/per*2*Math.PI);
    if(x===44)g.moveTo(x,y);else g.lineTo(x,y);}g.stroke();g.lineWidth=1;
  g.fillStyle='#9fb2c9';g.fillRect(172,H/2-40,6,80);g.fillStyle='#8b93a7';g.fillText('黒鉛膜',158,H/2+58);
  // スクリーン(右の円)
  var sx=430,sy=H/2,SR=120;
  g.fillStyle='#101720';g.beginPath();g.arc(sx,sy,SR,0,7);g.fill();
  g.strokeStyle='#2a3446';g.beginPath();g.arc(sx,sy,SR,0,7);g.stroke();
  g.fillStyle='#8b93a7';g.fillText('蛍光スクリーン（直径12 cm）',sx-80,sy+SR+18);
  // 中心スポット
  g.fillStyle='#b6ffcf';g.beginPath();g.arc(sx,sy,3,0,7);g.fill();
  // リング: 2d sinθ=λ, 画面半径 R=L tan(2θ)。スケール: SR px = 6cm
  var scale=SR/0.06;
  var rr=[];
  [[D1,1],[D2,0.7],[D1,2]].forEach(function(pair){var d=pair[0],ord=pair[1]<1?1:pair[1];var amp=pair[1]<1?0.7:1/ord;
    var s=ord*lam/(2*d);if(s<1){var th=Math.asin(s),R=LSCR*Math.tan(2*th)*scale;
      if(R<SR*0.98&&R>1){g.strokeStyle='rgba(126,231,135,'+(0.9*amp)+')';g.lineWidth=Math.max(1.5,4-R/40);
        g.beginPath();g.arc(sx,sy,R,0,7);g.stroke();rr.push(LSCR*Math.tan(2*th)*1000);}}});
  g.lineWidth=1;
  // ビーム線 膜→スクリーン
  g.strokeStyle='rgba(126,231,135,0.35)';g.beginPath();g.moveTo(178,H/2);g.lineTo(sx-SR,sy);g.stroke();
  document.getElementById('rL').textContent=lam>=10?lam.toFixed(1)+' pm':lam.toFixed(2)+' pm';
  document.getElementById('rR').textContent=rr.length?rr[0].toFixed(1)+' mm':'（リングが小さすぎて見えない）';
}
Vs.addEventListener('input',render);render();''')

# ===== 12 シュレーディンガー: 井戸型ポテンシャルの波動関数（En = n²h²/8mL²） =====
SIM["12_1933_schrodinger_dirac.html"] = (r'''    <h2>実験してみよう ── 箱に閉じ込めた電子の波</h2>
    <div class="hint">幅 L の「箱」（井戸型ポテンシャル）に電子を閉じ込めると、シュレーディンガー方程式の解は<b>両端がゼロの定在波</b>だけになり、エネルギーはとびとびの値 E<sub>n</sub> しか取れません。箱の幅と量子数 n を変えてみましょう。</div>
    <div class="xbox"><canvas id="cv" width="640" height="330"></canvas></div>
    <div class="cpanel">
      <div class="ctl"><label>箱の幅 L <output id="oL">1.00 nm</output></label><input id="L" type="range" min="30" max="300" value="100"></div>
      <div class="ctl"><label>量子数 n <output id="oN">1</output></label><input id="N" type="range" min="1" max="6" value="1"></div>
    </div>
    <div class="btns"><button id="bw" class="on">波動関数 ψ</button><button id="bp">存在確率 |ψ|²</button></div>
    <div class="rpanel"><span>エネルギー E<sub>n</sub> <b id="rE">–</b></span><span>n→n−1 で出る光の波長 <b id="rT">–</b></span></div>
    <div class="note">E<sub>n</sub> = n²π²ħ²/(2mL²)、ψ<sub>n</sub>(x) = √(2/L)·sin(nπx/L) という厳密解です。<b>箱を狭くするとエネルギーが L² に反比例して跳ね上がる</b>こと（電子を狭い場所に閉じ込めるには大きなエネルギーが要る＝原子がつぶれない理由の本質）、|ψ|² には電子が「見つかりやすい場所・絶対に見つからない場所（節）」があることを確かめてください。半導体の量子井戸レーザーはこの式そのもので発光色を設計しています。</div>''',
r'''var cv=document.getElementById('cv'),g=cv.getContext('2d'),W=cv.width,H=cv.height;
var Ls=document.getElementById('L'),Ns=document.getElementById('N');
var bw=document.getElementById('bw'),bp=document.getElementById('bp'),prob=false;
bw.addEventListener('click',function(){prob=false;bw.classList.add('on');bp.classList.remove('on');render();});
bp.addEventListener('click',function(){prob=true;bp.classList.add('on');bw.classList.remove('on');render();});
function En(n,L){return n*n*0.37603/(L*L);}   // eV (L in nm)
function render(){
  var L=+Ls.value/100,n=+Ns.value;
  document.getElementById('oL').textContent=L.toFixed(2)+' nm';
  document.getElementById('oN').textContent=n;
  g.clearRect(0,0,W,H);g.font='12px sans-serif';
  var X0=90,X1=W-180,YB=H-40,YT=36;
  var Emax=En(6,L)*1.08;
  function ey(E){return YB-(YB-YT)*E/Emax;}
  // 井戸の壁
  g.strokeStyle='#5c6470';g.lineWidth=3;g.beginPath();
  g.moveTo(X0,YT-6);g.lineTo(X0,YB);g.lineTo(X1,YB);g.lineTo(X1,YT-6);g.stroke();g.lineWidth=1;
  g.fillStyle='#8b93a7';g.fillText('L = '+L.toFixed(2)+' nm',(X0+X1)/2-30,YB+18);
  // 準位と波
  for(var k=1;k<=6;k++){var E=En(k,L),y=ey(E);
    var on=(k===n);
    g.strokeStyle=on?'#ffd257':'#3a4356';g.setLineDash(on?[]:[4,4]);
    g.beginPath();g.moveTo(X0,y);g.lineTo(X1,y);g.stroke();g.setLineDash([]);
    g.fillStyle=on?'#ffd257':'#5c6470';
    g.fillText('n='+k+'  '+E.toFixed(2)+' eV',X1+8,y+4);
    if(on){var A=Math.min(34,(ey(0)-ey(Emax))/14+18);
      g.strokeStyle='#c4b5fd';g.lineWidth=2.5;g.beginPath();
      for(var px=0;px<=X1-X0;px++){var s=Math.sin(k*Math.PI*px/(X1-X0));
        var v=prob?s*s:s;var yy=y-A*v;
        if(px===0)g.moveTo(X0,yy);else g.lineTo(X0+px,yy);}
      g.stroke();g.lineWidth=1;
      if(prob){g.fillStyle='rgba(196,181,253,0.25)';g.beginPath();g.moveTo(X0,y);
        for(px=0;px<=X1-X0;px++){var s2=Math.sin(k*Math.PI*px/(X1-X0));g.lineTo(X0+px,y-A*s2*s2);}
        g.lineTo(X1,y);g.closePath();g.fill();}}}
  var E1=En(n,L);
  document.getElementById('rE').textContent=E1.toFixed(2)+' eV';
  if(n>1){var dE=E1-En(n-1,L);var lam=1239.84/dE;
    document.getElementById('rT').textContent=lam>=1000?(lam/1000).toFixed(2)+' μm（赤外）':lam.toFixed(0)+' nm'+(lam<380?'（紫外）':lam<=780?'（可視光！）':'（赤外）');}
  else document.getElementById('rT').textContent='n=1 は基底状態（これ以上下がれない）';
}
[Ls,Ns].forEach(function(s){s.addEventListener('input',render);});render();''')

# ===== 13 チャドウィック: 反跳の運動学から中性子の質量を決める =====
SIM["13_1935_chadwick.html"] = (r'''    <h2>実験してみよう ── 見えない粒子の質量を「はじき飛ばし」から求める</h2>
    <div class="hint">正体不明の中性の放射線を<b>水素（陽子）</b>と<b>窒素</b>に当てたときの反跳の速さは測定できます。未知粒子の質量 m を仮定すると弾性衝突の式で反跳速度が予言できるので、<b>スライダーを動かして実測値と一致する質量を探して</b>ください──チャドウィックが実際にやった推理です。</div>
    <div class="xbox"><canvas id="cv" width="640" height="280"></canvas></div>
    <div class="cpanel">
      <div class="ctl"><label>仮定する未知粒子の質量 m <output id="oM">0.50 u</output></label><input id="M" type="range" min="5" max="300" value="50"></div>
    </div>
    <div class="status no" id="st">–</div>
    <div class="rpanel"><span>窒素の反跳の予言 <b id="rP">–</b></span><span>実測値 <b>4.7×10⁶ m/s</b></span><span>推定された質量 <b id="rM">–</b></span></div>
    <div class="note">正面弾性衝突の式 u = 2mv/(m+M) を使っています。粒子の速さ v は未知なので、まず水素の反跳の実測値（3.3×10⁷ m/s）に合うように v を決め、その同じ v で窒素（質量14 u）の反跳を予言して実測と比べます。<b>2つの実測を同時に説明できる質量はほぼ 1 u だけ</b>──陽子とほぼ同じ重さで電荷ゼロの粒子、中性子の発見です（γ線＝質量0の光では水素をこの速さではじき飛ばせないことも決め手でした）。</div>''',
r'''var cv=document.getElementById('cv'),g=cv.getContext('2d'),W=cv.width,H=cv.height;
var Ms=document.getElementById('M'),st=document.getElementById('st');
var UH=3.3e7,UN=4.7e6,MH=1.008,MN=14.003;   // 実測(想定)と標的質量
function render(){
  var m=+Ms.value/100;
  document.getElementById('oM').textContent=m.toFixed(2)+' u';
  // v0 を水素の実測に合わせて決める → 窒素を予言
  var v0=UH*(m+MH)/(2*m);
  var uN=2*m*v0/(m+MN);           // = UH*(m+MH)/(m+MN)
  g.clearRect(0,0,W,H);g.font='12px sans-serif';
  // 上: 衝突の図
  g.fillStyle='#8b93a7';g.fillText('未知粒子 (m, v)',40,34);
  g.fillStyle='#c4b5fd';g.beginPath();g.arc(60,60,Math.max(5,Math.min(16,8*Math.pow(m,1/3))),0,7);g.fill();
  g.strokeStyle='#c4b5fd';g.beginPath();g.moveTo(80,60);g.lineTo(130,60);g.stroke();
  g.fillStyle='#ff9a8a';g.beginPath();g.arc(180,60,7,0,7);g.fill();
  g.fillStyle='#8b93a7';g.fillText('水素の核（陽子, 1u）',200,50);
  g.fillText('→ 反跳 3.3×10⁷ m/s（実測）',200,70);
  g.fillStyle='#79c0ff';g.beginPath();g.arc(180,110,13,0,7);g.fill();
  g.fillStyle='#8b93a7';g.fillText('窒素の核（14u）',200,104);
  g.fillText('→ 反跳は？',200,124);
  // 下: 予言バー vs 実測バー
  var BX=120,BW=W-200,BY1=180,BY2=225,SC=BW/6e6;   // 6e6 m/s フルスケール
  g.fillStyle='#8b93a7';g.fillText('窒素の反跳速度',BX-100,BY1+13);
  g.fillText('　（×10⁶ m/s）',BX-100,BY1+29);
  // 目盛
  for(var v=0;v<=6;v++){var x=BX+v*1e6*SC;
    g.strokeStyle='#232b3d';g.beginPath();g.moveTo(x,BY1-14);g.lineTo(x,BY2+22);g.stroke();
    g.fillStyle='#5c6470';g.fillText(v,x-3,BY2+36);}
  var wP=Math.min(BW,uN*SC);
  g.fillStyle='#c4b5fd';g.fillRect(BX,BY1-10,wP,20);
  g.fillStyle='#e6e3d9';g.fillText('予言 '+(uN/1e6).toFixed(2),BX+wP+6,BY1+4);
  g.fillStyle='#7ee787';g.fillRect(BX,BY2-10,UN*SC,20);
  g.fillStyle='#e6e3d9';g.fillText('実測 4.70',BX+UN*SC+6,BY2+4);
  var err=Math.abs(uN-UN)/UN;
  document.getElementById('rP').textContent=(uN/1e6).toFixed(2)+'×10⁶ m/s';
  if(err<0.03){st.className='status yes';
    st.textContent='一致！ 質量 '+m.toFixed(2)+' u ── 陽子とほぼ同じ重さの中性粒子＝中性子だ';
    document.getElementById('rM').textContent='約 '+m.toFixed(2)+' u（現代の値 1.0087 u）';}
  else{st.className='status no';
    st.textContent=uN>UN?'予言が実測より速すぎる ── 質量を'+(m>1?'（もっと）小さく':'調整')+'してみよう':'予言が実測より遅い ── 質量を大きくしてみよう';
    document.getElementById('rM').textContent='まだ決まらない';}
}
Ms.addEventListener('input',render);render();''')

# ===== 23 パルサー: 自転周期から天体の正体を絞り込む（遠心力 vs 重力） =====
SIM["23_1974_pulsar.html"] = (r'''    <h2>実験してみよう ── パルスの周期から星の正体を推理する</h2>
    <div class="hint">パルサーは「宇宙の灯台」──自転する星のビームが地球を横切るたびに電波のパルスが届きます。周期を変えると、<b>その速さで自転してもバラバラにならない天体</b>がどれほど高密度でなければならないかが計算できます。ジョスリン・ベルが見つけた本物のパルサーも試してみましょう。</div>
    <div class="xbox"><canvas id="cv" width="640" height="300"></canvas></div>
    <div class="cpanel">
      <div class="ctl"><label>自転周期 P <output id="oP">0.10 秒</output></label><input id="P" type="range" min="0" max="100" value="60"></div>
      <div class="ctl"><label>ビームの幅 <output id="oB">10°</output></label><input id="B" type="range" min="4" max="25" value="10"></div>
    </div>
    <div class="btns">
      <button data-p="1337">CP1919（発見された最初のパルサー, 1.337秒）</button>
      <button data-p="33">かに星雲パルサー（0.033秒）</button>
      <button data-p="1.4">最速のミリ秒パルサー（0.0014秒）</button>
    </div>
    <div class="status no" id="st">–</div>
    <div class="rpanel"><span>必要な平均密度 <b id="rD">–</b></span><span>赤道の速さ（半径10 kmとして） <b id="rV">–</b></span></div>
    <div class="note">自転でちぎれ飛ばない条件（重力 &gt; 遠心力）から、平均密度は <b>ρ &gt; 3π/(GP²)</b> でなければなりません。周期 0.033 秒のかに星雲パルサーではこの下限が白色矮星の密度（〜10⁹ kg/m³）を大きく超え、<b>中性子星（〜10¹⁷ kg/m³）しかあり得ない</b>ことが分かります──パルサー発見が「中性子星は実在する」の証明になった理由です。灯台のアニメは実際より遅く再生しています。</div>''',
r'''var cv=document.getElementById('cv'),g=cv.getContext('2d'),W=cv.width,H=cv.height;
var Ps=document.getElementById('P'),Bs=document.getElementById('B'),st=document.getElementById('st');
document.querySelectorAll('.btns button').forEach(function(b){
  b.addEventListener('click',function(){var ms=+b.dataset.p;   // ミリ秒
    Ps.value=Math.round((Math.log10(ms/1000)+3)/3.3*100);
    document.querySelectorAll('.btns button').forEach(function(x){x.classList.toggle('on',x===b)});});});
var phase=0,last=null;
function period(){return Math.pow(10,-3+3.3*(+Ps.value)/100);}   // 0.001 .. 2 s
function loop(ts){
  if(last===null)last=ts;var dt=(ts-last)/1000;last=ts;
  var P=period();
  phase+=dt/Math.max(P,0.8)*2*Math.PI;      // 遅い再生（0.8s より速い周期はスロー表示）
  render();requestAnimationFrame(loop);
}
function render(){
  var P=period(),bw=+Bs.value*Math.PI/180;
  document.getElementById('oP').textContent=P>=0.01?P.toFixed(3)+' 秒':(P*1000).toFixed(1)+' ミリ秒';
  document.getElementById('oB').textContent=Bs.value+'°';
  g.clearRect(0,0,W,H);g.font='12px sans-serif';
  // 左: 灯台
  var cx=140,cy=120;
  for(var s2=0;s2<2;s2++){var a=phase+s2*Math.PI;
    var grd=g.createConicGradient?null:null;
    g.fillStyle='rgba(126,231,135,0.25)';
    g.beginPath();g.moveTo(cx,cy);g.arc(cx,cy,110,a-bw,a+bw);g.closePath();g.fill();}
  g.fillStyle='#c4b5fd';g.beginPath();g.arc(cx,cy,14,0,7);g.fill();
  g.strokeStyle='#8b93a7';g.beginPath();g.moveTo(cx,cy-22);g.lineTo(cx,cy+22);g.stroke();
  g.fillStyle='#8b93a7';g.fillText('中性子星（スロー再生）',cx-62,cy+140);
  g.fillText('地球へ→',cx+120,cy+4);
  // 右: パルス列（横軸は実時間）
  var PX0=300,PW=W-PX0-30,PY0=200,PH=110;
  g.strokeStyle='#8b93a7';g.beginPath();g.moveTo(PX0,PY0);g.lineTo(PX0+PW,PY0);g.stroke();
  var TW=4*P;   // 窓=4周期
  g.fillStyle='#8b93a7';
  g.fillText('受かる電波の強さ',PX0,PY0-PH-10);
  g.fillText('0',PX0-4,PY0+16);
  g.fillText(TW>=0.01?TW.toFixed(2)+' 秒':(TW*1000).toFixed(1)+' ミリ秒',PX0+PW-56,PY0+16);
  g.strokeStyle='#7ee787';g.lineWidth=2;g.beginPath();
  var obs=phase%(2*Math.PI);
  for(var px=0;px<=PW;px++){var t=TW*px/PW;
    var ph2=(t/P*2*Math.PI+obs)%Math.PI;var dd=Math.min(ph2,Math.PI-ph2);
    var I=Math.exp(-dd*dd/(2*bw*bw));
    var y=PY0-PH*I;if(px===0)g.moveTo(PX0,y);else g.lineTo(PX0+px,y);}
  g.stroke();g.lineWidth=1;
  // 密度の下限
  var G=6.674e-11,rho=3*Math.PI/(G*P*P);
  var v=2*Math.PI*1e4/P,c=2.998e8;
  document.getElementById('rD').textContent=(rho/1e9>=1000?(rho/1e12).toFixed(1)+'×10¹² ':(rho/1e9).toFixed(2)+'×10⁹ ')+'kg/m³ 以上';
  document.getElementById('rV').textContent=v/c>0.003?(v/c*100).toFixed(1)+'% × 光速':(v/1000).toFixed(0)+' km/s';
  if(rho>1e10){st.className='status yes';st.textContent='白色矮星（〜10⁹ kg/m³）ではちぎれ飛ぶ ── 中性子星しかあり得ない！';}
  else{st.className='status no';st.textContent='この周期なら白色矮星でもぎりぎり可能 ── 周期を短くすると…？';}
}
requestAnimationFrame(loop);''')

# ===== 24 CMB: 宇宙の温度と黒体スペクトル（T ∝ 1+z） =====
SIM["24_1978_cmb.html"] = (r'''    <h2>実験してみよう ── 宇宙をさかのぼって「昔の光」を見る</h2>
    <div class="hint">ペンジアスとウィルソンが見つけた宇宙マイクロ波背景放射（CMB）は、いまは 2.725 K の黒体放射です。スライダーで宇宙をさかのぼる（赤方偏移 z を上げる）と、宇宙の温度とスペクトルがどう変わるか見てみましょう。</div>
    <div class="xbox"><canvas id="cv" width="640" height="310"></canvas></div>
    <div class="cpanel">
      <div class="ctl"><label>赤方偏移 z（どれだけ昔か） <output id="oZ">0</output></label><input id="Z" type="range" min="0" max="1100" value="0"></div>
    </div>
    <div class="rpanel"><span>宇宙の温度 T = 2.725(1+z) <b id="rT">–</b></span><span>ピーク波長 <b id="rL">–</b></span><span>およその時代 <b id="rA">–</b></span></div>
    <div class="note">宇宙が膨張すると光の波長は (1+z) 倍に引き伸ばされ、黒体放射は<b>黒体放射のまま温度だけ 1/(1+z) に下がります</b>。z=1100（約38万歳の宇宙）では T≈3000 K──「晴れ上がり」直後のオレンジ色に光る宇宙の光が、138億年かけて引き伸ばされてマイクロ波として届いているのがCMBです。z=0 の点は COBE 衛星の実測（波長1 mm付近）のイメージで、プランクの式との一致は0.005%以内という「宇宙一完璧な黒体」でした。年代は物質優勢近似 t∝(1+z)^{-3/2} の概算です。</div>''',
r'''var cv=document.getElementById('cv'),g=cv.getContext('2d'),W=cv.width,H=cv.height;
var Zs=document.getElementById('Z');
function bbColor(T){var t=T/100,r,gg,b;
  if(T<1000)return '#20242e';
  r=t<=66?255:Math.min(255,Math.max(0,329.7*Math.pow(t-60,-0.133)));
  gg=t<=66?Math.min(255,Math.max(0,99.47*Math.log(t)-161.1)):Math.min(255,Math.max(0,288.1*Math.pow(t-60,-0.0755)));
  b=t>=66?255:(t<=19?0:Math.min(255,Math.max(0,138.5*Math.log(t-10)-305)));
  return 'rgb('+Math.round(r)+','+Math.round(gg)+','+Math.round(b)+')';}
var PX0=60,PY0=0,PW=0,PH=0;
function render(){
  var z=+Zs.value,T=2.725*(1+z);
  document.getElementById('oZ').textContent=z;
  g.clearRect(0,0,W,H);g.font='12px sans-serif';
  var X0=60,Y0=H-44,PWi=W-100,PHi=H-84;
  // x軸: ν/νpeak 0..4 （形は温度によらず同じ＝黒体のまま、が要点）
  g.strokeStyle='#8b93a7';g.beginPath();g.moveTo(X0,Y0-PHi);g.moveTo(X0,Y0);g.lineTo(X0+PWi,Y0);g.stroke();
  var npk=160.23*(1+z);  // GHz
  g.fillStyle='#8b93a7';
  for(var i=0;i<=4;i++){var lb=npk*i;
    g.fillText(lb>=1e6?(lb/1e6).toFixed(1)+'PHz':lb>=1000?(lb/1000).toFixed(0)+'THz':lb.toFixed(0)+'GHz',X0+PWi*i/4-18,Y0+18);}
  g.fillText('周波数',W/2-20,H-6);
  g.save();g.translate(14,H/2+40);g.rotate(-Math.PI/2);g.fillText('強さ（相対値）',0,0);g.restore();
  // プランク曲線（無次元形状 x³/(e^x−1), ピーク x≈2.82）
  function shape(u){return u*u*u/(Math.exp(u)-1);}
  var pk=shape(2.821);
  g.strokeStyle=z<50?'#7ee787':bbColor(T);if(z>=50&&T<1000)g.strokeStyle='#ff9a8a';
  g.lineWidth=3;g.beginPath();
  for(var px=1;px<=PWi;px++){var u=2.821*4*px/PWi;var y=Y0-PHi*0.92*shape(u)/pk;
    if(px===1)g.moveTo(X0+px,y);else g.lineTo(X0+px,y);}
  g.stroke();g.lineWidth=1;
  // z=0 のとき COBE 実測点(イメージ)
  if(z===0){g.fillStyle='#ffd257';
    for(var k=1;k<=12;k++){var u2=2.821*4*k/13,xx=X0+PWi*k/13,yy=Y0-PHi*0.92*shape(u2)/pk;
      g.beginPath();g.arc(xx,yy,3.5,0,7);g.fill();}
    g.fillText('● COBE衛星の実測イメージ ── 完璧な黒体',X0+PWi-280,Y0-PHi+16);}
  // 宇宙の色見本
  g.fillStyle=bbColor(T);g.fillRect(W-90,20,54,30);
  g.strokeStyle='#3a4356';g.strokeRect(W-90,20,54,30);
  g.fillStyle='#8b93a7';g.fillText('宇宙の色',W-88,66);
  document.getElementById('rT').textContent=T>=1000?T.toFixed(0)+' K':T.toFixed(1)+' K';
  var lpk=1.063/(1+z);   // mm
  document.getElementById('rL').textContent=lpk>=0.01?lpk.toFixed(3)+' mm（マイクロ波）':(lpk*1e6).toFixed(0)+' nm';
  var age=13.8e9/Math.pow(1+z,1.5);
  document.getElementById('rA').textContent=z===0?'現在（138億歳）':z>=1050?'晴れ上がり（約38万歳）':(age>=1e8?(age/1e8).toFixed(1)+'億歳ころ':(age/1e4).toFixed(0)+'万歳ころ');
}
Zs.addEventListener('input',render);render();''')

# ===== 26 チャンドラセカール: 白色矮星の質量-半径関係と限界質量 =====
SIM["26_1983_chandrasekhar.html"] = (r'''    <h2>実験してみよう ── 星に質量を積んでいくと…</h2>
    <div class="hint">燃え尽きた星の芯「白色矮星」は、電子の量子的な圧力（縮退圧）で自分の重力を支えています。スライダーで質量を増やしてみましょう。ふつうの星と違って<b>重いほど小さくなり</b>、1.4太陽質量に近づくと──。</div>
    <div class="xbox"><canvas id="cv" width="640" height="310"></canvas></div>
    <div class="cpanel">
      <div class="ctl"><label>白色矮星の質量 <output id="oM">0.60 太陽質量</output></label><input id="M" type="range" min="20" max="143" value="60"></div>
    </div>
    <div class="status" id="st">–</div>
    <div class="rpanel"><span>半径 <b id="rR">–</b></span><span>平均密度 <b id="rD">–</b></span><span>角砂糖1個分の重さ <b id="rS">–</b></span></div>
    <div class="note">質量-半径関係は R ∝ M<sup>−1/3</sup>√(1−(M/M<sub>Ch</sub>)<sup>4/3</sup>) （相対論的補正を入れた縮退星の近似式）で計算しています。電子が光速近くまで追い詰められると縮退圧の「腰折れ」が起き、<b>M<sub>Ch</sub> ≈ 1.4 太陽質量を超えては支えられない</b>──これがチャンドラセカール限界です。限界を超えた星の芯は中性子星やブラックホールへ崩壊し、Ia型超新星（2011年の加速膨張のページ参照）の明るさが揃う理由もこの限界質量にあります。</div>''',
r'''var cv=document.getElementById('cv'),g=cv.getContext('2d'),W=cv.width,H=cv.height;
var Ms=document.getElementById('M'),st=document.getElementById('st');
var MCH=1.44;
function radius(M){var x=Math.pow(M/MCH,4/3);if(x>=1)return 0;
  return 14350*Math.pow(M/0.6,-1/3)*Math.sqrt(1-x)*0.62;}   // km（0.6M☉で約8900km）
function render(){
  var M=+Ms.value/100;
  document.getElementById('oM').textContent=M.toFixed(2)+' 太陽質量';
  g.clearRect(0,0,W,H);g.font='12px sans-serif';
  // 左: M-R 曲線
  var X0=60,Y0=H-44,PWi=330,PHi=H-84;
  g.strokeStyle='#8b93a7';g.beginPath();g.moveTo(X0,Y0-PHi);g.lineTo(X0,Y0);g.lineTo(X0+PWi,Y0);g.stroke();
  g.fillStyle='#8b93a7';
  for(var m2=0.2;m2<=1.4;m2+=0.4)g.fillText(m2.toFixed(1),X0+PWi*(m2-0.1)/1.4-8,Y0+16);
  g.fillText('質量（太陽=1）',X0+PWi/2-40,H-6);
  g.save();g.translate(16,H/2);g.rotate(-Math.PI/2);g.fillText('半径 (km)',0,0);g.restore();
  var RMAX=16000;
  g.fillText('15000',X0-44,Y0-PHi*15000/RMAX+4);g.fillText('5000',X0-38,Y0-PHi*5000/RMAX+4);
  g.strokeStyle='#ffb454';g.lineWidth=2.5;g.beginPath();var st2=false;
  for(var px=0;px<=PWi;px++){var mm=0.1+1.4*px/PWi;if(mm>=MCH)break;
    var R=radius(mm),y=Y0-PHi*Math.min(R,RMAX)/RMAX;
    if(!st2){g.moveTo(X0+px,y);st2=true;}else g.lineTo(X0+px,y);}
  g.stroke();g.lineWidth=1;
  // 限界線
  var lx=X0+PWi*(MCH-0.1)/1.4;
  g.strokeStyle='#ff7b72';g.setLineDash([5,4]);g.beginPath();g.moveTo(lx,Y0);g.lineTo(lx,Y0-PHi);g.stroke();g.setLineDash([]);
  g.fillStyle='#ff7b72';g.fillText('チャンドラセカール限界 1.44',lx-140,Y0-PHi+14);
  var R=radius(M);
  var mx=X0+PWi*(M-0.1)/1.4,my=Y0-PHi*Math.min(R,RMAX)/RMAX;
  g.fillStyle='#ffd257';g.beginPath();g.arc(mx,my,6,0,7);g.fill();
  // 右: 星と地球の大きさ比べ
  var ex=520,ey=130,ER=6371,SCALE=70/ER;
  g.strokeStyle='#2563eb';g.beginPath();g.arc(ex,ey,ER*SCALE,0,7);g.stroke();
  g.fillStyle='#8b93a7';g.fillText('地球',ex-12,ey+92);
  if(R>0){g.fillStyle='#e8f0fe';g.beginPath();g.arc(ex,ey,Math.max(2,R*SCALE),0,7);g.fill();
    g.fillStyle='#8b93a7';g.fillText('白色矮星',ex-24,ey-84);}
  else{g.fillStyle='#ff7b72';g.fillText('崩壊！',ex-20,ey);}
  var MSUN=1.989e30;
  if(R>0){var rho=3*M*MSUN/(4*Math.PI*Math.pow(R*1000,3));
    document.getElementById('rR').textContent=R.toFixed(0)+' km（地球の'+(R/ER).toFixed(2)+'倍）';
    document.getElementById('rD').textContent=(rho/1e9).toFixed(2)+'×10⁹ kg/m³';
    document.getElementById('rS').textContent='約 '+(rho*1e-6/1000).toFixed(1)+' トン';
    if(M<1.3){st.className='status yes';st.textContent='電子の縮退圧で安定 ── 重いほど小さくなる不思議な星';}
    else{st.className='status no';st.textContent='限界が近い…あと少し質量が増えると支えきれない';}}
  else{document.getElementById('rR').textContent='0（崩壊）';
    document.getElementById('rD').textContent='∞へ';document.getElementById('rS').textContent='–';
    st.className='status no';st.textContent='限界を超えた ── 中性子星かブラックホールへ崩壊（超新星爆発）';}
}
Ms.addEventListener('input',render);render();''')

# ===== 27 STM: トンネル電流の指数関数的な距離依存性 =====
SIM["27_1986_stm.html"] = (r'''    <h2>実験してみよう ── 原子1個分の凹凸を「電流」で感じる</h2>
    <div class="hint">針（探針）と試料はくっついていないのに、すき間が1ナノメートル以下になると量子トンネル効果で電流が流れます。距離・電圧・材料（仕事関数）を変えて、電流計の変わり方を見てください。<b>縦軸は対数</b>です。</div>
    <div class="xbox"><canvas id="cv" width="640" height="300"></canvas></div>
    <div class="cpanel">
      <div class="ctl"><label>探針と試料の距離 z <output id="oZ">0.50 nm</output></label><input id="Z" type="range" min="20" max="120" value="50"></div>
      <div class="ctl"><label>バイアス電圧 <output id="oV">0.10 V</output></label><input id="V" type="range" min="1" max="200" value="10"></div>
      <div class="ctl"><label>仕事関数 φ（材料） <output id="oP">4.5 eV</output></label><input id="P" type="range" min="20" max="60" value="45"></div>
    </div>
    <div class="rpanel"><span>トンネル電流 <b id="rI">–</b></span><span>減衰定数 κ <b id="rK">–</b></span><span>0.1 nm 近づくと電流は <b id="rX">–</b></span></div>
    <div class="note">I ∝ V·e<sup>−2κz</sup>、κ = √(2mφ)/ħ という真空トンネルの式です（電流の絶対値は典型的なSTMに合わせて規格化）。<b>距離がわずか0.1 nm（原子半径ほど）変わるだけで電流が約1桁変わる</b>──この鋭さこそ、STMが原子1個ずつを見分けられる理由です。実際の装置はこの電流が一定になるよう針の高さをフィードバック制御しながら表面をなぞり、原子の地形図を描きます。</div>''',
r'''var cv=document.getElementById('cv'),g=cv.getContext('2d'),W=cv.width,H=cv.height;
var Zs=document.getElementById('Z'),Vs=document.getElementById('V'),Ps=document.getElementById('P');
function render(){
  var z=+Zs.value/100,V=+Vs.value/100,phi=+Ps.value/10;
  document.getElementById('oZ').textContent=z.toFixed(2)+' nm';
  document.getElementById('oV').textContent=V.toFixed(2)+' V';
  document.getElementById('oP').textContent=phi.toFixed(1)+' eV';
  var kap=5.123*Math.sqrt(phi);                 // /nm
  var I=5.26e5*V*Math.exp(-2*kap*z);            // nA
  g.clearRect(0,0,W,H);g.font='12px sans-serif';
  // 左: 探針と表面（原子）
  var sy=210,scale=140;                          // 1nm = 140px
  g.fillStyle='#26343f';g.fillRect(30,sy,300,60);
  g.fillStyle='#3f83bf';
  for(var ax=55;ax<=310;ax+=42){g.beginPath();g.arc(ax,sy,16,Math.PI,0);g.fill();}
  g.fillStyle='#8b93a7';g.fillText('試料の表面原子',40,sy+44);
  var tipY=sy-16-z*scale;
  g.fillStyle='#9fb2c9';g.beginPath();
  g.moveTo(180-38,tipY-90);g.lineTo(180+38,tipY-90);g.lineTo(180,tipY);g.closePath();g.fill();
  g.fillStyle='#8b93a7';g.fillText('探針',150,tipY-98);
  // トンネルする電子のイメージ
  if(I>1e-5){g.fillStyle='rgba(255,210,87,0.9)';
    var nDot=Math.min(8,Math.max(1,Math.round(Math.log10(I)+6)));
    for(var d2=0;d2<nDot;d2++){g.beginPath();g.arc(176+8*Math.sin(d2*2.1),tipY+ (sy-16-tipY)*(d2+0.5)/nDot,2.5,0,7);g.fill();}}
  g.strokeStyle='#3a4356';g.beginPath();g.moveTo(340,tipY);g.lineTo(360,tipY);g.moveTo(340,sy-16);g.lineTo(360,sy-16);g.stroke();
  g.fillStyle='#e6e3d9';g.fillText('z',364,(tipY+sy)/2);
  // 右: 対数電流メーター
  var MX=420,MY0=250,MH=200,MW=54;
  g.strokeStyle='#3a4356';g.strokeRect(MX,MY0-MH,MW,MH);
  g.fillStyle='#8b93a7';g.fillText('トンネル電流（対数）',MX-10,MY0-MH-12);
  var LGMIN=-6,LGMAX=3;                          // 1fA .. 1uA (nA基準: -6..3)
  ['1 fA','1 pA','1 nA','1 μA'].forEach(function(lb,i){var lg=-6+i*3;
    var yy=MY0-MH*(lg-LGMIN)/(LGMAX-LGMIN);
    g.strokeStyle='#3a4356';g.beginPath();g.moveTo(MX,yy);g.lineTo(MX+MW,yy);g.stroke();
    g.fillStyle='#5c6470';g.fillText(lb,MX+MW+6,yy+4);});
  var lgI=Math.log(I)/Math.LN10;
  var hh=Math.max(0,Math.min(MH,MH*(lgI-LGMIN)/(LGMAX-LGMIN)));
  g.fillStyle=hh>0?'#7ee787':'#3a4356';g.fillRect(MX+3,MY0-hh,MW-6,hh);
  var iTxt=I>=1000?(I/1000).toFixed(2)+' μA':I>=1?I.toFixed(2)+' nA':I>=1e-3?(I*1000).toFixed(2)+' pA':I>=1e-6?(I*1e6).toFixed(2)+' fA':'ほぼゼロ（離れすぎ）';
  document.getElementById('rI').textContent=iTxt;
  document.getElementById('rK').textContent=kap.toFixed(1)+' /nm';
  document.getElementById('rX').textContent='×'+Math.exp(2*kap*0.1).toFixed(0)+' 倍';
}
[Zs,Vs,Ps].forEach(function(s){s.addEventListener('input',render);});render();''')

# ===== 31 光ファイバー: 全反射と減衰（カオの20dB/km基準） =====
SIM["31_2009_fiber.html"] = (r'''    <h2>実験してみよう ── 光を100 km 先まで届ける</h2>
    <div class="hint">光ファイバーの芯（コア）に光を入れる角度と、ガラスの透明度（減衰率）、届ける距離を変えてみましょう。カオが示した実用化の目安は「<b>20 dB/km 以下なら通信に使える</b>」でした。</div>
    <div class="xbox"><canvas id="cv" width="640" height="300"></canvas></div>
    <div class="cpanel">
      <div class="ctl"><label>光を入れる角度（軸から） <output id="oA">4°</output></label><input id="A" type="range" min="0" max="16" value="4" step="0.5"></div>
      <div class="ctl"><label>距離 <output id="oL">10 km</output></label><input id="L" type="range" min="0" max="100" value="40"></div>
    </div>
    <div class="btns">
      <button data-a="1000">1965年の光学ガラス（1000 dB/km）</button>
      <button data-a="20" class="on">カオの目標（20 dB/km）</button>
      <button data-a="0.2">現代のファイバー（0.2 dB/km）</button>
    </div>
    <div class="status no" id="st">–</div>
    <div class="rpanel"><span>全反射の条件 <b id="rC">–</b></span><span>減衰の合計 <b id="rA">–</b></span><span>届く光 <b id="rP">–</b></span></div>
    <div class="note">全反射はスネルの法則（コア n₁=1.462、クラッド n₂=1.447 → 軸から約8.2°まで）、減衰は P = P₀·10<sup>−αL/10</sup> という実式です。カオの洞察は「ガラスが暗いのは宿命ではなく<b>不純物（鉄イオンなど）のせい</b>で、純化すれば20 dB/km を切れる」というもの。現代の 0.2 dB/km は理論限界（レイリー散乱）にほぼ到達した値で、100 km 先まで光の1%が届きます。</div>''',
r'''var cv=document.getElementById('cv'),g=cv.getContext('2d'),W=cv.width,H=cv.height;
var As=document.getElementById('A'),Ls=document.getElementById('L'),st=document.getElementById('st');
var alpha=20;
document.querySelectorAll('.btns button').forEach(function(b){
  b.addEventListener('click',function(){alpha=+b.dataset.a;
    document.querySelectorAll('.btns button').forEach(function(x){x.classList.toggle('on',x===b)});render();});});
var N1=1.462,N2=1.447,THC=Math.acos(N2/N1)*180/Math.PI;   // ≈8.2°
function render(){
  var th=+As.value,Lkm=Math.max(0.1,Math.pow(10,+Ls.value/100*3-1)); // 0.1..100 km（対数）
  document.getElementById('oA').textContent=th+'°';
  document.getElementById('oL').textContent=Lkm>=10?Lkm.toFixed(0)+' km':Lkm.toFixed(1)+' km';
  g.clearRect(0,0,W,H);g.font='12px sans-serif';
  // ファイバー断面
  var FX0=30,FX1=W-30,CY=110,CORE=34,CLAD=62;
  g.fillStyle='#1b2334';g.fillRect(FX0,CY-CLAD,FX1-FX0,2*CLAD);
  g.fillStyle='#24304d';g.fillRect(FX0,CY-CORE,FX1-FX0,2*CORE);
  g.fillStyle='#8b93a7';g.fillText('コア n₁=1.462',FX0+8,CY+5);
  g.fillText('クラッド n₂=1.447',FX0+8,CY-CORE-10);
  var tir=th<=THC;
  // 光線を反射させながら描く（減衰で薄く）
  var x=FX0+4,y=CY,dir=1,rad=th*Math.PI/180;
  var slope=Math.tan(rad);
  var db=alpha*Lkm,P=Math.pow(10,-db/10);
  g.lineWidth=2.6;
  var segs=0,alph=1;
  while(x<FX1&&segs<60){
    var dy=(dir>0? (CY+CORE-y):(y-(CY-CORE)));
    var dx=slope>1e-6?dy/slope:(FX1-x);
    var nx=Math.min(FX1,x+dx),ny=(nx===x+dx)?(dir>0?CY+CORE:CY-CORE):y+dir*slope*(FX1-x);
    // 徐々に減衰（表示用: 全長で P に）
    var frac=(nx-FX0)/(FX1-FX0);var aa=Math.pow(Math.max(P,1e-4),frac);
    g.strokeStyle='rgba(126,231,135,'+Math.max(0.06,aa).toFixed(3)+')';
    g.beginPath();g.moveTo(x,y);g.lineTo(nx,ny);g.stroke();
    if(!tir&&nx<FX1){ // 漏れ光
      g.strokeStyle='rgba(255,123,114,'+Math.max(0.08,alph*0.5).toFixed(2)+')';
      g.beginPath();g.moveTo(nx,ny);g.lineTo(nx+30,ny+(dir>0?26:-26));g.stroke();
      alph*=0.45;}
    x=nx;y=ny;dir=-dir;segs++;
    if(!tir&&alph<0.05)break;}
  g.lineWidth=1;
  // 受信メーター
  var MX=80,MW2=W-160,MY=232;
  g.fillStyle='#8b93a7';g.fillText('届いた光（対数目盛: 100% → 0.0001%）',MX,MY-10);
  g.strokeStyle='#3a4356';g.strokeRect(MX,MY,MW2,20);
  var lg=Math.max(-6,Math.log(P)/Math.LN10);   // 0..-6
  var wdt=MW2*(lg+6)/6;
  g.fillStyle=P>0.01?'#7ee787':P>1e-4?'#ffd257':'#ff7b72';
  if(tir)g.fillRect(MX+1,MY+1,Math.max(2,wdt-2),18);
  document.getElementById('rC').textContent=tir?'OK（'+th+'° ≦ 臨界 8.2°）':'破れ！ 光がクラッドへ漏れる';
  document.getElementById('rA').textContent=db>=1000?(db/1000).toFixed(1)+'×10³ dB':db.toFixed(1)+' dB';
  var pTxt=P>=0.01?(P*100).toFixed(1)+' %':P>=1e-6?(P*100).toExponential(1)+' %':'ほぼゼロ';
  document.getElementById('rP').textContent=tir?pTxt:'0 %（全反射の破れ）';
  if(!tir){st.className='status no';st.textContent='角度が深すぎて全反射にならない ── 8.2°以下にしましょう';}
  else if(db<=30){st.className='status yes';st.textContent='通信できる！ '+(alpha===0.2?'現代のファイバーなら海底ケーブルもこの原理':'この透明度なら実用になる（カオの基準クリア）');}
  else{st.className='status no';st.textContent='暗すぎて信号が消えた ── ガラスを純化して減衰率を下げるしかない（カオの主張）';}
}
[As,Ls].forEach(function(s){s.addEventListener('input',render);});render();''')

# ===== 33 加速膨張: 超新星ハッブル図と (Ωm, ΩΛ) フィット =====
SIM["33_2011_dark_energy.html"] = (r'''    <h2>実験してみよう ── 超新星のデータに宇宙モデルを合わせる</h2>
    <div class="hint">Ia型超新星は明るさの揃った「標準光源」。遠さ（見かけの暗さ）と赤方偏移の関係は、宇宙に何がどれだけ入っているかで変わります。<b>物質 Ω<sub>m</sub> と ダークエネルギー Ω<sub>Λ</sub> のスライダーを動かして、観測点（1998年ごろの観測のイメージ）に合う宇宙を探して</b>ください。</div>
    <div class="xbox"><canvas id="cv" width="640" height="320"></canvas></div>
    <div class="cpanel">
      <div class="ctl"><label>物質の量 Ω<sub>m</sub> <output id="oM">1.00</output></label><input id="M" type="range" min="0" max="100" value="100" step="5"></div>
      <div class="ctl"><label>ダークエネルギー Ω<sub>Λ</sub> <output id="oL">0.00</output></label><input id="L" type="range" min="0" max="100" value="0" step="5"></div>
    </div>
    <div class="status no" id="st">–</div>
    <div class="rpanel"><span>データとのずれ（χ²/点数） <b id="rX">–</b></span><span>減速パラメータ q₀ = Ω<sub>m</sub>/2 − Ω<sub>Λ</sub> <b id="rQ">–</b></span></div>
    <div class="note">曲線は光度距離 d<sub>L</sub>(z) をフリードマン方程式（H(z) = H₀√(Ω<sub>m</sub>(1+z)³+Ω<sub>k</sub>(1+z)²+Ω<sub>Λ</sub>)）から数値積分した本物の宇宙論計算です。縦軸は「物質だけの宇宙 (Ω<sub>m</sub>=1)」と比べた明るさの差（等級）。観測された超新星は物質だけの宇宙の予想より<b>約0.2〜0.5等級暗い＝遠い</b>──膨張が加速していないと説明できません。q₀&lt;0 が加速膨張の条件です（データ点は Ω<sub>m</sub>=0.3, Ω<sub>Λ</sub>=0.7 の宇宙から生成した模擬観測）。</div>''',
r'''var cv=document.getElementById('cv'),g=cv.getContext('2d'),W=cv.width,H=cv.height;
var Ms=document.getElementById('M'),Ls=document.getElementById('L'),st=document.getElementById('st');
function dc(z,om,ol){ // 共動距離 (c/H0=1)
  var ok=1-om-ol,n=200,s=0;
  for(var i=0;i<n;i++){var zz=z*(i+0.5)/n;
    var e=Math.sqrt(Math.max(1e-9,om*Math.pow(1+zz,3)+ok*Math.pow(1+zz,2)+ol));
    s+=1/e;}
  s*=z/n;
  if(ok>1e-6)s=Math.sinh(Math.sqrt(ok)*s)/Math.sqrt(ok);
  else if(ok<-1e-6)s=Math.sin(Math.sqrt(-ok)*s)/Math.sqrt(-ok);
  return s;}
function mu(z,om,ol){return 5*Math.log(Math.max(1e-9,(1+z)*dc(z,om,ol)))/Math.LN10;}
function dmu(z,om,ol){return mu(z,om,ol)-mu(z,1,0);}   // 基準: 物質だけの宇宙
// 模擬観測点（Ωm=0.3, ΩΛ=0.7 + ノイズ）
var DATA=[],seeds=[0.32,-0.55,0.11,0.72,-0.23,0.48,-0.61,0.05,0.66,-0.38,0.21,-0.12,0.53,-0.44,0.30,0.02];
for(var i2=0;i2<16;i2++){var zz2=0.05+0.9*i2/15;
  DATA.push([zz2,dmu(zz2,0.3,0.7)+seeds[i2]*0.09,0.12]);}
var PX0=64,PY0=0,PWi=0;
function render(){
  var om=+Ms.value/100,ol=+Ls.value/100;
  document.getElementById('oM').textContent=om.toFixed(2);
  document.getElementById('oL').textContent=ol.toFixed(2);
  g.clearRect(0,0,W,H);g.font='12px sans-serif';
  var X0=64,Y0=H-46,PWx=W-104,PHx=H-86,YMIN=-0.35,YMAX=0.75;
  function xz(z){return X0+PWx*z/1.0;}
  function ym(m){return Y0-PHx*(m-YMIN)/(YMAX-YMIN);}
  g.strokeStyle='#232b3d';g.beginPath();
  for(var yy=-0.2;yy<=0.7;yy+=0.2){g.moveTo(X0,ym(yy));g.lineTo(X0+PWx,ym(yy));}
  g.stroke();
  g.strokeStyle='#8b93a7';g.beginPath();g.moveTo(X0,ym(YMAX));g.moveTo(X0,Y0);g.lineTo(X0+PWx,Y0);g.stroke();
  g.strokeStyle='#5c6470';g.beginPath();g.moveTo(X0,ym(0));g.lineTo(X0+PWx,ym(0));g.stroke();
  g.fillStyle='#8b93a7';
  for(var z3=0;z3<=1.01;z3+=0.2)g.fillText(z3.toFixed(1),xz(z3)-8,Y0+16);
  g.fillText('赤方偏移 z（遠さ）',W/2-50,H-6);
  g.save();g.translate(14,H/2+80);g.rotate(-Math.PI/2);g.fillText('物質だけの宇宙より暗い ←→ 明るい（等級差）',0,0);g.restore();
  for(var yv=-0.2;yv<=0.75;yv+=0.2)g.fillText((yv>0?'+':'')+yv.toFixed(1),X0-34,ym(yv)+4);
  g.fillText('基準: Ωm=1 の宇宙',X0+PWx-130,ym(0)-6);
  // 観測点
  DATA.forEach(function(d){var x=xz(d[0]),y=ym(d[1]);
    g.strokeStyle='#8b93a7';g.beginPath();g.moveTo(x,ym(d[1]-d[2]));g.lineTo(x,ym(d[1]+d[2]));g.stroke();
    g.fillStyle='#ffd257';g.beginPath();g.arc(x,y,4,0,7);g.fill();});
  // ユーザーの宇宙
  g.strokeStyle='#7ee787';g.lineWidth=2.5;g.beginPath();var st3=false;
  for(var px=2;px<=PWx;px+=3){var z4=px/PWx;var y4=ym(dmu(z4,om,ol));
    if(!st3){g.moveTo(X0+px,y4);st3=true;}else g.lineTo(X0+px,y4);}
  g.stroke();g.lineWidth=1;
  g.fillStyle='#7ee787';g.fillText('あなたの宇宙モデル',X0+8,ym(dmu(0.15,om,ol))-10);
  // χ²
  var chi=0;DATA.forEach(function(d){var r=(dmu(d[0],om,ol)-d[1])/d[2];chi+=r*r;});
  chi/=DATA.length;
  var q0=om/2-ol;
  document.getElementById('rX').textContent=chi.toFixed(2)+(chi<1.5?'（よく合う！）':chi<4?'（おしい）':'（合わない）');
  document.getElementById('rQ').textContent=q0.toFixed(2)+(q0<0?'（加速膨張）':'（減速膨張）');
  if(chi<1.5&&q0<0){st.className='status yes';st.textContent='データと一致！ ダークエネルギーが優勢な「加速する宇宙」だけが超新星を説明できる';}
  else if(chi<1.5){st.className='status yes';st.textContent='ほぼ一致…だがまだ改善の余地あり';}
  else{st.className='status no';st.textContent=q0>=0?'この宇宙は減速膨張 ── 観測より明るすぎる予言になっている':'まだデータと合わない ── スライダーを調整してみよう';}
}
[Ms,Ls].forEach(function(s){s.addEventListener('input',render);});render();''')

# ===== 35 青色LED: InGaN の組成とバンドギャップ・発光色 =====
SIM["35_2014_blue_led.html"] = (r'''    <h2>実験してみよう ── 結晶の配合で光の色を設計する</h2>
    <div class="hint">窒化ガリウム（GaN）にインジウム（In）を混ぜた In<sub>x</sub>Ga<sub>1−x</sub>N は、混ぜる割合 x で<b>バンドギャップ</b>（電子が落ちる段差）が変わり、発光色が決まります。In の割合と電流を変えて、青色LEDを「設計」してみましょう。</div>
    <div class="xbox"><canvas id="cv" width="640" height="300"></canvas></div>
    <div class="cpanel">
      <div class="ctl"><label>In の割合 x <output id="oX">0.15</output></label><input id="X" type="range" min="0" max="35" value="15"></div>
      <div class="ctl"><label>電流 <output id="oI">10 mA</output></label><input id="I" type="range" min="0" max="30" value="10"></div>
    </div>
    <div class="status" id="st">–</div>
    <div class="rpanel"><span>バンドギャップ E<sub>g</sub> <b id="rE">–</b></span><span>発光波長 λ = 1240/E<sub>g</sub> <b id="rL">–</b></span><span>順方向電圧の目安 <b id="rV">–</b></span></div>
    <div class="note">E<sub>g</sub>(x) = 3.42(1−x) + 0.77x − 1.43x(1−x) eV（ボーイング付きの実験式）と λ = 1240/E<sub>g</sub> nm による計算です。x≈0.15〜0.2 でちょうど<b>青（450 nm 前後）</b>になります。難題は物理より材料でした──良質な GaN 結晶の成長と p型化は「20世紀中は不可能」と言われ、赤﨑・天野が低温バッファ層と p型化を、中村が量産技術を突破。青が完成したことで（青＋蛍光体＝）白色LED照明が生まれました。</div>''',
r'''var cv=document.getElementById('cv'),g=cv.getContext('2d'),W=cv.width,H=cv.height;
var Xs=document.getElementById('X'),Is=document.getElementById('I'),st=document.getElementById('st');
function wl2rgb(w){var r=0,gg=0,b=0;
  if(w<380)return [170,120,255];
  if(w<440){r=-(w-440)/60;b=1;}else if(w<490){gg=(w-440)/50;b=1;}
  else if(w<510){gg=1;b=-(w-510)/20;}else if(w<580){r=(w-510)/70;gg=1;}
  else if(w<645){r=1;gg=-(w-645)/65;}else{r=1;}
  return [Math.round(255*r),Math.round(255*gg),Math.round(255*b)];}
function render(){
  var x=+Xs.value/100,mA=+Is.value;
  document.getElementById('oX').textContent=x.toFixed(2);
  document.getElementById('oI').textContent=mA+' mA';
  var Eg=3.42*(1-x)+0.77*x-1.43*x*(1-x);
  var lam=1239.84/Eg;
  var c=wl2rgb(lam),bri=Math.min(1,mA/12);
  g.clearRect(0,0,W,H);g.font='12px sans-serif';
  // 左: バンド図
  var BX=60,BW2=200,VY=210,CY2=VY-Eg*36;
  g.fillStyle='#3a4356';g.fillRect(BX,VY,BW2,14);g.fillRect(BX,CY2-14,BW2,14);
  g.fillStyle='#8b93a7';g.fillText('伝導帯（電子）',BX+4,CY2-22);
  g.fillText('価電子帯（正孔）',BX+4,VY+30);
  g.strokeStyle='#e6e3d9';g.beginPath();g.moveTo(BX+BW2/2,CY2);g.lineTo(BX+BW2/2,VY-6);g.stroke();
  g.beginPath();g.moveTo(BX+BW2/2,VY-6);g.lineTo(BX+BW2/2-5,VY-15);g.moveTo(BX+BW2/2,VY-6);g.lineTo(BX+BW2/2+5,VY-15);g.stroke();
  g.fillStyle='#e6e3d9';g.fillText('Eg = '+Eg.toFixed(2)+' eV',BX+BW2/2+8,(CY2+VY)/2);
  // 電子と正孔
  if(mA>0){g.fillStyle='#79c0ff';g.beginPath();g.arc(BX+BW2/2,CY2-7,5,0,7);g.fill();
    g.fillStyle='#ff9a8a';g.beginPath();g.arc(BX+BW2/2,VY+7,5,0,7);g.fill();}
  // LED の光
  var lx=430,ly=120;
  if(mA>0){var glow=g.createRadialGradient(lx,ly,4,lx,ly,60+40*bri);
    glow.addColorStop(0,'rgba('+c[0]+','+c[1]+','+c[2]+','+(0.95*bri)+')');
    glow.addColorStop(1,'rgba('+c[0]+','+c[1]+','+c[2]+',0)');
    g.fillStyle=glow;g.beginPath();g.arc(lx,ly,110,0,7);g.fill();}
  g.fillStyle='rgba('+c[0]+','+c[1]+','+c[2]+','+(0.25+0.75*bri)+')';
  g.beginPath();g.arc(lx,ly,20,Math.PI,0);g.fill();g.fillRect(lx-20,ly,40,26);
  g.strokeStyle='#3a4356';g.beginPath();g.moveTo(lx-8,ly+26);g.lineTo(lx-8,ly+58);g.moveTo(lx+8,ly+26);g.lineTo(lx+8,ly+50);g.stroke();
  g.fillStyle='#8b93a7';g.fillText('In'+x.toFixed(2)+'Ga'+(1-x).toFixed(2)+'N',lx-34,ly+78);
  // 下: スペクトル帯
  var SX=60,SW2=W-120,SY=H-40;
  for(var px=0;px<=SW2;px++){var lam2=340+(700-340)*px/SW2,cc=wl2rgb(lam2);
    g.fillStyle=lam2<380?'#2a2440':'rgb('+cc[0]+','+cc[1]+','+cc[2]+')';
    g.fillRect(SX+px,SY,1.5,16);}
  g.fillStyle='#8b93a7';
  [350,400,450,500,550,600,650,700].forEach(function(l){g.fillText(l,SX+SW2*(l-340)/360-10,SY+30);});
  var mx2=SX+SW2*(Math.min(700,Math.max(340,lam))-340)/360;
  g.strokeStyle='#fff';g.lineWidth=2.5;g.beginPath();g.moveTo(mx2,SY-6);g.lineTo(mx2,SY+22);g.stroke();g.lineWidth=1;
  document.getElementById('rE').textContent=Eg.toFixed(2)+' eV';
  document.getElementById('rL').textContent=lam.toFixed(0)+' nm';
  document.getElementById('rV').textContent='約 '+Eg.toFixed(1)+' V';
  var name=lam<380?'紫外線（GaNそのもの）':lam<430?'紫':lam<490?'青 ── 20世紀の宿題！':lam<550?'緑':lam<590?'黄':'橙〜赤';
  if(mA===0){st.className='status no';st.textContent='電流を流すと発光します';}
  else if(lam>=430&&lam<490){st.className='status yes';st.textContent='青色LEDの完成！（'+name.replace(' ── 20世紀の宿題！','')+'・'+lam.toFixed(0)+' nm）これで光の三原色が揃った';}
  else{st.className='status';st.style.background='#fff7e6';st.style.color='#8a5a00';st.textContent='いまの発光は「'+name+'」── In の割合を調整して青を狙おう';}
}
[Xs,Is].forEach(function(s){s.addEventListener('input',render);});render();''')

# ===== 36 梶田: ニュートリノ振動の生存確率（L/E プロット） =====
SIM["36_2015_kajita.html"] = (r'''    <h2>実験してみよう ── ニュートリノが「変身」する確率を計算する</h2>
    <div class="hint">大気ニュートリノは、頭上からは約15 km、地球の裏側からは約12800 km 飛んでスーパーカミオカンデに届きます。質量差 Δm²・混ざり具合 sin²2θ・エネルギー E を変えて、ミュー型ニュートリノが「ミュー型のまま」でいる確率を見てみましょう。</div>
    <div class="xbox"><canvas id="cv" width="640" height="310"></canvas></div>
    <div class="cpanel">
      <div class="ctl"><label>質量の差 Δm² <output id="oD">2.4×10⁻³ eV²</output></label><input id="D" type="range" min="10" max="40" value="24"></div>
      <div class="ctl"><label>混ざり具合 sin²2θ <output id="oS">1.00</output></label><input id="S" type="range" min="50" max="100" value="100"></div>
      <div class="ctl"><label>ニュートリノのエネルギー E <output id="oE">1.0 GeV</output></label><input id="E" type="range" min="5" max="100" value="10"></div>
    </div>
    <div class="rpanel"><span>上から（L≈15 km）の生存率 <b id="rD2">–</b></span><span>地球の裏から（L≈12800 km） <b id="rU">–</b></span><span>観測された上下比 <b>約 0.5（欠損！）</b></span></div>
    <div class="note">2世代振動の式 <b>P(ν<sub>μ</sub>→ν<sub>μ</sub>) = 1 − sin²2θ·sin²(1.27Δm²L/E)</b> の正確な計算です（L:km, E:GeV, Δm²:eV²）。横軸は飛行距離÷エネルギー L/E。上から来るニュートリノは振動する間もなく届く（生存率≈1）のに、地球を貫通してくるものは振動して<b>約半分がタウ型に変身して「消える」</b>──この上下の差こそスーパーカミオカンデの発見で、振動が起きるには<b>ニュートリノに質量が必要</b>です。曲線の右端が0.5に落ち着くのは、細かい振動がエネルギーの広がりで平均化されるためです。</div>''',
r'''var cv=document.getElementById('cv'),g=cv.getContext('2d'),W=cv.width,H=cv.height;
var Ds=document.getElementById('D'),Ss=document.getElementById('S'),Es=document.getElementById('E');
function render(){
  var dm2=+Ds.value/10*1e-3,s22=+Ss.value/100,E=+Es.value/10;
  document.getElementById('oD').textContent=(+Ds.value/10).toFixed(1)+'×10⁻³ eV²';
  document.getElementById('oS').textContent=s22.toFixed(2);
  document.getElementById('oE').textContent=E.toFixed(1)+' GeV';
  g.clearRect(0,0,W,H);g.font='12px sans-serif';
  var X0=60,Y0=H-46,PWx=W-100,PHx=H-90;
  // x: log10(L/E) 0..4.5 (km/GeV)
  var LGMIN=0,LGMAX=4.5;
  function xle(le){return X0+PWx*(Math.log(le)/Math.LN10-LGMIN)/(LGMAX-LGMIN);}
  function yp(p){return Y0-PHx*p;}
  g.strokeStyle='#232b3d';g.beginPath();
  [0.25,0.5,0.75,1].forEach(function(p){g.moveTo(X0,yp(p));g.lineTo(X0+PWx,yp(p));});
  g.stroke();
  g.strokeStyle='#8b93a7';g.beginPath();g.moveTo(X0,yp(1.02));g.moveTo(X0,Y0);g.lineTo(X0+PWx,Y0);g.stroke();
  g.fillStyle='#8b93a7';
  [1,10,100,1000,10000].forEach(function(v){g.fillText(v,xle(v)-10,Y0+16);});
  g.fillText('L/E（km/GeV・対数目盛）',W/2-70,H-6);
  ['0','0.5','1'].forEach(function(t,i){g.fillText(t,X0-26,yp(i*0.5)+4);});
  g.save();g.translate(14,H/2+60);g.rotate(-Math.PI/2);g.fillText('ミュー型のままの確率',0,0);g.restore();
  // 平均化なしの曲線 + 平均化（分解能）曲線
  function P(le){return 1-s22*Math.pow(Math.sin(1.267*dm2*le),2);}
  function Pavg(le){ // エネルギー分解能±30%で平均
    var n=15,s=0;for(var i=0;i<n;i++){var f=0.7+0.6*i/(n-1);s+=P(le*f);}return s/n;}
  g.strokeStyle='rgba(126,231,135,0.35)';g.lineWidth=1.5;g.beginPath();var st2=false;
  for(var px=0;px<=PWx;px++){var le=Math.pow(10,LGMIN+(LGMAX-LGMIN)*px/PWx);
    var y=yp(P(le));if(!st2){g.moveTo(X0+px,y);st2=true;}else g.lineTo(X0+px,y);}
  g.stroke();
  g.strokeStyle='#7ee787';g.lineWidth=2.5;g.beginPath();st2=false;
  for(px=0;px<=PWx;px++){var le2=Math.pow(10,LGMIN+(LGMAX-LGMIN)*px/PWx);
    var y2=yp(Pavg(le2));if(!st2){g.moveTo(X0+px,y2);st2=true;}else g.lineTo(X0+px,y2);}
  g.stroke();g.lineWidth=1;
  g.fillStyle='#7ee787';g.fillText('観測にかかる平均（濃い線）',X0+PWx-190,yp(0.98));
  // 上・下のマーカー
  var leD=15/E,leU=12800/E;
  [[leD,'#79c0ff','上から 15km'],[leU,'#ff9a8a','地球の裏から 12800km']].forEach(function(m){
    var x=xle(Math.max(1,m[0]));
    g.strokeStyle=m[1];g.setLineDash([4,4]);g.beginPath();g.moveTo(x,Y0);g.lineTo(x,yp(1));g.stroke();g.setLineDash([]);
    g.fillStyle=m[1];g.fillText(m[2],Math.min(x-30,W-170),yp(1)-6);});
  document.getElementById('rD2').textContent=(Pavg(leD)*100).toFixed(0)+' %';
  document.getElementById('rU').textContent=(Pavg(leU)*100).toFixed(0)+' %';
}
[Ds,Ss,Es].forEach(function(s){s.addEventListener('input',render);});render();''')

# ===== 38 LIGO: ブラックホール連星のチャープ波形（ニュートン近似） =====
SIM["38_2017_ligo.html"] = (r'''    <h2>実験してみよう ── ブラックホールの質量で重力波の「声」が変わる</h2>
    <div class="hint">2つのブラックホールの質量と距離を変えると、合体直前の重力波の波形（チャープ＝さえずり）がどう変わるでしょうか。<b>軽いほど長く高く鳴き、重いほど短く低い</b>──LIGOはこの波形から天体の正体を読み取ります。</div>
    <div class="xbox"><canvas id="cv" width="640" height="300"></canvas></div>
    <div class="cpanel">
      <div class="ctl"><label>ブラックホール1の質量 <output id="oM1">36 太陽質量</output></label><input id="M1" type="range" min="5" max="80" value="36"></div>
      <div class="ctl"><label>ブラックホール2の質量 <output id="oM2">29 太陽質量</output></label><input id="M2" type="range" min="5" max="80" value="29"></div>
      <div class="ctl"><label>地球からの距離 <output id="oD">410 Mpc</output></label><input id="D" type="range" min="100" max="3000" value="410" step="10"></div>
    </div>
    <div class="btns"><button id="gw">GW150914（初検出）の値にセット</button></div>
    <div class="rpanel"><span>チャープ質量 <b id="rMc">–</b></span><span>合体直前の周波数 <b id="rF">–</b></span><span>最大ひずみ h <b id="rH">–</b></span><span>腕4 kmの伸び縮み <b id="rL">–</b></span></div>
    <div class="note">波形は一般相対論のニュートン近似チャープ f(t) ∝ (t<sub>合体</sub>−t)<sup>−3/8</sup>、振幅 h ∝ M<sub>c</sub><sup>5/3</sup>f<sup>2/3</sup>/D で計算しています（合体後のリングダウンは省略）。波形全体の形を決めるのは<b>チャープ質量 M<sub>c</sub> = (m₁m₂)<sup>3/5</sup>/(m₁+m₂)<sup>1/5</sup></b> という組合せだけ──だから波形から質量が分かります。h〜10⁻²¹ とは、4 kmの腕が陽子1個の直径の千分の一ほど伸び縮みするということ。それを検出したのがLIGO（＝巨大なマイケルソン干渉計）です。</div>''',
r'''var cv=document.getElementById('cv'),g=cv.getContext('2d'),W=cv.width,H=cv.height;
var M1s=document.getElementById('M1'),M2s=document.getElementById('M2'),Ds=document.getElementById('D');
document.getElementById('gw').addEventListener('click',function(){M1s.value=36;M2s.value=29;Ds.value=410;render();});
function render(){
  var m1=+M1s.value,m2=+M2s.value,D=+Ds.value;
  document.getElementById('oM1').textContent=m1+' 太陽質量';
  document.getElementById('oM2').textContent=m2+' 太陽質量';
  document.getElementById('oD').textContent=D+' Mpc';
  var Mc=Math.pow(m1*m2,0.6)/Math.pow(m1+m2,0.2),Mt=m1+m2;
  var tMc=Mc*4.925e-6;                      // GMc/c³ [s]
  var fEnd=4400/Mt*2;                       // 合体直前のGW周波数の目安 [Hz]
  var f0=Math.max(20,fEnd/12);              // 表示開始周波数
  function tau(f){return 5/256*Math.pow(tMc,-5/3)*Math.pow(Math.PI*f,-8/3);}
  var T=tau(f0),tEnd=tau(fEnd);
  // 振幅 h(f)
  var MPC=3.086e22,GM=Mc*1.327e20,c=2.998e8;
  function amp(f){return 4*Math.pow(GM,5/3)*Math.pow(Math.PI*f,2/3)/(Math.pow(c,4)*D*MPC);}
  var hMax=amp(fEnd);
  g.clearRect(0,0,W,H);g.font='12px sans-serif';
  var X0=52,Y0=H/2,PWx=W-92,A=H/2-52;
  g.strokeStyle='#232b3d';g.beginPath();g.moveTo(X0,Y0);g.lineTo(X0+PWx,Y0);g.stroke();
  g.fillStyle='#8b93a7';
  g.fillText('時間 →（合体まで '+(T<1?(T*1000).toFixed(0)+' ミリ秒':T.toFixed(2)+' 秒'+'')+'）',W/2-80,H-8);
  g.save();g.translate(14,H/2+40);g.rotate(-Math.PI/2);g.fillText('ひずみ h（×10⁻²¹）',0,0);g.restore();
  // 目盛
  var scl=A/(hMax*1.05);
  g.fillText('+'+(hMax*1e21).toFixed(1),X0-40,Y0-A+10);g.fillText('−'+(hMax*1e21).toFixed(1),X0-40,Y0+A);
  // 波形: 位相を積分しながら描く
  g.strokeStyle='#7ee787';g.lineWidth=1.8;g.beginPath();
  var phase=0,prevT=0,started=false;
  var NPT=1400;
  for(var i=0;i<=NPT;i++){var t=T*i/NPT;var ta=Math.max(T-t,tEnd);
    var f=1/Math.PI*Math.pow(5/(256*ta),3/8)*Math.pow(tMc,-5/8);
    phase+=2*Math.PI*f*(t-prevT);prevT=t;
    var h=amp(f)*Math.sin(phase);
    var x=X0+PWx*i/NPT,y=Y0-h*scl;
    if(!started){g.moveTo(x,y);started=true;}else g.lineTo(x,y);
    if(T-t<=tEnd)break;}
  g.stroke();g.lineWidth=1;
  g.fillStyle='#ff9a8a';g.fillText('← 合体！（この先のリングダウンは省略）',Math.min(X0+PWx-230,W-240),Y0-A-2);
  document.getElementById('rMc').textContent=Mc.toFixed(1)+' 太陽質量';
  document.getElementById('rF').textContent=fEnd.toFixed(0)+' Hz（'+(fEnd<260?'低い音':fEnd<520?'真ん中のドの音あたり':'高い音')+'）';
  document.getElementById('rH').textContent=(hMax*1e21).toFixed(2)+'×10⁻²¹';
  document.getElementById('rL').textContent='陽子の直径の '+(hMax*4000/1.7e-15*1000).toFixed(1)+'/1000';
}
[M1s,M2s,Ds].forEach(function(s){s.addEventListener('input',render);});render();''')

# ===== 40 系外惑星: 視線速度法（ドップラー・ゆらぎ K の計算） =====
SIM["40_2019_exoplanet.html"] = (r'''    <h2>実験してみよう ── 星の「ふらつき」から見えない惑星を見つける</h2>
    <div class="hint">惑星が恒星を引っぱるので、恒星もわずかに円を描いて「ふらつき」ます。そのふらつきの速さ K を、星の光のドップラー効果で測るのが視線速度法。惑星の質量と軌道を変えて、<b>1995年の装置（精度13 m/s）で見つけられる惑星</b>を探してみましょう。</div>
    <div class="xbox"><canvas id="cv" width="640" height="300"></canvas></div>
    <div class="cpanel">
      <div class="ctl"><label>惑星の質量 <output id="oM">1.0 木星質量</output></label><input id="M" type="range" min="5" max="1300" value="100"></div>
      <div class="ctl"><label>軌道半径 <output id="oA">1.00 au</output></label><input id="A" type="range" min="0" max="100" value="67"></div>
      <div class="ctl"><label>恒星の質量 <output id="oS">1.0 太陽質量</output></label><input id="S" type="range" min="70" max="150" value="100"></div>
    </div>
    <div class="btns"><button id="peg">ペガスス座51番星b（1995年発見）にセット</button></div>
    <div class="status no" id="st">–</div>
    <div class="rpanel"><span>公転周期 <b id="rP">–</b></span><span>星のふらつき速度 K <b id="rK">–</b></span></div>
    <div class="note">ケプラーの第3法則 P² = a³/M<sub>★</sub> と、視線速度の半振幅 K = 28.4 (M<sub>p</sub>/M<sub>木</sub>)(P/年)<sup>−1/3</sup>(M<sub>★</sub>/M<sub>☉</sub>)<sup>−2/3</sup> m/s（円軌道・真横から見た場合）による計算です。木星でも太陽を 12.5 m/s しか揺らせないのに、マイヨールとケローが見つけた51 Peg b は「4日で1周する灼熱の巨大惑星」だったので K≈56 m/s と大きく、当時の精度でも見えた──「惑星は星の近くに巨大ガス惑星を作らない」という常識を壊した発見でした。</div>''',
r'''var cv=document.getElementById('cv'),g=cv.getContext('2d'),W=cv.width,H=cv.height;
var Ms=document.getElementById('M'),As=document.getElementById('A'),Ss=document.getElementById('S'),st=document.getElementById('st');
document.getElementById('peg').addEventListener('click',function(){Ms.value=47;As.value=14;Ss.value=106;render();});
var t0=0;
function render(){
  var mp=+Ms.value/100,ms=+Ss.value/100;
  var a=Math.pow(10,-1.7+2.4*(+As.value)/100);         // 0.02 .. 5 au（対数）
  document.getElementById('oM').textContent=mp.toFixed(2)+' 木星質量';
  document.getElementById('oA').textContent=a<0.1?a.toFixed(3)+' au':a.toFixed(2)+' au';
  document.getElementById('oS').textContent=ms.toFixed(1)+' 太陽質量';
  var P=Math.sqrt(a*a*a/ms);                            // 年
  var K=28.4*mp*Math.pow(P,-1/3)*Math.pow(ms,-2/3);     // m/s
  g.clearRect(0,0,W,H);g.font='12px sans-serif';
  // 左: 軌道アニメ（重心のまわり）
  var cx=130,cy=110,orbP=Math.max(30,Math.min(90,20+30*Math.log(a/0.02)));
  var th=t0;
  g.strokeStyle='#2a3446';g.beginPath();g.arc(cx,cy,orbP,0,7);g.stroke();
  var pr=Math.max(3,Math.min(9,3+3*Math.log(mp+1)));
  g.fillStyle='#79c0ff';g.beginPath();g.arc(cx+orbP*Math.cos(th),cy+orbP*Math.sin(th),pr,0,7);g.fill();
  var so=Math.min(14,orbP*mp/(ms*1047)*40+2);           // 星のふらつき（誇張表示）
  var sx=cx-so*Math.cos(th),sy=cy-so*Math.sin(th);
  var vlos=Math.sin(th);                                // 視線方向成分（下向きを視線とする）
  var col=vlos>0.1?'#ff9a8a':vlos<-0.1?'#8ab6ff':'#ffd257';
  g.fillStyle=col;g.beginPath();g.arc(sx,sy,16,0,7);g.fill();
  g.fillStyle='#8b93a7';g.fillText('恒星（ふらつき誇張）',cx-56,cy+orbP+30);
  g.fillText('↓ 地球はこちら',cx-36,cy+orbP+48);
  g.fillText(vlos>0.1?'遠ざかる→赤っぽく':vlos<-0.1?'近づく→青っぽく':'',cx-50,30);
  // 右: 視線速度カーブ
  var X0=290,Y0=150,PWx=W-X0-30,Aamp=90;
  var KMAX=Math.max(15,K*1.2);
  g.strokeStyle='#232b3d';g.beginPath();g.moveTo(X0,Y0);g.lineTo(X0+PWx,Y0);g.stroke();
  // 精度の帯
  g.fillStyle='rgba(255,210,87,0.12)';g.fillRect(X0,Y0-Aamp*13/KMAX,PWx,2*Aamp*13/KMAX);
  g.fillStyle='#8b93a7';g.fillText('1995年の測定精度 ±13 m/s',X0+6,Y0-Aamp*13/KMAX-4);
  g.strokeStyle='#7ee787';g.lineWidth=2.5;g.beginPath();
  for(var px=0;px<=PWx;px++){var ph=4*Math.PI*px/PWx-t0;
    var y=Y0-Aamp*(K*Math.sin(ph))/KMAX;
    if(px===0)g.moveTo(X0,y);else g.lineTo(X0+px,y);}
  g.stroke();g.lineWidth=1;
  g.fillStyle='#8b93a7';g.fillText('時間（2周期分）→',X0+PWx-110,Y0+Aamp+24);
  g.fillText('視線速度',X0,Y0-Aamp-14);
  g.fillText('+'+K.toFixed(1)+' m/s',X0+PWx-70,Y0-Aamp*K/KMAX-4);
  var pd=P*365.25;
  document.getElementById('rP').textContent=pd<60?pd.toFixed(1)+' 日':P<1?(P*12).toFixed(1)+' か月':P.toFixed(1)+' 年';
  document.getElementById('rK').textContent=K.toFixed(1)+' m/s（'+(K>3?'自転車':K>0.3?'カメ':'カタツムリ')+'なみ）';
  if(K>13){st.className='status yes';st.textContent='1995年の装置で検出できる！ 短周期の巨大惑星ほど見つけやすい';}
  else if(K>1){st.className='status';st.style.background='#fff7e6';st.style.color='#8a5a00';st.textContent='当時は無理でも現代の装置（精度〜1 m/s）なら検出できる';}
  else{st.className='status no';st.textContent='ふらつきが小さすぎる ── 地球型惑星の検出が難しい理由';}
}
[Ms,As,Ss].forEach(function(s){s.addEventListener('input',render);});
setInterval(function(){t0+=0.03;render();},33);''')

# ===== 42 真鍋: CO2と放射対流平衡（対流圏の温暖化・成層圏の寒冷化） =====
SIM["42_2021_manabe.html"] = (r'''    <h2>実験してみよう ── CO₂を増やすと大気の温度分布はどうなる？</h2>
    <div class="hint">真鍋の1次元「放射対流平衡モデル」を単純化した実験です。CO₂濃度と水蒸気フィードバックの有無を変えて、高さごとの気温の変化を見てみましょう。注目は<b>対流圏（下層）は暖まるのに、成層圏（上層）は逆に冷える</b>こと──温室効果の紛れもない指紋です。</div>
    <div class="xbox"><canvas id="cv" width="640" height="320"></canvas></div>
    <div class="cpanel">
      <div class="ctl"><label>CO₂濃度 <output id="oC">280 ppm</output></label><input id="C" type="range" min="150" max="1200" value="280" step="10"></div>
    </div>
    <div class="btns"><button id="fb" class="on">水蒸気フィードバック：あり</button></div>
    <div class="rpanel"><span>放射強制力 ΔF = 5.35 ln(C/280) <b id="rF">–</b></span><span>地表気温の変化 <b id="rT">–</b></span><span>成層圏（高度25 km） <b id="rS">–</b></span></div>
    <div class="note">地表の応答は ΔT = λ·ΔF（λ は気候感度パラメータ。水蒸気フィードバックありで約0.65、なしで約0.35 K/(W·m⁻²)：真鍋・ウェザラルド1967年の「CO₂倍増で+2.4 ℃／+1.3 ℃」を再現する値）。成層圏の寒冷化も同モデルの帰結を簡略化して描いています。「暖まるだけなら太陽活動でも説明できるが、<b>下が暖まり上が冷えるのはCO₂しかない</b>」──この指紋は実際の観測でも確認されており、真鍋のモデルの予言どおりでした。</div>''',
r'''var cv=document.getElementById('cv'),g=cv.getContext('2d'),W=cv.width,H=cv.height;
var Cs=document.getElementById('C'),fbBtn=document.getElementById('fb'),fb=true;
fbBtn.addEventListener('click',function(){fb=!fb;
  fbBtn.textContent='水蒸気フィードバック：'+(fb?'あり':'なし');
  fbBtn.classList.toggle('on',fb);render();});
function profile(C){  // 高度z[km] → 気温[℃]
  var dF=5.35*Math.log(C/280);
  var dTs=(fb?0.65:0.35)*dF;
  var dTst=-4.2*Math.log(C/280)/Math.LN2;   // 成層圏の寒冷化（簡略）
  return function(z){
    if(z<=12)return 15+dTs-6.5*z*(1+ -0*(0)); // 対流圏: 湿潤断熱風の固定減率
    var base=15+dTs-6.5*12;
    var f=Math.min(1,(z-12)/8);
    return base+f*dTst+(z>20?(z-20)*0.6:0);   // 成層圏: オゾン加熱でゆるく上昇
  };}
function render(){
  var C=+Cs.value;document.getElementById('oC').textContent=C+' ppm';
  g.clearRect(0,0,W,H);g.font='12px sans-serif';
  var X0=70,Y0=H-46,PWx=W-260,PHx=H-86,TMIN=-80,TMAX=40,ZMAX=35;
  function tx(T){return X0+PWx*(T-TMIN)/(TMAX-TMIN);}
  function zy(z){return Y0-PHx*z/ZMAX;}
  // 格子と軸
  g.strokeStyle='#232b3d';g.beginPath();
  for(var T=-80;T<=40;T+=20){g.moveTo(tx(T),Y0);g.lineTo(tx(T),Y0-PHx);}
  for(var z=0;z<=35;z+=5){g.moveTo(X0,zy(z));g.lineTo(X0+PWx,zy(z));}
  g.stroke();
  g.strokeStyle='#8b93a7';g.beginPath();g.moveTo(X0,Y0-PHx);g.lineTo(X0,Y0);g.lineTo(X0+PWx,Y0);g.stroke();
  g.fillStyle='#8b93a7';
  for(T=-80;T<=40;T+=40)g.fillText(T+'℃',tx(T)-12,Y0+16);
  for(z=0;z<=35;z+=10)g.fillText(z+'km',X0-38,zy(z)+4);
  g.fillText('気温',X0+PWx/2-12,H-6);
  // 対流圏/成層圏の帯
  g.fillStyle='rgba(37,99,235,0.08)';g.fillRect(X0,zy(35),PWx,zy(12)-zy(35));
  g.fillStyle='rgba(22,163,74,0.08)';g.fillRect(X0,zy(12),PWx,zy(0)-zy(12));
  g.fillStyle='#5c6470';g.fillText('成層圏',X0+PWx-56,zy(28));g.fillText('対流圏',X0+PWx-56,zy(5));
  // 基準(280ppm) 破線
  var p0=profile(280),p1=profile(C);
  g.strokeStyle='#8b93a7';g.setLineDash([5,4]);g.lineWidth=2;g.beginPath();
  for(var i=0;i<=100;i++){var zz=ZMAX*i/100,xx=tx(p0(zz)),yy=zy(zz);
    if(i===0)g.moveTo(xx,yy);else g.lineTo(xx,yy);}
  g.stroke();g.setLineDash([]);
  g.strokeStyle='#ff9a8a';g.lineWidth=2.6;g.beginPath();
  for(i=0;i<=100;i++){var z2=ZMAX*i/100,x2=tx(p1(z2)),y2=zy(z2);
    if(i===0)g.moveTo(x2,y2);else g.lineTo(x2,y2);}
  g.stroke();g.lineWidth=1;
  g.fillStyle='#8b93a7';g.fillText('- - - 産業革命前（280 ppm）',X0+PWx+14,60);
  g.fillStyle='#ff9a8a';g.fillText('── いまの設定（'+C+' ppm）',X0+PWx+14,80);
  g.fillStyle='#8b93a7';g.fillText('下は暖まり',X0+PWx+14,120);
  g.fillText('上は冷える ──',X0+PWx+14,138);
  g.fillText('CO₂の「指紋」',X0+PWx+14,156);
  var dF=5.35*Math.log(C/280),dTs=(fb?0.65:0.35)*dF,dSt=p1(25)-p0(25);
  document.getElementById('rF').textContent=(dF>=0?'+':'')+dF.toFixed(2)+' W/m²';
  document.getElementById('rT').textContent=(dTs>=0?'+':'')+dTs.toFixed(2)+' ℃';
  document.getElementById('rS').textContent=(dSt>=0?'+':'')+dSt.toFixed(2)+' ℃';
}
Cs.addEventListener('input',render);render();''')

# ===== 43 量子もつれ: 相関の測定とベル不等式（CHSH） =====
SIM["43_2022_entanglement.html"] = (r'''    <h2>実験してみよう ── もつれた光子で「ベル不等式」を破る</h2>
    <div class="hint">光子ペアを2人（AとB）に送り、それぞれ偏光板の角度を決めて測ります。角度差に対する<b>相関の強さ E</b> が、量子力学と「隠れた変数」理論（測る前から答えが決まっている説）で違う──それを白黒つけるのがベルのテストです。角度を動かし、「測定」ボタンでデータを集めてみましょう。</div>
    <div class="xbox"><canvas id="cv" width="640" height="300"></canvas></div>
    <div class="cpanel">
      <div class="ctl"><label>Aの偏光板の角度 <output id="oA">0°</output></label><input id="A" type="range" min="0" max="90" value="0"></div>
      <div class="ctl"><label>Bの偏光板の角度 <output id="oB">22°</output></label><input id="B" type="range" min="0" max="90" value="22"></div>
    </div>
    <div class="btns">
      <button id="src" class="on">光源：量子もつれ</button>
      <button id="meas">この角度で1000ペア測定</button>
      <button id="chsh">ベルテスト（CHSHのSを測る）</button>
    </div>
    <div class="status" id="st">角度を決めて「測定」を押してみましょう</div>
    <div class="rpanel"><span>いまの角度差 <b id="rD">–</b></span><span>相関 E の理論値 <b id="rE">–</b></span><span>CHSHの S <b id="rS">まだ測っていない</b></span></div>
    <div class="note">量子力学の予言は E = cos2(a−b)、「隠れた変数」の代表的モデルは折れ線（グラフの点線）で、<b>CHSH量 S は隠れた変数なら必ず |S|≦2、量子力学なら最大 2√2 ≈ 2.83</b>。測定ボタンは実際に乱数で1000ペアを生成する本物のシミュレーションです（量子側は cos²で相関する乱数、古典側は共通の隠れた偏光 λ を持つ粒子ペア）。アスペらの実験は S>2 を確認し、「自然は測る前から答えを決めていない」ことを示しました。</div>''',
r'''var cv=document.getElementById('cv'),g=cv.getContext('2d'),W=cv.width,H=cv.height;
var As=document.getElementById('A'),Bs=document.getElementById('B'),st=document.getElementById('st');
var quantum=true,pts=[],Sres=null;
document.getElementById('src').addEventListener('click',function(){quantum=!quantum;
  this.textContent='光源：'+(quantum?'量子もつれ':'古典粒子（隠れた変数）');
  this.classList.toggle('on',quantum);pts=[];Sres=null;render();});
function samplePair(a,b){ // 1ペアの測定結果 (+1/-1, +1/-1)
  var ar=a*Math.PI/180,br=b*Math.PI/180;
  if(quantum){ // もつれ状態: P(同じ)=cos²(a-b)
    var A2=Math.random()<0.5?1:-1;
    var same=Math.random()<Math.pow(Math.cos(ar-br),2);
    return [A2,same?A2:-A2];
  }else{ // 隠れた変数: 共通のλを持ち、偏光板と45°以内なら+1
    var lam=Math.random()*Math.PI;
    function det(t){var d=Math.abs(((t-lam)%Math.PI+Math.PI)%Math.PI);d=Math.min(d,Math.PI-d);
      return d<Math.PI/4?1:-1;}
    return [det(ar),det(br)];
  }}
function measureE(a,b,n){var s=0;for(var i=0;i<n;i++){var r=samplePair(a,b);s+=r[0]*r[1];}return s/n;}
document.getElementById('meas').addEventListener('click',function(){
  var a=+As.value,b=+Bs.value,E=measureE(a,b,1000);
  pts.push([Math.abs(a-b),E]);
  st.className='status yes';st.textContent='1000ペア測定 → E = '+E.toFixed(3)+'（グラフに点を打ちました）';
  render();});
document.getElementById('chsh').addEventListener('click',function(){
  var E1=measureE(0,22.5,2000),E2=measureE(0,67.5,2000),E3=measureE(45,22.5,2000),E4=measureE(45,67.5,2000);
  Sres=E1-E2+E3+E4;
  if(Sres>2.05){st.className='status yes';st.textContent='S = '+Sres.toFixed(2)+' > 2 ── ベル不等式が破れた！ 隠れた変数では説明できない';}
  else{st.className='status no';st.textContent='S = '+Sres.toFixed(2)+' ≦ 2 ── 隠れた変数の範囲内（古典光源では破れない）';}
  render();});
function render(){
  var a=+As.value,b=+Bs.value,d=Math.abs(a-b);
  document.getElementById('oA').textContent=a+'°';document.getElementById('oB').textContent=b+'°';
  g.clearRect(0,0,W,H);g.font='12px sans-serif';
  var X0=60,Y0=H/2+40,PWx=W-100,Aamp=H/2-60;
  function xd(dd){return X0+PWx*dd/90;}
  function ye(E){return Y0-Aamp*E;}
  g.strokeStyle='#232b3d';g.beginPath();g.moveTo(X0,ye(0));g.lineTo(X0+PWx,ye(0));g.stroke();
  g.strokeStyle='#8b93a7';g.beginPath();g.moveTo(X0,ye(1));g.moveTo(X0,ye(-1)+0);g.moveTo(X0,Y0+Aamp);g.moveTo(X0,ye(1));g.lineTo(X0,ye(-1));g.stroke();
  g.fillStyle='#8b93a7';
  [0,30,60,90].forEach(function(v){g.fillText(v+'°',xd(v)-8,ye(-1)+18);});
  g.fillText('偏光板の角度差 |a−b|',X0+PWx/2-56,ye(-1)+36);
  g.fillText('+1（いつも同じ結果）',X0+6,ye(1)-6);
  g.fillText('−1（いつも逆）',X0+6,ye(-1)+12);
  g.fillText('0（無関係）',X0+PWx-70,ye(0)-6);
  // 量子: cos2Δ
  g.strokeStyle='#7ee787';g.lineWidth=2.5;g.beginPath();
  for(var px=0;px<=PWx;px++){var dd=90*px/PWx,E=Math.cos(2*dd*Math.PI/180);
    var y=ye(E);if(px===0)g.moveTo(X0,y);else g.lineTo(X0+px,y);}
  g.stroke();g.lineWidth=1;
  g.fillStyle='#7ee787';g.fillText('量子力学 E=cos2(a−b)',xd(6),ye(0.92));
  // 古典: 折れ線 1-4Δ/90... E=1-|Δ|/22.5? sawtooth 1→-1 at 90: E=1-2Δ/45? Δ=45→-1: E=1-Δ/22.5
  g.strokeStyle='#ff9a8a';g.setLineDash([5,4]);g.lineWidth=2;g.beginPath();
  for(px=0;px<=PWx;px++){var d2=90*px/PWx,Ec=1-d2/22.5;if(Ec<-1)Ec=-1;
    if(d2>45)Ec=-1+(d2-45)/22.5;if(Ec>1)Ec=1;
    var y2=ye(Ec);if(px===0)g.moveTo(X0,y2);else g.lineTo(X0+px,y2);}
  g.stroke();g.setLineDash([]);g.lineWidth=1;
  g.fillStyle='#ff9a8a';g.fillText('隠れた変数モデル（点線）',xd(40),ye(-0.55));
  // 現在の角度差ライン
  g.strokeStyle='#ffd257';g.setLineDash([3,4]);g.beginPath();g.moveTo(xd(d),ye(1));g.lineTo(xd(d),ye(-1));g.stroke();g.setLineDash([]);
  // 測定点
  pts.forEach(function(p){g.fillStyle='#ffd257';g.beginPath();g.arc(xd(p[0]),ye(p[1]),4.5,0,7);g.fill();});
  document.getElementById('rD').textContent=d+'°';
  document.getElementById('rE').textContent=(quantum?Math.cos(2*d*Math.PI/180):Math.max(-1,Math.min(1,d<=45?1-d/22.5:-1+(d-45)/22.5))).toFixed(3)+(quantum?'（量子）':'（古典）');
  document.getElementById('rS').textContent=Sres===null?'まだ測っていない':Sres.toFixed(2)+'（古典の上限2 / 量子の最大2.83）';
}
[As,Bs].forEach(function(s){s.addEventListener('input',render);});render();''')

# ===== 45 ホップフィールド: 連想記憶ネットワークの想起（本物のホップフィールド網） =====
SIM["45_2024_ml.html"] = (r'''    <h2>実験してみよう ── 壊れた記憶をエネルギー最小化で思い出す</h2>
    <div class="hint">8×8のホップフィールド・ネットワークに「T」「X」「口」の3つのパターンを記憶させてあります。パターンを選んでノイズをかけ、「1ステップ想起」を押していくと──ネットワークが<b>エネルギーを下げながら</b>正しい記憶を復元します。</div>
    <div class="xbox"><canvas id="cv" width="640" height="300"></canvas></div>
    <div class="btns">
      <button data-p="0" class="on">T</button><button data-p="1">X</button><button data-p="2">口</button>
    </div>
    <div class="cpanel">
      <div class="ctl"><label>ノイズ（反転させる割合） <output id="oN">15 %</output></label><input id="N" type="range" min="0" max="45" value="15"></div>
    </div>
    <div class="btns">
      <button id="noise">ノイズをかけ直す</button>
      <button id="step">1ステップ想起</button>
      <button id="run">最後まで想起</button>
    </div>
    <div class="status" id="st">–</div>
    <div class="rpanel"><span>ネットワークのエネルギー <b id="rE">–</b></span><span>正解との一致 <b id="rM">–</b></span></div>
    <div class="note">結合 W = Σξξᵀ（ヘッブ学習）、更新 s ← sign(Ws)、エネルギー E = −½sᵀWs という<b>本物のホップフィールド網（1982年のモデルそのもの）</b>を計算しています。1ステップごとにエネルギーが必ず下がり、記憶パターン＝エネルギーの谷に落ち込む──「記憶の想起」を物理学のエネルギー地形の問題に置き換えたこの発想が、スピングラス物理とニューラルネットをつなぎ、現代のAIへ続く出発点になりました。ノイズを45%にすると別の谷（間違った記憶や裏返しパターン）に落ちることもあります。</div>''',
r'''var cv=document.getElementById('cv'),g=cv.getContext('2d'),W=cv.width,H=cv.height;
var Ns=document.getElementById('N'),st=document.getElementById('st');
var PT=[
 ["########","...##...","...##...","...##...","...##...","...##...","...##...","...##..."],
 ["#......#",".#....#.","..#..#..","...##...","...##...","..#..#..",".#....#.","#......#"],
 ["########","#......#","#......#","#......#","#......#","#......#","#......#","########"]];
var N2=64,pats=PT.map(function(p){var a=[];p.forEach(function(row){row.split('').forEach(function(ch){a.push(ch==='#'?1:-1);});});return a;});
var Wm=[];for(var i=0;i<N2;i++){Wm.push([]);for(var j=0;j<N2;j++){var s=0;
  if(i!==j)pats.forEach(function(p){s+=p[i]*p[j];});Wm[i].push(s/N2);}}
var target=0,state=pats[0].slice(),hist=[];
document.querySelectorAll('.btns button[data-p]').forEach(function(b){
  b.addEventListener('click',function(){target=+b.dataset.p;
    document.querySelectorAll('.btns button[data-p]').forEach(function(x){x.classList.toggle('on',x===b)});
    doNoise();});});
function energy(s){var e=0;for(var i=0;i<N2;i++)for(var j=0;j<N2;j++)e-=0.5*Wm[i][j]*s[i]*s[j];return e;}
function overlap(s){var m=0;for(var i=0;i<N2;i++)m+=s[i]*pats[target][i];return m/N2;}
function doNoise(){state=pats[target].slice();
  var nf=+Ns.value/100;
  for(var i=0;i<N2;i++)if(Math.random()<nf)state[i]*=-1;
  hist=[energy(state)];
  st.className='status no';st.textContent='ノイズをかけました ──「1ステップ想起」で復元してみましょう';
  render();}
function stepOnce(){var order=[];for(var i=0;i<N2;i++)order.push(i);
  for(i=N2-1;i>0;i--){var j=Math.floor(Math.random()*(i+1));var t=order[i];order[i]=order[j];order[j]=t;}
  var changed=0;
  order.forEach(function(k){var h2=0;for(var j2=0;j2<N2;j2++)h2+=Wm[k][j2]*state[j2];
    var nv=h2>=0?1:-1;if(nv!==state[k]){state[k]=nv;changed++;}});
  hist.push(energy(state));
  var ov=overlap(state);
  if(changed===0){
    if(Math.abs(ov)>0.99){st.className='status yes';st.textContent=ov>0?'完全に思い出した！ エネルギーの谷（記憶）に到達':'裏返しパターンの谷に落ちた（これも安定解）';}
    else{st.className='status no';st.textContent='収束したが別の谷に落ちた ── ノイズが多すぎたかも';}}
  else{st.className='status';st.style.background='#fff7e6';st.style.color='#8a5a00';st.textContent='想起中…（'+changed+' 個のニューロンが反転）';}
  render();return changed;}
document.getElementById('noise').addEventListener('click',doNoise);
document.getElementById('step').addEventListener('click',stepOnce);
document.getElementById('run').addEventListener('click',function(){var n=0;
  (function go(){if(stepOnce()>0&&n++<20)setTimeout(go,220);})();});
Ns.addEventListener('input',function(){document.getElementById('oN').textContent=Ns.value+' %';});
function render(){
  document.getElementById('oN').textContent=Ns.value+' %';
  g.clearRect(0,0,W,H);g.font='12px sans-serif';
  // 状態グリッド
  var CS=28,GX=60,GY=36;
  for(var i=0;i<N2;i++){var x=GX+(i%8)*CS,y=GY+Math.floor(i/8)*CS;
    g.fillStyle=state[i]>0?'#7ee787':'#141a28';
    g.fillRect(x,y,CS-2,CS-2);}
  g.fillStyle='#8b93a7';g.fillText('ネットワークの状態（64ニューロン）',GX,GY-10);
  // 正解（小さく）
  var cs2=10,PX=330,PY=44;
  g.fillText('記憶している正解',PX,PY-8);
  for(i=0;i<N2;i++){var x2=PX+(i%8)*cs2,y2=PY+Math.floor(i/8)*cs2;
    g.fillStyle=pats[target][i]>0?'#8ab6ff':'#141a28';
    g.fillRect(x2,y2,cs2-1,cs2-1);}
  // エネルギー推移
  var EX=330,EY=270,EW=270,EH=100;
  g.strokeStyle='#8b93a7';g.beginPath();g.moveTo(EX,EY-EH);g.lineTo(EX,EY);g.lineTo(EX+EW,EY);g.stroke();
  g.fillStyle='#8b93a7';g.fillText('エネルギーの推移（ステップごと）',EX,EY-EH-8);
  var e0=energy(pats[target]);   // 谷の底
  if(hist.length>0){var emax=Math.max.apply(null,hist),emin=e0;
    g.strokeStyle='#ffd257';g.lineWidth=2;g.beginPath();
    hist.forEach(function(e,k){var x3=EX+EW*k/Math.max(6,hist.length-1);
      var y3=EY-4-EH*0.9*(e-emin)/Math.max(1e-9,emax-emin);
      if(k===0)g.moveTo(x3,y3);else g.lineTo(x3,y3);});
    g.stroke();g.lineWidth=1;}
  document.getElementById('rE').textContent=energy(state).toFixed(1)+'（記憶の谷の底: '+e0.toFixed(1)+'）';
  var ov=overlap(state);
  document.getElementById('rM').textContent=(ov*100).toFixed(0)+' %';
}
doNoise();''')




