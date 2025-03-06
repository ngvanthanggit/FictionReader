<a id="readme-top"></a>
# Fiction Reader
I used to read fiction online. I made this project as a hobby!

## Built With
* [![Django][Django.com]][Django-url]
* [![DjangoRestframework][DjangoRestframework]][DjangoRestframework-url]

## Getting Started
This is how you create a local version of this platform.

1. Clone this repository
   ```sh
   git clone https://github.com/ngvanthanggit/FictionReader.git
   ```
2. Create Virtual Environment
   ```sh
   python -m venv myenv
   ```
   Activate the virtual environment
   ```sh
   source myenv/bin/activate
   ```
3. Install all required packages
   ```sh
   pip install -r requirements.txt
   ```
   or
   ```sh
   python -m pip install -r requirements.txt
   ```
4. Run migration(s) (if needed)
   ```sh
   python manage.py makemigrations
   ```
   then migrate/apply the changes
   ```sh
   python manage.py migrate
   ```
6. Run server locally
   ```sh
   python manage.py runserver
   ```
   or (with custom port number)
   ```sh
   python manage.py runserver <port number>
   ```
## Contact

Thang Nguyen Van - [@ngvanthangig](https://www.instagram.com/ngvanthangig/) - thangitcbg@gmail.com

Project Link: [https://github.com/ngvanthanggit/FriendStardi](https://github.com/ngvanthanggit/FriendStardi)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

[Django.com]: https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green
[Django-url]: https://www.djangoproject.com/
[DjangoRestframework]: https://img.shields.io/badge/django--rest--framework-3.12.4-blue?style=for-the-badge&labelColor=333333&logo=django&logoColor=white&color=blue
[DjangoRestframework-url]: https://www.django-rest-framework.org/
