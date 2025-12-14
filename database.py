import singlestoredb as s2


def get_connection():
  return s2.connect(
      host=
      "svc-3482219c-a389-4079-b18b-d50662524e8a-shared-dml.aws-virginia-6.svc.singlestore.com",
      port=3333,
      user="anirudh",
      password="u*xZ%1#ljdR$o1%-C-1X[UuAo",
      database="db_anirudh_f9191",
      results_type='dict')


def load_jobs_from_db():
  conn = get_connection()
  try:
    with conn.cursor() as cur:
      cur.execute("SELECT * FROM jobs")
      return cur.fetchall()
  finally:
    conn.close()


def load_job_from_db(id):
  conn = get_connection()
  try:
    with conn.cursor() as cur:
      cur.execute("SELECT * FROM jobs WHERE id = %s", (id, ))
      row = cur.fetchone()
      return row if row else None
  finally:
    conn.close()


def add_application_to_db(job_id, data):
  conn = get_connection()
  try:
    with conn.cursor() as cur:
      cur.execute(
          """
              INSERT INTO applications
              (job_id, full_name, email, linkedin_url, education, work_experience, resume_url)
              VALUES (%s, %s, %s, %s, %s, %s, %s)
          """,
          (job_id, data["full_name"], data["email"], data["linkedin_url"],
           data["education"], data["work_experience"], data["resume_url"]))
  finally:
    conn.close()
