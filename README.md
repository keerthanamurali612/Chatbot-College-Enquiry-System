# CHATBOT FOR COLLEGE ENQUIRY SYSTEM USING MACHINE LEARNING

 <p> The main objective of the "College Enquiry Chatbot" is to minimize the time required to solve the queries of a user, reduce the workload on the college’s office staff, save the time and strength of a user of visiting and contacting the administration office often, keep the user fully updated about the ongoing and upcoming events of college, etc.
 </p>

 <h3 align="left"> :hammer_and_wrench:Languages and Tools:</h3> <br>
 	:zap:  HTML, CSS, JAVASCRIPT, PYTHON, FLASK <br>
  :zap: IDE:	VScode

<h3>Flask Project Layout: </h3>
<p> A Flask application can be as simple as a single file.</p> 
<p>hello.py </p>

```
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'
```

<h3>Templates: </h3>
<p> Templates are files that contain static data as well as placeholders for dynamic data. A template is rendered with specific data to produce a final document. Flask uses the Jinja template library to render templates.</p> <br>

<p> You’ve written the authentication views for your application, but if you’re running the server and try to go to any of the URLs, you’ll see a TemplateNotFound error. That’s because the views are calling render_template(), but you haven’t written the templates yet. The template files will be stored in the templates directory inside the flaskr package.</p><br>

<p>📁In my project file is template/index.html </p>

<h3>Static Files: </h3>
<p> The authentication views and templates work, but they look very plain right now. Some CSS can be added to add style to the HTML layout you constructed. The style won’t change, so it’s a static file rather than a template.

</p> 
<p> 📁In my project static file is static/chat.css  </p>

```
{{ url_for('static', filename='style.css') }}
```
:writing_hand: Learn More: Flask Documentaion
