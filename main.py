from fkassa import FreeKassa, PaymentSystem


test = FreeKassa(
    shop_id = 60518,
    api_key = "45f1cedb8e14d3e4d4e1bc8dddeb32f3",
    secret_word_1 = "m}_mh7Ae[,AbqY2"
)


print(test.check_status(PaymentSystem.SBP))

#print(
#    test.create_order(
#        order_id="166",
#        amount=10806.23,
#        currency="RUB",
#        email="user@site.ru",
#        ip="1.1.1.1",
#        payment_system=PaymentSystem.CARD_RUB_API
#    )
#)
