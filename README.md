# Hotel Reservation System

This project is a GUI-based hotel reservation system built using Python and Tkinter. It interacts with a MySQL database to manage hotel rooms and reservations. The system allows users to add, view, update, and delete room and reservation records.

## Features
- Add, view, update, and delete hotel room records.
- Manage reservations with guest and room details.
- User-friendly interface built with Tkinter.
- Integration with MySQL for database operations.

## Database Schema

### Room Table
| Column      | Type        | Description                     |
|-------------|-------------|---------------------------------|
| id          | int (PK)    | Primary key for the room table. |
| room_number | varchar(10) | Room number.                   |
| type        | varchar(20) | Type of the room.              |
| price       | int         | Price of the room.             |
| status      | varchar(20) | Status of the room (e.g., Available, Occupied). |

### Reservation Table
| Column         | Type        | Description                                  |
|----------------|-------------|----------------------------------------------|
| id             | int (PK)    | Primary key for the reservation table.       |
| guest_id       | int         | ID of the guest making the reservation.      |
| room_id        | int         | ID of the room reserved.                     |
| check_in_date  | date        | Check-in date for the reservation.           |
| check_out_date | date        | Check-out date for the reservation.          |
| status         | varchar(20) | Status of the reservation (e.g., Confirmed). |

## Requirements
- Python 3.x
- MySQL
- Tkinter (comes with Python)
- MySQL Connector for Python

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/chethanareddy-2801/hotel-reservation-system.git
   cd hotel-reservation-system
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up the MySQL database:
   - Create a database named `HotelReservationSystem`.
   - Create the `Room` and `Reservation` tables using the schema above.

4. Update the MySQL credentials in the Python script (`host`, `user`, `password`, `database`).

## Usage

1. Run the application:
   ```bash
   python main.py
   ```

2. Use the GUI to manage rooms and reservations:
   - Add new rooms or reservations.
   - View existing records.
   - Update or delete records as needed.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.
