import mysql.connector as sql
from mysql.connector import Error
from modules.creds import user_pwd
from cv_schema_init import *

try:
    # Connect to MySQL
    mycon = sql.connect(
        host='localhost',
        user='root',
        passwd=user_pwd
    )

    if mycon.is_connected():
        cur = mycon.cursor()

        # Create schema
        cur.execute(CREATE_SCHEMA)
        cur.execute("USE mydb")  # Use your DB after creation

        # Create tables
        cur.execute(Create_users_Table)
        cur.execute(Create_recruiter_Table)
        cur.execute(Create_client_Table)
        cur.execute(Create_Job_Table)
        cur.execute(Create_Application_Table)
        cur.execute(Create_DELJOB_Table)
        cur.execute(Create_DELAPP_Table)
        cur.execute(Create_NEWJOB_Table)
        cur.execute(Create_NEWAPP_Table)
        cur.execute(CREATE_Admin)

        # Triggers
        cur.execute(JobTrig1)
        cur.execute(JobTrig2)
        cur.execute(AppTrig)

        # Views or stored procedures
        cur.execute(totalAPP)
        cur.execute(totalJOB)
        cur.execute(totalUSERS)
        cur.execute(Log_View)

        mycon.commit()
        print("✅ Database initialized successfully.")

except Error as e:
    print("❌ Error while connecting to MySQL:", e)

finally:
    if mycon.is_connected():
        cur.close()
        mycon.close()
        print("🔒 MySQL connection closed.")
