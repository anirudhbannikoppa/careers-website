import singlestoredb as s2

conn = s2.connect(
    "anirudh:u*xZ%1#ljdR$o1%-C-1X[UuAo@svc-3482219c-a389-4079-b18b-d50662524e8a-shared-dml.aws-virginia-6.svc.singlestore.com:3333/db_anirudh_f9191"
)

with conn:
  with conn.cursor(dictionary=True) as cur:
    cur.execute("SELECT * FROM jobs")
    print(cur.fetchall())
