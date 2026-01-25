#!/usr/bin/env python
# coding: utf-8


import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import text
import click 


@click.command()
@click.option("--pg_user", default="root", show_default=True, help="PostgreSQL user")
@click.option("--pg_pass", default="root", show_default=True, help="PostgreSQL password")
@click.option("--pg_host", default="pgdatabase", show_default=True, help="PostgreSQL host (컨테이너 실행이면 pgdatabase)")
@click.option("--pg_port", default=5432, type=int, show_default=True, help="PostgreSQL port")
@click.option("--pg_db", default="ny_taxi", show_default=True, help="PostgreSQL database name")
@click.option("--target_table", default="zones", show_default=True, help="Target table name")
@click.option("--csv_path", default="taxi_zone_lookup.csv", show_default=True, help="CSV path inside container")
def run(pg_user, pg_pass, pg_host, pg_port, pg_db, target_table, csv_path):
    # df = pd.read_csv("taxi_zone_lookup.csv", encoding="utf-8")
    df = pd.read_csv(csv_path, encoding="utf-8")

    # 2) 컬럼명을 DB용으로 통일(소문자)
    df.columns = [c.strip().lower() for c in df.columns]  # locationid, borough, zone, service_zone

    # 3) Postgres 연결
    engine = create_engine(f"postgresql+psycopg2://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}")


    # ✅ 트랜잭션 시작 (블록 끝나면 commit)
    with engine.begin() as conn:
        # (선택) 현재 연결 정보 출력
        db_info = conn.execute(text("SELECT current_database(), inet_server_addr(), inet_server_port()")).fetchone()
        print("DB info:", db_info)

        # ✅ 테이블 없으면 자동 생성 + 데이터 INSERT
        df.to_sql(target_table, con=conn, schema="public", if_exists="append", index=False)

        # ✅ 같은 트랜잭션 안에서 바로 검증
        cnt = conn.execute(text(f"SELECT COUNT(*) FROM public.{target_table}")).scalar()
        print("DB rows:", cnt)

    print("Inserted rows:", len(df))


if __name__ == '__main__':
    run()