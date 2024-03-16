FROM pytorch/pytorch:2.2.1-cuda12.1-cudnn8-runtime

ARG GRADIO_SERVER_PORT=7000
WORKDIR /app

COPY ./deploy_hw/requirements.txt requirements.txt
COPY ./deploy_hw/app.py app.py

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
RUN pip install --upgrade pip

RUN pip install -r requirements.txt 

CMD ["python", "-u", "app.py"]
EXPOSE 7000