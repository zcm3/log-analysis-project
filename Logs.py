import psycopg2

def main():
    conn = psycopg2.connect("dbname=news")
    cur = conn.cursor()
    # Question 1
    query_1 = """
    select title, count(*) as views_num from articles, 
    log where log.path = '/article/' || articles.slug 
    group by title 
    order by views_num desc limit 3;
    """
    cur.execute(query_1)
    print("The popular articles:")
    for (title, view) in cur.fetchall():
        print("    {} - {} views".format(title, view))
    print("-" * 20)

    # Question 2
    query_2 = """
    select name, count(*) as views_num 
    from authors join articles 
    on articles.author = authors.id join log on log.path = '/article/' || articles.slug 
    group by name order by views_num desc;
    """
    cur.execute(query_2)
    print("The popular authors:")
    for (name, view) in cur.fetchall():
        print("    {} - {} views".format(name, view))
    print("-" * 20)

    # Question 3
    query_3 = """
    Select date, not_found*100.0/ web_req as error_req_rate 
    from (select  time::date  as daydate , count(*) as web_req 
    from log group by time::date) as traffic , (select  time::date  date, count(*) 
    as not_found from log where status != '200 OK' group by date) 
    as num_errors where daydate = date and num_errors.not_found >  traffic.web_req*0.01 order by date desc;
    """
    cur.execute(query_3)
    print("Errors rate above 1%:")
    for (date, percentage) in cur.fetchall():
        print("    {} - {}% errors ".format(date, percentage))
    print("-" * 20)

    cur.close()
    conn.close()

if __name__ == "__main__":
    main()