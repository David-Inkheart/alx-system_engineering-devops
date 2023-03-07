<h1>Tasks on Application server</h1>

[architecture image](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/9/c7d1ed0a2e10d1b4e9b3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230307%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230307T105725Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=a53e34eac2a8ce77e4d17563538b481f2b11f01287d0af83a9c89f82499f26f4) ---

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
