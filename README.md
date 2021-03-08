# NIA-Body-Cancer-Project

# NIA 체부암 인공지능 데이터 구축 및 활용
- 체부암(폐암, 갑상선암, 유방암)
- 컨소시엄
  - NIA
  - AITrics
  - 고신대학 복음병원
  - 경북대학 병원
  - BRFrame
  - AMSquare
  - ManiaMind
  
# 수행절차
  1. 데이터 수집
    - 고신대학 복음병원(폐암, 갑상선암)
    - 경북대학 병원(유방암)
  2. 데이터 비식별화
    - 폐암, 갑상선암 : 고신대학 복음병원, BRFrame
    - 유방암 : 경북대학 병원, 경북대학교 컴퓨터학부
  3. 데이터 어노테이션
    - 폐암(Chest CT, PET CT, X-Ray), 갑상선암(Neck CT, Ultrasound) : JLK의 HelloData Platform
    - 갑상선암(Pathology) : Qupath(오픈 소스 소프트웨어)
    - 유방암(Mammo, MRI, Ultrasound) : 경북대학교 컴퓨터학부 자체제작 소프트웨어 도구
  4. 데이터 구축
    - 폐암, 갑상선암 : BRFrame
    - 유방암 : 경북대학교 컴퓨터학부
  5. 인공지능 활용
    - 폐암 : AMSquare
    - 갑상선암 : AITrics
    - 유방암 : 경북대학교 컴퓨터학부
