
FROM python:3.13.11-slim

RUN pip install pandas pyarrow

WORKDIR /code
ENV PATH="/code/.venv/bin:$PATH"

COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

COPY "pyproject.toml" "uv.lock" ".python-version" ./

RUN uv sync --locked

# ✅ 스크립트 2개 모두 복사
COPY ingest_data.py .
COPY df_zone.py .
COPY taxi_zone_lookup.csv .

ENTRYPOINT ["python"]
CMD ["ingest_data.py"]