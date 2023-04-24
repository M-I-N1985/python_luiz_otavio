# Documentação: https://www.sqlite.org/doclist.html
# Tutorial: https://www.techonthenet.com/sqlite/index.php
# download DBeaver: https://dbeaver.io/download/

import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# SQL

cursor.close()
connection.close()
