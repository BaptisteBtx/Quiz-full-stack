import jwt_utils

def verify_auth(headers):
    print("headerS", headers)
    header = headers.get('Authorization')
    print(header)
    if header==None:
        return False
    else :
        print(1)
        try:
            print(2)
            jwt_utils.decode_token(header)
            print(4)
        except Exception as e:
            print(e)
            return False

        return True
