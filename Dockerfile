FROM python:3.11 as build

ARG PIP_OPTIONS=.

RUN python -m venv /venv
ENV PATH=/venv/bin:$PATH

COPY . /context
WORKDIR /context

RUN pip install ${PIP_OPTIONS}

FROM python:3.11-slim as runtime

RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

COPY --from=build /venv/ /venv/
ENV PATH=/venv/bin:$PATH

ENTRYPOINT ["mail-in"]
CMD ["--version"]