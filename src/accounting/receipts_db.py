import sqlite3


def import_receipts():
    conn = sqlite3.connect('receipt_db')
    cd = conn.cursor()
    cd.execute('DROP TABLE receipts')
    cd.execute('CREATE TABLE receipts (emp_id TEXT NOT NULL, last_name TEXT, item TEXT, units TEXT, unit_cost TEXT, total REAL NOT NULL)')

    rec_hand = open('receipts.csv', 'r')
    count = 0
    for line in rec_hand:
        if count != 0:
            comma_count = 0
            line2 = ''
            for cha in range(0, len(line)):
                if line[cha] == ',':
                    comma_count += 1
                    if comma_count > 5:
                        continue
                    else:
                        line2 = line2 + ','
                else:
                    line2 = line2 + line[cha]

            receipt = line2.split(',')
            total = receipt[5].strip()
            total = total.strip('"')
            total = total.strip()
            totalf = float(total)

            cd.execute(
                'INSERT INTO receipts (emp_id, last_name, item, units, unit_cost, total) VALUES (?, ?, ?, ?, ?, ?)', (receipt[0], receipt[1], receipt[2], receipt[3], receipt[4], totalf))
        count += 1

    rec_hand.close()
    conn.commit()
    conn.close()

