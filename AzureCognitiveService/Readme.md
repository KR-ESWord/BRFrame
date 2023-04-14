# Azure Cognitive Service POC

## 대상 : SK TNS

- 개요 : Azure Cognitive Service의 API를 이용하여 Computer Vision 모형을 학습하여 건설 작업 현장에서의 안전 상태 판별을 위한 POC 수행

- 목적 : 작업자들의 안전 장비 착용 유무 판별, 작업 현장 시설물 설치 여부 판별, 안전 진단 체크리스트 작성 여부 판별

- 구성 환경
  - 파이썬
  - Azure Cognitive Service API
    -  Computer Vision, Custom Vision, Face API, OCR
  -  VoTT

-  데이터 유형
  -  TBM : 작업 시작 전 소규모 모임 또는 1인 사진
  -  Directional Sign : 작업 현장 표시 간판 설치 사진
  -  Facility 1 : 차량 차체 트리거 및 바퀴 서포터 설치 사진
  -  Facility 2 : 러버콘 설치 사진
  -  Chain : 전신주 작업 시 안전 고리 체결 사진
  -  Document : 작업 허가서, 현장 위험성 평가서, 무재해 확인서 체크 및 서명 사진

-  수행 절차
  1. 각 작업 현장 별 작업 상황 사진 획득
  2. Image Bounding Box Labeling
  3. Azure Cognitive Service API 호출하여 AI 모형 학습
  4. Test Image를 이용하여 모형 평가
