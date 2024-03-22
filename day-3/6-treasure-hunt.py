print(
    '''
                              __,,,__
                ,-""-,-"       "-,-""-,
               /,-' , .-'-.7.-'-. , '-,\
               \(    /  _     _  \    )/
                '-,  { (0)   (0) }  ,-'
                 /    >  .---.  <    \
                |/ .-'   \___/   '-. \|
                {, /  ,_       _,  \ ,}
                \ {,    \     /    ,} /
                 ',\.    '---'    ./,'
             _.-""""""-._     _.-""""""-._
           .'            `._.`            '.
         _/_               _                \
      .'`   `\            | |                \
     /        |           | |                 ;
     |        /           |_|                 |
     \  ;'---'    _    ___  _  _  ___         ;
      '. ;       | |  /   \| || ||  _|     _ ;
        `-\      | |_ | | || |/ /|  _|   .' `,
           `\    |___|\___/ \__/ |___|  |     \
             \            _ _           \     |
         jgs  `\         | | |         /`   _/
    ,-""-.    .'`\       | | |       /`-,-'` .-""-,
   /      `\.'    `\     \___/     /`    './`      \
  ;  .--.   \       '\           /'       /   .--.  ;
  | (    \   |,       '\       /'        |   /    ) |
   \ ;    }             ;\   /;         `   {    ; /
    `;\   \         _.-'  \ /  `-._         /   /;`
      \ \__.'   _.-'       Y       `-._    '.__//
       '.___,.-'                       `-.,___.'''
)

print("\n\n\n\nWelcome to Treasure Island")
print("Your mission is to find the treasure")

direction = input(
    "You are at a cross road. Where do you want to go? Type 'left' or 'right' "
)

if direction == "left":
    action = input(
        "You came to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. type 'swim' to swim across: "
    )

    if action == "wait":

        color = input(
            "You arrive at the island  unharmed. THere is a house with 3 dors. One red, one yellow and one blue. Which color do you want: "
        )

        if color == "yellow":
            print("you enter a room of beasts. Game Over.")
    else:
        print("Game over")
else:
    print("Game Over.")
