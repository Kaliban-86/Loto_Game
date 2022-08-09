from card import Card, show_card
from pouch_with_barrels import Pouch
from player import Player

player_one = Player('Player')
player_two = Player('Computer')

# создаем мешочек с 90 бочонками
new_pouch = Pouch()

# создаем карточку первого игрока
player_card = Card()
player_card.create_cards(player_one.name)

# создаем карточку второго игрока
computer_card = Card()
computer_card.create_cards(player_two.name)

# Создаем лист с каротчками
card_list = [player_card, computer_card]
player_list = [player_one, player_two]


def play_loto(card_list_to_play, player_list_to_play):
    is_play = True
    player_number = 0

    print(player_one == player_two)
    print(player_card == player_card)


    while is_play:
        print(' ')
        print(f'Счет: {player_list_to_play[0].name} - {player_list_to_play[0].cross_count} очк.'
              f' {player_list_to_play[1].name} - {player_list_to_play[1].cross_count} очк.')
        print(f'Сейчас ход игрока: {card_list_to_play[player_number].card_name}')
        barrel_num = str(new_pouch.get_barrel())
        print(f'Бочонок №: {barrel_num}, осталось {len(new_pouch.pouch)}')
        print(card_list[0])
        print(card_list[1])

        if player_number == 0:
            answer = str(input('Зачеркивать число? (да/нет): '))
            if answer == 'да' and barrel_num in card_list_to_play[player_number].card_values:
                card_list_to_play[player_number].cross_out(barrel_num)
                player_list_to_play[player_number].counting_win()

            elif answer == 'да' and barrel_num not in card_list_to_play[player_number].card_values:
                print(f'Игрок {card_list_to_play[player_number].card_name}  проиграл!')
                break

            elif answer == 'нет' and barrel_num in card_list_to_play[player_number].card_values:
                print(f'Игрок {card_list_to_play[player_number].card_name}  проиграл!')
                break

            elif answer == 'нет' and barrel_num not in card_list_to_play[player_number].card_values:
                pass
        else:
            if barrel_num in card_list_to_play[player_number].card_values:
                card_list_to_play[player_number].cross_out(barrel_num)
                player_list_to_play[player_number].counting_win()
            else:
                pass

        if player_number == 0:
            player_number = 1
        else:
            player_number = 0

        if player_list_to_play[player_number].cross_count == 15:
            print(f' Игрок {player_list_to_play[player_number].name} победил!!!!')
            break
        elif len(new_pouch.pouch) == 0:
            if player_list_to_play[0].cross_count > player_list_to_play[1].cross_count:
                print(f'Победил {player_list_to_play[0].name}!!!!')
                break
            elif player_list_to_play[0].cross_count == player_list_to_play[1].cross_count:
                print('Ничья!')
                break
            else:
                print(f'Победил {player_list_to_play[1].name}!!!!')
                break


play_loto(card_list, player_list)
