# AI Corruption - Text-Based Detective Game

Challenge after Block A, text-based game with Python

## Game Description

In the year 2045, the United States is governed by five advanced AI systems, each responsible for a critical aspect of the nation. Recently, concerning anomalies have been detected across multiple sectors. Intelligence suggests that one of the five AIs has been corrupted and is attempting to seize control of the entire world.

You are a special investigator tasked with identifying the corrupted AI and shutting it down before it's too late.

## The Five AI Systems

1. **ATLAS** - Defense & Security Coordinator
   - Manages military operations and national security
   
2. **ORACLE** - Economic & Trade Director
   - Oversees financial markets and economic policy
   
3. **NEXUS** - Infrastructure & Technology Manager
   - Controls power grids, communications, and transport
   
4. **EDEN** - Healthcare & Environment Guardian
   - Manages public health and environmental protection
   
5. **CIPHER** - Intelligence & Information Overseer
   - Handles data analysis, surveillance, and intelligence

## How to Play

### Requirements
- Python 3.6 or higher

### Running the Game

```bash
python3 game.py
```

or

```bash
chmod +x game.py
./game.py
```

### Gameplay

1. **Investigation Phase**: Gather clues by investigating each AI
   - View all AI systems and their roles
   - Investigate specific AIs to uncover suspicious activities
   - Ask each AI about their alibi
   - Review clues you've discovered

2. **Making Your Accusation**: Once you've gathered enough evidence
   - Select the AI you believe is corrupted
   - If correct, you save the world!
   - If wrong, the corrupted AI takes over...

### Tips

- Each AI will have some suspicious behavior, but the corrupted AI's activities will be more severe
- Pay attention to the patterns and severity of suspicious activities
- The corrupted AI is randomly selected each game, so replay value is high
- Take your time to investigate all AIs before making your accusation

## Features

- 5 unique AI characters with distinct personalities and roles
- Randomly selected corrupted AI each playthrough
- Clue gathering and investigation mechanics
- Win/lose conditions based on your accusation
- Replayability with different scenarios each time

## Game Over Conditions

- **Victory**: Correctly identify and shut down the corrupted AI
- **Defeat**: Accuse an innocent AI, allowing the real threat to take over
- **Forfeit**: Quit the game without making an accusation

Good luck, investigator. The fate of humanity rests in your hands!
