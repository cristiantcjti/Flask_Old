<h1>GOOGLY EYE TOOL</h1>

<h2>Topics about the project :</h2>

<ul>
    <li>Project structure</li>
    <li>Set up</li>
    <li>Run</li>
    <li>Tests</li>
    <li>PS: Folder .pictures_to_upload</li>

</ul>

<h2>Project structure</h2>

The idea behind this structure is to bring scalability and make any adjustment or improvement<br>
as easy as possible.<br>
======================================<br>
|---.pictures_to_upload<br>
|-----|---<br>
|---client<br>
|-----|---index.html<br>
|-----|---style.css<br>
|---server<br>
|-----|---blueprints<br>
|-----|--------|---init.py<br>
|-----|--------|---googly_eyes.py<br>
|-----|---custom<br>
|-----|--------|---init.py<br>
|-----|--------|---client_exception.py<br>
|-----|--------|---custom_exceptions.py<br>
|-----|---process_image<br>
|-----|--------|---haarcascades<br>
|-----|--------|--------|---init.py<br>
|-----|--------|--------|---_'haarcascade_files.xml'_<br>
|-----|--------|---pictures<br>
|-----|--------|--------|---init.py<br>
|-----|--------|--------|---googly_eye_a.png<br>
|-----|--------|--------|---googly_eye_b.png<br>
|-----|--------|---tests<br>
|-----|--------|------|---init.py<br>
|-----|--------|------|---test_process_image.py<br>
|-----|--------|---init.py<br>
|-----|--------|---process_image.py<br>
|-----|---tests<br>
|-----|------|---init.py<br>
|-----|------|---test_app.py<br>
|-----|---util_tests<br>
|-----|------|---picture_test<br>
|-----|------|------|---init.py<br>
|-----|------|------|---image1.jpg<br>
|-----|------|------|---no_face.jpg<br>
|-----|------|---init.py<br>
|-----|------|---util_tests.py<br>
|-----|---init.py<br>
|-----|---app.py<br>
|-----|---run.py<br>
|-----|---settings.py<br>
|---venv<br>
|-----|---___venv_files___<br>
|---.gitignore<br>
|---README.md<br>
|---requirements.txt

<h2>Set up</h2>

Python's Version 3.8.10

Create a virtual environment:

> python -m venv venv

**Active** the <strong>virtual environment</strong>:

Observation: The '.' in the beginning of the command should be used only in **bash** terminals

#### Windows OS:
>. venv/Scripts/activate

#### Linux OS or MacOS OS:
>source venv/bin/activate 

You will notice the virtual environment activated on the beginning of the terminal path description:
**(venv)**

Install the requirements:
> pip install -r requirements.txt

<h2>Run</h2>

Configure an IDE like Pycharm or a text editor like VsCode. 

Here is an example on how the configurantion may be like:

>1º - Go to settings and add a new python interpreter pointing to:
    
    > googly_eyes > venv > bin > python   

>2º - Open the Run/Edit configuration

>3º - Add a new python configuration

    > Name the configuration with whatever name you want

>4º - In the configuration option:

    > Script path: insert the path to the run.py file

    > Python interpreter: Select the python interpreter you have added

    > working directory: Set the path to server folder of the project

>5º - Just click on apply and the configuration will be added

Now you should be able to run the project just clicking on the green 'Run' button on the right top bar.

Run the file **index.html**, upload an image and enjoy. 😉

<h2>Tests</h2>

The tests' configurantion is pretty much the same the previous one. 

>1º - Open the Run/Edit configuration

>2º - Add a new python **test** configuration

    > Name the configuration with whatever name you want

>3º - In the configuration option:

    > Python interpreter: Select the python interpreter you have added

    > working directory: Set the path to server folder of the project

>4º - Just click on apply and the configuration will be added

Now you should be able to test the project just clicking on the green 'Run' button on the right top bar.

<h2>PS: Folder .pictures_to_upload</h2>

This project was built based on the images inside this folder. Therefore, you can reproduce exactly the<br>
same behaviour that I had throughout my tests.



