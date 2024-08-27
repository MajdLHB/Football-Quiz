import random
import difflib
import os
import json
from tkinter import Tk, StringVar, Label, Entry, Button, messagebox
from tkinter import ttk

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the JSON file
HIGH_SCORE_FILE = os.path.join(current_dir, "high_score.json")

class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game 2.0")
        self.root.configure(bg='#1E1E1E')  # Dark background color
        self.score = 0
        self.tries = 0
        self.players = [
    ["Lionel Messi", "Argentinian footballer", "Plays for Inter Miami", "7-time Ballon d'Or winner", 36],
    ["Cristiano Ronaldo", "Portuguese footballer", "Plays for Al Nassr", "5-time Ballon d'Or winner", 39],
    ["Kylian Mbappe", "French footballer", "Plays for PSG", "2018 World Cup winner", 25],
    ["Erling Haaland", "Norwegian footballer", "Plays for Manchester City", "Top scorer of the Premier League 2023-2024", 24],
    ["Kevin De Bruyne", "Belgian footballer", "Plays for Manchester City", "Considered one of the best midfielders", 32],
    ["Karim Benzema", "French footballer", "Plays for Al-Ittihad", "2022 Ballon d'Or winner", 36],
    ["Robert Lewandowski", "Polish footballer", "Plays for FC Barcelona", "Best FIFA Men's Player 2020", 36],
    ["Neymar Jr", "Brazilian footballer", "Plays for Al Hilal", "Skillful winger and playmaker", 32],
    ["Harry Kane", "English footballer", "Plays for Bayern Munich", "Top scorer in Tottenham's history", 30],
    ["Mohamed Salah", "Egyptian footballer", "Plays for Liverpool", "Premier League Golden Boot winner", 32],
    ["Sadio Mane", "Senegalese footballer", "Plays for Al-Nassr", "2022 African Player of the Year", 32],
    ["Virgil van Dijk", "Dutch footballer", "Plays for Liverpool", "Regarded as one of the best defenders", 33],
    ["Trent Alexander-Arnold", "English footballer", "Plays for Liverpool", "Known for his crossing ability", 25],
    ["Bruno Fernandes", "Portuguese footballer", "Plays for Manchester United", "Creative playmaker", 29],
    ["Marcus Rashford", "English footballer", "Plays for Manchester United", "Known for his speed and finishing", 26],
    ["Raheem Sterling", "English footballer", "Plays for Chelsea", "Pacy winger", 29],
    ["Phil Foden", "English footballer", "Plays for Manchester City", "Highly talented young midfielder", 24],
    ["Mason Mount", "English footballer", "Plays for Manchester United", "Energetic and versatile midfielder", 25],
    ["Kai Havertz", "German footballer", "Plays for Arsenal", "Scored the winner in the 2021 Champions League Final", 25],
    ["Bukayo Saka", "English footballer", "Plays for Arsenal", "Promising young winger", 22],
    ["Gabriel Jesus", "Brazilian footballer", "Plays for Arsenal", "Former Manchester City forward", 27],
    ["Joao Cancelo", "Portuguese footballer", "Plays for Barcelona", "Versatile full-back", 30],
    ["Ilkay Gundogan", "German footballer", "Plays for Barcelona", "Instrumental in Manchester City's treble", 33],
    ["Rodri Hernandez", "Spanish footballer", "Plays for Manchester City", "Key defensive midfielder", 28],
    ["Ruben Dias", "Portuguese footballer", "Plays for Manchester City", "Solid center-back", 27],
    ["Bernardo Silva", "Portuguese footballer", "Plays for Manchester City", "Skilful attacking midfielder", 29],
    ["Jack Grealish", "English footballer", "Plays for Manchester City", "Known for his dribbling", 28],
    ["Ederson Moraes", "Brazilian footballer", "Plays for Manchester City", "Excellent ball-playing goalkeeper", 31],
    ["Allison Becker", "Brazilian footballer", "Plays for Liverpool", "Top-class goalkeeper", 31],
    ["Casemiro Santos", "Brazilian footballer", "Plays for Manchester United", "Experienced defensive midfielder", 32],
    ["Raphael Varane", "French footballer", "Plays for Manchester United", "World Cup winner", 31],
    ["Lisandro Martinez", "Argentinian footballer", "Plays for Manchester United", "Known as 'The Butcher'", 26],
    ["David de Gea", "Spanish footballer", "Free agent", "Former Manchester United goalkeeper", 33],
    ["Jadon Sancho", "English footballer", "Plays for Manchester United", "Skilful winger", 24],
    ["Christian Eriksen", "Danish footballer", "Plays for Manchester United", "Midfield playmaker", 32],
    ["Thiago Alcantara", "Spanish footballer", "Plays for Liverpool", "Masterful in possession", 33],
    ["Fabinho Tavares", "Brazilian footballer", "Plays for Al-Ittihad", "Defensive stalwart", 30],
    ["Andrew Robertson", "Scottish footballer", "Plays for Liverpool", "Best left-back in the world", 30],
    ["Diogo Jota", "Portuguese footballer", "Plays for Liverpool", "Dynamic forward", 27],
    ["Darwin Nunez", "Uruguayan footballer", "Plays for Liverpool", "Fast and powerful striker", 25],
    ["Joao Felix", "Portuguese footballer", "Plays for Barcelona", "Young attacking talent", 24],
    ["Martin Odegaard", "Norwegian footballer", "Plays for Arsenal", "Arsenal captain", 25],
    ["Declan Rice", "English footballer", "Plays for Arsenal", "Former West Ham captain", 25],
    ["Reece James", "English footballer", "Plays for Chelsea", "Dynamic right-back", 24],
    ["Enzo Fernandez", "Argentinian footballer", "Plays for Chelsea", "World Cup 2022 winner", 23],
    ["Christopher Nkunku", "French footballer", "Plays for Chelsea", "Former Bundesliga top scorer", 26],
    ["Thiago Silva", "Brazilian footballer", "Plays for Chelsea", "Veteran center-back", 39],
    ["Kalidou Koulibaly", "Senegalese footballer", "Plays for Al Hilal", "Former Napoli star defender", 33],
    ["N'Golo Kante", "French footballer", "Plays for Al-Ittihad", "Workhorse midfielder", 33],
    ["Hakim Ziyech", "Moroccan footballer", "Plays for Galatasaray", "Creative winger", 31],
    ["Pierre-Emerick Aubameyang", "Gabonese footballer", "Plays for Marseille", "Former Arsenal striker", 35],
    ["Riyad Mahrez", "Algerian footballer", "Plays for Al-Ahli", "Skillful winger", 33],
    ["James Maddison", "English footballer", "Plays for Tottenham Hotspur", "Creative midfielder", 27],
    ["Heung-Min Son", "South Korean footballer", "Plays for Tottenham Hotspur", "Prolific forward", 32],
    ["Jordan Pickford", "English footballer", "Plays for Everton", "England's number one goalkeeper", 30],
    ["Dominic Calvert-Lewin", "English footballer", "Plays for Everton", "Aerial threat", 27],
    ["Lucas Digne", "French footballer", "Plays for Aston Villa", "Reliable left-back", 30],
    ["Ollie Watkins", "English footballer", "Plays for Aston Villa", "Prolific striker", 28],
    ["Emiliano Martinez", "Argentinian footballer", "Plays for Aston Villa", "World Cup-winning goalkeeper", 32],
    ["John Stones", "English footballer", "Plays for Manchester City", "Versatile defender", 30],
    ["Aaron Ramsdale", "English footballer", "Plays for Arsenal", "Promising goalkeeper", 26],
    ["William Saliba", "French footballer", "Plays for Arsenal", "Rising star defender", 23],
    ["Gabriel Magalhaes", "Brazilian footballer", "Plays for Arsenal", "Solid center-back", 26],
    ["James Ward-Prowse", "English footballer", "Plays for West Ham United", "Set-piece specialist", 29],
    ["Jarrod Bowen", "English footballer", "Plays for West Ham United", "Winger with a good scoring record", 27],
    ["Lucas Paqueta", "Brazilian footballer", "Plays for West Ham United", "Creative midfielder", 26],
    ["Kurt Zouma", "French footballer", "Plays for West Ham United", "Strong center-back", 29],
    ["Alphonse Areola", "French footballer", "Plays for West Ham United", "Backup goalkeeper", 31],
    ["Callum Wilson", "English footballer", "Plays for Newcastle United", "Clinical striker", 32],
    ["Bruno Guimaraes", "Brazilian footballer", "Plays for Newcastle United", "Key midfielder", 26],
    ["Sven Botman", "Dutch footballer", "Plays for Newcastle United", "Tall center-back", 24],
    ["Miguel Almiron", "Paraguayan footballer", "Plays for Newcastle United", "Dynamic winger", 30],
    ["Alexander Isak", "Swedish footballer", "Plays for Newcastle United", "Tall and skillful forward", 25],
    ["Dan Burn", "English footballer", "Plays for Newcastle United", "Versatile defender", 32],
    ["Kieran Trippier", "English footballer", "Plays for Newcastle United", "Set-piece specialist", 34],
    ["Nick Pope", "English footballer", "Plays for Newcastle United", "Commanding goalkeeper", 32],
    ["Jamaal Lascelles", "English footballer", "Plays for Newcastle United", "Club captain", 30],
    ["Alexander Lacazette", "French footballer", "Plays for Lyon", "Former Arsenal striker", 32],
    ["Matteo Guendouzi", "French footballer", "Plays for Lazio", "Dynamic midfielder", 25],
    ["Memphis Depay", "Dutch footballer", "Plays for Atletico Madrid", "Skilful forward", 30],
    ["Rodrigo De Paul", "Argentinian footballer", "Plays for Atletico Madrid", "Workhorse midfielder", 30],
    ["Antoine Griezmann", "French footballer", "Plays for Atletico Madrid", "Versatile forward", 33],
    ["Angel Correa", "Argentinian footballer", "Plays for Atletico Madrid", "Tricky winger", 29],
    ["Jan Oblak", "Slovenian footballer", "Plays for Atletico Madrid", "One of the best goalkeepers", 31],
    ["Thibaut Courtois", "Belgian footballer", "Plays for Real Madrid", "Top goalkeeper", 32],
    ["Vinicius Junior", "Brazilian footballer", "Plays for Real Madrid", "Skillful winger", 24],
    ["Rodrygo Goes", "Brazilian footballer", "Plays for Real Madrid", "Promising young talent", 23],
    ["Federico Valverde", "Uruguayan footballer", "Plays for Real Madrid", "Versatile midfielder", 26],
    ["Eduardo Camavinga", "French footballer", "Plays for Real Madrid", "Young midfield star", 21],
    ["Aurelien Tchouameni", "French footballer", "Plays for Real Madrid", "Rising midfield talent", 24],
    ["Luka Modric", "Croatian footballer", "Plays for Real Madrid", "Ballon d'Or winner", 38],
    ["Toni Kroos", "German footballer", "Plays for Real Madrid", "Midfield maestro", 34],
    ["David Alaba", "Austrian footballer", "Plays for Real Madrid", "Versatile defender", 32],
    ["Dani Carvajal", "Spanish footballer", "Plays for Real Madrid", "Experienced right-back", 32],
    ["Nacho Fernandez", "Spanish footballer", "Plays for Real Madrid", "Reliable defender", 34],
    ["Joselu Mato", "Spanish footballer", "Plays for Real Madrid", "Prolific striker", 34],
    ["Robert Sanchez", "Spanish footballer", "Plays for Chelsea", "Tall goalkeeper", 26],
    ["Alvaro Morata", "Spanish footballer", "Plays for Atletico Madrid", "Experienced striker", 31],
    ["Eden Hazard", "Belgian footballer", "Retired", "Former Chelsea and Real Madrid star", 33],
    ["Sergio Ramos", "Spanish footballer", "Plays for Sevilla", "Legendary defender", 38],
    ["Gerard Pique", "Spanish footballer", "Retired", "Former Barcelona star defender", 37],
    ["Xavi Hernandez", "Spanish footballer", "Retired", "Barcelona legend and coach", 44],
    ["Cesc Fabregas", "Spanish footballer", "Retired", "Ex-Arsenal and Chelsea playmaker", 37],
    ["Luis Suarez", "Uruguayan footballer", "Plays for Gremio", "Prolific former Barcelona striker", 37],
    ["Jordi Alba", "Spanish footballer", "Plays for Inter Miami", "Former Barcelona left-back", 35],
    ["Andres Iniesta", "Spanish footballer", "Plays for Emirates Club", "Former Barcelona midfield genius", 40],
    ["Iago Aspas", "Spanish footballer", "Plays for Celta Vigo", "Reliable goal scorer", 36],
    ["Unai Simon", "Spanish footballer", "Plays for Athletic Bilbao", "Spanish national team goalkeeper", 26],
    ["Inaki Williams", "Spanish footballer", "Plays for Athletic Bilbao", "Pacy forward", 30],
    ["Aitor Fernandez", "Spanish footballer", "Plays for Osasuna", "Solid goalkeeper", 32],
    ["David Silva", "Spanish footballer", "Retired", "Former Manchester City and Real Sociedad playmaker", 38],
    ["Sergio Busquets", "Spanish footballer", "Plays for Inter Miami", "Legendary Barcelona midfielder", 36],
    ["Hugo Lloris", "French footballer", "Plays for Tottenham Hotspur", "World Cup-winning goalkeeper", 37],
    ["Keylor Navas", "Costa Rican footballer", "Plays for Nottingham Forest", "Former Real Madrid goalkeeper", 37],
    ["Manuel Neuer", "German footballer", "Plays for Bayern Munich", "Sweeper-keeper", 38],
    ["Leon Goretzka", "German footballer", "Plays for Bayern Munich", "Box-to-box midfielder", 29],
    ["Joshua Kimmich", "German footballer", "Plays for Bayern Munich", "Versatile midfielder", 29],
    ["Jamal Musiala", "German footballer", "Plays for Bayern Munich", "Young attacking talent", 21],
    ["Thomas Muller", "German footballer", "Plays for Bayern Munich", "Experienced forward", 34],
    ["Leroy Sane", "German footballer", "Plays for Bayern Munich", "Pacy winger", 28],
    ["Kingsley Coman", "French footballer", "Plays for Bayern Munich", "Scored the winning goal in the 2020 Champions League Final", 28],
    ["Serge Gnabry", "German footballer", "Plays for Bayern Munich", "Former Arsenal winger", 29],
    ["Harry Maguire", "English footballer", "Plays for Manchester United", "England national team defender", 31],
    ["Marcus Thuram", "French footballer", "Plays for Inter Milan", "Son of French legend Lilian Thuram", 26],
    ["Romelu Lukaku", "Belgian footballer", "Plays for Roma", "Powerful striker", 31],
    ["Denzel Dumfries", "Dutch footballer", "Plays for Inter Milan", "Dynamic full-back", 28],
    ["Stefan de Vrij", "Dutch footballer", "Plays for Inter Milan", "Solid center-back", 32],
    ["Milan Skriniar", "Slovakian footballer", "Plays for PSG", "Commanding defender", 29],
    ["Lautaro Martinez", "Argentinian footballer", "Plays for Inter Milan", "Top scorer in Serie A", 26],
    ["Paul Pogba", "French footballer", "Plays for Juventus", "World Cup-winning midfielder", 31],
    ["Federico Chiesa", "Italian footballer", "Plays for Juventus", "Skillful winger", 26],
    ["Dusan Vlahovic", "Serbian footballer", "Plays for Juventus", "Prolific striker", 24],
    ["Alvaro Morata", "Spanish footballer", "Plays for Atletico Madrid", "Experienced forward", 31],
    ["Arkadiusz Milik", "Polish footballer", "Plays for Juventus", "Former Napoli forward", 30],
    ["Leandro Paredes", "Argentinian footballer", "Plays for Roma", "Former PSG midfielder", 30],
    ["Gianluigi Donnarumma", "Italian footballer", "Plays for PSG", "Italy's national team goalkeeper", 25],
    ["Marquinhos Correa", "Brazilian footballer", "Plays for PSG", "Club captain", 29],
    ["Achraf Hakimi", "Moroccan footballer", "Plays for PSG", "Speedy full-back", 25],
    ["Marco Verratti", "Italian footballer", "Plays for Al-Arabi", "Midfield maestro", 31],
    ["Kepa Arrizabalaga", "Spanish footballer", "Plays for Real Madrid", "Tall goalkeeper", 29],
    ["Leonardo Bonucci", "Italian footballer", "Plays for Union Berlin", "Experienced defender", 37],
    ["Kalvin Phillips", "English footballer", "Plays for Manchester City", "Former Leeds United midfielder", 28],
    ["Richarlison Andrade", "Brazilian footballer", "Plays for Tottenham Hotspur", "Versatile forward", 27],
    ["Ivan Perisic", "Croatian footballer", "Plays for Tottenham Hotspur", "Veteran winger", 35],
    ["Emerson Royal", "Brazilian footballer", "Plays for Tottenham Hotspur", "Energetic full-back", 25],
    ["James Ward-Prowse", "English footballer", "Plays for West Ham United", "Free-kick specialist", 29],
    ["Lucas Paqueta", "Brazilian footballer", "Plays for West Ham United", "Creative midfielder", 26],
    ["Kurt Zouma", "French footballer", "Plays for West Ham United", "Strong center-back", 29],
    ["Declan Rice", "English footballer", "Plays for Arsenal", "Box-to-box midfielder", 25],
    ["Gabriel Jesus", "Brazilian footballer", "Plays for Arsenal", "Skillful striker", 27],
    ["Kai Havertz", "German footballer", "Plays for Arsenal", "Former Chelsea attacker", 25],
    ["Jorginho Frello", "Italian footballer", "Plays for Arsenal", "Former Chelsea midfielder", 32],
    ["Martin Odegaard", "Norwegian footballer", "Plays for Arsenal", "Club captain", 25],
    ["William Saliba", "French footballer", "Plays for Arsenal", "Strong center-back", 23],
    ["Ben White", "English footballer", "Plays for Arsenal", "Versatile defender", 26],
    ["Aaron Ramsdale", "English footballer", "Plays for Arsenal", "Young goalkeeper", 25],
    ["Bukayo Saka", "English footballer", "Plays for Arsenal", "Young talent", 22],
    ["Eddie Nketiah", "English footballer", "Plays for Arsenal", "Goal poacher", 25],
    ["Reece James", "English footballer", "Plays for Chelsea", "Skilful right-back", 24],
    ["Enzo Fernandez", "Argentinian footballer", "Plays for Chelsea", "Record transfer signing", 23],
    ["Thiago Silva", "Brazilian footballer", "Plays for Chelsea", "Veteran defender", 39],
    ["Raheem Sterling", "English footballer", "Plays for Chelsea", "Pacy winger", 29],
    ["Christopher Nkunku", "French footballer", "Plays for Chelsea", "Versatile attacker", 26],
    ["Conor Gallagher", "English footballer", "Plays for Chelsea", "Young midfielder", 24],
    ["Nicolas Jackson", "Senegalese footballer", "Plays for Chelsea", "Promising forward", 23],
    ["Marc Cucurella", "Spanish footballer", "Plays for Chelsea", "Energetic left-back", 26],
    ["Levi Colwill", "English footballer", "Plays for Chelsea", "Promising young center-back", 21],
    ["Moises Caicedo", "Ecuadorian footballer", "Plays for Chelsea", "Record transfer signing", 22],
    ["Malo Gusto", "French footballer", "Plays for Chelsea", "Promising right-back", 21],
    ["Mykhailo Mudryk", "Ukrainian footballer", "Plays for Chelsea", "Pacy winger", 23],
    ["Romeo Lavia", "Belgian footballer", "Plays for Chelsea", "Young midfielder", 20],
    ["Robert Sanchez", "Spanish footballer", "Plays for Chelsea", "Tall goalkeeper", 26],
    ["Gabriel Martinelli", "Brazilian footballer", "Plays for Arsenal", "Young winger", 23],
    ["Takehiro Tomiyasu", "Japanese footballer", "Plays for Arsenal", "Versatile defender", 25],
    ["Mohamed Elneny", "Egyptian footballer", "Plays for Arsenal", "Experienced midfielder", 32],
    ["Fabio Vieira", "Portuguese footballer", "Plays for Arsenal", "Creative midfielder", 24],
    ["Leandro Trossard", "Belgian footballer", "Plays for Arsenal", "Versatile attacker", 29],
    ["James Maddison", "English footballer", "Plays for Tottenham Hotspur", "Creative midfielder", 27],
    ["Heung-Min Son", "South Korean footballer", "Plays for Tottenham Hotspur", "Star forward", 32],
    ["Yves Bissouma", "Malian footballer", "Plays for Tottenham Hotspur", "Tough-tackling midfielder", 27],
    ["Pape Sarr", "Senegalese footballer", "Plays for Tottenham Hotspur", "Young midfielder", 21],
    ["Oliver Skipp", "English footballer", "Plays for Tottenham Hotspur", "Energetic midfielder", 23],
    ["Moussa Diaby", "French footballer", "Plays for Aston Villa", "Pacy winger", 25],
    ["Ollie Watkins", "English footballer", "Plays for Aston Villa", "Prolific striker", 28],
    ["Tyrone Mings", "English footballer", "Plays for Aston Villa", "Tall center-back", 31],
    ["Douglas Luiz", "Brazilian footballer", "Plays for Aston Villa", "Strong midfielder", 26],
    ["Lucas Digne", "French footballer", "Plays for Aston Villa", "Experienced left-back", 30],
    ["John McGinn", "Scottish footballer", "Plays for Aston Villa", "Industrious midfielder", 29],
    ["Emiliano Martinez", "Argentinian footballer", "Plays for Aston Villa", "World Cup-winning goalkeeper", 32],
    ["Luka Jovic", "Serbian footballer", "Plays for Fiorentina", "Former Real Madrid striker", 26],
    ["Ruben Neves", "Portuguese footballer", "Plays for Al Hilal", "Former Wolves midfielder", 27],
    ["Aleksandar Mitrovic", "Serbian footballer", "Plays for Al Hilal", "Prolific goal scorer", 29],
    ["Sergio Reguilon", "Spanish footballer", "Plays for Manchester United", "Left-back on loan from Tottenham", 27],
    ["Dean Henderson", "English footballer", "Plays for Crystal Palace", "Former Manchester United goalkeeper", 26],
    ["Sam Johnstone", "English footballer", "Plays for Crystal Palace", "Reliable goalkeeper", 31],
    ["Joachim Andersen", "Danish footballer", "Plays for Crystal Palace", "Tall center-back", 27],
    ["Eberechi Eze", "English footballer", "Plays for Crystal Palace", "Skillful midfielder", 26],
    ["Michael Olise", "French footballer", "Plays for Crystal Palace", "Pacy winger", 22],
    ["Wilfried Zaha", "Ivorian footballer", "Plays for Galatasaray", "Skillful forward", 31],
    ["Jordan Ayew", "Ghanaian footballer", "Plays for Crystal Palace", "Experienced forward", 32],
    ["Abdoulaye Doucoure", "Malian footballer", "Plays for Everton", "Tough-tackling midfielder", 31],
    ["Amadou Onana", "Belgian footballer", "Plays for Everton", "Tall midfielder", 23],
    ["Dwight McNeil", "English footballer", "Plays for Everton", "Pacy winger", 24],
    ["Dominic Calvert-Lewin", "English footballer", "Plays for Everton", "Tall striker", 27],
    ["Jordan Pickford", "English footballer", "Plays for Everton", "England national team goalkeeper", 30],
    ["Conor Coady", "English footballer", "Plays for Leicester City", "Strong center-back", 31],
    ["Harry Souttar", "Australian footballer", "Plays for Leicester City", "Tall defender", 25],
    ["Ricardo Pereira", "Portuguese footballer", "Plays for Leicester City", "Attacking full-back", 30],
    ["Jamie Vardy", "English footballer", "Plays for Leicester City", "Prolific striker", 37],
    ["Harvey Barnes", "English footballer", "Plays for Newcastle United", "Pacy winger", 26],
    ["James Tarkowski", "English footballer", "Plays for Everton", "Strong defender", 31],
    ["Wout Weghorst", "Dutch footballer", "Plays for Hoffenheim", "Tall striker", 31],
    ["Pablo Sarabia", "Spanish footballer", "Plays for Wolverhampton Wanderers", "Versatile attacker", 32],
    ["Goncalo Guedes", "Portuguese footballer", "Plays for Benfica", "Skillful winger", 27],
    ["Joao Felix", "Portuguese footballer", "Plays for Barcelona", "Creative forward", 24],
    ["Joao Cancelo", "Portuguese footballer", "Plays for Barcelona", "Attacking full-back", 30],
    ["Andre Silva", "Portuguese footballer", "Plays for Real Sociedad", "Prolific striker", 28],
    ["Martin Zubimendi", "Spanish footballer", "Plays for Real Sociedad", "Defensive midfielder", 25],
    ["Alexander Sorloth", "Norwegian footballer", "Plays for Villarreal", "Tall striker", 28],
    ["Lamine Yamal", "Spanish footballer", "Plays for Barcelona", "Promising young talent", 17],
    ["Ferran Torres", "Spanish footballer", "Plays for Barcelona", "Versatile forward", 24],
    ["Ousmane Dembele", "French footballer", "Plays for Paris Saint-Germain", "Skillful winger", 27],
    ["Achraf Hakimi", "Moroccan footballer", "Plays for Paris Saint-Germain", "Attacking full-back", 25],
    ["Marco Verratti", "Italian footballer", "Plays for Al-Arabi", "Experienced midfielder", 31],
    ["Sergio Ramos", "Spanish footballer", "Plays for Sevilla", "Veteran defender", 38],
    ["Nicolas Pepe", "Ivorian footballer", "Plays for Trabzonspor", "Pacy winger", 29],
    ["Jean-Clair Todibo", "French footballer", "Plays for Nice", "Tall center-back", 24],
    ["Hugo Lloris", "French footballer", "Plays for Nice", "Veteran goalkeeper", 37],
    ["Wesley Fofana", "French footballer", "Plays for Chelsea", "Tall center-back", 23],
    ["Kepa Arrizabalaga", "Spanish footballer", "Plays for Real Madrid", "On loan from Chelsea", 29],
    ["Marc-Andre ter Stegen", "German footballer", "Plays for Barcelona", "Experienced goalkeeper", 32],
    ["Riyad Mahrez", "Algerian footballer", "Plays for Al-Ahli", "Skillful winger", 33],
    ["Franck Kessie", "Ivorian footballer", "Plays for Al-Ahli", "Strong midfielder", 28],
    ["Karim Benzema", "French footballer", "Plays for Al-Ittihad", "Ballon d'Or-winning striker", 36],
    ["N'Golo Kante", "French footballer", "Plays for Al-Ittihad", "Tough-tackling midfielder", 33],
    ["Roberto Firmino", "Brazilian footballer", "Plays for Al-Ahli", "Skillful forward", 33],
    ["Gabriel Barbosa", "Brazilian footballer", "Plays for Flamengo", "Prolific striker", 27],
    ["Vitor Roque", "Brazilian footballer", "Plays for Athletico Paranaense", "Promising young forward", 19],
    ["Renato Sanches", "Portuguese footballer", "Plays for AS Roma", "Strong midfielder", 27],
    ["Pedro", "Brazilian footballer", "Plays for Flamengo", "Skillful striker", 31],
    ["Andre", "Brazilian footballer", "Plays for Fluminense", "Promising young midfielder", 23],
    ["Giorgio Chiellini", "Italian footballer", "Plays for LAFC", "Veteran center-back", 40],
    ["Javier Hernandez", "Mexican footballer", "Plays for LA Galaxy", "Veteran striker", 36],
    ["Keylor Navas", "Costa Rican footballer", "Plays for Paris Saint-Germain", "Experienced goalkeeper", 37],
    ["Antonio Rudiger", "German footballer", "Plays for Real Madrid", "Tall center-back", 31],
    ["David Alaba", "Austrian footballer", "Plays for Real Madrid", "Versatile defender", 32],
    ["Federico Valverde", "Uruguayan footballer", "Plays for Real Madrid", "Industrious midfielder", 26],
    ["Eduardo Camavinga", "French footballer", "Plays for Real Madrid", "Promising young midfielder", 21],
    ["Rodrygo", "Brazilian footballer", "Plays for Real Madrid", "Skillful winger", 23],
    ["Vinicius Jr", "Brazilian footballer", "Plays for Real Madrid", "Star forward", 24],
    ["Thibaut Courtois", "Belgian footballer", "Plays for Real Madrid", "Tall goalkeeper", 32],
    ["Aurelien Tchouameni", "French footballer", "Plays for Real Madrid", "Strong midfielder", 24],
    ["Rasmus Hojlund", "Danish footballer", "Plays for Manchester United", "Promising young striker", 21],
    ["Casemiro", "Brazilian footballer", "Plays for Manchester United", "Strong midfielder", 32],
    ["Marcus Rashford", "English footballer", "Plays for Manchester United", "Pacy forward", 26],
    ["Bruno Fernandes", "Portuguese footballer", "Plays for Manchester United", "Creative midfielder", 29],
    ["Antony", "Brazilian footballer", "Plays for Manchester United", "Skillful winger", 25],
    ["Harry Maguire", "English footballer", "Plays for Manchester United", "Tall center-back", 31],
    ["Jadon Sancho", "English footballer", "Plays for Manchester United", "Pacy winger", 24],
    ["Diogo Dalot", "Portuguese footballer", "Plays for Manchester United", "Attacking full-back", 25],
    ["Alphonse Areola", "French footballer", "Plays for West Ham United", "Tall goalkeeper", 31],
    ["Tomas Soucek", "Czech footballer", "Plays for West Ham United", "Tough-tackling midfielder", 29],
    ["Said Benrahma", "Algerian footballer", "Plays for West Ham United", "Skillful winger", 28],
    ["Edson Alvarez", "Mexican footballer", "Plays for West Ham United", "Strong midfielder", 26],
    ["Dominic Solanke", "English footballer", "Plays for Bournemouth", "Prolific striker", 27],
    ["Philip Billing", "Danish footballer", "Plays for Bournemouth", "Tall midfielder", 28],
    ["Neto", "Brazilian footballer", "Plays for Bournemouth", "Veteran goalkeeper", 35],
    ["Lewis Cook", "English footballer", "Plays for Bournemouth", "Industrious midfielder", 27],
    ["Antoine Griezmann", "French footballer", "Plays for Atletico Madrid", "World Cup-winning forward", 33],
    ["Jose Maria Gimenez", "Uruguayan footballer", "Plays for Atletico Madrid", "Strong center-back", 29],
    ["Gavi", "Spanish footballer", "Plays for Barcelona", "Young midfielder", 21],
    ["Ansu Fati", "Spanish footballer", "Plays for Brighton & Hove Albion", "Promising young forward", 21],
    ["Mason Mount", "English footballer", "Plays for Manchester United", "Creative midfielder", 25],
    ["Victor Lindelof", "Swedish footballer", "Plays for Manchester United", "Versatile defender", 30],
    ["Lisandro Martinez", "Argentinian footballer", "Plays for Manchester United", "Tough center-back", 26],
    ["Raphael Varane", "French footballer", "Plays for Manchester United", "Experienced center-back", 31],
    ["Manuel Ugarte", "Uruguayan footballer", "Plays for Paris Saint-Germain", "Strong midfielder", 23],
    ["Kylian Mbappe", "French footballer", "Plays for Paris Saint-Germain", "Star forward", 25],
    ["Gianluigi Donnarumma", "Italian footballer", "Plays for Paris Saint-Germain", "Tall goalkeeper", 25],
    ["Sandro Tonali", "Italian footballer", "Plays for Newcastle United", "Industrious midfielder", 24],
    ["Nick Pope", "English footballer", "Plays for Newcastle United", "Tall goalkeeper", 32],
    ["Bruno Guimaraes", "Brazilian footballer", "Plays for Newcastle United", "Strong midfielder", 27],
    ["Kalidou Koulibaly", "Senegalese footballer", "Plays for Al-Hilal", "Tall center-back", 33],
    ["Sadio Mane", "Senegalese footballer", "Plays for Al Nassr", "Pacy forward", 32],
    ["Lionel Messi", "Argentinian footballer", "Plays for Inter Miami", "World Cup-winning forward", 37],
    ["Sergio Busquets", "Spanish footballer", "Plays for Inter Miami", "Veteran midfielder", 36],
    ["Andres Iniesta", "Spanish footballer", "Plays for Emirates Club", "Veteran midfielder", 40],
    ["Luis Suarez", "Uruguayan footballer", "Plays for Gremio", "Veteran striker", 37],
    ["Diogo Jota", "Portuguese footballer", "Plays for Liverpool", "Versatile attacker", 27],
    ["Virgil van Dijk", "Dutch footballer", "Plays for Liverpool", "Tall center-back", 33],
    ["Trent Alexander-Arnold", "English footballer", "Plays for Liverpool", "Attacking full-back", 25],
    ["Mohamed Salah", "Egyptian footballer", "Plays for Liverpool", "Top Premier League goal scorer", 32]
        ]
        self.current_player = None
        self.hints_used = []
        self.remaining_hints = []
        self.help_used = False

        self.player_name_var = StringVar()
        self.hint_var = StringVar()
        self.tries_var = StringVar()
        self.score_var = StringVar()
        self.high_score_var = StringVar()
        self.hint1_var = StringVar()  # First hint (nationality or club)
        self.age_var = StringVar()

        self.load_high_score()
        self.setup_ui()
        self.new_game()

    def setup_ui(self):
        # Style configuration
        style = ttk.Style()
        style.configure('TButton', background='#333333', foreground='black', padding=6, font=('Arial', 12))
        style.configure('TLabel', background='#1E1E1E', foreground='white', font=('Arial', 12))
        style.configure('TEntry', background='#333333', foreground='white', padding=5)

        # Labels for high score, score, and tries
        Label(self.root, text="High Score:", bg='#1E1E1E', fg='white').grid(row=0, column=0, padx=10, pady=10, sticky='w')
        Label(self.root, textvariable=self.high_score_var, bg='#1E1E1E', fg='white', font=('Arial', 14)).grid(row=0, column=1, padx=10, pady=10)

        Label(self.root, text="Score:", bg='#1E1E1E', fg='white').grid(row=1, column=0, padx=10, pady=10, sticky='w')
        Label(self.root, textvariable=self.score_var, bg='#1E1E1E', fg='white', font=('Arial', 14)).grid(row=1, column=1, padx=10, pady=10)

        Label(self.root, text="Tries:", bg='#1E1E1E', fg='white').grid(row=2, column=0, padx=10, pady=10, sticky='w')
        Label(self.root, textvariable=self.tries_var, bg='#1E1E1E', fg='white', font=('Arial', 14)).grid(row=2, column=1, padx=10, pady=10)

        Label(self.root, text="Age:", bg='#1E1E1E', fg='white').grid(row=3, column=0, padx=10, pady=10, sticky='w')
        Label(self.root, textvariable=self.age_var, bg='#1E1E1E', fg='white', font=('Arial', 14)).grid(row=3, column=1, padx=10, pady=10)

        # Labels for hints
        Label(self.root, text="Hint 1 (Nationality/Club):", bg='#1E1E1E', fg='white').grid(row=4, column=0, padx=10, pady=10, sticky='w')
        Label(self.root, textvariable=self.hint1_var, bg='#1E1E1E', fg='white', font=('Arial', 14)).grid(row=4, column=1, padx=10, pady=10)

        Label(self.root, text="Hint:", bg='#1E1E1E', fg='white').grid(row=5, column=0, padx=10, pady=10, sticky='w')
        self.hint_label = Label(self.root, text="", bg='#1E1E1E', fg='white', font=('Arial', 12))
        self.hint_label.grid(row=5, column=1, padx=10, pady=10)

        Label(self.root, text="Player Guess:", bg='#1E1E1E', fg='white').grid(row=6, column=0, padx=10, pady=10, sticky='w')
        self.player_guess_entry = ttk.Entry(self.root, textvariable=self.player_name_var, foreground='black')
        self.player_guess_entry.grid(row=6, column=1, padx=10, pady=10)
        self.player_guess_entry.bind("<Return>", self.submit_answer_event)

        # Buttons
        ttk.Button(self.root, text="Submit Answer", command=self.submit_answer).grid(row=7, column=0, padx=10, pady=10)
        ttk.Button(self.root, text="Hint", command=self.provide_hint).grid(row=7, column=1, padx=10, pady=10)
        ttk.Button(self.root, text="Help", command=self.provide_help).grid(row=8, column=0, padx=10, pady=10)
        ttk.Button(self.root, text="New Game", command=self.new_game).grid(row=8, column=1, padx=10, pady=10)

        # Message label for game status
        self.status_label = Label(self.root, text="", bg='#1E1E1E', fg='white', font=('Arial', 14))
        self.status_label.grid(row=9, column=0, columnspan=2, padx=10, pady=10)

    def submit_answer_event(self, event):
        self.submit_answer()

    def similarity_score(self, a, b):
        return difflib.SequenceMatcher(None, a, b).ratio()

    def new_game(self):
        self.current_player = random.choice(self.players)
        self.hints_used = []
        self.remaining_hints = self.current_player[2:4]  # Initial hints (excluding nationality/club and age)
        self.help_used = False

        # Set the initial information
        self.age_var.set(f"Age: {self.current_player[4]}")
        self.hint1_var.set(f"{self.current_player[1]}")  # Nationality or club
        self.hint_label.config(text="")  # Clear hint label
        self.player_name_var.set("")
        self.update_ui()

    def submit_answer(self):
        player_name = self.current_player[0]
        user_answer = self.player_name_var.get().strip()
        
        if self.similarity_score(user_answer, player_name) >= 0.7:
            if self.help_used:
                self.score += 2  # Increase score by 2 points if help was used
            else:
                # Determine points based on number of hints used
                if len(self.hints_used) == 1:
                    self.score += 4
                elif len(self.hints_used) >= 2:
                    self.score += 3
                else:
                    self.score += 5
            self.status_label.config(text=f"Correct! It's {player_name}!\nYou earned {self.score} points.")
        else:
            if self.help_used:
                self.score -= 4
            elif len(self.hints_used) == 1:
                self.score -= 2
            elif len(self.hints_used) >= 2:
                self.score -= 3
            else:
                self.score -= 1
            self.status_label.config(text=f"Incorrect. The correct answer is: {player_name}")

        self.tries += 1
        self.update_ui()
        self.save_high_score()
        self.new_game()

    def provide_hint(self):
        if self.remaining_hints:
            next_hint = self.remaining_hints.pop(0)
            self.hint_label.config(text=next_hint)
            self.hints_used.append(next_hint)
            # No score change when the hint button is pressed
        else:
            messagebox.showinfo("No More Hints", "No more hints available!")


    def provide_help(self):
        self.help_used = True
        self.status_label.config(text="Help is used! If correct, you'll earn 2 points.")
        if self.current_player:
            first_name = self.current_player[0].split()[0]  # Get only the first name
            self.player_name_var.set(first_name)  # Show only the first name in the entry field

    def update_ui(self):
        self.score_var.set(f"Score: {self.score}")
        self.tries_var.set(f"Tries: {self.tries}")
        self.high_score_var.set(f"High Score: {self.high_score}")

    def load_high_score(self):
        if os.path.exists(HIGH_SCORE_FILE):
            with open(HIGH_SCORE_FILE, "r") as file:
                data = json.load(file)
                self.high_score = data.get("score", 0)
                self.high_score_tries = data.get("tries", 0)
        else:
            self.high_score = 0
            self.high_score_tries = 0

    def save_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.high_score_tries = self.tries
            with open(HIGH_SCORE_FILE, "w") as file:
                json.dump({"score": self.high_score, "tries": self.high_score_tries}, file)

if __name__ == "__main__":
    root = Tk()
    game = QuizGame(root)
    root.mainloop()
