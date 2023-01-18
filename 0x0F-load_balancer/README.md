## Tasks on Load balancer

### 0. Double the number of webservers

- Configure webserver web-02 to be identical with web-01 using scripts already created to automate the configuration of as many webservers as needed.

- We’re placing our web servers behind a load balancer for this project, we want to add a custom Nginx response header. The goal here is to be able to track which web server is answering our HTTP requests, to understand and track the way a load balancer works

Requirements:

- Configure Nginx so that its HTTP response contains a custom header (on web-01 and web-02)
- The name of the custom HTTP header must be X-Served-By
- The value of the custom HTTP header must be the hostname of the server Nginx is running on
- Write 0-custom_http_response_header so that it configures a brand new Ubuntu machine to the requirements asked in this task
- Ignore SC2154 for shellcheck


