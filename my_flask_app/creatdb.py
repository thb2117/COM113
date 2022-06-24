import psycopg2

#conn = psycopg2.connect(
#   database="postgres", user='dbuser', password='dbpass123', host='127.0.0.1', port= '5432'
#)
#conn.autocommit = True

#cursor = conn.cursor()

#cursor.execute("""DROP database IF EXISTS dbinventory;""")

#cursor.execute("""CREATE database dbinventory""")

#conn.close()

conn = psycopg2.connect(
   database="proj1part2", user='thb2117', password='5664', host='35.196.192.139', port= '5432'
)
conn.autocommit = True

cursor = conn.cursor()

cursor.execute("""DROP table IF EXISTS sales_invoces_details;""")

cursor.execute("""DROP table IF EXISTS sales_invoces;""")

cursor.execute("""DROP table IF EXISTS purchase_invoces_details;""")

cursor.execute("""DROP table IF EXISTS purchase_invoces;""")

cursor.execute("""DROP table IF EXISTS sales_invoices_details;""")

cursor.execute("""DROP table IF EXISTS sales_invoices;""")

cursor.execute("""DROP table IF EXISTS purchase_invoices_details;""")

cursor.execute("""DROP table IF EXISTS purchase_invoices;""")

cursor.execute("""DROP table IF EXISTS Inventory;""")

cursor.execute("""DROP table IF EXISTS vendor;""")

cursor.execute("""DROP table IF EXISTS customer;""")

cursor.execute("""CREATE TABLE customer ( customer_id SERIAL PRIMARY KEY,customer_name varchar (50) NOT NULL, customer_phone varchar (50) NOT NULL);""")

cursor.execute("""CREATE TABLE vendor ( vendor_id SERIAL PRIMARY KEY, vendor_name varchar (50) NOT NULL, vendor_phone varchar (50) NOT NULL);""")

cursor.execute("""CREATE TABLE Inventory ( item_id SERIAL PRIMARY KEY, item_name varchar (50) NOT NULL, item_type varchar (50) NOT NULL, item_qty int NOT NULL, item_purchasePrice int NOT NULL, item_salePrice int NOT NULL, item_CreatedOn Date NULL);""")

cursor.execute("""CREATE TABLE purchase_invoices ( invoice_id SERIAL PRIMARY KEY, invoice_date Date NOT NULL, invoice_total_amount int NOT NULL, vendor_id int, CONSTRAINT fk_vendor FOREIGN KEY(vendor_id) REFERENCES vendor(vendor_id));""")

cursor.execute("""CREATE TABLE sales_invoices ( invoice_id SERIAL PRIMARY KEY, invoice_date Date NOT NULL, invoice_total_amount int NOT NULL, customer_id int, FOREIGN KEY (customer_id) references customer(customer_id));""")

cursor.execute("""CREATE TABLE purchase_invoices_details ( PND_id SERIAL PRIMARY KEY, purchase_qty int NOT NULL, purchase_price int NOT NULL, purchase_discount int NOT NULL, invoice_total int NOT NULL, invoice_id int, FOREIGN KEY(invoice_id) references purchase_invoices(invoice_id), item_id int, FOREIGN KEY (item_id) references inventory(item_id));""")

cursor.execute("""CREATE TABLE sales_invoices_details ( SND_id SERIAL PRIMARY KEY, sale_qty int NOT NULL, sale_price int NOT NULL, sale_discount int NOT NULL, sale_total int NOT NULL, invoice_id int, FOREIGN KEY(invoice_id) references sales_invoices(invoice_id), item_id int, FOREIGN KEY (item_id) references Inventory(item_id));""")

#cursor.execute("""Insert Into CUSTOMER(customer_id,customer_name,customer_phone)Values(123,'Amit','9877562389');""")

#cursor.execute("""Insert Into CUSTOMER(customer_id, customer_name, customer_phone)Values(124,'Rohit','8877562389');""")

#cursor.execute("""Insert Into CUSTOMER(customer_id, customer_name, customer_phone)Values(125,'Mohit','9877662389');""")

#cursor.execute("""Insert Into CUSTOMER(customer_id, customer_name, customer_phone)Values(126,'Rahul','9877562559');""")

#cursor.execute("""Insert Into CUSTOMER(customer_id, customer_name, customer_phone)Values(127,'Karan','8177562389');""")

#cursor.execute("""Insert Into CUSTOMER(customer_id, customer_name, customer_phone)Values(128,'Chirag','9877562300');""")

#cursor.execute("""Insert Into CUSTOMER(customer_id, customer_name, customer_phone)Values(129,'Kapil','9777562389');""")

#cursor.execute("""Insert Into CUSTOMER(customer_id, customer_name, customer_phone)Values(120,'Ajay','9677562380');""")

#cursor.execute("""Insert Into CUSTOMER(customer_id, customer_name, customer_phone)Values(121,'Abhi','9477562380');""")

#cursor.execute("""Insert Into CUSTOMER(customer_id, customer_name, customer_phone)Values(122,'Kartik','8977560089');""")

#cursor.execute("""Insert Into VENDOR (vendor_id, vendor_name, vendor_phone)Values(121,'Metro Electricals','9678435760');""")

#cursor.execute("""Insert Into VENDOR (vendor_id, vendor_name, vendor_phone)Values(122,'Oneplus Electricals','9878435760');""")

#cursor.execute("""Insert Into VENDOR (vendor_id, vendor_name, vendor_phone)Values(123,'Havells','9678435000');""")

#cursor.execute("""Insert Into VENDOR (vendor_id, vendor_name, vendor_phone)Values(124,'ABB','9670005760');""")

#cursor.execute("""Insert Into VENDOR (vendor_id, vendor_name, vendor_phone)Values(125,'Tesla','8978435760');""")

#cursor.execute("""Insert Into VENDOR (vendor_id, vendor_name, vendor_phone)Values(126,'Amazon','9678435760');""")

#cursor.execute("""Insert Into VENDOR (vendor_id, vendor_name, vendor_phone)Values(127,'Flipkart','9000435760');""")

#cursor.execute("""Insert Into VENDOR (vendor_id, vendor_name, vendor_phone)Values(128,'Wallmart','9677735760');""")

#cursor.execute("""Insert Into VENDOR (vendor_id, vendor_name, vendor_phone)Values(129,'Borosil','9678666760');""")

#cursor.execute("""Insert Into VENDOR (vendor_id, vendor_name, vendor_phone)Values(130,'LG','9678454546');""")

cursor.execute("""Insert Into INVENTORY (item_id, item_name, item_type, item_qty, item_purchasePrice, item_salePrice,item_CreatedOn)Values(01,'Laptop Fan','Computer',200,100,120,'2022-05-22');""")

cursor.execute("""Insert Into INVENTORY (item_id, item_name, item_type, item_qty, item_purchasePrice, item_salePrice,item_CreatedOn)Values(02,'Laptop Screen','Computer',100,900,990,'2022-06-01');""")

cursor.execute("""Insert Into INVENTORY (item_id, item_name, item_type, item_qty, item_purchasePrice, item_salePrice,item_CreatedOn)Values(03,'Mouse','Computer',500,50,90,'2022-06-02');""")

cursor.execute("""Insert Into INVENTORY (item_id, item_name, item_type, item_qty, item_purchasePrice, item_salePrice,item_CreatedOn)Values(04,'Celling Fan','Electical',50,500,590,'2022-06-10');""")

cursor.execute("""Insert Into INVENTORY (item_id, item_name, item_type, item_qty, item_purchasePrice, item_salePrice,item_CreatedOn)Values(05,'Bell Door','Electical',60,300,390,'2022-06-08');""")

cursor.execute("""Insert Into INVENTORY (item_id, item_name, item_type, item_qty, item_purchasePrice, item_salePrice,item_CreatedOn)Values(06,'Printer','Computer',10,3000,3200,'2022-06-07');""")

cursor.execute("""Insert Into INVENTORY (item_id, item_name, item_type, item_qty, item_purchasePrice, item_salePrice,item_CreatedOn)Values(07,'Hard Drive','Computer',20,3500,3900,'2022-06-06');""")

cursor.execute("""Insert Into INVENTORY (item_id, item_name, item_type, item_qty, item_purchasePrice, item_salePrice,item_CreatedOn)Values(08,'Hard Drive','Computer',20,3500,3900,'2022-06-06');""")

cursor.execute("""Insert Into INVENTORY (item_id, item_name, item_type, item_qty, item_purchasePrice, item_salePrice,item_CreatedOn)Values(09,'Key Board','Computer',20,200,2200,'2022-06-05');""")

cursor.execute("""Insert Into INVENTORY (item_id, item_name, item_type, item_qty, item_purchasePrice, item_salePrice,item_CreatedOn)Values(10,'Head Phones','Computer',10,80,95,'2022-06-04');""")

#cursor.execute("""Insert Into PURCHASE_INVOICES (invoice_id, invoice_date, invoice_total_amount, vendor_id) Values(01,'2022-05-22',700,121);""")

#cursor.execute("""Insert Into PURCHASE_INVOICES (invoice_id, invoice_date, invoice_total_amount, vendor_id) Values(02,'2022-05-12',5000,122);""")

#cursor.execute("""Insert Into PURCHASE_INVOICES (invoice_id, invoice_date, invoice_total_amount, vendor_id) Values(03,'2022-05-10',500,122);""")

#cursor.execute("""Insert Into PURCHASE_INVOICES (invoice_id, invoice_date, invoice_total_amount, vendor_id) Values(04,'2022-06-10',990,123);""")

#cursor.execute("""Insert Into PURCHASE_INVOICES (invoice_id, invoice_date, invoice_total_amount, vendor_id) Values(05,'2022-06-12',590,124);""")

#cursor.execute("""Insert Into PURCHASE_INVOICES (invoice_id, invoice_date, invoice_total_amount, vendor_id) Values(06,'2022-06-11',5990,121);""")

#cursor.execute("""Insert Into PURCHASE_INVOICES (invoice_id, invoice_date, invoice_total_amount, vendor_id) Values(07,'2022-06-08',790,129);""")

#cursor.execute("""Insert Into PURCHASE_INVOICES (invoice_id, invoice_date, invoice_total_amount, vendor_id) Values(08,'2022-06-07',7790,128);""")

#cursor.execute("""Insert Into PURCHASE_INVOICES (invoice_id, invoice_date, invoice_total_amount, vendor_id) Values(09,'2022-06-04',90,127);""")

#cursor.execute("""Insert Into PURCHASE_INVOICES (invoice_id, invoice_date, invoice_total_amount, vendor_id) Values(10,'2022-06-02',4980,126);""")

#cursor.execute("""Insert Into SALES_INVOICES (invoice_id, invoice_date, invoice_total_amount, customer_id) Values(01,'2022-05-22',2500,123);""")

#cursor.execute("""Insert Into SALES_INVOICES (invoice_id, invoice_date, invoice_total_amount, customer_id) Values(02,'2022-06-02',500,124);""")

#cursor.execute("""Insert Into SALES_INVOICES (invoice_id, invoice_date, invoice_total_amount, customer_id) Values(03,'2022-06-03',9000,125);""")

#cursor.execute("""Insert Into SALES_INVOICES (invoice_id, invoice_date, invoice_total_amount, customer_id) Values(04,'2022-06-13',7600,123);""")

#cursor.execute("""Insert Into SALES_INVOICES (invoice_id, invoice_date, invoice_total_amount, customer_id) Values(05,'2022-06-04',6900,126);""")

#cursor.execute("""Insert Into SALES_INVOICES (invoice_id, invoice_date, invoice_total_amount, customer_id) Values(06,'2022-06-05',70,127);""")

#cursor.execute("""Insert Into SALES_INVOICES (invoice_id, invoice_date, invoice_total_amount, customer_id) Values(07,'2022-06-07',90,123);""")

#cursor.execute("""Insert Into SALES_INVOICES (invoice_id, invoice_date, invoice_total_amount, customer_id) Values(08,'2022-06-08',3876,124);""")

#cursor.execute("""Insert Into SALES_INVOICES (invoice_id, invoice_date, invoice_total_amount, customer_id) Values(09,'2022-06-09',876,125);""")

#cursor.execute("""Insert Into SALES_INVOICES (invoice_id, invoice_date, invoice_total_amount, customer_id) Values(10,'2022-06-09',595,127);""")

#cursor.execute("""Insert Into PURCHASE_INVOICES_DETAILS (PND_id, purchase_qty, purchase_price ,purchase_discount, invoice_total, invoice_id,item_id) Values(01,8,120,0,960,01,01);""")

#cursor.execute("""Insert Into PURCHASE_INVOICES_DETAILS (PND_id, purchase_qty, purchase_price ,purchase_discount, invoice_total, invoice_id,item_id) Values(02,10,120,0,1200,02,02);""")

#cursor.execute("""Insert Into PURCHASE_INVOICES_DETAILS (PND_id, purchase_qty, purchase_price ,purchase_discount, invoice_total, invoice_id,item_id) Values(03,20,220,0,4400,03,03);""")

#cursor.execute("""Insert Into PURCHASE_INVOICES_DETAILS (PND_id, purchase_qty, purchase_price ,purchase_discount, invoice_total, invoice_id,item_id) Values(04,30,320,0,9600,04,04);""")

#cursor.execute("""Insert Into PURCHASE_INVOICES_DETAILS (PND_id, purchase_qty, purchase_price ,purchase_discount, invoice_total, invoice_id,item_id) Values(05,40,120,0,4800,05,05);""")

#cursor.execute("""Insert Into PURCHASE_INVOICES_DETAILS (PND_id, purchase_qty, purchase_price ,purchase_discount, invoice_total, invoice_id,item_id) Values(06,20,120,0,2400,06,06);""")

#cursor.execute("""Insert Into PURCHASE_INVOICES_DETAILS (PND_id, purchase_qty, purchase_price ,purchase_discount, invoice_total, invoice_id,item_id) Values(07,10,120,0,1200,07,07);""")

#cursor.execute("""Insert Into PURCHASE_INVOICES_DETAILS (PND_id, purchase_qty, purchase_price ,purchase_discount, invoice_total, invoice_id,item_id) Values(08,10,180,0,1800,08,08);""")

#cursor.execute("""Insert Into PURCHASE_INVOICES_DETAILS (PND_id, purchase_qty, purchase_price ,purchase_discount, invoice_total, invoice_id,item_id) Values(09,10,32,0,320,09,09);""")

#cursor.execute("""Insert Into PURCHASE_INVOICES_DETAILS (PND_id, purchase_qty, purchase_price ,purchase_discount, invoice_total, invoice_id,item_id) Values(10,10,880,0,8800,10,10);""")

#cursor.execute("""Insert Into SALES_INVOICES_DETAILS (SND_id, sale_qty, sale_price , sale_discount, sale_total, invoice_id,item_id) Values(01,10,100,0,1000,01,01);""")

#cursor.execute("""Insert Into SALES_INVOICES_DETAILS (SND_id, sale_qty, sale_price , sale_discount, sale_total, invoice_id,item_id) Values(02,20,100,0,2000,02,02);""")

#cursor.execute("""Insert Into SALES_INVOICES_DETAILS (SND_id, sale_qty, sale_price , sale_discount, sale_total, invoice_id,item_id) Values(03,30,100,0,3000,03,03);""")

#cursor.execute("""Insert Into SALES_INVOICES_DETAILS (SND_id, sale_qty, sale_price , sale_discount, sale_total, invoice_id,item_id) Values(04,40,100,0,4000,04,04);""")

#cursor.execute("""Insert Into SALES_INVOICES_DETAILS (SND_id, sale_qty, sale_price , sale_discount, sale_total, invoice_id,item_id) Values(05,50,100,0,5000,05,05);""")

#cursor.execute("""Insert Into SALES_INVOICES_DETAILS (SND_id, sale_qty, sale_price , sale_discount, sale_total, invoice_id,item_id) Values(06,60,100,0,6000,06,06);""")

#cursor.execute("""Insert Into SALES_INVOICES_DETAILS (SND_id, sale_qty, sale_price , sale_discount, sale_total, invoice_id,item_id) Values(07,70,100,0,7000,07,07);""")

#cursor.execute("""Insert Into SALES_INVOICES_DETAILS (SND_id, sale_qty, sale_price , sale_discount, sale_total, invoice_id,item_id) Values(08,80,100,0,8000,08,08);""")

#cursor.execute("""Insert Into SALES_INVOICES_DETAILS (SND_id, sale_qty, sale_price , sale_discount, sale_total, invoice_id,item_id) Values(09,3,100,0,300,09,09);""")

#cursor.execute("""Insert Into SALES_INVOICES_DETAILS (SND_id, sale_qty, sale_price , sale_discount, sale_total, invoice_id,item_id) Values(10,4,100,0,400,10,10);""")

conn.close()

