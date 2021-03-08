# 엑셀 파일 포멧
  - Section : 데이터 수집 차수
  - De-identification_ID : 비식별 환자 ID
  - Patient_ID : 환자 ID
  - Modality : 검사 항목(ex. Chest CT, Ultrasound 등)

{
  'Section' : str,
  'De-identification_ID' : str,
  'Patient_ID' : str,
  'Modality' : str
}

# 실행법
  1. 엑셀 파일 작성
    1) Section : 병원에서 수집한 데이터 업로드 차수 (필수 X)
    2) De-identification_ID : 초기값 'N'
    3) Patient_ID : 데이터의 환자 ID
    4) Modality : 검사 항목
  2. 코드 실행
    1) 코드에서 De-identification_ID의 항목 중 'N' 항목 접근
    2) 7자리의 난수로 되어있는 비식별화 ID 생성 후 할당
    3) 이전에 할당 되어진 비식별화 ID들과 비교하여 중복성 검사
      - 중복일 경우 비식별화 ID 새로 생성 후 중복성 검사 반복
    4) 비식별화 ID가 할당된 엑셀 파일 저장
