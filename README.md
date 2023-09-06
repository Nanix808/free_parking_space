<h1 align="center">✨ Free Parking Space ✨</h1>

<p align="center">  
<img src="https://img.shields.io/badge/python-3.11 -blueviolet.svg">
<img src="https://badges.frapsoft.com/os/v1/open-source.svg?v=103" >

</p>


## ***Навигация***
- [Описание](#описание)
- [Возможные неполадки](#возможные_неполадки)
- [Как пользоваться сервисом](#как_пользоваться)
  - [Архитектура](#архитектура)
  - [Технологии](#Технологии)
- [How to install](#how_to_install)

<a name="описание"></a> 
## ***Описание***

Сервис реализован для распознавания свободных мест на парковке автомобилей.
Пользователь сможет заранее проверить парковку на наличие и количество свободных мест.
Пользователь может сам задавать RTSP путь к видеокамере и рисовать произвольные парковочные места.



<a name="возможные_неполадки"></a> 
## ***Возможные неполадки***

При использовании сервиса возможно некорректное отображение парковочного места.

**Решение проблемы:**

Правильно размещать видеокамеру

<a name="как_пользоваться"></a> 
## ***Как пользоваться сервисом***
-  Если камера уже добавлена
    - После нажатия на нужную кнопку - пользователь установит соединение с WEB камерой, и отобразится информация о заполненности парковки. Предположительные свободные места будут отмечены **зеленым кругом**. 
    <p align="center">
    <img src="./readme_asserts/main.png" width="70%"></p>

 
-  Если необходимо добавить камеру
    <p align="center">
    <img src="./readme_asserts/use.svg" width="70%"></p>

<a name="архитектура"></a> 
### Архитектура

<p align="center">
<img src="./readme_asserts/parking.vt.svg" width="70%"></p> 

<a name="computer_vision_and_machine_learning"></a> 
### Технологии

- [OpenCV](https://opencv.org/)
- [AioRtc](https://github.com/aiortc/aiortc)
- [VUE](https://vuejs.org/)
- [YOLO](https://docs.ultralytics.com/)

<a name="how_to_install"></a> 
## ***How to install***

- Метод №1 (Подходит для разворачивания на Linux системах (На Windows и Mac работать не будет)):
  - Клонировать репозиторий
  - Выполнить команду docker-compose build
  - Выполнить команду docker-compose up
  - Пререйти по адресу 127.0.0.1:8080

- Метод №2 (Подходит для любых систем (local)):
  - Клонировать репозиторий
  - Настройка BACKEND
    - Установить python https://www.python.org/
    - Перейти в папку cd backend
    - Установить зависимости pip install -r requirements.txt
    - Запустить файл main.py
    - Должен запуститься webserver на 127.0.0.1:8000
  - Настройка FRONTEND
    - Установить nodejs https://nodejs.org/en
    - Перейти в папку cd frontend
    - Запустить команду npm install
    - Запустить команду npm run dev
    - Должен запуститься webserver на 127.0.0.1:8000