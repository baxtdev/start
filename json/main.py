import json


blackjack_hand = {"name":"tom"}
print(f"У нас есть обьект {blackjack_hand} и type {type(blackjack_hand)}")
encoded_hand = json.dumps(blackjack_hand)
print(f"Мы преобразовали на JSON{type(encoded_hand)} и у нас,в такоком виде{encoded_hand}")
decoded_hand = json.loads(encoded_hand)
print(f"Так как у нас был json{type(encoded_hand)},Мы переобразуемм этот оббьект на {type(decoded_hand)}, Получилось у нас{decoded_hand}")



