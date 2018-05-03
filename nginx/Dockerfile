FROM nginx:1.13.12-alpine

ADD entrypoint.sh entrypoint.sh

ADD /consul/templates/app.conf.tmpl /etc/consul-templates/app.conf.tmpl
ADD /consul/templates/index.html.tmpl /etc/consul-templates/index.html.tmpl

ADD /consul/consul-template.service /etc/service/consul-template.service
ADD /service/nginx.service /etc/service/nginx.service

ENV PATH="${PATH}:/consul-template"

RUN mkdir consul-template && \
    wget https://releases.hashicorp.com/consul-template/0.19.4/consul-template_0.19.4_linux_amd64.tgz && \
    tar -C consul-template -xzvf consul-template_0.19.4_linux_amd64.tgz && \
    rm consul-template_0.19.4_linux_amd64.tgz

ENTRYPOINT [ "./entrypoint.sh" ]