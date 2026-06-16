import sqlite3
from datetime import datetime
from pathlib import Path
from database import create_tasks_table
from database import add_task

create_tasks_table()

while True:
    choice = input("Izvēlies vienu:\n1 - Pievienot uzdevumu\n2 - Parādīt visus uzdevumus\n3 - Atzīmēt uzdevumu kā pabeigtu\n4 - Izdzēst uzdevumu\n5 - Iziet no programmas \n")

    if choice == "1":
        title = input("Nosaukums: ")
        deadline = input("termiņš: ")
        add_task(title, deadline)
    