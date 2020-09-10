# StockAnalysis
**Use Django framework to build the web.**
[URL](https://meow-stock.herokuapp.com/)

### Some Notes
- requirements.txt
	- Remember to add psycopg2==2.8.6 although we don't need it in local.

- Procfile
	- Check the wsgi correlating with the correct app name.

- setting.py
	- Modigy DEBUG = False and add the Heroku ip to ALLOWED_HOSTS.
	- Add 'whitenoise.middleware.WhiteNoiseMiddleware' to MIDDLEWARE.
