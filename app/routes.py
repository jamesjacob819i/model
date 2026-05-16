from flask import request

def calculate_discount(cart):
    coupon_code = request.args.get('coupon_code')
    if coupon_code is None:
        return 0
