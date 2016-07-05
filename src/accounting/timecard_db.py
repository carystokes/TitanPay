import sqlite3


def import_timecards():
    conn = sqlite3.connect('time_card_db')
    cd = conn.cursor()
    cd.execute('DROP TABLE t_cards')
    cd.execute('CREATE TABLE t_cards (emp_id TEXT NOT NULL, time_in TEXT NOT NULL, time_out TEXT NOT NULL,\
        tc_date TEXT)')

    tc_hand = open('timecards.csv', 'r')
    count = 0
    for card in tc_hand:
        if count != 0:
            tc = card.split(',')
            tc[3] = tc[3].strip()
            cd.execute(
                'INSERT INTO t_cards(emp_id, time_in, time_out, tc_date) VALUES (?, ?, ?, ?)', (tc[0], tc[1], tc[2], tc[3]))
        count += 1

    tc_hand.close()
    conn.commit()
    conn.close()
