# clipnote-extension

[clipnote](https://github.com/zlej123/clipnote)의 크롬 확장. 유튜브 how-to 영상 페이지에서 버튼 한 번으로:

1. Gemini가 영상을 분석해 단계 + 시각 가이드(애매한 표현의 타임스탬프)를 뽑고
2. **재생 중인 플레이어에서 직접** before/center/after 후보 프레임을 canvas로 캡처하고
3. 사용자가 장면을 고르면 `document.md` + 선택한 이미지가 다운로드됩니다.

서버 없이 동작합니다(사용자 본인 Gemini 키, BYOK). 영상 다운로드가 없으므로 yt-dlp도, 봇 차단 문제도 없습니다.

## 설치 (개발자 모드)

1. 이 레포를 clone
2. `chrome://extensions` → 우상단 **개발자 모드** 켜기
3. **압축해제된 확장 프로그램을 로드** → 이 폴더 선택
4. 확장 아이콘 클릭 → Gemini API 키 입력 ([aistudio.google.com/apikey](https://aistudio.google.com/apikey), 무료·카드 불필요)

## 사용

유튜브 영상 페이지(`/watch`) 우하단의 **📋 clipnote** 버튼 클릭 → 분석 → 장면 선택 → 문서 만들기.

- 캡처 중 플레이어가 잠깐 움직입니다(음소거 상태로 seek). 끝나면 원래 위치로 복원됩니다.
- 적합한 장면이 없는 가이드는 "부적합"을 고르면 유튜브 타임스탬프 링크로 대체됩니다.

## clipnote-server 경유 (선택)

설정에서 서버 URL을 넣으면 Gemini 직접 호출 대신 [clipnote-server](https://github.com/zlej123/clipnote-server)의 `/v1/analyze`를 사용합니다. 프롬프트를 확장 재배포 없이 갱신하고 싶을 때 유용합니다.

## skill-core 자산

`assets/skill-core/`는 코어 레포의 프롬프트/스키마 복사본입니다. 코어가 바뀌면:

```bash
python sync_assets.py ../clipnote
```

## 알려진 제약

- `/watch` 페이지 전용 (Shorts 페이지는 아직 미지원)
- 광고 재생 중에는 캡처하지 마세요 — 광고 프레임이 찍힙니다
- DRM 영상(영화 대여 등)은 canvas 캡처가 차단됩니다 (일반 유튜브 영상은 해당 없음)

## 라이선스

MIT
