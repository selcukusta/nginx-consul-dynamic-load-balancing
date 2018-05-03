# Dynamic Nginx upstream definition with Consul and Registrator

* [Consul](http://www.consul.io) for service discovery
* [Registrator](https://github.com/gliderlabs/registrator) to register services with Consul. **Registrator** monitors for containers being started and stopped and updates Consul when a container changes state.
* [NGINX](http://nginx.org/) for load balancing

---
*[This](https://github.com/nginxinc/NGINX-Demos/tree/master/consul-template-demo) repository was the source of inspiration for this work.*
