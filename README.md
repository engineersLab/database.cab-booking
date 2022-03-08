## Migration file - `cab-booking` database

## QUICK START INSTRUCTIONS
### Db setup
1. Setup a local mysql db with docker or mysql
2. Create database named `cab-booking`
3. Clone this repo
4. Reinitialize your virtual environment:  `rm -rf venv/ && python3 -m venv venv`
5. Activate your virtual environment:  `source venv/bin/activate`
6. Install pip requirements: `pip install -r requirements.txt`
7. `flask db upgrade` to connect to database and run the migrations
