import json
import os
import re
from sys import exit

from Miitopia_Randomizer.MiitopiaRandomizer.util import get_csv_rows_from_sarc
from Miitopia_Randomizer.MiitopiaRandomizer.const import base_output_dir

# noinspection SpellCheckingInspection
dishes_internal_to_localized_name = {
    'Alien': 'Space Food',
    'Armor': 'Flaming Chilli Soup',
    'Banshee': 'Banshee Tears',
    'Bomb': 'Bomble Gum',
    'Bread': 'Sandwich',
    'Burger': 'Hamburger',
    'Butterfly': 'Butterfly Honey',
    'Cactus': 'Cactus Juice',
    'Cake': 'Cake',
    'Cerberus': 'Hell Dog',
    'Cheesecake': 'Cheesecake',
    'Cloud': 'Cotton Candy',
    'Cobra': 'Fried Cobra',
    'Crepe': 'Mysterious Crepe',
    'Crystal': 'Iceberg Salad',
    'Demon': 'Devil Protein',
    'Devil': 'Devil\'s Food Cake',
    'Dog': 'Doggy Doughnut',
    'DonerKebab': 'Doner Kebab',
    'Dragon': 'Dragon Fruit',
    'EatPlant': 'Bitingly Bitter Tea',
    'Excite': 'Guitar Pick Nachos',
    'Fluff': 'Fluffy Marshmallows',
    'Frog': 'Frog Juice',
    'FrozenFood': 'Frozen Ready Meal',
    'Goblin': 'Goblin Ham',
    'Golem': 'Golem Steak',
    'Gorilla': 'Gorilla Protein',
    'Gremlin': 'Hobgob Doughnuts',
    'Griffon': 'Roast Griffin',
    'Hammer': 'Tenderized Tartare',
    'Harpy': 'Fluffy Omelette',
    'Hieroglyph': 'Hieroglyph Toast',
    'IceQueen': 'Icy Mints',
    'IronBall': 'Sharp Stew',
    'KingMeat': 'Royal Roast',
    'Lizardman': 'Roast Lizard Tail',
    'Mahimahi': 'Grilled Mahimahi',
    'Medusa': 'Rock Candy',
    'Mimit': 'Snurp Radish',
    'Minotaur': 'Beefburger',
    'Mole': 'Strata Sundae',
    'Monitor': 'Pixel Grub',
    'Mouse': 'Mouse Treat',
    'Mummy': 'Mummy Jerky',
    'Mushroom': 'Mushroom Sauté',
    'Nose': 'Fragrant Tea',
    'Nostrum': 'Elven Potion',
    'Owl': 'Forest Nuts',
    'Painting': 'Art Cookie',
    'Penguin': 'Penguin Treat',
    'Pharaoh': 'Dynastic Soup',
    'Pizza': 'Geothermal Pizza',
    'Puppet': 'Puppet Pepper',
    'Robot': 'Robojuice',
    'Rock': 'Choc Rock',
    'Satan': 'Ultimate Delicacy',
    'Scorpion': 'BBQ Scorpion',
    'Serpent': 'Snake Meunière',
    'Shield': 'Shield Gratin',
    'Skeleton': 'Bone Biscuit',
    'Slime': 'Slime Jelly',
    'Snail': 'Steamed Snails',
    'Snowman': 'Snowmilk',
    'Soup': 'Warming Soup',
    'Spider': 'Spider Roll',
    'Sword': 'Sword Sashimi',
    'Tadpole': 'Baby Food',
    'Tomato': 'Tomato Spaghetti',
    'Turkey': 'Turkey Curry',
    'Ufo': 'Alien Gummy Candy',
    'Wind': 'Tornado Lemonade',
}

job_info: dict[str, tuple[str, str]] = {
    'Fighter': ('Warrior', 'Jump Slash'),
    'Wizard': ('Mage', 'Fire'),
    'Priest': ('Cleric', 'Cure'),
    'Thief': ('Thief', 'Booby Trap'),
    'Idol': ('Pop Star', 'Earworm'),
    'Vampire': ('Vampire', 'Curse'),
    'Cook': ('Chef', 'Home Cooking'),
    'Tank': ('Tank', 'Human Cannonball'),
    'Devil': ('Imp', 'Naughty Pitchfork'),
    'Royalty': ('Princess', 'Royal Wave'),
    'Flower': ('Flower', 'Gentle Fragrance'),
    'Scientist': ('Scientist', 'Glitch'),
    'Cat': ('Cat', 'Playful Antics'),
    'Elf': ('Elf', 'Dancing Arrow')
}


def get_csv_rows_from_output_sarc(file_path: str, file_in_sarc: str):
    return get_csv_rows_from_sarc(os.path.join(base_output_dir, file_path), file_in_sarc)


class BingoBoard(list):
    def __init__(self, *cells):
        super(BingoBoard, self).__init__(
            {'name': cell} for cell in cells
        )

    def add_cell(self, name: str):
        self.append({'name': name})


def main():
    if not os.path.isdir(base_output_dir):
        print('\'Output\' directory not found')
        exit(1)

    board = BingoBoard(
        'Earn 3 Medals',
        'Defeat a Snurp',
        'Defeat a Boss',
        'Eat a One Star Food',
        'Obtain Revive Sprinkles',
        'Activate Hang On',
        'Activate Warm Up',
        'Activate Spare',
        'Activate Nah...',
        'Use a Quirk for the First Time',
        'Activate Avoid',
        'Activate Oops!',
        'Activate Bluff',
        'Use a Skill for the First Time',
        'Meet The Great Sage',
        'Go to the Powdered Peaks',
        'Open 3 Chests',
        'Rescue 100 Faces',
        'Talk to the Nintendo Fan',
        'Eat a Two Star Food',
        'Get Friendship Level 10',
        'Have 4 Level 4 Friendships',
        'Start an Inn Event',
        'Defeat the General Princess',
        'Reach Level 10',
        'Have 4 Level 5 Miis',
        'Have 4 Party Members',
        'Defeat an Enemy with Blue Eyes',
        'Obtain 5 Weapons',
        'Obtain 5 Outfits',
        'Meet the King',
        'Get 4 Polkadot Outfits',
        'Eat a Loved Food',
        'Get an Outfit from the Arcade',
        'Win Rock Paper Scissors',
        'Get 3 Gold Flags',
        'Get into a Quarrel',
        'Meet the Prince from a Nearby Land'
    )

    enemies_to_search: list[str] = []
    enemies_to_search += get_csv_rows_from_output_sarc('stage/World01.sarc', 'W1_0_04_enemy.csv')[1][2:11]
    enemies_to_search += get_csv_rows_from_output_sarc('stage/World01.sarc', 'W1_0_06_enemy.csv')[0][2:11]
    # Remove empty entries
    enemies_to_search = [enemy for enemy in enemies_to_search if enemy]

    for enemy in enemies_to_search:
        dish_name = re.match(r"([a-z]+)([0-9]+)", enemy, re.I).groups()[0]
        board.add_cell('Eat ' + dishes_internal_to_localized_name[dish_name])

    for job in get_csv_rows_from_output_sarc('job.sarc', 'JobInfo.csv'):
        job_name, job_move = job_info[job[0]]
        job_world = job[1]
        if job_world == '1':
            board.add_cell(f'Get a level 5 {job_name}')
            board.add_cell(f'Use {job_move}')

    with open('Board.txt', 'w') as f:
        json.dump(board, f, indent=4)
    print('Done!')


if __name__ == '__main__':
    main()
