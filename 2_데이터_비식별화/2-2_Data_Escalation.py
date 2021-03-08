from azure.storage.fileshare import ShareServiceClient as SSC
from azure.storage.fileshare import ShareFileClient as SFC
from azure.storage.fileshare import ShareDirectoryClient as SDC

from azure.storage.blob import BlobServiceClient as BSC
from azure.storage.blob import BlobClient as BC
from azure.storage.blob import ContainerClient as CC

import shutil
import pandas as pd
import os
import random
import numpy as np
from tqdm import tqdm
import time

# Azure File Storage - 원본 데이터
file_storage_connect_str = '<Azure File Storage 연결 문자열>'
# Azure Blob Storage - 비식별 데이터
blob_storage_connect_str = '<Azure Blob Storage 연결 문자열>'

# Azure File Storage Share Service Client Connect
afs_file_service = SSC.from_connection_string(file_storage_connect_str)
# Azure File Storage File Share folder select
cancer = '<암 종 선택>' # 'lung' or 'thyroid'
afs_file_shares = afs_file_service.get_share_client(cancer)

# Blob Service Client Connect
bs_blob_service_client = BSC.from_connection_string(blob_storage_connect_str)

# 데이터를 Blob Storage로 업로드 하는 함수 정의
# NIA 데이터 경로 정의 : 암 종 / 검사 항목 / 양성 or 악성 or 정상 / 비식별 환자 ID / 시리즈 번호 / json, dcm, binary
# 단, JLK의 HelloData Platform 특성상 검사 항목을 각 Blob Container로 지정
# blob_container : 검사 항목
# path0 : 수집 차수
# path1 : 비식별 환자 ID
# path2 : 시리즈 번호
# path3 : 비식별 데이터 파일(dcm)
# local_data_path : 로컬 환경에 생성된 비식별 데이터의 경로
def blob_upload_data(blob_container, path0, path1, path2, path3, local_data_path):
    blob_path = os.path.join(path0, path1, path2, path3)
    blob_client = bs_blob_service_client.get_blob_client(container=blob_container, blob=blob_path)
        
    with open(local_data_path, "rb") as upload_data:
        blob_client.upload_blob(upload_data)

# 원본 데이터 업로드 경로
# 업로드 날짜 / 데이터 수집 차수 / 검사 항목 / 원본 환자 ID / 원본 데이터(dcm)
# 1. Azure File Storage에서 각 암 종별 작업하고자 하는 업로드 날짜 목록 생성
u_date_folder_list = []
for u_date_folder in tqdm(afs_file_shares.list_directories_and_files()):
    u_date_folder_list.append(u_date_folder['name'])

# 2. 목록 출력
for u_date in range(len(u_date_folder_list)):
    print(u_date, ':', u_date_folder_list[u_date])
try:
  # 3. 작업 하고자 하는 목록 선택
    s_u_date = int(input('Select Upload Data Date : '))
    u_date_path = u_date_folder_list[s_u_date]
except:
    print('ERROR!')
# 4. 선택한 목록 확인
print('Work Dir : ', u_date_folder_list[s_u_date])

# 데이터 수집 차수 선택
# 1. 작업하고자 하는 데이터 차수 목록 생성
c_date_list = []
for c_date in afs_file_shares.list_directories_and_files(u_date_path):
    c_date_list.append(c_date['name'])

# 2. 목록 출력
for c_d in range(len(c_date_list)):
    print(c_d, ':', c_date_list[c_d])
    
try:
  # 3. 작업 하고자 하는 차수 선택
    s_c_date = int(input('Select Work Directory : '))
    c_date_path = os.path.join(u_date_path, c_date_list[s_c_date])
except:
    print('ERROR!')

# 4. 선택한 목록 확인
print('Select Work Dir : ', c_date_list[s_c_date])

# 선택한 차수 폴더에서 Azure Blob Storage의 path0의 정보 추출
# 폴더 예시 : 폐악성_CT_20210308_1차_100건
# 폴더 명의 규칙을 찾아서 문자 분리
c_date_n_list = list(c_date_list[s_c_date].split('_'))
print(c_date_n_list)
for c_d_i in range(len(c_date_n_list)):
    # DateTime
    # 문자열 중 수집 일자에 해당하는 정보 찾아서 추출
    if len(c_date_n_list[c_d_i]) == 8 or c_date_n_list[c_d_i][0:4] == '2020' or c_date_n_list[c_d_i][0:4] == '2021':
        datetime = c_date_n_list[c_d_i]
    # Modality
    # 검사 항목 정보를 추출 하여 Blob Container 선택
    if 'CT' in c_date_n_list[c_d_i]:
        modality = 'CT'
        blob_container = 'chest-ct'
        
    elif 'PT' in c_date_n_list[c_d_i]:
        modality = 'PT'
        blob_container = 'pet-ct'
        
    elif 'CR' in c_date_n_list[c_d_i]:
        modality = 'CR'
        blob_container = 'x-ray'
        
    elif 'NCT' in c_date_n_list[c_d_i]:
        modality = 'NCT'
        blob_container = 'neck-ct'
        
    elif 'NCT' in c_date_n_list[c_d_i]:
        modality = 'NCT'
        blob_container = 'neck-ct'
        
# 원본 데이터 임시 저장 경로 정의
# 로컬에 Temporary 폴더가 없을 경우 생성 필요
local_modal_path = os.path.join(os.getcwd(), 'Temporary')

# 추출한 정보 확인
print('DateTime : ', datetime)
print('Modallity : ', modality)

# 암 상태 및 차수 선택(폴더 명에서 추출 가능할 경우 수집 일자 추출법으로 동일하게 추출)
print('Caner State')
print('0 : Malignanent')
print('1 : Benign')
print('2 : Steady')
try:
    s_s = int(input('Select State : '))
    if s_s == 0:
        state = 'm'
    elif s_s == 1:
        state = 'b'
    elif s_s == 2:
        state = 's'
    
    c_n = input('차수 입력 : ')
except:
    print('ERROR!')
    
# path0 생성
path0 = '_'.join((datetime, state, c_n))
print('path0 : ', path0)

# Main
print('Uploading Start!')
modal_path = os.path.join(c_date_path, modality)
for pid_folder in tqdm(afs_file_shares.list_directories_and_files(modal_path)):
    path1 = pid_folder['name'] # Patinet ID
    
    pid_path = os.path.join(modal_path, path1)
    for data in afs_file_shares.list_directories_and_files(pid_path):
        data_name = data['name']
        # ex. 1234567_1_1.dcm
        dcm_name = data_name.split('.')[0]
        dcm_ext = data_name.split('.')[-1]
        d_n_list = list(dcm_name.split('_'))
        pid = d_n_list[0]
        series = str(d_n_list[1]).zfill(7)
        image_num = str(d_n_list[2]).zfill(7)
        
        path2 = series
        path3 = data_name
        
        dcm_path = os.path.join(pid_path, data_name)
        temp_data_path = os.path.join(os.getcwd(), data_name)
        
        # Download Azure File Storage
        afs_file_client = SFC.from_connection_string(file_storage_connect_str, cancer, dcm_path)
        with open(data_name, "wb") as down_data:
            stream = afs_file_client.download_file()
            down_data.write(stream.readall())
        shutil.move(temp_data_path, local_modal_path)
        
        re_dcm_name = '.'.join((('_'.join((pid, series, image_num))), dcm_ext))
        if os.path.isfile(os.path.join(local_modal_path, data_name)):
            os.rename(os.path.join(local_modal_path, data_name),
                      os.path.join(local_modal_path, re_dcm_name))
        while True:
            if os.path.isfile(os.path.join(local_modal_path, data_name)):
                os.remove(os.path.join(local_modal_path, data_name))
                continue
            else :
                break
        
        # Upload Azure Blob Storage
        path3_1 = re_dcm_name
        local_data_path = os.path.join(local_modal_path, re_dcm_name)
        blob_upload_data(blob_container, path0, path1, path2, path3_1, local_data_path)
        
        # 원본 데이터 
        if os.path.isfile(os.path.join(local_modal_path, re_dcm_name)):
            os.remove(os.path.join(local_modal_path, re_dcm_name))
print('Uploading Done!')
