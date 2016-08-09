#Dockerfile

FROM  10.63.241.108:5000/ubuntu:latest
#FROM 10.62.55.202:5000/ubuntu_fakeapp:latest

ENV LD_LIBRARY_PATH /usr/local/lib

COPY ./*.so* /usr/local/lib/

EXPOSE 8000

RUN mkdir -p service
RUN mkdir -p data
ADD ./*.json /data/
ADD ./FakeApp_frame /service/app

VOLUME ["/core"]
#CMD /service/app
CMD ulimit -c 1000000000000; /service/app
