from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

@app.route('/addcustomer',methods=["GET"])
def addcustomer():
    return render_template('addcustomer.html')

@app.route('/addcustomer',methods=["POST"])
def customeraddpost():
    name = request.form["name"]
    phone = request.form["phone"]
    conn = psycopg2.connect(database="proj1part2", user='thb2117', password='5664', host='35.196.192.139', port= '5432')
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute("""Insert Into Customer(customer_name, customer_phone) values('"""+name+"""','"""+phone+"""')""")
    conn.close()
    return render_template('addcustomer.html')

@app.route('/listcustomer',methods=["GET"])
def listcustomer():
    conn = psycopg2.connect(database="proj1part2", user='thb2117', password='5664', host='35.196.192.139', port= '5432')
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute("""Select customer_id, customer_name, customer_phone From Customer""");
    customers = cursor.fetchall()
    conn.close()
    return render_template("listcustomer.html", customers=customers)

@app.route('/addvendor',methods=["GET"])
def addvendor():
    return render_template('addvendor.html')

@app.route('/addvendor',methods=["POST"])
def vendoraddpost():
    name = request.form["name"]
    phone = request.form["phone"]
    conn = psycopg2.connect(database="proj1part2", user='thb2117', password='5664', host='35.196.192.139', port= '5432')
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute("""Insert Into vendor(vendor_name, vendor_phone) values('"""+name+"""','"""+phone+"""')""")
    conn.close()
    return render_template('addvendor.html')

@app.route('/listvendor',methods=["GET"])
def listvendor():
    conn = psycopg2.connect(database="proj1part2", user='thb2117', password='5664', host='35.196.192.139', port= '5432')
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute("""Select vendor_id, vendor_name, vendor_phone From Vendor""");
    vendors = cursor.fetchall()
    conn.close()
    return render_template("listvendor.html", vendors=vendors)

@app.route('/',methods=["GET"])
def listinventory():
    conn = psycopg2.connect(database="proj1part2", user='thb2117', password='5664', host='35.196.192.139', port= '5432')
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute("""Select item_id, item_name, item_type, item_qty, item_purchasePrice, item_salePrice,item_CreatedOn From Inventory""");
    inventory = cursor.fetchall()
    conn.close()
    return render_template("home.html", inventory=inventory)

@app.route('/createpinvoice',methods=["GET"])
def createpinvoice():
    conn = psycopg2.connect(database="proj1part2", user='thb2117', password='5664', host='35.196.192.139', port= '5432')
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute("""Select vendor_id, vendor_name From Vendor""");
    vendors = cursor.fetchall()
    cursor.execute("""Select item_id, item_name, item_purchasePrice From Inventory""")
    inventory = cursor.fetchall()
    conn.close()
    return render_template("createpinvoice.html", vendors=vendors, inventory=inventory)

@app.route('/createpinvoice',methods=["POST"])
def createpinvoicepost():
    vendor = request.form["vendor"]
    #print(str(vendor))
    item = request.form["item"]
    #print(str(item))
    pprice = request.form["pprice"]
    quantity = request.form["quantity"]
    discount = request.form["discount"]
    total = request.form["total"]
    conn = psycopg2.connect(database="proj1part2", user='thb2117', password='5664', host='35.196.192.139', port= '5432')
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute("""Insert Into purchase_invoices(invoice_date,invoice_total_amount,vendor_id) values(now(),'"""+total+"""','"""+vendor+"""') returning invoice_id;""")
    invoice_id = cursor.fetchone()[0]
    #print(str(invoice_id))
    cursor.execute("Insert Into purchase_invoices_details(purchase_qty, purchase_price,purchase_discount, invoice_total, invoice_id, item_id) values(%s,%s,%s,%s,%s,%s)",(quantity,pprice,discount,total,invoice_id,item))
    cursor.execute("""Select vendor_id, vendor_name From Vendor;""");
    vendors = cursor.fetchall()
    cursor.execute("""Select item_id, item_name, item_purchasePrice From Inventory;""")
    inventory = cursor.fetchall()
    conn.close()
    return render_template("createpinvoice.html", vendors=vendors, inventory=inventory)
    #return render_template("createpinvoice.html")

@app.route('/listpinvoice',methods=["GET"])
def listpinvoice():
    conn = psycopg2.connect(database="proj1part2", user='thb2117', password='5664', host='35.196.192.139', port= '5432')
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute("Select a.invoice_id, invoice_date, (Select vendor_name from vendor where vendor_id=a.vendor_id),(Select item_name from inventory where item_id=b.item_id), b.purchase_qty, b.purchase_price, b.purchase_discount, b.invoice_total From purchase_invoices as a join purchase_invoices_details b on a.invoice_id=b.invoice_id;");
    pinvoices = cursor.fetchall()
    conn.close()
    return render_template("listpinvoice.html", pinvoices=pinvoices)

@app.route('/createsinvoice',methods=["GET"])
def createsinvoice():
    conn = psycopg2.connect(database="proj1part2", user='thb2117', password='5664', host='35.196.192.139', port= '5432')
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute("""Select customer_id, customer_name From Customer""");
    customers = cursor.fetchall()
    cursor.execute("""Select item_id, item_name, item_salePrice From Inventory""")
    inventory = cursor.fetchall()
    conn.close()
    return render_template("createsinvoice.html", customers=customers, inventory=inventory)

@app.route('/createsinvoice',methods=["POST"])
def createsinvoicepost():
    customer = request.form["customer"]
    #print(str(vendor))
    item = request.form["item"]
    #print(str(item))
    sprice = request.form["sprice"]
    quantity = request.form["quantity"]
    discount = request.form["discount"]
    total = request.form["total"]
    conn = psycopg2.connect(database="proj1part2", user='thb2117', password='5664', host='35.196.192.139', port= '5432')
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute("""Insert Into sales_invoices(invoice_date,invoice_total_amount,customer_id) values(now(),'"""+total+"""','"""+customer+"""') returning invoice_id;""")
    invoice_id = cursor.fetchone()[0]
    #print(str(invoice_id))
    cursor.execute("Insert Into sales_invoices_details(sale_qty, sale_price, sale_discount, sale_total, invoice_id, item_id) values(%s,%s,%s,%s,%s,%s)",(quantity, sprice, discount, total, invoice_id, item ))
    cursor.execute("""Select customer_id, customer_name From Customer;""");
    customers = cursor.fetchall()
    cursor.execute("""Select item_id, item_name, item_salePrice From Inventory;""")
    inventory = cursor.fetchall()
    conn.close()
    return render_template("createsinvoice.html", customers=customers, inventory=inventory)
    #return render_template("createpinvoice.html")

@app.route('/listsinvoice',methods=["GET"])
def listsinvoice():
    conn = psycopg2.connect(database="proj1part2", user='thb2117', password='5664', host='35.196.192.139', port= '5432')
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute("Select a.invoice_id, invoice_date, (Select customer_name from customer where customer_id=a.customer_id),(Select item_name from inventory where item_id=b.item_id), b.sale_qty, b.sale_price, b.sale_discount, b.sale_total From sales_invoices as a join sales_invoices_details b on a.invoice_id=b.invoice_id;")
    sinvoices = cursor.fetchall()
    conn.close()
    return render_template("listsinvoice.html", sinvoices=sinvoices)

