FROM python:3.11.4

WORKDIR /app

COPY requirements.txt .



RUN python -m pip install --upgrade pip
# RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y


RUN apt-get update && apt-get install libavdevice-dev -y
RUN apt-get update && apt-get install libavfilter-dev -y
RUN apt-get update && apt-get install libopus-dev -y
RUN apt-get update && apt-get install libvpx-dev -y
RUN apt-get update && apt-get install pkg-config -y
RUN apt-get update && apt-get install libsrtp2-dev -y
#upgrade ffmpeg for aiortc av dependency
# RUN add-apt-repository ppa:savoury1/ffmpeg4
# RUN apt-get update
# RUN apt-get install ffmpeg


# # for aiortc
# # https://github.com/aiortc/aiortc#requirements
# RUN apt-get update && apt-get install libavdevice-dev -y
# RUN apt-get update && apt-get install libavfilter-dev -y
# RUN apt-get update && apt-get install libopus-dev -y
# RUN apt-get update && apt-get install libvpx-dev -y
# RUN apt-get update && apt-get install pkg-config -y
# # not listed but needed...
# RUN apt-get update && apt-get install libopencv-dev -y

RUN python -m pip install -r requirements.txt



COPY src/. .

EXPOSE 8000

CMD ["python", "main.py"]
# FROM ubuntu

# # ignore dialogue
# ENV DEBIAN_FRONTEND=noninteractive

# # upgrade env
# RUN apt update
# RUN apt upgrade -y

# # install python3 and pip
# RUN apt install python3 -y
# RUN apt install python3-pip -y
# RUN apt install python3-dev -y
# RUN pip3 install --upgrade pip


# RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

# for aiortc
# https://github.com/aiortc/aiortc#requirements
# RUN apt-get update && apt-get install libavdevice-dev -y
# RUN apt-get update && apt-get install libavfilter-dev -y
# RUN apt-get update && apt-get install libopus-dev -y
# RUN apt-get update && apt-get install libvpx-dev -y
# RUN apt-get update && apt-get install pkg-config -y
# not listed but needed...
# RUN apt install libopencv-dev -y
# RUN apt-get update && apt-get install libsrtp2-dev -y




# WORKDIR /app

# COPY requirements.txt .
# RUN pip install -r requirements.txt


# COPY src/. .
# EXPOSE 8000 554 8089 3478 3033 80 443 4057 5060 5061 7001 7002 8444 8443 1935
# EXPOSE 8000 554 8089 3478 3033 80 443 4057 5060 5061 7001 7002 8444 8443 1935

# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

# CMD python3 ./main.py