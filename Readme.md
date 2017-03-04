# Django E-commerce


```bash
clone git@github.com:olivx/ecommerce.git project_name
cd project_name
python -m venv .project_name
source .project_name\bin\activate
pip install -r requirements.txt
python contrib/secret_gen.py
python manager.py migrate
python manager.py test
python manager.py runserver
```