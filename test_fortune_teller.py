from fortune_teller import majors, swords, cups, wands, coins


def test_legal():
    assert majors[0].legal(swords[0]) == False
    assert majors[0].legal(cups[0]) == False
    assert coins[10].legal(majors[11]) == False
    assert wands[12].legal(cups[12]) == False
    assert swords[12].legal(swords[12]) == False
    assert majors[21].legal(majors[0]) == False
    assert majors[7].legal(majors[6])
    assert majors[4].legal(majors[5])
    assert swords[4].legal(swords[5])
