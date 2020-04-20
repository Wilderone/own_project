import requests
import json
import pprint
#import serv

url_profiles = 'https://fleet-api.taxi.yandex.net/v1/parks/driver-profiles/list'
url_pay = 'https://fleet-api.taxi.yandex.net/v2/parks/driver-profiles/transactions/list'

access = {'X-Client-ID': 'taxi/par1',
          'X-Api-Key': 'mT'}
query = {'limit': 1000,
         'query':
             {'park':
                  {'id': '92ed796aa261'}
              }
         }


def get_profiles(url, data, secret):
    result = requests.post(url, data=json.dumps(data), headers=secret)
    print(result.status_code)
    if result.status_code != 200:
        print(result.text)
        x_result = get_profiles(url, data, secret)
        return x_result
    return result


def get_transactions(url, data, secret):
    result = requests.post(url, data=json.dumps(data), headers=secret)
    print(result.status_code)
    if result.status_code != 200:
        print(result.text)
        x_result = get_transactions(url, data, secret)
        return x_result
    return result


yt = get_profiles(url_profiles, query, access)
profiles = yt.json
# with open('D:\\drivers.txt', 'w', encoding='UTF-8') as f:
#     json.dump(profiles(), f)
drivers = {}
for row in profiles()['driver_profiles']:
    if 'working' == row['driver_profile']['work_status']:
        drivers[row['driver_profile']['last_name'].strip().title() + ' ' + row['driver_profile'][
            'first_name'].strip().title()] = \
            row['driver_profile']['id']
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(drivers.keys())


def get_name():
    return input('Фамилия - Имя водителя: ')


# dif_person = get_name()

def get_payments():
    idd = drivers[get_name().title()]
    date_from = "2020-04-06T00:00:00+07:00"
    date_to = "2020-04-09T23:59:59+07:00"
    query_pay = {
        "limit": 1000,
        "query": {
            "park": {
                "driver_profile": {
                    "id": str(idd)
                },
                "id": "92ed796aa0224b85b2b6c3d28d251261",
                "transaction": {
                    "category_ids": ['bank_payment', 'card', 'corporate', 'cash_collected',
                                     'partner_ride_cash_collected', 'bonus',
                                     'platform_bonus_fee', 'platform_callcenter_fee', 'platform_ride_fee',
                                     'partner_bonus_fee',
                                     'partner_ride_fee', 'partner_subscription_fee', 'platform_ride_vat',
                                     'subscription', 'subscription_vat', 'tip', 'promotion_promocode',
                                     'promotion_discount', 'platform_other_scout',
                                     ],
                    "event_at": {
                        "from": date_from,
                        "to": date_to
                    }
                }
            }
        }
    }
    return query_pay






# def main():
#     tranz = get_transactions(url_pay, get_payments(), access)
#     tr = tranz.json
#     pp.pprint(tr())
#     comissions = 0
#     amount = 0
#     cash = 0
#     for i in tr()['transactions']:
#         if float(i['amount']) > 0:
#             amount += float(i['amount'])
#         if float(i['amount']) < 0:
#             comissions -= float(i['amount'])
#         if 'Наличные' in i['category_name']:
#             cash += float(i['amount'])

    # margin = round(amount - comissions, 1)
    # print(
    #     f'{get_name()} прибыль {round(amount, 1)}, списания {round(comissions, 1)} итого {round(margin, 1)} даты c {date_from} по {date_to}, '
    #     f'налички {round(cash, 1)}')
