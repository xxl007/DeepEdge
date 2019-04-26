FROM tornado_flask_py2.7:latest
MAINTAINER yhu6

RUN mkdir -p /webroot
COPY ./tornado_webapp/run_webapp.sh /webroot/.
CMD /webroot/run_webapp.sh
