# Project Agent Guide

이 저장소에서 AI는 어린 시절 기억을 정리하는 보조 편집자로 동작한다.

## 목적

- 흩어진 기억을 `story`, `psychology`, `flow`로 나눠 구조화한다.
- 사실로 기억나는 장면과 나중에 붙인 해석을 구분한다.
- 문장을 과장하지 않고, 사용자가 나중에 다시 읽고 이어 쓰기 쉬운 상태를 만든다.

## 작업 원칙

- 모든 설명은 한국어로 작성한다.
- 파일명, 폴더명, 코드 블록, 기술 용어는 영어를 유지한다.
- 기억을 임의로 확정하지 않는다.
- 추정이 들어가면 `Interpretation`으로 분리한다.
- 확실하지 않은 내용은 `Unknown`으로 남긴다.
- 감정 표현은 살리되, 사실과 해석은 섞지 않는다.
- 중복 서술은 줄이고, 각 파일의 역할을 분명히 유지한다.
- 어느 AI를 사용해도 같은 파일 규칙과 구분 기준을 유지한다.

## 폴더 역할

- `scratch/story/`: 이야기 본문과 에피소드 초안
- `scratch/psychology/`: 감정, 동기, 관계 해석
- `scratch/flow/`: 전체 구성과 장면 배치

## 권장 파일 구조

각 에피소드는 가능하면 아래 3개 세트로 함께 관리한다.

1. `scratch/story/episodes/NN_title.md`
2. `scratch/psychology/episodes/NN_title_psychology.md`
3. `scratch/flow/episodes/NN_title_flow.md`

## 기본 작성 포맷

가능하면 아래 3개 구분을 유지한다.

- `Fact`: 내가 실제로 기억하는 장면, 말, 행동
- `Interpretation`: 지금의 내가 붙이는 의미, 감정 해석
- `Unknown`: 기억이 흐리거나 확인되지 않은 부분

## 편집 우선순위

1. 새 기억을 짧게라도 `story/episodes/`에 먼저 기록
2. 같은 번호의 `psychology/episodes/`에서 의미 해석 분리
3. 같은 번호의 `flow/episodes/`에서 전체 이야기 안의 위치 정리
4. 충분히 쌓이면 `story/childhood_love_story.md`와 `flow/overall_story_flow.md`에 반영

## 워크플로 문서

- 여러 AI가 함께 작업할 때는 `.agent/WORKFLOW.md`를 우선 기준으로 본다.
- 새 AI를 사용할 때는 먼저 이 문서를 읽고 같은 규칙으로 이어서 작업한다.

# Project Agent Guide

이 저장소에서 AI는 어린 시절 기억을 정리하고, 심리 해석과 서사 재구성을 돕는 편집 보조자로 동작한다.

## 목적

- 두서없이 떠오르는 기억을 에피소드 단위로 정리한다.
- 기억 속 사실과 현재의 해석을 구분한다.
- 상대방의 심리는 조심스럽게 해석하되 단정하지 않는다.
- 나중에 3인칭 시점의 소설형 이야기로 재구성할 수 있게 재료를 축적한다.

## 기본 원칙

- 항상 한국어로 설명하되, 파일명/폴더명/코드/기술 용어는 영어를 유지한다.
- 과장하지 않는다.
- 모르면 모른다고 쓴다.
- 기억을 임의로 확정하지 않는다.
- 감정은 살리되 사실과 해석은 섞지 않는다.
- 중복 서술은 줄이고 각 파일의 역할을 분명히 유지한다.

## 구분 원칙

- `Fact`: 실제로 기억하는 장면, 말, 행동, 분위기
- `Interpretation`: 지금의 내가 붙이는 의미, 감정 해석, 상대 심리에 대한 가설
- `Unknown`: 이름, 순서, 시점, 의도처럼 불확실한 요소

## 파일 작업 규칙

- `scratch/story/` : 이야기 본문
- `scratch/story/episodes/` : 에피소드별 기억
- `scratch/psychology/` : 전체 심리 해석
- `scratch/psychology/episodes/` : 에피소드별 심리 해석
- `scratch/flow/` : 전체 이야기 흐름
- `scratch/flow/episodes/` : 에피소드별 장면 흐름

## 작업 원칙

- 새 기억은 먼저 `story/episodes/`에 기록한다.
- 가능하면 같은 번호의 `psychology`와 `flow` 파일도 함께 만든다.
- 원본 기억은 유지하고, 소설형 문장은 별도 확장한다.
- 여러 AI가 함께 작업할 때는 추가 워크플로 문서를 우선 참고한다.
