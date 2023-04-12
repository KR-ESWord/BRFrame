# BRFrame

- Azure Cognitive Service
  - Azure Cognitive Service를 이용하여 SK TNS에서 제공한 건설 현장 촬영 사진을 통한 Computer Vision을 이용한 안전 진단 프로젝트
  - Process 1. 건설 작업 현장에서 작업자의 안전 장비 착용 유무 및 현장 안전 설비 설치 유무 Classification 및 Object Detection 진행
  - Process 2. 건설 현장 관리자의 안전 진단 체크리스트 문서에서 항목별 체크 여부 및 관리자 서명 여부의 OCR
  - 수행 역할
    - 이미지 데이터 라벨링
    - Azure Cognitive Service API를 이용한 Python 학습 코드 및 추론 코드 구성

- Azure IoT Hub & Central
  - Azure의 IoT Hub 및 Central 서비스 교육 및 데모 진행

- NIA 데이터 구축 사업
  - 정부 주관 의료 데이터 구축 사업과 관련하여 컨소시엄에 참가하여 인공지능 학습용 데이터 구축하여 AI Hub 등재
  - 수행 역할
    - 개인정보 데이터 비식별화
      - 병원에서 사용하는 환자 개인으 고유 ID를 새로운 ID로 재생성하고 dcm 등 의료 이미지 데이터의 메타데이터에서 환자 개인정보 삭제
      - 새로 생성한 ID는 병원에서만 관리하여 개인정보의 유출을 방지
    - 데이터 관리 및 검수
      - Azure Storage에 라벨링 대상 데이터 업로드 현황 파악
      - 라벨링 작업이 완료된 데이터 현황 파악
      - 제출 기준에 따른 데이터 검수
      - NIA Amazon S3에 제출
    - Azure VM 관리
      - 전문가의 라벨링 작업 공간인 Azure VM의 자원 관리
    - 라벨링 데이터 형식 변환
      - 좌표 및 메타 데이터를 병합하여 COCO dataset format으로 변환 작업 수행

- Azure Video Analyzer(서비스 종료) & Spatial Analytics
  - 폐쇄회로 카메라(CCTV) 및 GPU 컴퓨팅 자원을 이용하여 실시간 비디오 데이터를 전달받아서 Object Detection, Spatial Analytics를 수행하는 Topology 구성 및 IoT Hub의 Message 기능을 이용하여 실시간으로 결과를 보여주는 Python 코드 구성
  - Spatial Analytics란? 실시간 영상 화면의 임의의 공간에 직선 또는 다각형 도형을 그려서 해당 구역으로 사람 또는 물체가 들어오는지 나가는지, 어떠한 경로로 움직이는지를 분석하는 서비스

- Azure Kinect DK
  - Azure Kinect DK란?
