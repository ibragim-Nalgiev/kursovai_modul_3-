import pytest


from utils import get_data, get_last_data, get_formatted_data, get_filtered_data


def test_get_data():
    url = "https://file.notion.so/f/s/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?spaceId=0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&table=block&id=f11058ed-10ad-42ea-a13d-aad1945e5421&expirationTimestamp=1678782630818&signature=x347G3X1wAP3I7ysx-Kq86bKYInXm8IrD1Jmirw_dyo&downloadName=operations.json"
    assert get_data(url) is not None
    url = "https://file.notion.so/f/s/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?spaceId=0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&table=block&id=f11058ed-10ad-42ea-a13d-aad1945e5421&expirationTimestamp=1678782630818&signature=x347G3X1wAP3I7ysx-Kq86bKYInXm8IrD1Jmirw_dyo&downloadNam=operations.json"
    data, info = get_data(url)
    assert data is None
    assert info == "WARNING: Статус ответа:419"
    url = "https://fil.notion.so/f/s/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?spaceId=0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&table=block&id=f11058ed-10ad-42ea-a13d-aad1945e5421&expirationTimestamp=1678782630818&signature=x347G3X1wAP3I7ysx-Kq86bKYInXm8IrD1Jmirw_dyo&downloadNam=operations.json"
    data, info = get_data(url)
    assert data is None
    assert info == "ERROR: requests.exceptions.ConnectionError"


def test_get_filtered_data(test_data):
    assert len(get_filtered_data(test_data)) == 5
    assert len(get_filtered_data(test_data, filtered_empty_from=True)) == 4



def test_get_last_data(test_data):
    data = get_last_data(test_data, count_last_values=2)
    print(data)


def test_get_formatted_data(test_data):
    data = get_formatted_data(test_data[:1])
    assert data == ['26.08.2019 Перевод организации \nMaestro 1596 83** *** 5199 -> Счет: **9589\n31957.58 руб.']


