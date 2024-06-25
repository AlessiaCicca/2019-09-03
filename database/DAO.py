from database.DB_connect import DBConnect
from model.connessione import Connessione



class DAO():
    def __init__(self):
        pass



    @staticmethod
    def getNodi(calorie):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct p.portion_display_name as tipo
from food_pyramid_mod.portion p 
where p.calories <%s """

        cursor.execute(query,(calorie,))

        for row in cursor:
            result.append(row["tipo"])

        cursor.close()
        conn.close()
        return result
    @staticmethod
    def getConnessioni(calorie):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select t1.p1 as v1,t2.p2 as v2, count(distinct t1.c1) as peso
from(select p.food_code as c1, p.portion_display_name as p1
from food_pyramid_mod.portion p 
where p.calories <%s) as t1,
(select p.food_code as c2,p.portion_display_name as p2
from food_pyramid_mod.portion p 
where p.calories <%s) as t2
where t1.c1=t2.c2 and t1.p1<t2.p2
group by t1.p1,t2.p2"""

        cursor.execute(query,(calorie,calorie,))

        for row in cursor:
            result.append(Connessione(**row))

        cursor.close()
        conn.close()
        return result
