import sqlite3

def get_person_and_pets(person_id):
    conn = sqlite3.connect('pets.db')
    cur = conn.cursor()

    cur.execute('SELECT first_name, last_name, age FROM person WHERE id = ?', (person_id,))
    person = cur.fetchone()

    if person:
        print(f"{person[0]} {person[1]}, {person[2]} years old")
        cur.execute('''
        SELECT pet.name, pet.breed, pet.age, pet.dead
        FROM pet
        JOIN person_pet ON pet.id = person_pet.pet_id
        WHERE person_pet.person_id = ?
        ''', (person_id,))
        pets = cur.fetchall()
        for pet in pets:
            status = "that is deceased" if pet[3] else "that is alive"
            print(f"  - Owned {pet[0]}, a {pet[1]}, that was {pet[2]} years old and {status}.")
    else:
        print("Person not found.")

    conn.close()


while True:
    try:
        user_input = int(input("Enter person ID (-1 to exit): "))
        if user_input == -1:
            break
        get_person_and_pets(user_input)
    except ValueError:
        print("Please enter a valid integer.")
        
if __name__ == "__main__":
    print("Running query_pets.py")
