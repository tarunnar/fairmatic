import csv

orders_map = {}

with open("/home/manoj/Downloads/instacart/instacart_2017_05_01/orders.csv") as orders_fp:
    reader = csv.DictReader(orders_fp)
    for row in reader:
        order_id = row["order_id"]
        if order_id not in orders_map:
            orders_map[order_id] = row

departments_map = dict()

with open("/home/manoj/Downloads/instacart/instacart_2017_05_01/departments.csv") as dept_fp:
    reader = csv.DictReader(dept_fp)
    for row in reader:
        department_id = row["department_id"]
        if department_id not in departments_map:
            departments_map[department_id] = row["department"]

products_department_map = dict()
with open("/home/manoj/Downloads/instacart/instacart_2017_05_01/products.csv") as products_fp:
    reader = csv.DictReader(products_fp)
    for row in reader:
        product_id = row.get("product_id")
        department_id = row.get("department_id")
        if product_id and department_id:
            if product_id not in products_department_map:
                products_department_map[product_id] = {
                    "department_id": department_id,
                    "department_name": departments_map.get(department_id)
                }


with open("/home/manoj/Downloads/instacart/instacart_2017_05_01/order_products__train.csv") as orders_products_fp:
    reader = csv.DictReader(orders_products_fp)
    for row in reader:
        order_id = row["order_id"]
        product_id = row["product_id"]
        if order_id in orders_map:
            if "products" not in orders_map[order_id]:
                orders_map[order_id]["products"] = []
            if product_id in products_department_map:
                record = {
                    "product_id": product_id,
                    "department_id": products_department_map[product_id]["department_id"],
                    "department_name": products_department_map[product_id]["department_name"]
                }
                orders_map[order_id]["products"].append(record)

resultant_map = dict()
for order_id in orders_map:
    day = orders_map[order_id]["order_dow"]
    hour = orders_map[order_id]["order_hour_of_day"]
    user_id = orders_map[order_id]["user_id"]
    key = (day,hour)
    if "products" in orders_map[order_id]:
        for product in orders_map[order_id]["products"]:
            product_dept_name = product["department_name"]
            product_dept_id = product["department_id"]
            if key not in resultant_map:
                resultant_map[key] = {
                    "total_orders": {(order_id, product_dept_id)},
                    product_dept_name: {
                        "users": set(user_id),
                        "orders": {order_id}
                    }
                }
            else:
                if product_dept_name not in resultant_map[key]:
                    resultant_map[key][product_dept_name] = {
                        "users": set(),
                        "orders": set()
                    }
                if user_id not in resultant_map[key][product_dept_name]["users"]:
                    resultant_map[key][product_dept_name]["users"].add(user_id)
                    resultant_map[key][product_dept_name]["orders"].add(order_id)
                    resultant_map[key]["total_orders"].add((order_id, product_dept_id))


data_tuples = [
    {
        "key": key,
        "data": resultant_map[key]
    } for key in resultant_map
]

sum = 0
data_tuples = sorted(data_tuples, key=lambda x: x["key"])
for data in data_tuples:
    key = data["key"]
    dept_data = data["data"]
    total_orders = len(data["data"]["total_orders"])
    #print("total_orders", total_orders)
    sum = 0
    for dept in dept_data:
        if dept != "total_orders":
            dept_orders = len(dept_data[dept]["orders"])
            #print(dept, "dept_orders", dept_orders, dept_data[dept]["orders"])
            percentage = (dept_orders*100)/total_orders
            sum += percentage
            print({
                "day": key[0],
                "hour": key[1],
                "department": dept,
                "percentage": percentage
            })
    #print("sum", sum)

