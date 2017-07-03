
FROM python:3.5-slim
ADD . /root/betdaq_py/
RUN pip install -r /root/betdaq_py/requirements.txt
WORKDIR /root/betdaq_py/
RUN python setup.py install