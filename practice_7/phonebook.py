import csv
from connect import conn, cur

# #2 - Import contacts 
def import_csv():
    try:
        with open("contacts.csv", "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                name, phone = row
                cur.execute(
                    "INSERT INTO contacts(name, phone) VALUES(%s, %s)",
                    (name, phone)
                )
        conn.commit()
        print("CSV data imported successfully!")
    except Exception as e:
        print("Error importing CSV:", e)

# #3 - Console input
def add_contact():
    try:
        name = input("Name: ")
        phone = input("Phone: ")
        cur.execute(
            "INSERT INTO contacts(name, phone) VALUES(%s, %s)",
            (name, phone)
        )
        conn.commit()
        print("Contact added successfully!")
    except Exception as e:
        print("Error adding contact:", e)

# #4 - Show all contacts
def show_contacts():
    try:
        cur.execute("SELECT * FROM contacts")
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except Exception as e:
        print("Error showing contacts:", e)

# #4 - Update 
def update_contact():
    try:
        name = input("Enter the name to update: ")
        new_phone = input("Enter new phone: ")
        cur.execute(
            "UPDATE contacts SET phone=%s WHERE name=%s",
            (new_phone, name)
        )
        conn.commit()
        print("Contact updated successfully!")
    except Exception as e:
        print("Error updating contact:", e)

# #4 - Delete
def delete_contact():
    try:
        name = input("Enter the name to delete: ")
        cur.execute(
            "DELETE FROM contacts WHERE name=%s",
            (name,)
        )
        conn.commit()
        print("Contact deleted successfully!")
    except Exception as e:
        print("Error deleting contact:", e)

# Main
if __name__ == "__main__":
    import_csv()      
    add_contact()     
    show_contacts()   
    update_contact()  
    delete_contact()  


cur.close()
conn.close()