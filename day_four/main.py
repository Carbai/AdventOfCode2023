with open('input.txt') as ifile:
    input = ifile.read().splitlines()

def get_combinations(lines: list) -> tuple:
    winners_lst = []
    elf_num_lst = []
    for line in lines:
        card = line.split(':')[-1]
        winners_lst.append(card.split('|')[0].strip())
        elf_num_lst.append(card.split('|')[-1].strip())
    return (winners_lst, elf_num_lst)

def get_winners(win: list, your_comb: list) -> list:
    winners_num = []
    for n,card in enumerate(your_comb):
        int_comb = [int(x) for x in card.split()]
        int_win= [int(x) for x in win[n].split()]
        card_winners = [x for x in int_comb if x in int_win]
        winners_num.append(card_winners)
    return winners_num

def get_score(winners: list) -> int:
    score = []
    for winner in winners:
        card_score = 0
        for i in range(len(winner)):
            if card_score == 0:
                card_score += 1
            else:
                card_score = card_score*2
        score.append(card_score)
    return sum(score)

def duplicate_cards(matches: list) -> list:
    cards_number = [1]*len(matches)
    
    for n,match in enumerate(matches):
        for i in range(n+1,n+1+match):
            cards_number[i]=cards_number[i]+(1*cards_number[n])
    return sum(cards_number)

winn, your_num = get_combinations(input)
winning_numbers=get_winners(winn, your_num)
print('Part one: ', get_score(winning_numbers))
print('Part two: ', duplicate_cards([len(x) for x in winning_numbers]))

