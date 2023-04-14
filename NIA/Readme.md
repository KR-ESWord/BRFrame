# NIA Body Cancer 인공지능 학습용 Dataset 구축

- 기간 : 2020.11 ~ 2021.06

- 대상 : NIA, 고신대학병원, 경북대학병원, AITrics, AMSquare, ManiaMind

- 개요 : 인공지능 학습용 의료 이미지 데이터셋 구축 사업

- 목적 : 체부암의 CT, X-Ray, PET-CT, 초음파, 병리 이미지 데이터를 전문가가 병변의 위치에 Bounding Box 및 폴리곤의 형태로 라벨링하여 이를 인공지능 모델이 학습 할 수 있도록 가공하여 AI Hub에 등재

- 구성 환경
  - 유방암 : X-Ray, CT, 초음파 -> 경북대 자체 개발 라벨링 도구
  - 폐암 : X-Ray, CT, PET-CT, 초음파 -> Web 기반 라벨링 도구 / 병리 -> QuPath, Azure VM

- 데이터 유형
  - X-Ray, CT, PET-CT, 초음파 : dicom
  - 병리 : tif
  - Annotation : json

- 수행 절차
  1. 각 병원에서 의료 이미지 데이터 수집
  2. 환자 정보 비식별화 진행
  3. 비식별화 데이터를 Azure Storage로 업로드
  4. 각 전문가들이 Web 기반 라벨링 도구 및 QuPath를 이용하여 라벨링 수행
  5. 라벨링 데이터 검수
  6. 인공지능 학습용 coco dataset format으로 가공 후 Azure Storage 업로드
  7. 인공지능 베이스라인 모형(U-Net) 구성하여 데이터 품질 검증
  8. AI Hub 등재

- 역할
  - Azure Storage 및 Virtual Machine, QuPath 관리
  - 데이터 수집, 라벨링, 정제 현환 집계
  - 환자 정보 비식별화
  - 데이터 가공 및 AI Hub 등재

- 결과
  - 폐암 : [https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=229]
- 갑상선암 : [https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=201]
- 유방암 : [https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=215]
