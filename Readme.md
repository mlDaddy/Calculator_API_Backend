# Environement Setup
- conda create -n django_tutorial python=3.7
- conda activate django_tutorial
- pip install Django djangorestframework
- or simply install requirements.txt file
    ```
    conda install --file requirements.txt
    ```

# Clone this Repo
```
git clone https://github.com/mlDaddy/Calculator_API_Backend.git
```

# Initialize Django App from Scratch (If not interested in cloning)
- mkdir Calculator_API_Backend
- cd Calculator_API_Backend
- django-admin startproject calculator_project
- copy fol code in calculator_app/views.py
    ```
    from rest_framework.views import APIView
    from rest_framework.response import Response
    from rest_framework import status

    class CalculatorView(APIView):
        def get(self, request, operation):
            instructions = f"Please send a PUT request with the 'a' and 'b' parameters to perform {operation} operation."
            return Response(instructions, status=status.HTTP_200_OK)

        def put(self, request, operation):
            if operation not in ['add', 'sub', 'mul', 'div']:
                return Response("Invalid operation.", status=status.HTTP_400_BAD_REQUEST)

            a = float(request.data.get('a'))
            b = float(request.data.get('b'))

            if operation == 'add':
                result = a + b
            elif operation == 'sub':
                result = a - b
            elif operation == 'mul':
                result = a * b
            elif operation == 'div':
                if b == 0:
                    return Response("Division by zero is not allowed.", status=status.HTTP_400_BAD_REQUEST)
                result = a / b

            return Response(f"Result of {operation}: {result}", status=status.HTTP_200_OK)

    ```
    - copy fol code in calculator_project/urls.py
    ```
    from django.urls import path
    from calculator_app.views import CalculatorView

    urlpatterns = [
        path('add/', CalculatorView.as_view(), {'operation': 'add'}),
        path('sub/', CalculatorView.as_view(), {'operation': 'sub'}),
        path('mul/', CalculatorView.as_view(), {'operation': 'mul'}),
        path('div/', CalculatorView.as_view(), {'operation': 'div'}),
    ]
    ```
    - calculator_project/settings.py, add your app to the INSTALLED_APPS list and configure the REST framework settings:
    ```
    INSTALLED_APPS = [
        # ...
        'rest_framework',
        'calculator_app',
    ]
    ```
    - Append fol code to calculator_project/settings.py file
    ```
    REST_FRAMEWORK = {
        'DEFAULT_PERMISSION_CLASSES': (
            'rest_framework.permissions.AllowAny',
        ),
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework.authentication.SessionAuthentication',
            'rest_framework.authentication.TokenAuthentication',
        ),
    }
    ```
    - Add allowed hosts in calculator_project/settings.py file
    ```
    ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
    ```

# Starting Django App
- python manage.py makemigrations
- python manage.py migrate
- python manage.py runserver

# Testing using Postman
- install postman on ubuntu
    ```
    sudo snap install postman
    ```
- Launch Postman on ubuntu
- Import tests/Calculator_API_Backend.postman_collection.json file in Postman
- Test each call one by one (total 8 calls)

# Deployment on AWS/EC2
- Launch your EC2 instance with following settings (leave everything else as default)
    - Amazon Machine Image (AMI): Ubuntu Server
    - Instance type: t2.micro
    - Allow SSH traffic from: Anywhere
    - Allow HTTPS traffic from the internet: Yes
    - Allow HTTP traffic from the internet: Yes
- Update the public IP of your EC2 instance in calculator_project/settings.py file
    ```
    ALLOWED_HOSTS = ['127.0.0.1:8000/', 'localhost:8000']
    ```
- Install conda and setup environment on EC2 using SSH
- Clone github repo
- Start Django app in a manner similar to the one used previously on local machine.
- Test using Postman (You may have to change the urls in previousely imported json file)

# Deployment using Docker
- Installing Docker on Ubuntu (Local or EC2 wherever you are trying to Deploy your api)
    - Update Package Lists by opening a terminal and ensuring your package lists are up-to-date:
    ```
    sudo apt update
    ```
    - Install the necessary packages to allow apt to use a repository over HTTPS:
    ```
    sudo apt install -y apt-transport-https ca-certificates curl software-properties-common
    ``` 
    - Add Docker's official GPG key:
    ``` 
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
    ``` 
    - Add the Docker repository to your system:
    ``` 
    echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    ``` 
    - Install Docker from the Docker repository:
    ``` 
    sudo apt update
    sudo apt install -y docker-ce docker-ce-cli containerd.io
    ```
    - Start the Docker service and enable it to start on boot:
    ``` 
    sudo systemctl start docker
    sudo systemctl enable docker
    ``` 
    - Verify that Docker is installed and running by running the following command. You should see the Docker version information.
    ``` 
    sudo docker --version
    ```
# Deploying Your Django API with Docker
- Create Dockerfile
- Build the Docker image using the docker build command.
    ```
    sudo docker build -t calculator_app .
- Run a Docker container based on the image you built. Map the host port to the container's port, and provide any environment variables as needed:
    ```
    sudo docker run -p 8000:8000 --name calculator_app_container calculator_app
    ```
    This command runs a container named calculator_app_container based on the calculator_app image, exposing the Django application on port 8000. You will see 'Watching for file changes with StatReloader' from django server on your terminal.
- Access Your API using the previousely defined urls and test them using Postman as done earlier.