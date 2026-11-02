const CFG = {
  api: '__barn', title: '소 잃고 외양간 고친다', titleSize: 84, sub: '잃고 나서야 고치는 게임', unit: '교훈', tapLabel: '땅! 고치기',
  icon: ['hammer'],
  colors: { bg: '#1b1512', band: '#120e0c', accent: '#e8a33a', dim: '#a8968a', cream: '#f2e6cf', leaf: '#7fb069', panel: '#271e19', line: '#3a2d25', faint: '#7d6d62', gold: '#f3c34f', red: '#e5484d', ink: '#1b1512', btnShade: '#8d5a22' },
  stat: () => `잃을 것 ${fmt(window.__barn.D().mk)} · 대신 고치는 손 ${window.__barn.D().au}번/초`,
  tap: J => J.fixTap(),
  endCard: [['소 잃기 전에,', 600, 110, 'accent'], ['외양간 고치자.', 740, 110, 'accent'], ['잃고 나서야 고치는 게임', 940, 54, 'cream'], ['지금 외양간 고치러 가기', 1080, 60, 'leaf'], ['baramutzero-netizen.github.io/barnfix', 1180, 40, 'cream', 'Galmuri11']],
  async play(h) {
    h.cap('소가 빠져나갔다', '그래서 고쳤다');
    await h.tapFor(2400, 5);
    h.cap('또 빠져나갔다', '또 고쳤다');
    { const tp = h.tapFor(1800, 5); await h.buyAll(0, 100); await tp; }
    h.cap('가게를 차렸더니', '주문 실수로 손님이 떠났다');
    h.buy('v1'); await h.tapFor(1700, 5); await h.buyAll(1, 10);
    h.cap('방송을 켰더니', '말실수로 시청자가 떠났다');
    h.buy('v2'); await h.tapFor(1700, 5); await h.buyAll(2, 10);
    h.cap('회사에선 사고로 고객을,', '청문회에선 신뢰를 잃었다');
    await h.venue(3, 10, 1200); await h.venue(4, 10, 1200);
    h.cap('AI 회사를 세웠더니', '"다른 AI 쓰고 말지"');
    h.buy('v5'); await h.tapFor(1500, 5); await h.buyAll(5, 10);
    h.cap('집에선 가족과의 시간을,', '거울 앞에선 건강을');
    await h.venue(6, 10, 1100); await h.venue(7, 10, 1100);
    h.cap('그리고 마침내', '');
    window.__endK = 0.42; h.buy('end');
  },
};
