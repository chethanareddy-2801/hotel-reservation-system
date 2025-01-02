import tkinter as tk
from tkinter import messagebox
import mysql.connector

# MySQL connection
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',  # Replace with your MySQL password
    database=''  # Replace with your database name
)
cursor = conn.cursor()

# Function to get the next available room ID
def get_next_room_id():
    try:
        cursor.execute("SELECT MAX(id) FROM Room")
        result = cursor.fetchone()
        return result[0] + 1 if result[0] else 1
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error fetching next room ID: {err}")
        return None

# Function to add a room
def add_room():
    room_id = get_next_room_id()
    room_number = entry_room_number.get()
    room_type = entry_room_type.get()
    room_price = entry_price.get()
    room_status = entry_status.get()
    
    if room_id and room_number and room_type and room_price and room_status:
        try:
            cursor.execute("INSERT INTO Room (id, room_number, type, price, status) VALUES (%s, %s, %s, %s, %s)",
                           (room_id, room_number, room_type, room_price, room_status))
            conn.commit()
            messagebox.showinfo("Success", "Room added successfully!")
            entry_room_number.delete(0, tk.END)
            entry_room_type.delete(0, tk.END)
            entry_price.delete(0, tk.END)
            entry_status.delete(0, tk.END)
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error adding room: {err}")
    else:
        messagebox.showwarning("Input Error", "All fields are required")

# Function to view rooms
def view_rooms():
    try:
        cursor.execute("SELECT * FROM Room")
        rooms = cursor.fetchall()
        
        view_window = tk.Toplevel()
        view_window.title("View Rooms")
        
        for idx, room in enumerate(rooms):
            tk.Label(view_window, text=f"Room {idx+1}: {room}").pack()
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error fetching rooms: {err}")

# Function to delete a room
def delete_room():
    room_id = entry_room_id.get()
    if room_id:
        try:
            if messagebox.askyesno("Confirmation", "Are you sure you want to delete this room?"):
                cursor.execute("DELETE FROM Room WHERE id = %s", (room_id,))
                conn.commit()
                messagebox.showinfo("Success", "Room deleted successfully!")
                entry_room_id.delete(0, tk.END)
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error deleting room: {err}")
    else:
        messagebox.showwarning("Input Error", "Please enter Room ID to delete")

# Function to update a room
def update_room():
    room_id = entry_room_id.get()
    room_number = entry_room_number.get()
    room_type = entry_room_type.get()
    room_price = entry_price.get()
    room_status = entry_status.get()
    
    if room_id and room_number and room_type and room_price and room_status:
        try:
            cursor.execute("UPDATE Room SET room_number=%s, type=%s, price=%s, status=%s WHERE id=%s",
                           (room_number, room_type, room_price, room_status, room_id))
            conn.commit()
            messagebox.showinfo("Success", "Room updated successfully!")
            entry_room_id.delete(0, tk.END)
            entry_room_number.delete(0, tk.END)
            entry_room_type.delete(0, tk.END)
            entry_price.delete(0, tk.END)
            entry_status.delete(0, tk.END)
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error updating room: {err}")
    else:
        messagebox.showwarning("Input Error", "All fields and Room ID are required")

# Tkinter main window
root = tk.Tk()
root.title("Hotel Reservation System")

# Room ID
tk.Label(root, text="Room ID").grid(row=0, column=0)
entry_room_id = tk.Entry(root)
entry_room_id.grid(row=0, column=1)

# Room Number
tk.Label(root, text="Room Number").grid(row=1, column=0)
entry_room_number = tk.Entry(root)
entry_room_number.grid(row=1, column=1)

# Room Type
tk.Label(root, text="Room Type").grid(row=2, column=0)
entry_room_type = tk.Entry(root)
entry_room_type.grid(row=2, column=1)

# Price
tk.Label(root, text="Price").grid(row=3, column=0)
entry_price = tk.Entry(root)
entry_price.grid(row=3, column=1)

# Status
tk.Label(root, text="Status").grid(row=4, column=0)
entry_status = tk.Entry(root)
entry_status.grid(row=4, column=1)

# Buttons
tk.Button(root, text="Add Room", command=add_room).grid(row=5, column=0, columnspan=2)
tk.Button(root, text="View Rooms", command=view_rooms).grid(row=6, column=0, columnspan=2)
tk.Button(root, text="Update Room", command=update_room).grid(row=7, column=0, columnspan=2)
tk.Button(root, text="Delete Room", command=delete_room).grid(row=8, column=0, columnspan=2)

root.mainloop()

# Close the database connection when done
conn.close()
