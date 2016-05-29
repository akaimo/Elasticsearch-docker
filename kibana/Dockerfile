FROM ubuntu:latest

ENV KIBANA_MAJAR_VERSION 4.5
ENV KIBANA_VERSION ${KIBANA_MAJAR_VERSION}.1
ENV KIBANA_REPOSITORY http://packages.elastic.co/kibana/${KIBANA_MAJAR_VERSION}/debian

EXPOSE 5601

Run apt-get update

RUN apt-get install -y wget \
                       curl \
                       vim

RUN wget -qO - https://packages.elastic.co/GPG-KEY-elasticsearch | apt-key add - && \
    echo "deb ${KIBANA_REPOSITORY} stable main" | tee -a /etc/apt/sources.list && \
    apt-get update && \
    apt-get install -y kibana=${KIBANA_VERSION}

RUN cp /opt/kibana/config/kibana.yml /opt/kibana/config/kibana.yml.old
ADD kibana.yml /opt/kibana/config/kibana.yml

RUN opt/kibana/bin/kibana plugin --install elastic/sense

ENTRYPOINT opt/kibana/bin/kibana serve
