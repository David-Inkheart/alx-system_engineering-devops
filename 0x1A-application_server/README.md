<h1>Tasks on Application server</h1>

![App-server](https://user-images.githubusercontent.com/106752187/223699597-0caaa6ea-9d7a-4f18-858e-490ecd268815.jpg)

<h2>Background Context</h2>

<p> 
    Your web infrastructure is already serving web pages via Nginx that you installed in your first
    web stack project. While a web server can also serve dynamic content, this task is usually given
    to an application server. In this project you will add this piece to your infrastructure,
    plug it to your Nginx and make is serve your Airbnb clone project.
</p>

<h3>0. Set up development with Python</h3>

<p>
    Let’s serve what you built for AirBnB clone v2 - Web framework on web-01. This task is an
    exercise in setting up your development environment, which is used for testing and debugging
    your code before deploying it to production.
</p>

<h4>Requirements:</h4>

<ul>
    Make sure that task #3 of your SSH project is completed for web-01. The checker will connect to your servers.
    Git clone your AirBnB_clone_v2 on your web-01 server.
    Configure the file web_flask/0-hello_route.py to serve its content from the route /airbnb-onepage/ on port 5000.
    Your Flask application object must be named app (This will allow us to run and check your code).
</ul>

<p>Example:</p>

<h5>Window 1:</h5>

```
ubuntu@229-web-01:~/AirBnB_clone_v2$ python3 -m web_flask.0-hello_route
 * Serving Flask app "0-hello_route" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
35.231.193.217 - - [02/May/2019 22:19:42] "GET /airbnb-onepage/ HTTP/1.1" 200 -
```

<h5>Window 2:</h5>

```
ubuntu@229-web-01:~/AirBnB_clone_v2$ curl 127.0.0.1:5000/airbnb-onepage/
Hello HBNB!ubuntu@229-web-01:~/AirBnB_clone_v2$
```

</h3>1. Set up production with Gunicorn</h3>

Now that you have your development environment set up, let’s get your production
application server set up with **Gunicorn** on **web-01**, port **5000**. You’ll need
to install **Gunicorn** and any libraries required by your application. Your **Flask**
application object will serve as a **WSGI** entry point into your application. This will
be your production environment. As you can see we want the production and development of
your application to use the same port, so the conditions for serving your dynamic
content are the same in both environments.

<h4>Requirements:</h4>

- Install **Gunicorn** and any other libraries required by your application.
- The Flask application object should be called app.
    (This will allow us to run and check your code)
- You will serve the same content from the same route as in the previous task. You can
    verify that it’s working by binding a **Gunicorn** instance to localhost listening
    on port **5000** with your application object as the entry point.
- In order to check your code, the checker will bind a Gunicorn instance to port 6000,
    so make sure nothing is listening on that port.

Example:

<h5>Terminal 1:</h5>

```
ubuntu@229-web-01:~/AirBnB_clone_v2$ gunicorn --bind 0.0.0.0:5000 web_flask.0-hello_route:app
[2019-05-03 20:47:20 +0000] [3595] [INFO] Starting gunicorn 19.9.0
[2019-05-03 20:47:20 +0000] [3595] [INFO] Listening at: http://0.0.0.0:5000 (3595)
[2019-05-03 20:47:20 +0000] [3595] [INFO] Using worker: sync
[2019-05-03 20:47:20 +0000] [3598] [INFO] Booting worker with pid: 3598
```

<h5>Terminal 2:</h5>

```
ubuntu@229-web-01:~$ curl 127.0.0.1:5000/airbnb-onepage/
Hello HBNB!ubuntu@229-web-01:~$
```

<h3>2. Serve a page with Nginx</h3>

Building on your work in the previous tasks, configure Nginx to serve
your page from the route */airbnb-onepage/*

<h4>Requirements:</h4>

- **Nginx** must serve this page both locally and on its public IP on port 80.
- **Nginx** should proxy requests to the process listening on port 5000.
- Include your Nginx config file as *2-app_server-nginx_config.*

<h4>Notes:</h4>

- In order to test this you’ll have to spin up either your production or development
   application server (listening on port 5000)
- In an actual production environment the application server will be configured to start
   upon startup in a system initialization script. This will be covered in the advanced tasks.
- You will probably need to reboot your server (by using the command `$ sudo reboot`) to have
   Nginx publicly accessible
   
Example:

<h3>On my server:</h3>
<h4>Window 1:</h4>

```
ubuntu@229-web-01:~/AirBnB_clone_v2$ gunicorn --bind 0.0.0.0:5000 web_flask.0-hello_route:app
[2019-05-06 20:43:57 +0000] [14026] [INFO] Starting gunicorn 19.9.0
[2019-05-06 20:43:57 +0000] [14026] [INFO] Listening at: http://0.0.0.0:5000 (14026)
[2019-05-06 20:43:57 +0000] [14026] [INFO] Using worker: sync
[2019-05-06 20:43:57 +0000] [14029] [INFO] Booting worker with pid: 14029

<h4>Window 2:</h4>

ubuntu@229-web-01:~/AirBnB_clone_v2$ curl 127.0.0.1/airbnb-onepage/
Hello HBNB!ubuntu@229-web-01:~/AirBnB_clone_v2$

<h3>On my local terminal:</h3>

vagrant@ubuntu-xenial:~$ curl -sI 35.231.193.217/airbnb-onepage/
HTTP/1.1 200 OK
Server: nginx/1.10.3 (Ubuntu)
Date: Mon, 06 May 2019 20:44:55 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 11
Connection: keep-alive
X-Served-By: 229-web-01

vagrant@ubuntu-xenial:~$ curl 35.231.193.217/airbnb-onepage/
Hello HBNB!vagrant@ubuntu-xenial:~$
```

<h3>3. Add a route with query parameters</h3>

Building on what you did in the previous tasks, let’s expand our web application
by adding another service for **Gunicorn** to handle.
In *AirBnB_clone_v2/web_flask/6-number_odd_or_even*, the route */number_odd_or_even/<int:n>*
should already be defined to render a page telling you whether an integer is odd or even.
You’ll need to configure **Nginx** to proxy HTTP requests to the route
*/airbnb-dynamic/number_odd_or_even/(any integer)* to a **Gunicorn** instance listening on port 5001.
The key to this exercise is getting **Nginx** configured to proxy requests to processes listening
on two different ports. You are not expected to keep your application server processes running.
If you want to know how to run multiple instances of **Gunicorn** without having multiple terminals
open, see tips below.

<h4>Requirements</h4>

- Nginx must serve this page both locally and on its public IP on port 80.
- Nginx should proxy requests to the route */airbnb-dynamic/number_odd_or_even/(any integer)*
    the process listening on port 5001.
- Include your Nginx config file as *3-app_server-nginx_config.*

<h4>Tips</h4>

- Check out these articles/docs for clues on how to configure Nginx:
    [Understanding Nginx Server and Location Block Selection Algorithms](https://www.digitalocean.com/community/tutorials/understanding-nginx-server-and-location-block-selection-algorithms#matching-location-blocks), 
    [Understanding Nginx Location Blocks Rewrite Rules](http://blog.pixelastic.com/2013/09/27/understanding-nginx-location-blocks-rewrite-rules/),
    [Nginx Reverse Proxy.](https://docs.nginx.com/nginx/admin-guide/web-server/reverse-proxy/#)

- In order to spin up a Gunicorn instance as a detached process you can use the terminal multiplexer utility `tmux`.
Enter the command `tmux new-session -d 'gunicorn --bind 0.0.0.0:5001 web_flask.6-number_odd_or_even:app'`
and if successful you should see no output to the screen. You can verify that the process has been created
by running `pgrep gunicorn` to see its PID. Once you’re ready to end the process you can either run `tmux a`
to reattach to the processes, or you can run `kill <PID>` to terminate the background process by ID.

Example:

<h5>Terminal 1:</h5>

```
ubuntu@229-web-01:~/AirBnB_clone_v2$ tmux new-session -d 'gunicorn --bind 0.0.0.0:5000 web_flask.0-hello_route:app'
ubuntu@229-web-01:~/AirBnB_clone_v2$ pgrep gunicorn
1661
1665
ubuntu@229-web-01:~/AirBnB_clone_v2$ tmux new-session -d 'gunicorn --bind 0.0.0.0:5001 web_flask.6-number_odd_or_even:app'
ubuntu@229-web-01:~/AirBnB_clone_v2$ pgrep gunicorn
1661
1665
1684
1688

ubuntu@229-web-01:~/AirBnB_clone_v2$ curl 127.0.0.1:5000/airbnb-onepage/
Hello HBNB!ubuntu@229-web-01:~/AirBnB_clone_v2$

ubuntu@229-web-01:~/AirBnB_clone_v2$ curl 127.0.0.1:5001/number_odd_or_even/6
<!DOCTYPE html>
<HTML lang="en">
  <HEAD>
    <TITLE>HBNB</TITLE>
  </HEAD>
  <BODY><H1>Number: 6 is even</H1></BODY>
</HTML>ubuntu@229-web-01:~/AirBnB_clone_v2
ubuntu@229-web-01:~$ 
ubuntu@229-web-01:~/AirBnB_clone_v2$ curl 127.0.0.1/airbnb-dynamic/number_odd_or_even/5
<!DOCTYPE html>
<HTML lang="en">
  <HEAD>
    <TITLE>HBNB</TITLE>
  </HEAD>
  <BODY><H1>Number: 5 is odd</H1></BODY>
</HTML>ubuntu@229-web-01:~/AirBnB_clone_v2$
```

<h5>Local machine:</h5>

```
vagrant@ubuntu-xenial:~$ curl 35.231.193.217/airbnb-dynamic/number_odd_or_even/6
<!DOCTYPE html>
<HTML lang="en">
  <HEAD>
    <TITLE>HBNB</TITLE>
  </HEAD>
  <BODY><H1>Number: 6 is even</H1></BODY>
</HTML>vagrant@ubuntu-xenial:~$
```

<h3>4. Let's do this for your API</h3>

Let’s serve what you built for *AirBnB clone v3 - RESTful API* on **web-01**.

<h4>Requirements</h4>

- Git clone your AirBnB_clone_v3
- Setup Nginx so that the route */api/* points to a **Gunicorn** instance
    listening on port 5002
- **Nginx** must serve this page both locally and on its public IP on port **80**
- To test your setup you should bind **Gunicorn** to *api/v1/app.py*
- It may be helpful to import your data (and environment variables) from [this project](https://intranet.alxswe.com/projects/301)
- Upload your Nginx config file as /4-app_server-nginx_config/

Example: 

<h5>Terminal 1:</h5>

```
ubuntu@229-web-01:~/AirBnB_clone_v3$ tmux new-session -d 'gunicorn --bind 0.0.0.0:5002 api.v1.app:app'
ubuntu@229-web-01:~/AirBnB_clone_v3$ curl 127.0.0.1:5002/api/v1/states
[{"__class__":"State","created_at":"2019-05-10T00:39:27.032802","id":"7512f664-4951-4231-8de9-b18d940cc912",
"name":"California","updated_at":"2019-05-10T00:39:27.032965"},{"__class__":"State",
"created_at":"2019-05-10T00:39:36.021219","id":"b25625c8-8a7a-4c1f-8afc-257bf9f76bc8",
"name":"Arizona","updated_at":"2019-05-10T00:39:36.021281"}]
ubuntu@229-web-01:~/AirBnB_clone_v3$
ubuntu@229-web-01:~/AirBnB_clone_v3$ curl 127.0.0.1/api/v1/states
[{"__class__":"State","created_at":"2019-05-10T00:39:27.032802","id":"7512f664-4951-4231-8de9-b18d940cc912",
"name":"California","updated_at":"2019-05-10T00:39:27.032965"},{"__class__":"State",
"created_at":"2019-05-10T00:39:36.021219","id":"b25625c8-8a7a-4c1f-8afc-257bf9f76bc8",
"name":"Arizona","updated_at":"2019-05-10T00:39:36.021281"}]
ubuntu@229-web-01:~/AirBnB_clone_v3$
```

<h5>Local Terminal:</h5>

```
vagrant@ubuntu-xenial:~$ curl 35.231.193.217/api/v1/states
[{"__class__":"State","created_at":"2019-05-10T00:39:27.032802","id":"7512f664-4951-4231-8de9-b18d940cc912","name":"California","updated_at":"2019-05-10T00:39:27.032965"},{"__class__":"State","created_at":"2019-05-10T00:39:36.021219","id":"b25625c8-8a7a-4c1f-8afc-257bf9f76bc8","name":"Arizona","updated_at":"2019-05-10T00:39:36.021281"}]
vagrant@ubuntu-xenial:~$
```
