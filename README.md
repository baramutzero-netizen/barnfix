# 소 잃고 외양간 고친다

잃고 나서야 고치는 도트 인크리멘탈 게임입니다.
외양간에서 소를 잃는 것으로 시작해 가게, 방송, 회사, 청문회, 집, 거울 앞까지 — 갈수록 잃는 것도, 그 책임도 점점 나에게 가까워집니다.

**바로 플레이:** https://baramutzero-netizen.github.io/barnfix/

`index.html` 한 파일로 돌아가서, 내려받아 브라우저로 열어도 됩니다(그림·소리·글꼴이 모두 한 파일에 들어 있음).

## 하는 법

- 현장 탭에서 "땅! 고치기"(또는 장면, 스페이스바)를 누르면 무언가를 하나 잃고, 망치가 바로 그 자리를 수습합니다. 그때마다 **교훈**이 쌓입니다.
- 위의 판에는 지금 장소에서 잃은 것이 나옵니다. "미리 막은 일"은 언제나 0번입니다.
- 대책도 탭의 노드 트리에서 교훈으로 사후 대책을 세웁니다. 외양간엔 판자, 가게엔 사과 안내문, 방송엔 사과 자막, 회사엔 보도자료, 청문회엔 해명 자료, 냉장고와 거울엔 포스트잇이 점점 뒤덮입니다.
- 아직 가지 않은 장소의 노드는 `?`로 가려집니다. 모든 대책을 세운 뒤 **미리 고치기**를 사면 엔딩이 나옵니다. 한 판은 5분 남짓입니다.

## 담긴 것

| 장소 | 잃는 것 | 잃는 까닭 |
| --- | --- | --- |
| 시골 외양간 | 소 | 낡은 판자 |
| 동네 가게 | 손님 | 내 실수 |
| 방송 스튜디오 | 시청자 | 내 말실수 |
| 대기업 | 고객 | 내가 맡은 일의 사고 |
| 청문회 | 신뢰 | 사회적 문제에 대한 내 책임 |
| 우리 집 | 가족과의 시간 | 지키지 못한 약속 |
| 거울 앞 | 건강 | 나 자신 |

- **대책 75개:** 판자 덧대기, 자물쇠, 사과 안내문, 다음에 쓰는 쿠폰, 사과 방송, 금칙어 필터, 보도자료, 보상 쿠폰, 재발 방지 TF, 청문회 답변, 해명 자료, 사퇴 표명, 미안하다는 쪽지, 늦은 선물, "다음 주엔 꼭", 영양제 한 움큼, 헬스장 1년권, "내일부터"…
- **소들:** 누렁소, 얼룩젖소, 흑우, 물소, 야크, 흰 소 — [소 귀에 경 읽기](https://baramutzero-netizen.github.io/moktak/)의 그 소들입니다
- **악단:** 장소마다 두 파트이며 이전 장소 악단도 계속 연주합니다(망치 장단·음메 합창, 문종·포스기 비트, 후원 알림음·로파이, 통화 대기 음악·경보음, 의사봉·카메라 플래시, 거실 TV·자장가, 심장 박동·숨소리)
- **엔딩:** 모든 걸 다 막은 텅 빈 철옹성을 본 뒤, 처음으로 일이 생기기 전에 고칩니다
- **사후 보고서:** 결과 카드 PNG 저장·공유, 다른 게임 추천

## 폴더

| 경로 | 내용 |
| --- | --- |
| `index.html` | 완성된 게임 한 파일 |
| `game.src.html` | 게임 소스 (글꼴·그림 자리 표시자 포함) |
| `assets/aseprite/` | 도트 원본 `.aseprite` (`herd.aseprite`는 소 종류별 프레임, `person`·`heart`는 사람과 건강) |
| `assets/png/` | 같은 그림 4배 PNG |
| `tools/sprites.py` | 모든 도트의 원본 데이터 → `sprites.json`, `.aseprite`, PNG 생성 |
| `tools/cows_from_sogwi.json` | 소 귀에 경 읽기에서 가져온 소 도트 |
| `tools/build.py` | 글꼴을 쓰는 글자만 잘라 넣고 `index.html`을 만듦 |

## 다시 빌드하기

Python 3와 갈무리 글꼴(`npm pack galmuri`)이 필요합니다.

```bash
pip install pillow fonttools brotli
cd tools && python3 sprites.py && cd ..
GALMURI=경로/package/dist python3 tools/build.py
```

## 만든 것과 빌린 것

- 도트 그림과 소리는 모두 직접 그리고 합성했습니다(소리는 브라우저에서 실시간 합성). 게임 속 장소와 인물은 모두 지어낸 것입니다.
- 글꼴: [갈무리(Galmuri)](https://github.com/quiple/galmuri) © Lee Minseo, SIL Open Font License 1.1 — 게임에 쓰는 글자만 잘라 넣었습니다. 라이선스 전문은 `fonts/Galmuri-OFL.txt`.
- 진행 기록은 브라우저(localStorage)에만 저장되고 어디에도 보내지 않습니다.

## 같은 만든이의 다른 게임

- [소 귀에 경 읽기](https://baramutzero-netizen.github.io/moktak/)
- [조삼모사](https://baramutzero-netizen.github.io/josammosa/)
- [앙천이타](https://baramutzero-netizen.github.io/skyspit/)

## 문의

baramutzero@gmail.com
