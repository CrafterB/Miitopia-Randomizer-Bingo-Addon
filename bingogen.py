import csv
import sarc
import os
from io import StringIO

def get_csv_from_input_sarc(file_path: str, file_in_sarc: str):
    return get_csv_rows_from_sarc(os.path.join(job_output_dir, file_path), file_in_sarc)
    
def get_csv_for_enemy(file_path: str, file_in_sarc: str):
    return get_csv_rows_from_sarc(os.path.join(enemy_output_dir, file_path), file_in_sarc)
    
def get_csv_rows_from_sarc(sarc_or_filename: sarc.SARC | str, file_in_sarc: str) -> list[list[str]]:
    if isinstance(sarc_or_filename, sarc.SARC):
        sarc_reader = sarc_or_filename
    else:
        with open(sarc_or_filename, 'rb') as f:
            sarc_reader = sarc.read_file_and_make_sarc(f)
    file_data = StringIO(
        sarc_reader.get_file_data(file_in_sarc).tobytes().decode(),
        newline=''
    )
    csv_reader = csv.reader(file_data)
    return [*csv_reader]

def search(list, objective):
    for i in range(len(list)):
        if list[i] == objective:
            return True
    return False

def search_nest(list_one, list_two):
    global status
    for i in range(len(list_one)): 
        for x in range(len(list_two)):
            for y in range(len(list_two[x])):
                if list_one[i] == list_two[x][y]:
                        status[x] = 1
    return False
    
enemy_output_dir = os.path.join('Release', 'Output', 'romfs', 'cmn', 'param', 'stage')
job_output_dir = os.path.join('Release', 'Output', 'romfs', 'cmn', 'param')

with open('Release/Board.txt', "w") as bingo:
    bingo.write('[ {"name": "Earn 3 Medals"},\n')
    
enemy_reader_one = get_csv_for_enemy('World01.sarc', 'W1_0_04_enemy.csv')
enemy_reader_two = get_csv_for_enemy('World01.sarc', 'W1_0_06_enemy.csv')
job_reader = get_csv_from_input_sarc('job.sarc', 'JobInfo.csv')

line_count = 0
banshee_status = 0
bomb_status = 0
bread_status = 0
butterfly_status = 0
cactus_status = 0
cloud_status = 0
cobra_status = 0
crystal_status = 0
devil_status = 0
fluff_status = 0
fossil_status = 0
goblin_deez_status = 0
hammer_status = 0
harpy_status = 0
hieroglyph_status = 0
iron_ball_status = 0
mole_status = 0
monitor_status = 0
mouse_status = 0
mummy_status = 0
mural_status = 0
mushroom_status = 0
nose_status = 0
painting_status = 0
penguin_status = 0
robot_status = 0
rock_status = 0
scorpion_status = 0
shield_status = 0
skeleton_status = 0
slime_status = 0
snail_status = 0
snowman_status = 0
sword_status = 0
tadpole_status = 0
tomato_status = 0
turkey_status = 0
ufo_status = 0
wind_status = 0
status = [banshee_status, bomb_status, bread_status, butterfly_status, cactus_status, cloud_status, cobra_status, crystal_status, devil_status, fluff_status, fossil_status, goblin_deez_status, hammer_status, harpy_status, hieroglyph_status, iron_ball_status, mole_status, monitor_status, mouse_status, mummy_status, mural_status, mushroom_status, nose_status, painting_status, penguin_status, robot_status, rock_status, scorpion_status, shield_status, skeleton_status, slime_status, snail_status, snowman_status, sword_status, tadpole_status, tomato_status, turkey_status, ufo_status, wind_status]
food = ['Banshee Tears', 'Bomble Gum', 'Sandwich', 'Butterfly Honey', 'Cactus Juice', 'Cotton Candy', 'Fried Cobra', 'Iceberg Salad', 'Devil\'s Food Cake', 'Fluffy Marshmallow', 'Hieroglyph Toast', 'Goblin Ham', 'Tenderized Tartare', 'Fluffy Omelette', 'Hieroglyph Toast', 'Sharp Stew', 'Strata Sunday', 'Pixel Grub', 'Mouse Treat', 'Mummy Jerky', 'Heiroglyph Toast', 'Mushroom Saute', 'Fragrent Tea', 'Art Cookie', 'Penguin Treat', 'Robojuice', 'Choc Rock', 'BBQ Scorpion', 'Shield Gratin', 'Bone Biscuit', 'Steamed Snails', 'Snowmilk', 'Sword Sashimi', 'Baby Food', 'Tomato Spaghetti', 'Turkey Curry', 'Alien Gummy Candy', 'Tornado Lemonade']
banshee_group = ['Banshee0', 'Banshee1', 'Banshee2', 'Banshee3']
bomb_group = ['Bomb0', 'Bomb1', 'Bomb2']
bread_group = ['Bread1', 'Bread2']
butterfly_group = ['Butterfly0_1', 'Butterfly0_2', 'Butterfly1', 'Butterfly2', 'Butterfly3', 'Butterfly4', 'Butterfly5', 'Butterfly6', 'Butterfly7', 'Butterfly8', 'Butterfly9']
cactus_group = ['Cactus0', 'Cactus1', 'Cactus3']
cloud_group = ['Cloud0', 'Cloud1', 'Cloud2', 'Cloud3', 'Cloud4']
cobra_group = ['Cobra0', 'Cobra1', 'Cobra2', 'Cobra3', 'Cobra4', 'Cobra5']
crystal_group = ['Crystal0', 'Crystal1', 'Crystal2']
devil_group = ['Devil0', 'Devil1', 'Devil2', 'Devil3', 'Devil4', 'Devil5', 'Devil6', 'Devil7', 'Devil8', 'Devil9']
fluff_group = ['Fluff0', 'Fluff1', 'Fluff2', 'Fluff3', 'Fluff4', 'Fluff5', 'Fluff6', 'Fluff7', 'Fluff8']
fossil_group = ['Fossil0', 'Fossil1', 'Fossil2', 'Fossil3', 'Fossil4', 'Fossil5']
goblin_deez_group = ['Goblin0', 'Goblin0_Dish', 'GoblinFairy', 'GoblinMagic', 'GoblinRed', 'GoblinRobot', 'GoblinSpace', 'Goblin10', 'Goblin11']
hammer_group = ['Hammer0', 'Hammer1', 'Hammer2']
harpy_group = ['Harpy0', 'Harpy1', 'Harpy2']
hieroglyph_group = ['Hieroglyph0', 'Hieroglyph1', 'Hieroglyph2']
iron_ball_group = ['IronBall0', 'IronBall1', 'IronBall2']
mole_group = ['Mole0', 'Mole1', 'Mole2']
monitor_group = ['Monitor0', 'Monitor1', 'Monitor2', 'Monitor3', 'Monitor4', 'Monitor5']
mouse_group = ['Mouse0', 'Mouse1', 'Mouse2', 'Mouse3', 'Mouse4', 'Mouse5', 'Mouse6']
mummy_group = ['Mummy0', 'Mummy1', 'Mummy2']
mural_group = ['Mural0', 'Mural1']
mushroom_group = ['Mushroom0', 'Mushroom1', 'Mushroom2']
nose_group = ['Nose0', 'Nose1', 'Nose2']
painting_group = ['Painting0', 'Painting1', 'Painting2', 'Painting3', 'Painting4', 'Painting5', 'Painting6', 'Painting7']
penguin_group = ['Penguin0', 'Penguin1', 'Penguin2']
robot_group = ['Robot1', 'Robot2']
rock_group = ['Rock0', 'Rock1', 'Rock2', 'Rock3', 'Rock4', 'Rock5', 'Rock6']
scorpion_group = ['Scorpion0', 'Scorpion1', 'Scorpion2']
shield_group = ['Shield0', 'Shield1', 'Shield2', 'Shield3', 'Shield4']
skeleton_group = ['Skeleton0', 'Skeleton1', 'Skeleton2']
slime_group = ['Slime1', 'Slime2', 'Slime3', 'Slime4', 'Slime5', 'Slime6', 'Slime7', 'Slime8']
snail_group = ['Snail0', 'Snail1', 'Snail2']
snowman_group = ['Snowman0', 'Snowman1', 'Snowman2']
sword_group = ['Sword0', 'Sword1', 'Sword2', 'Sword3']
tadpole_group = ['Tadpole0', 'Tadpole1', 'Tadpole2', 'Tadpole3']
tomato_group = ['Tomato1', 'Tomato2']
turkey_group = ['Turkey0', 'Turkey1', 'Turkey2']
ufo_group = ['Ufo0', 'Ufo1', 'Ufo2', 'Ufo3', 'Ufo4', 'Ufo5']
wind_group = ['Wind0', 'Wind1', 'Wind2', 'Wind4']
group_group = [banshee_group, bomb_group, bread_group, butterfly_group, cactus_group, cloud_group, cobra_group, crystal_group, devil_group, fluff_group, fossil_group, goblin_deez_group, hammer_group, harpy_group, hieroglyph_group, iron_ball_group, mole_group, monitor_group, mouse_group, mummy_group, mural_group, mushroom_group, nose_group, painting_group, penguin_group, robot_group, rock_group, scorpion_group, shield_group, skeleton_group, slime_group, snail_group, snowman_group, sword_group, tadpole_group, tomato_group, turkey_group, ufo_group, wind_group]
status_signal = search_nest(enemy_reader_one[1], group_group)
status_signal = search_nest(enemy_reader_two[0], group_group)
with open('Release/Board.txt', "a") as bingo:
    for p in range(len(status)):
        if status[p] == 1:
            bingo.write('  {"name": "Eat ' + food[p] + '"},\n')

line_count = 0
objective = '1'
warrior_status = 0
wizard_status = 0
cleric_status = 0
thief_status = 0
idol_status = 0
vampire_status = 0
chef_status = 0
tank_status = 0
imp_status = 0
princess_status = 0
flower_status = 0
scientist_status = 0
cat_status = 0
elf_status = 0
warrior = job_reader[0]
if search(warrior, objective):
    warrior_status = 1
wizard = job_reader[1]
if search(wizard, objective):
    wizard_status = 1
cleric = job_reader[2]
if search(cleric, objective):
    cleric_status = 1
thief = job_reader[3]
if search(thief, objective):
    thief_status = 1
idol = job_reader[4]
if search(idol, objective):
    idol_status = 1
vampire = job_reader[5]
if search(vampire, objective):
    vampire_status = 1
chef = job_reader[6]
if search(chef, objective):
    chef_status = 1
tank = job_reader[7]
if search(tank, objective):
    tank_status = 1
imp = job_reader[8]
if search(imp, objective):
    imp_status = 1
princess = job_reader[9]
if search(princess, objective):
    princess_status = 1
flower = job_reader[10]
if search(flower, objective):
     flower_status = 1
scientist = job_reader[11]
if search(scientist, objective):
    scientist_status = 1
cat = job_reader[12]
if search(cat, objective):
    cat_status = 1
elf = job_reader[13]
if search(elf, objective):
    elf_status = 1
with open('Release/Board.txt', "a") as bingo:
    if warrior_status == 1:
        bingo.write('  {"name": "Get a level 5 Warrior"},\n')
        bingo.write('  {"name": "Use Jumpslash"},\n')
    if wizard_status == 1:
        bingo.write('  {"name": "Get a level 5 Wizard"},\n')
        bingo.write('  {"name": "Use Fire"},\n')
    if cleric_status == 1:
        bingo.write('  {"name": "Get a level 5 Cleric"},\n')
        bingo.write('  {"name": "Use Cure"},\n')
    if thief_status == 1:
        bingo.write('  {"name": "Get a level 5 Thief"},\n')
        bingo.write('  {"name": "Use Booby Trap"},\n')
    if idol_status == 1:
        bingo.write('  {"name": "Get a level 5 Pop Star"},\n')
        bingo.write('  {"name": "Use Earworm"},\n')
    if vampire_status == 1:
        bingo.write('  {"name": "Get a level 5 Vampire"},\n')
        bingo.write('  {"name": "Use Curse"},\n')
    if chef_status == 1:
        bingo.write('  {"name": "Get a level 5 Chef"},\n')
        bingo.write('  {"name": "Use Home Cooking"},\n')
    if tank_status == 1:
        bingo.write('  {"name": "Get a level 5 Tank"},\n')
        bingo.write('  {"name": "Use Human Cannonball"},\n')
    if imp_status == 1:
        bingo.write('  {"name": "Get a level 5 Imp"},\n')
        bingo.write('  {"name": "Use Naughty Pitchfork"},\n')
    if princess_status == 1:
        bingo.write('  {"name": "Get a level 5 Princess"},\n')
        bingo.write('  {"name": "Use Royal Wave"},\n')
    if flower_status == 1:
        bingo.write('  {"name": "Get a level 5 Flower"},\n')
        bingo.write('  {"name": "Use Gentle Fragrance"},\n')
    if scientist_status == 1:
        bingo.write('  {"name": "Get a level 5 Scientist"},\n')
        bingo.write('  {"name": "Use Glitch"},\n')
    if cat_status == 1:
        bingo.write('  {"name": "Get a level 5 Cat"},\n')
        bingo.write('  {"name": "Use Playful Antics"},\n')
    if elf_status == 1:
        bingo.write('  {"name": "Get a level 5 Elf"},\n')
        bingo.write('  {"name": "Use Dancing Arrow"},\n')
    bingo.write('  {"name": "Defeat a Snurp"},\n  {"name": "Defeat a Boss"},\n  {"name": "Eat a One Star Food"},\n  {"name": "Obtain Revive Sprinkles"},\n  {"name": "Activate Hang On"},\n  {"name": "Activate Warm Up"},\n  {"name": "Activate Spare"},\n  {"name": "Activate Nah..."},\n  {"name": "Use a Quirk for the First Time"},\n  {"name": "Activate Avoid"},\n  {"name": "Activate Oops!"},\n  {"name": "Activate Bluff"},\n  {"name": "Use a Skill for the First Time"},\n  {"name": "Meet The Great Sage"},\n  {"name": "Go to the Powdered Peaks"},\n  {"name": "Open 3 Chests"},\n  {"name": "Rescue 100 Faces"},\n  {"name": "Talk to the Nintendo Fan"},\n  {"name": "Eat a Two Star Food"},\n  {"name": "Get Friendship Level 10"},\n  {"name": "Have 4 Level 4 Friendships"},\n  {"name": "Start an Inn Event"},\n  {"name": "Defeat the General Princess"},\n  {"name": "Reach Level 10"},\n  {"name": "Have 4 Level 5 Miis"},\n  {"name": "Have 4 Party Members"},\n  {"name": "Defeat an Enemy with Blue Eyes"},\n  {"name": "Obtain 5 Weapons"},\n  {"name": "Obtain 5 Outfits"},\n  {"name": "Meet the King"},\n  {"name": "Get 4 Polkadot Outfits"},\n  {"name": "Eat a Loved Food"},\n  {"name": "Get an Outfit from the Arcade"},\n  {"name": "Win Rock Paper Scissors"},\n  {"name": "Get 3 Gold Flags"},\n  {"name": "Get into a Quarrel"},\n  {"name": "Meet the Prince from a Nearby Land"} ]')