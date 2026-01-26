
---

## ✨ Extra: Additional Data Ingestion (Beyond the Lecture)

강의에서는 `yellow_taxi_trips_2021_1` 데이터(1개)만 주입하고 종료했습니다.  
하지만 저는 파이프라인을 더 확장해 **추가 데이터까지 주입하는 과정**을 직접 구현했습니다.

### ✅ What I added
- `zones` 데이터(`df_zone.py`)를 추가로 주입
- 주입할 파이썬 스크립트가 컨테이너 이미지 내부에 포함되도록 Docker 이미지 재빌드
- 서로 다른 데이터 주입 작업을 동일한 네트워크(`pipeline_default`) 환경에서 실행

### 📌 Why this matters
- 실무에서는 한 번에 하나의 데이터만 처리하지 않고, **다양한 테이블/소스 데이터를 반복적으로 적재**
- ingestion 스크립트만 추가/교체해서 확장 가능한 구조를 만드는 것이 중요

✅ 결과적으로 강의 범위를 넘어 **데이터 적재(ingestion) 파이프라인 확장 경험**을 추가로 학습했습니다.


<br><br>

---

<br>


◼️ 실행 순서
1) Docker Compose 실행
```
docker compose up -d
```

<br><br>


2) 컨테이너 정상 실행 확인
```
docker ps
```
아래 컨테이너가 Up 상태여야 합니다.

- pipeline-pgdatabase-1 → Up
- pipeline-pgadmin-1 → Up (환경에 따라 이름이 pgadmin이 아니라 이렇게 뜰 수 있어요)

<br><br>

3) 네트워크 확인
```
docker network ls
```
-> pipeline_default 네트워크가 자동 생성되어 있어야 합니다.

<br><br>

4) pgAdmin 접속

브라우저에서 pgAdmin 접속 (compose 파일의 포트 기준)

URL 예시: http://localhost:8085 (또는 Codespaces 포워딩 주소)

- Email: admin@admin.com
- Password: root

<br><br>

5) pgAdmin에서 서버 등록

Register > Server에서 아래 값으로 등록합니다.

- Host name/address: pgdatabase
- Port: 5432
- Username: root
- Password: root

<br><br>

6) 데이터 주입 컨테이너 실행
   
(1) 첫 번째 데이터: yellow_taxi_trips_2021_1
```
docker run -it --rm \
  --network=pipeline_default \
  taxi_ingest:v001 \
  --pg_user=root \
  --pg_pass=root \
  --pg_host=pgdatabase \
  --pg_port=5432 \
  --pg_db=ny_taxi \
  --target_table=yellow_taxi_trips_2021_1 \
  --year=2021 \
  --month=1 \
  --chunksize=5000
```

<br><br>

(2) 두 번째 데이터: zones (df_zone.py)

먼저 이미지 빌드:
```
docker build -t taxi_ingest:v005 .
```

그 다음 실행:
```
docker run -it --rm \
  --network=pipeline_default \
  taxi_ingest:v005 \
  df_zone.py \
  --pg_user=root \
  --pg_pass=root \
  --pg_host=pgdatabase \
  --pg_port=5432 \
  --pg_db=ny_taxi \
  --target_table=zones
```

◾ 포인트
df_zone.py처럼 “다른 주입 작업”을 실행하려면, 해당 파이썬 파일이 컨테이너 이미지(컨테이너 실행 스크립트) 안에 포함되어 있어야 합니다.

<br><br>





