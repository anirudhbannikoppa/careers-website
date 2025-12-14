import singlestoredb as s2

conn = s2.connect(
    host="svc-3482219c-a389-4079-b18b-d50662524e8a-shared-dml.aws-virginia-6.svc.singlestore.com",
    port=3333,
    user="anirudh",
    password="u*xZ%1#ljdR$o1%-C-1X[UuAo",
    database="db_anirudh_f9191",
    results_type='dict'
)

with conn:
  with conn.cursor() as cur:
    cur.execute("SELECT * FROM jobs")
    print(cur.fetchall())
