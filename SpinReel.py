import random
import sys
class SpinReel:
    def __init__(self):
        self.icons = ['$', '%', '@', '#', '?', "*", "&"]
        self.losses = 0
        self.wins = 0
    
    def display_welcome(self):
        print("WElCOME TO MY SLOT-MACHINE GAME!!!")

    #take & validate user input
    def ask_user(self):
        while True:
            ask = input("Do you want to play the game? (Y/N) ").strip().lower()
            if ask in ['yes', 'y']:
                return True
            elif ask in ['no', 'n']:
                return False
            else:
                print("Please answer Yes(y) or No(n)!")
        
    #selects x random elements from icons list
    def selected_options(self, number_of_slots):
        return random.choices(self.icons, k=number_of_slots)
    
    #custom number of selections for the random.choices function
    def number_of_slots_inp(self):
        while True:
            take = input("Enter the number of slots:").strip()
            if take.isdigit():
                take = int(take)
                if 1 <= take <= len(self.icons):
                    return take
                else: 
                    print(f"Please only enter numbers (1-{len(self.icons)})!")
            else:
                print(f"Please enter a number of slots (1-{len(self.icons)})!")
            
    #checks if the selected icons are same & display win/lose message
    def gameplay(self):
        no_of_slots = self.number_of_slots_inp()
        drawn = self.selected_options(no_of_slots)
        print("-"*70)
        print(f"You picked: {" ".join(drawn)}")
        if len(set(drawn)) == 1:
            self.wins += 1
            print("You win!!!")
        else:
            self.losses += 1
            print("Aww! You lose, try again!")
        print("-"*70)

        print(f"Wins: {self.wins} \t Losses: {self.losses}")

    def display_summary(self):
        total_games = self.wins + self.losses
        win_rate = ((self.wins / total_games) * 100) if total_games > 0 else 0
        print("-" * 70)
        print(f"Game Summary:")
        print(f"Total Games: {total_games}")
        print(f"Wins: {self.wins}")
        print(f"Losses: {self.losses}")
        print(f"Win Rate: {win_rate:.2f}%")
        print("-" * 70)

    def main(self):
        if not self.ask_user():
            print("Exiting Game...")
            return
        while True:
            self.gameplay()
            while True:
                again = input("Do you want to play again? (Y/N)").strip().lower()
                if again in ['yes', 'y']:
                    break
                elif again in ['n', 'no']:
                    self.display_summary()
                    print("Exiting the game...")
                    sys.exit()
                else:
                    print("Please answer Yes(y) or No(n)!")