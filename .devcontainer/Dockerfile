## Iniciamos con la imagen base de Python 3.13 en Debian 11
FROM python:3.13-bullseye

ENV DEBIAN_FRONTEND=noninteractive
ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

## Actualizamos y instalamos dependencias necesarias junto con pandoc, curl, gdebi que requiere Quarto
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    git \
    vim \
    pandoc \
    pandoc-citeproc \
    gdebi-core \
    && rm -rf /var/lib/apt/lists/*

## Creamos un entorno virtual para aislar dependencias de Python
RUN python3 -m venv $VIRTUAL_ENV

## Copiamos los requirements
WORKDIR /app
COPY requirements.txt .

## Instalamos los paquetes de Python en el entorno virtual
RUN pip install --upgrade pip setuptools wheel && \
    pip install -r requirements.txt

## Instalamos Quarto
RUN curl -LO https://quarto.org/download/latest/quarto-linux-arm64.deb && \
    gdebi --non-interactive quarto-linux-arm64.deb && \
    rm -f quarto-linux-arm64.deb

## Definimos el workspace y puerto a exponer
WORKDIR /workspace
EXPOSE 8888

## Comando por defecto abre bash
CMD ["bash"]
