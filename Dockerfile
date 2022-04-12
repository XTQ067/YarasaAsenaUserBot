

FROM fusuf/asenauserbot:latest
RUN git clone https://github.com/XTQ067/YarasaAsenaUserBot/ /root/YarasaAsenaUserBot
WORKDIR /root/YarasaAsenaUserBot/
RUN pip3 install -r requirements.txt
CMD ["python3", "main.py"]  
