#!/usr/bin/python3
import json
import requests
import sys

def collect_account():
    print('Enter the account to be deleted')
    acct_id = input()
    return acct_id


def append_account_to_dictionary(id):
    name = ''
    trans_key = ''
    return {"deleteCustomerProfileRequest": {"merchantAuthentication": {"name": name, "transactionKey": trans_key}, "customerProfileId": id}}


def post_delete_request(account_data):
    return requests.post('https://apitest.authorize.net/xml/v1/request.api', data=account_data)


def create_json_from_dictionary(account):
    return json.dumps(account)


def main():
    while True:
        acct_id = collect_account()
        account = append_account_to_dictionary(acct_id)
        json = create_json_from_dictionary(account)
        response = post_delete_request(json)
        print(response.text[:300])
        repeat = input("Got another? (Y/N): ")
        if str(repeat).lower() != 'y':
            sys.exit('Thanks!')


if __name__ == "__main__":
    main()
