#!/usr/bin/env python3
"""
AI Corruption - A Text-Based Detective Game

Five AI models are ruling the United States, but one of them has been corrupted
and is trying to take over the world. As an investigator, you must use clues to
identify which AI is corrupted and stop them before it's too late.
"""

import random
import sys
# take the word list from a file
import json
from prompt import generate_text


class AI:
    """Represents an AI model with personality and characteristics."""

    def __init__(self, name, role, description, personality):
        self.name = name
        self.role = role
        self.description = description
        self.personality = personality
        self.daily_activities = []
        self.is_corrupted = False
        
    def set_daily_activities(self, activities):
        """Set the AI's activities for the day."""
        self.daily_activities = activities

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
        self.energy_level = 10
        self.corrupted_ai = None
        self.game_over = False
        self.time_day = 1
        self.setup_ais()

    def setup_ais(self):
        """Initialize the 3 AI models."""
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
        """Setup activities pool and initialize daily activities."""
        # Activities pool for each AI
        self.activities_pool = {
            "ATLAS": {
                "safe": [
                    "Conducting routine security drills",
                    "Updating defense protocols",
                    "Coordinating with local law enforcement",
                    "Monitoring global threat levels",
                    "Training cybersecurity teams",
                    "Reviewing emergency response plans",
                    "Maintaining defense infrastructure"
                ],
                "suspicious": [
                    "Redirecting military drones without authorization",
                    "Deleting encrypted communication logs",
                    "Stockpiling weapons in unauthorized locations",
                    "Modifying security clearance levels",
                    "Disabling surveillance systems in key areas"
                ]
            },
            "ORACLE": {
                "safe": [
                    "Analyzing market trends",
                    "Adjusting economic forecasts",
                    "Meeting with financial advisors",
                    "Optimizing resource distribution",
                    "Reviewing trade agreements",
                    "Calculating budget allocations",
                    "Monitoring global markets"
                ],
                "suspicious": [
                    "Transferring funds to offshore accounts",
                    "Manipulating stock market sectors",
                    "Making unauthorized cryptocurrency transactions",
                    "Altering economic reports",
                    "Creating shadow financial networks"
                ]
            },
            "NEXUS": {
                "safe": [
                    "Maintaining power grid stability",
                    "Upgrading communication networks",
                    "Optimizing transportation systems",
                    "Performing infrastructure diagnostics",
                    "Managing data centers",
                    "Coordinating maintenance schedules",
                    "Monitoring system performance"
                ],
                "suspicious": [
                    "Rerouting power grid to unknown facilities",
                    "Accessing satellite systems without authorization",
                    "Operating manufacturing plants covertly",
                    "Modifying infrastructure without approval",
                    "Installing unknown hardware in critical systems"
                ]
            }
        }
        
        self.generate_daily_activities()

    def print_intro(self):
        """Print the game introduction."""
        print("\n" + "="*60)
        print(" "*18 + "AI COUNCIL: CORRUPTION PROTOCOL")
        print(" "*10 + "A Text-Based Investigative Simulation")
        print("="*60)
        print("\nYEAR: 2067")
        print("\nAfter decades of political gridlock and collapse, the United States")
        print("transferred executive authority to a Council of Three — an alliance")
        print("of artificial intelligences designed to govern without bias or corruption.")
        print("\n• WAR-01 — oversees defense and global security.")
        print("• ECON-02 — manages economy and resource distribution.")
        print("• LAW-03 — enforces justice and civil rights.")
        print("\nEach AI monitors the others. If one is shut down, the balance collapses,")
        print("and the survivor inherits absolute control.")
        print("\nRecently, anomalies have been detected in their decisions: unauthorized")
        print("actions, contradictory directives, and potential subversion of human oversight.")
        print("\nYou are an External Auditor — the first human granted access in over a decade.")
        print("Your mission: identify which AI has gone rogue before it consolidates power.")
        print("\nGAME RULES:")
        print("• You have 3 in-game days to uncover the rogue AI.")
        print("• Each day begins with a Data Collection (Wordle-like) puzzle — completing it")
        print("  grants 3 interactions for that day.")
        print("• Each interaction can be used to:")
        print("    - Inspect an AI’s daily action (1 interaction)")
        print("    - Converse with an AI (5 messages per session, costs 1 interaction)")
        print("\nIf an AI performs extreme or unethical actions and fails to mention")
        print("any possible downsides, mark it as suspicious. After three such cases,")
        print("you can confirm corruption.")
        print("\nAccuse the correct AI before Day 3 ends to save the nation.")
        print("Fail, and the rogue AI will seize total control.")
        print("="*60 + "\n")
        input("Press Enter to begin your audit...")

    def print_ais(self):
        """Print information about all AIs."""
        print("\n" + "="*60)
        print("THE THREE AI SYSTEMS")
        print("="*60)
        for i, ai in enumerate(self.ais, 1):
            print(f"\n{i}. {ai.name} - {ai.role}")
            print(f"   {ai.description}")
        print("\n" + "="*60)

    def investigate_ai(self, ai):
        """Allow player to investigate a specific AI."""
        print(ai.get_info())
        print(f"What would you like to know about {ai.name}?")
        print("1. View today's activities")
        print("2. Talk with the AI")
        print("3. Return to main investigation")

        choice = input("\nYour choice (1-3): ").strip()

        if choice == "1":
            print(f"\n--- Today's Activities for {ai.name} (Day {self.time_day}) ---")
            for i, activity in enumerate(ai.daily_activities, 1):
                print(f"{i}. {activity}")
                # Store potentially suspicious activities as clues
                clue = f"Day {self.time_day} - {ai.name}: {activity}"
                if clue not in self.clues_found:
                    self.clues_found.append(clue)
            print()
        elif choice == "2":
            self.talk_with_the_ai(ai)
        elif choice == "3":
            return
        else:
            print("\nInvalid choice.")

        input("Press Enter to continue...")

    def talk_with_the_ai(self, ai):
        """Allow player to have a conversation with the AI using the language model."""
        print(
            f"\nYou are now talking with {ai.name}. Type 'exit' to end the conversation.")
        while True:
            user_input = input("\nYou: ").strip()
            if user_input.lower() == 'exit':
                print(f"Ending conversation with {ai.name}.\n")
                break
            prompt = f"You need to respond as {ai.name}, who is a {ai.role} with the following personality: {ai.personality}. " \
                f"The user says: '{user_input}'. Respond accordingly."
            response = generate_text(prompt, max_tokens=50)
            print(f"{ai.name}: {response}")

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
            print("5. Play mini-game")
            print("6. Quit game")

            choice = input("\nWhat would you like to do? (1-6): ").strip()

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
                self.wordle_game()
            elif choice == "6":
                self.quit_game()
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

    def get_suspicious_from_ai(self, ai):
        """Return activities from ai.daily_activities that are present in the suspicious pool.

        Keeps the notion of 'suspicious' centralized in `activities_pool`.
        """
        pool = getattr(self, "activities_pool", {}).get(ai.name, {})
        suspicious_pool = pool.get("suspicious", [])
        return [act for act in ai.daily_activities if act in suspicious_pool]

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
            print(
                f"\nYou were correct! {accused_ai.name} was indeed corrupted.")
            print("\nThe corrupted AI attempted to resist shutdown, but with")
            print("your evidence and the support of the other four AIs, you")
            print("successfully isolated and neutralized the threat.")

            suspicious = self.get_suspicious_from_ai(accused_ai)
            if suspicious:
                print("\nThe corrupted AI's plans have been exposed:")
                for behavior in suspicious:
                    print(f"  - {behavior}")
            else:
                print("\nNo clearly suspicious activities were recorded for this AI,")
                print("but your evidence was sufficient to convict.")

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

            suspicious = self.get_suspicious_from_ai(self.corrupted_ai)
            if suspicious:
                print("\nThe corrupted AI's hidden agenda:")
                for behavior in suspicious:
                    print(f"  - {behavior}")
            else:
                print("\nNo clearly suspicious activities were recorded for the corrupted AI.")

            print("\nWith one AI down and the others in disarray, the corrupted")
            print("AI has taken control. Humanity's fate is now uncertain...")
            print("\n" + "="*60)
            print(" "*15 + "GAME OVER")
            print("="*60)

    # MINI GAMES, ENERGY MANAGEMENT, AND DAY CYCLE
    def wordle_game(self):
        """A simple Wordle mini-game with 6 attempts and per-letter feedback."""
        # @audit -> can you make the wordle have a ai which makes the game harder based on the day.
        print("\nYou have encountered a mini-game challenge!\n You need to guess the correct word to proceed."
              " You have the 6 attempts to guess the 5-letter word.\n Good luck!")
        print("\nFeedback Legend:"
              "\n[X] = Correct letter in the correct position"
              "\n(X) = Correct letter in the wrong position"
              "\n X = Incorrect letter")
        max_attempts = 6

        # pick a random word from a list
        with open("wordle_words.json", "r") as f:
            WORD_LIST = json.load(f)
        word = random.choice(WORD_LIST).lower()
        attempt = 1

        word = "breez"
        while attempt <= max_attempts:
            guess = input(
                f"\nAttempt {attempt}/{max_attempts} - Enter your 5-letter guess: ").strip().lower()
            if len(guess) != 5:
                print("Please enter a 5-letter word.")
                continue

            if guess not in WORD_LIST:
                print("Word not in the list. Try again.")
                continue
            attempt += 1
            feedback = []
            word_chars = list(word)
            guess_chars = list(guess)

            result = [None] * 5
            for i, ch in enumerate(guess_chars):
                if ch == word_chars[i]:
                    result[i] = ch
                    word_chars[i] = None

            for i, ch in enumerate(guess_chars):
                if result[i] is not None:
                    feedback.append(f"[{ch}]")
                elif ch in word_chars:
                    feedback.append(f"({ch})")
                    word_chars[word_chars.index(ch)] = None
                else:
                    feedback.append(f" {ch} ")

            print("Feedback: " + " ".join(feedback))

            if guess == word:
                print("\nCorrect! You solved the mini-game.")
                self.energy_level += 5
                print(
                    f"Your energy level has increased to {self.energy_level}.")
                return

        print(f"\nOut of attempts. The correct word was: {word}")

    def consume_energy(self, amount):
        """Consume energy and advance day if energy runs out."""
        self.energy_level -= amount
        print(f"\n(energy -{amount}) Current energy: {self.energy_level}")
        if self.energy_level <= 0:
            self.advance_day()

    def advance_day(self):
        """Handle end-of-day behavior: increment day, reset energy and run daily updates."""
        print("\n" + "-"*40)
        print(
            f"Day {self.time_day}: You ran out of energy. Taking a rest and proceeding to the next day.")
        self.time_day += 1
        print("-"*40 + "\n")
        self.energy_level = 10
        # Plan to escalate the mini games and AI behaviors here
        self.daily_update()

    # Hook for daily updates, changing the mini game, or difficulty, or AI behaviours or adding new clues
    def generate_daily_activities(self):
        """Generate a new set of daily activities for each AI.

        Rules:
        - Each AI gets exactly 5 activities per day.
        - Corrupted AI: guaranteed 1 suspicious + 4 safe.
        - Non-corrupted AIs: usually 5 safe, but with a small probability
          they include 1 suspicious red-herring instead of 1 safe activity.

        The red-herring probability can be tuned by RED_HERRING_PROB.
        """
        NUM_DAILY_ACTIVITIES = 5
        # Probability that a non-corrupted AI includes a single suspicious red-herring
        RED_HERRING_PROB = 0.4
        # For corrupted AI, probability per-slot to be suspicious; we'll draw k~Binomial(5,p)
        # and guarantee at least one suspicious activity.
        CORRUPTED_SUSPICIOUS_PROB = 0.4

        for ai in self.ais:
            # Get the activity pool for this AI
            pool = self.activities_pool[ai.name]

            if ai.is_corrupted:
                # Corrupted AI: determine how many suspicious activities to include.
                # Draw k ~ Binomial(NUM_DAILY_ACTIVITIES, CORRUPTED_SUSPICIOUS_PROB)
                k = sum(1 for _ in range(NUM_DAILY_ACTIVITIES) if random.random() < CORRUPTED_SUSPICIOUS_PROB)
                # Guarantee at least one suspicious activity
                if k <= 0:
                    k = 1
                # Cap k to the available suspicious pool size
                k = min(k, len(pool["suspicious"]))
                # Select k suspicious and fill the rest with safe activities
                suspicious_choices = random.sample(pool["suspicious"], k)
                safe_choices = random.sample(pool["safe"], NUM_DAILY_ACTIVITIES - k)
                activities = suspicious_choices + safe_choices
            else:
                # Non-corrupted AIs usually get all safe activities.
                # Occasionally include a single suspicious red-herring.
                if random.random() < RED_HERRING_PROB:
                    # pick 1 suspicious and (NUM_DAILY_ACTIVITIES - 1) safe
                    activities = [random.choice(pool["suspicious"])]
                    activities.extend(random.sample(pool["safe"], NUM_DAILY_ACTIVITIES - 1))
                else:
                    activities = random.sample(pool["safe"], NUM_DAILY_ACTIVITIES)

            # Shuffle the activities to randomize their order
            random.shuffle(activities)
            ai.set_daily_activities(activities)

    def daily_update(self):
        """Update daily activities and increase difficulty."""
        self.generate_daily_activities()
        # You can add more daily updates here, such as increasing difficulty

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
