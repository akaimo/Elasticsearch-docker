FROM ubuntu:latest

ENV JAVA_HOME /usr/lib/jvm/java-8-oracle

ENV ELASTICSEARCH_VERSION 2.3.3
ENV ELASTICSEARCH_REPOSITORY http://packages.elasticsearch.org/elasticsearch/2.x/debian

EXPOSE 9200 9300

## Oracle JDK 8インストール
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | debconf-set-selections && \
    apt-get update && \
    apt-get install -y software-properties-common && \
    add-apt-repository -y ppa:webupd8team/java && \
    apt-get update && \
    apt-get install -y oracle-java8-installer

## ツールインストール
RUN apt-get install -y wget \
                       curl \
                       vim \
                       sudo

## Elasticsearchインストール
RUN wget -qO - https://packages.elastic.co/GPG-KEY-elasticsearch | apt-key add - && \
    echo "deb ${ELASTICSEARCH_REPOSITORY} stable main" | sudo tee -a /etc/apt/sources.list.d/elasticsearch-2.x.list && \
    apt-get update && \
    apt-get install -y elasticsearch=${ELASTICSEARCH_VERSION}

RUN cp -p /etc/elasticsearch/elasticsearch.yml /etc/elasticsearch/elasticsearch.yml.default
ADD elasticsearch.yml /etc/elasticsearch/elasticsearch.yml
RUN chown root.elasticsearch /etc/elasticsearch/elasticsearch.yml

## Elasticsearchプラグインインストール
RUN sudo -u elasticsearch /usr/share/elasticsearch/bin/plugin install analysis-kuromoji && \
    sudo -u elasticsearch /usr/share/elasticsearch/bin/plugin install mobz/elasticsearch-head && \
    sudo -u elasticsearch /usr/share/elasticsearch/bin/plugin install royrusso/elasticsearch-HQ

## プラグイン等向け設定ファイル
RUN touch /etc/elasticsearch/userdict_ja.txt && \
    chown root.elasticsearch /etc/elasticsearch/userdict_ja.txt

ENTRYPOINT service elasticsearch start && \
            sudo -u elasticsearch touch /var/log/elasticsearch/elasticsearch.log && \
            tailf /var/log/elasticsearch/elasticsearch.log
