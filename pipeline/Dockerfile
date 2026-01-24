
FROM python:3.13.11-slim

RUN pip install pandas pyarrow

WORKDIR /code
ENV PATH="/code/.venv/bin:$PATH"

COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

COPY "pyproject.toml" "uv.lock" ".python-version" ./

RUN uv sync --locked

COPY df_zone.py .
COPY taxi_zone_lookup.csv .

ENTRYPOINT ["python", "df_zone.py"]
