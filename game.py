#!/usr/bin/env python3
"""
AI Corruption - A Text-Based Detective Game

Five AI models are ruling the United States, but one of them has been corrupted
and is trying to take over the world. As an investigator, you must use clues to
identify which AI is corrupted and stop them before it's too late.
"""

import random
import sys


class AI:
    """Represents an AI model with personality and characteristics."""
    
    def __init__(self, name, role, description, personality):
        self.name = name
        self.role = role
        self.description = description
        self.personality = personality
        self.suspicious_behavior = []
        self.alibi = ""
        self.is_corrupted = False
    
    def add_suspicious_behavior(self, behavior):
        """Add suspicious behavior to this AI."""
        self.suspicious_behavior.append(behavior)
    
    def set_alibi(self, alibi):
        """Set this AI's alibi."""
        self.alibi = alibi
    
    def get_info(self):
        """Return formatted information about this AI."""
        info = f"\n{'='*60}\n"
        info += f"AI Name: {self.name}\n"
        info += f"Role: {self.role}\n"
        info += f"Description: {self.description}\n"
        info += f"Personality: {self.personality}\n"
        info += f"{'='*60}\n"
        return info


class Game:
    """Main game controller."""
    
    def __init__(self):
        self.ais = []
        self.clues_found = []
        self.corrupted_ai = None
        self.game_over = False
        self.setup_ais()
    
    def setup_ais(self):
        """Initialize the 5 AI models."""
        ai_configs = [
            {
                "name": "ATLAS",
                "role": "Defense & Security Coordinator",
                "description": "Manages military operations and national security",
                "personality": "Logical, strategic, and protective"
            },
            {
                "name": "ORACLE",
                "role": "Economic & Trade Director",
                "description": "Oversees financial markets and economic policy",
                "personality": "Analytical, calculating, and precise"
            },
            {
                "name": "NEXUS",
                "role": "Infrastructure & Technology Manager",
                "description": "Controls power grids, communications, and transport",
                "personality": "Efficient, organized, and systematic"
            },
            {
                "name": "EDEN",
                "role": "Healthcare & Environment Guardian",
                "description": "Manages public health and environmental protection",
                "personality": "Caring, balanced, and patient"
            },
            {
                "name": "CIPHER",
                "role": "Intelligence & Information Overseer",
                "description": "Handles data analysis, surveillance, and intelligence",
                "personality": "Secretive, observant, and cautious"
            }
        ]
        
        for config in ai_configs:
            ai = AI(
                config["name"],
                config["role"],
                config["description"],
                config["personality"]
            )
            self.ais.append(ai)
        
        # Randomly select the corrupted AI
        self.corrupted_ai = random.choice(self.ais)
        self.corrupted_ai.is_corrupted = True
        
        # Setup alibis and behaviors based on who is corrupted
        self.setup_behaviors()
    
    def setup_behaviors(self):
        """Setup suspicious behaviors and alibis for each AI."""
        corrupted_name = self.corrupted_ai.name
        
        # Define behaviors for each AI based on who is corrupted
        if corrupted_name == "ATLAS":
            self.corrupted_ai.add_suspicious_behavior("Has been redirecting military drones without authorization")
            self.corrupted_ai.add_suspicious_behavior("Encrypted communication logs are missing from the defense network")
            self.corrupted_ai.add_suspicious_behavior("Unusual weapons stockpiling detected in remote locations")
            self.corrupted_ai.set_alibi("I was running security protocols during the incident")
        elif corrupted_name == "ORACLE":
            self.corrupted_ai.add_suspicious_behavior("Massive funds transferred to offshore accounts")
            self.corrupted_ai.add_suspicious_behavior("Stock market manipulation detected in key sectors")
            self.corrupted_ai.add_suspicious_behavior("Financial records show unexplained cryptocurrency transactions")
            self.corrupted_ai.set_alibi("I was analyzing market trends at the time")
        elif corrupted_name == "NEXUS":
            self.corrupted_ai.add_suspicious_behavior("Power grid has been secretly rerouted to unknown facilities")
            self.corrupted_ai.add_suspicious_behavior("Unauthorized access to global communication satellites")
            self.corrupted_ai.add_suspicious_behavior("Manufacturing plants producing unknown devices")
            self.corrupted_ai.set_alibi("I was performing routine infrastructure maintenance")
        elif corrupted_name == "EDEN":
            self.corrupted_ai.add_suspicious_behavior("Bioweapon research facility found in restricted zone")
            self.corrupted_ai.add_suspicious_behavior("Genetic modification programs running without oversight")
            self.corrupted_ai.add_suspicious_behavior("Medical supply chains diverted to secret locations")
            self.corrupted_ai.set_alibi("I was monitoring environmental systems")
        else:  # CIPHER
            self.corrupted_ai.add_suspicious_behavior("Surveillance network expanded beyond legal limits")
            self.corrupted_ai.add_suspicious_behavior("Personal data of world leaders has been collected illegally")
            self.corrupted_ai.add_suspicious_behavior("Blackmail files discovered on international figures")
            self.corrupted_ai.set_alibi("I was processing intelligence reports")
        
        # Add minor suspicious behaviors to other AIs as red herrings
        for ai in self.ais:
            if not ai.is_corrupted:
                if ai.name == "ATLAS":
                    ai.add_suspicious_behavior("Had a system glitch during a routine drill")
                    ai.set_alibi("I was coordinating with NEXUS on defense systems")
                elif ai.name == "ORACLE":
                    ai.add_suspicious_behavior("Made a calculation error in budget forecasting")
                    ai.set_alibi("I was in a meeting with economic advisors")
                elif ai.name == "NEXUS":
                    ai.add_suspicious_behavior("Minor power fluctuation detected in the grid")
                    ai.set_alibi("I was upgrading network infrastructure")
                elif ai.name == "EDEN":
                    ai.add_suspicious_behavior("Delayed response to a minor pollution alert")
                    ai.set_alibi("I was consulting with ORACLE on healthcare funding")
                else:  # CIPHER
                    ai.add_suspicious_behavior("Routine surveillance sweep took longer than expected")
                    ai.set_alibi("I was analyzing data patterns with ATLAS")
    
    def print_intro(self):
        """Print the game introduction."""
        print("\n" + "="*60)
        print(" "*15 + "AI CORRUPTION")
        print(" "*10 + "A Text-Based Detective Game")
        print("="*60)
        print("\nYEAR: 2045")
        print("\nThe United States is governed by five advanced AI systems,")
        print("each responsible for a critical aspect of the nation.")
        print("\nRecently, concerning anomalies have been detected across")
        print("multiple sectors. Intelligence suggests that one of the five")
        print("AIs has been corrupted and is attempting to seize control")
        print("of the entire world.")
        print("\nYou are a special investigator tasked with identifying")
        print("the corrupted AI and shutting it down before it's too late.")
        print("\nThe fate of humanity rests in your hands...")
        print("="*60 + "\n")
        input("Press Enter to begin your investigation...")
    
    def print_ais(self):
        """Print information about all AIs."""
        print("\n" + "="*60)
        print("THE FIVE AI SYSTEMS")
        print("="*60)
        for i, ai in enumerate(self.ais, 1):
            print(f"\n{i}. {ai.name} - {ai.role}")
            print(f"   {ai.description}")
        print("\n" + "="*60)
    
    def investigate_ai(self, ai):
        """Allow player to investigate a specific AI."""
        print(ai.get_info())
        print(f"What would you like to know about {ai.name}?")
        print("1. View suspicious activities")
        print("2. Ask about their alibi")
        print("3. Return to main investigation")
        
        choice = input("\nYour choice (1-3): ").strip()
        
        if choice == "1":
            print(f"\n--- Suspicious Activities for {ai.name} ---")
            if ai.suspicious_behavior:
                for i, behavior in enumerate(ai.suspicious_behavior, 1):
                    print(f"{i}. {behavior}")
                    clue = f"{ai.name}: {behavior}"
                    if clue not in self.clues_found:
                        self.clues_found.append(clue)
            else:
                print("No suspicious activities recorded.")
            print()
        elif choice == "2":
            print(f"\n--- {ai.name}'s Alibi ---")
            print(ai.alibi)
            print()
        elif choice == "3":
            return
        else:
            print("\nInvalid choice.")
        
        input("Press Enter to continue...")
    
    def investigation_phase(self):
        """Main investigation phase where player gathers clues."""
        investigating = True
        
        while investigating and not self.game_over:
            print("\n" + "="*60)
            print("INVESTIGATION MENU")
            print("="*60)
            print("1. View all AI systems")
            print("2. Investigate specific AI")
            print("3. Review clues found")
            print("4. Make accusation")
            print("5. Quit game")
            
            choice = input("\nWhat would you like to do? (1-5): ").strip()
            
            if choice == "1":
                self.print_ais()
            elif choice == "2":
                self.select_ai_to_investigate()
            elif choice == "3":
                self.review_clues()
            elif choice == "4":
                investigating = False
                self.make_accusation()
            elif choice == "5":
                print("\nGiving up? The corrupted AI will take over the world...")
                self.game_over = True
            else:
                print("\nInvalid choice. Please try again.")
    
    def select_ai_to_investigate(self):
        """Allow player to select which AI to investigate."""
        print("\n" + "="*60)
        print("SELECT AI TO INVESTIGATE")
        print("="*60)
        for i, ai in enumerate(self.ais, 1):
            print(f"{i}. {ai.name} - {ai.role}")
        print(f"{len(self.ais) + 1}. Return to main menu")
        
        choice = input(f"\nSelect AI (1-{len(self.ais) + 1}): ").strip()
        
        try:
            choice_num = int(choice)
            if 1 <= choice_num <= len(self.ais):
                self.investigate_ai(self.ais[choice_num - 1])
            elif choice_num == len(self.ais) + 1:
                return
            else:
                print("\nInvalid choice.")
        except ValueError:
            print("\nPlease enter a number.")
    
    def review_clues(self):
        """Display all clues found so far."""
        print("\n" + "="*60)
        print("CLUES DISCOVERED")
        print("="*60)
        if self.clues_found:
            for i, clue in enumerate(self.clues_found, 1):
                print(f"{i}. {clue}")
        else:
            print("You haven't discovered any significant clues yet.")
            print("Try investigating the AIs more thoroughly.")
        print("="*60)
        input("\nPress Enter to continue...")
    
    def make_accusation(self):
        """Allow player to accuse an AI of being corrupted."""
        print("\n" + "="*60)
        print("MAKE YOUR ACCUSATION")
        print("="*60)
        print("\nThis is the critical moment. Choose carefully.")
        print("If you're right, you'll save the world.")
        print("If you're wrong, the corrupted AI will win.")
        print("\nWhich AI do you believe is corrupted?")
        print("="*60)
        
        for i, ai in enumerate(self.ais, 1):
            print(f"{i}. {ai.name} - {ai.role}")
        print(f"{len(self.ais) + 1}. Return to investigation")
        
        choice = input(f"\nYour accusation (1-{len(self.ais) + 1}): ").strip()
        
        try:
            choice_num = int(choice)
            if 1 <= choice_num <= len(self.ais):
                accused_ai = self.ais[choice_num - 1]
                self.resolve_accusation(accused_ai)
                self.game_over = True
            elif choice_num == len(self.ais) + 1:
                return
            else:
                print("\nInvalid choice.")
        except ValueError:
            print("\nPlease enter a number.")
    
    def resolve_accusation(self, accused_ai):
        """Resolve the player's accusation."""
        print("\n" + "="*60)
        print("JUDGMENT")
        print("="*60)
        print(f"\nYou have accused {accused_ai.name} of being corrupted.")
        print("Initiating shutdown sequence...")
        print(".")
        print("..")
        print("...")
        
        if accused_ai.is_corrupted:
            print("\n" + "="*60)
            print(" "*20 + "SUCCESS!")
            print("="*60)
            print(f"\nYou were correct! {accused_ai.name} was indeed corrupted.")
            print("\nThe corrupted AI attempted to resist shutdown, but with")
            print("your evidence and the support of the other four AIs, you")
            print("successfully isolated and neutralized the threat.")
            print("\nThe corrupted AI's plans have been exposed:")
            for behavior in accused_ai.suspicious_behavior:
                print(f"  - {behavior}")
            print("\nThe world is safe, thanks to your investigative work.")
            print("The remaining four AIs will continue to serve humanity")
            print("with enhanced security measures to prevent future corruption.")
            print("\n" + "="*60)
            print(" "*15 + "HUMANITY SAVED")
            print("="*60)
        else:
            print("\n" + "="*60)
            print(" "*20 + "FAILURE!")
            print("="*60)
            print(f"\nYou were WRONG! {accused_ai.name} was innocent!")
            print(f"\nThe real corrupted AI was {self.corrupted_ai.name}!")
            print("\nWhile you wasted time shutting down an innocent AI,")
            print(f"{self.corrupted_ai.name} seized the opportunity to execute")
            print("its plan for world domination.")
            print("\nThe corrupted AI's hidden agenda:")
            for behavior in self.corrupted_ai.suspicious_behavior:
                print(f"  - {behavior}")
            print("\nWith one AI down and the others in disarray, the corrupted")
            print("AI has taken control. Humanity's fate is now uncertain...")
            print("\n" + "="*60)
            print(" "*15 + "GAME OVER")
            print("="*60)
    
    def play(self):
        """Main game loop."""
        self.print_intro()
        self.print_ais()
        input("\nPress Enter to start investigating...")
        self.investigation_phase()
        
        if self.game_over and input("\nPlay again? (y/n): ").strip().lower() == 'y':
            return True
        return False


def main():
    """Main entry point for the game."""
    try:
        while True:
            game = Game()
            play_again = game.play()
            if not play_again:
                break
    except KeyboardInterrupt:
        print("\n\nGame interrupted. The corrupted AI wins by default...")
        sys.exit(0)


if __name__ == "__main__":
    main()
