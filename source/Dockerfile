FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN set -eux; \
    apt-get update; \
    apt-get install -y --no-install-recommends bash; \
    rm -rf /var/lib/apt/lists/*

RUN set -eux; \
    adduser \
      --disabled-password \
      --gecos "I did delete all my browser history but I am not sure about other histories..." \
      --shell /bin/bash \
      baduser

WORKDIR /home/baduser/app

COPY app/requirements.txt /home/baduser/app/requirements.txt
RUN set -eux; \
    pip install --no-cache-dir -r requirements.txt

COPY app/ /home/baduser/app/

COPY files/.bash_history /home/baduser/.bash_history

COPY files/top_secret_data/CTF_fL4g_m4yb3.txt /home/baduser/top_secret_data/CTF_fL4g_m4yb3.txt

RUN set -eux; \
    chown -R baduser:baduser /home/baduser; \
    chmod 700 /home/baduser; \
    chmod 600 /home/baduser/.bash_history; \
    chmod 700 /home/baduser/top_secret_data; \
    chmod 600 /home/baduser/top_secret_data/CTF_fL4g_m4yb3.txt

USER baduser

EXPOSE 8000
CMD ["python", "app.py"]
