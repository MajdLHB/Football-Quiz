import random
import difflib

class M:
    Bool = False
    score = 0
    tries = 0
    Players = [[ 'Lionel Messi', 'Fc Barcelona > PSG > Inter Miami', 'Argentina', 'Short Number: 10', 'Age:36', 'La polga', 'He won The world cup', 'He wonts 47 titels'],
[ 'Cristiano Ronaldo', 'Sporting > Manchester United > Fc Real Madrid > Juventus > Manchester United > Al nasr', 'Portugal', 'Short Number: 7', 'Age:38', 'The' 'He won The Uero', 'He wonts 36 titels'],
[ 'Neymar Jr', 'Santos > Fc Barcelona > PSG > Al Hilal', 'Brazil', 'Short Number: 10', 'Age:29', 'He play with Messi',],
[ 'Robert Lewandowski', 'Znicz Pruszków > Lech Poznań > Borussia Dortmund > Bayern Munich > FC Barcelona', 'Poland', 'Short Number: 9', 'One of the best strikers in the world'],
[ 'Kylian Mbappé', 'Monaco > PSG', 'France', 'Short Number: 7', 'Age:24', 'The Tuetle'],
[ 'Kevin De-Bruyne', 'Genk > Chelsea > Werder Bremen > Wolfsburg > Manchester City', 'Belgium', 'Short Number: 17',  'He won the Uero', 'He wonts 17 titels'],
[ 'Harry Kane', 'Tottenham Hotspur', 'England', 'Short Number: 10', 'Age:28', 'He play with Son', 'He wonts 0 titels'],
[ 'Erling Haaland', 'Bryne > Molde > Red Bull Salzburg > Borussia Dortmund > Man City', 'Norway', 'Short Number: 9',  'He play with Marco Reus', 'He is the top scorer in Primier League 2023'],
[ 'Romelu Lukaku', 'Anderlecht > Chelsea > West Bromwich Albion > Everton > Manchester United > Inter Milan', 'Belgium', 'Short Number: 9', 'He play with Lautaro Martinez'],
[ 'Mohamed Salah', 'El Mokawloon > Basel > Chelsea > Fiorentina > Roma > Liverpool', 'Egypt', 'Short Number: 11' 'He play with Sadio Mane',],
[ 'Karim Benzema', 'Lyon > Real Madrid > Al Itihad', 'France', 'Short Number: 9', 'Age:33', 'He won the ballon dor 2022'],
[ 'Sadio Mané', 'Metz > Red Bull Salzburg > Southampton > Liverpool > Al Nasr', 'Senegal', 'Short Number: 10', 'He won the African Golden Ball '],
[ 'Luis Suárez', 'Nacional > Groningen > Ajax > Liverpool > Barcelona > Atlético Madrid', 'Uruguay', 'Short Number: 9'],
[ 'Raheem Sterling', 'Queens Park Rangers > Liverpool > Manchester City > Chelsea', 'England', 'Short Number: 7'],
[ 'Eden Hazard', 'Lille > Chelsea > Real Madrid', 'Belgium', 'Short Number: 7', 'He play with Karim Benzema'],
[ 'Antoine Griezmann', 'Real Sociedad > Atlético Madrid > Barcelona > Atlético Madrid', 'France', 'Short Number: 7', 'He play 11 seasons in Laliga without winning the league'],
[ 'Paul Pogba', 'Le Havre > Manchester United > Juventus > Manchester United > Juventos', 'France', 'Short Number: 6', 'He is fined'],
[ 'Luka Modrić', 'Dinamo Zagreb > Zrinjski Mostar > Inter Zaprešić > Dinamo Zagreb > Tottenham Hotspur > Real Madrid', 'Croatia', 'Short Number: 10', 'He play with Karim Benzema'],
[ 'Bruno Fernandes', 'Boavista > Novara > Udinese > Sampdoria > Sporting CP > Manchester United', 'Portugal', 'Short Number: 18', 'Famous Medfielder'],
[ 'Toni Kroos', 'Bayern Munich > Bayer Leverkusen > Bayern Munich > Real Madrid', 'Germany', 'Short Number: 8', 'He won the champions league 5 times'],
[ 'Sergio Ramos', 'Sevilla > Real Madrid > Paris Saint-Germain > Sevelia', 'Spain', 'Short Number: 4', 'We won The world cup', 'He play with Lionel Messi and Cristiono Ronaldo'],
[ 'Virgil van Dijk', 'FC Groningen > Celtic > Southampton > Liverpool', 'Netherlands', 'Short Number: 4', 'He won the champions league 2019'],
[ 'Manuel Neuer', 'Schalke 04 > Bayern Munich', 'Germany', 'Short Number: 1', 'One of the best goalkeepers in the world'],
[ 'Alisson Becker', 'Internacional > Roma > Liverpool', 'Brazil', 'Short Number: 1', 'Goalkeeper of the year 2019'],
[ 'Thibaut Courtois', 'Genk > Atlético Madrid > Chelsea > Real Madrid', 'Belgium', 'Short Number: 1', 'Famous Goalkeeper'],
[ 'Marc-André ter Stegen', 'Borussia Mönchengladbach > Barcelona', 'Germany', 'Short Number: 1', 'He is a famous goalkeeper'],
[ 'Jan Oblak', 'Benfica > Atlético Madrid', 'Slovenia', 'Short Number: 13', 'He didnt win the champions league'],
[ 'Ederson', 'Benfica > Manchester City', 'Brazil', 'Short Number: 31', 'He won the champions league 2023'],
[ 'David de-Gea', 'Atlético Madrid > Manchester United', 'Spain', 'Short Number: 1', 'He is a famous goalkeeper without a club'],
[ 'Joshua Kimmich', 'VfB Stuttgart > RB Leipzig > Bayern Munich', 'Germany', 'Short Number: 6', 'He is playing right now'],
[ 'N\'Golo Kanté', 'Boulogne > Caen > Leicester City > Chelsea', 'France', 'Short Number: 7', 'He won the world cup 2018'],
[ 'Carlos Casemiro', 'São Paulo > Real Madrid > Man utd.', 'Brazil', 'Short Number: 14',],
[ 'Frenkie de-Jong', 'Willem II > Ajax > Barcelona', 'Netherlands', 'Short Number: 21', 'He transfered to Barcelona for 75 million euros'],
[ 'Thomas Müller', 'Bayern Munich', 'Germany', 'Short Number: 25', 'He never left Bayern Munich'],
[ 'Jadon Sancho', 'Manchester City > Borussia Dortmund > Manchester United', 'England', 'Short Number: 7', 'He play with Erling Haaland'],
[ 'Marquinhos', 'Corinthians > Roma > Paris Saint-Germain', 'Brazil', 'Short Number: 5', 'He became the captain of PSG'],
[ 'Sergio Busquets', 'Barcelona', 'Spain', 'Short Number: 5', 'He won the world cup 2010'],
[ 'Heung-min Son', 'Hamburger SV > Bayer Leverkusen > Tottenham Hotspur', 'South Korea', 'Short Number: 7', 'He is the best Asian player'],
[ 'Gerard Piqué', 'Manchester United > Barcelona', 'Spain', 'Short Number: 3', 'He retired'],
[ 'David Silva', 'Valencia > Manchester City > Real Sociedad', 'Spain', 'Short Number: 21'],
[ 'Trent Alexander-Arnold', 'Liverpool', 'England', 'Short Number: 66', 'He won the champions league 2019'],
[ 'Sergio Agüero', 'Atlético Madrid > Manchester City > Barcelona', 'Argentina', 'Short Number: 10', 'He retired'],
[ 'Leroy Sané', 'Schalke 04 > Manchester City > Bayern Munich', 'Germany', 'Short Number: 19', 'He is playing right now'],
[ 'Ángel Di-María', 'Rosario Central > Benfica > Real Madrid > Manchester United > Paris Saint-Germain > Juventos >Benfica', 'Argentina', 'Short Number: 11', ],
[ 'Gianluigi Donnarumma', 'Milan > Paris Saint-Germain', 'Italy', 'Short Number: 50', 'He won the Euro 2021'],
[ 'Hakim Ziyech', 'Heerenveen > Twente > Ajax > Chelsea', 'Morocco', 'Short Number: 22', 'He play with N\'Golo Kanté'],
[ 'Paulo Dybala', 'Instituto > Palermo > Juventus', 'Argentina', 'Short Number: 10', 'He is playing right now'],
[ 'Christian Eriksen', 'Ajax > Tottenham Hotspur > Internazionale > Brentfors > Man Utd', 'Denmark', 'Short Number: 24', 'He retired because of a heart attack and back to football'],
[ 'Memphis Depay', 'Transfer History: PSV Eindhoven > Manchester United > Lyon > Barcelona > Atlético Madrid', 'Netherlands', 'Short Number: 10', 'A fact about the player: He play with Lionel Messi', 'A fact about the player: He play with Antoine Griezmann'],
[ 'Lautaro Martínez', 'Racing Club > Inter Milan', 'Argentina', 'Short Number: 10', 'A fact about the player: He play with Romelu Lukaku', 'A fact about the player: He won the Copa America 2021'],
[ 'Nicolò Barella', 'Inter Milan', 'Italy', 'Short Number: 23', 'A fact about the player: He play with Romelu Lukaku', 'A fact about the player: He won the Euro 2021'],
[ 'Jude Bellingham', 'Birmingham City > Borussia Dortmund > Real Madrid', 'England', 'Short Number: 22', 'A fact about the player: He is 20 years old', 'A fact about the player: He is the youngest player in the Euro 2021'],
[ 'Phil Foden', 'Manchester City', 'England', 'Short Number: 47'],
[ 'Pedri Gonzalez', 'Las Palmas > Barcelona', 'Spain', 'Short Number: 16', 'A fact about the player: He is 20 years old', 'A fact about the player: He is the youngest Spain player in the Euro 2021'],
[ 'Federico Chiesa', 'Fiorentina > Juventus', 'Italy', 'Short Number: 22' ],
[ 'Mason Mount', 'Chelsea > Man utd', 'England', 'Short Number: 19', 'A fact about the player: He is 24 years old' ],
[ 'Jack Grealish', 'Aston Villa > Manchester City', 'England', 'Short Number: 10', 'A fact about the player: He is 26 years old', 'A fact about the player: He won the champions league 2023'],
['Jorginho', 'Hellas Verona > Napoli > Chelsea', 'Italy', 'Short Number: 8', 'A fact about the player: He is 29 years old', 'A fact about the player: He won the champions league 2021'],
['Declan Rice', 'Chelsea > West Ham United > Arsenal', 'England', 'Short Number: 4', 'A fact about the player: He is 22 years old'],
['Luis Figo', 'Sporting CP > Barcelona > Real Madrid > Inter Milan', 'Portugal', 'Short Number: 7', 'Former FIFA World Player of the Year'],
['Andres Iniesta', 'Barcelona > Vissel Kobe', 'Spain', 'Short Number: 8', 'Scored the winning goal in the 2010 World Cup final'],
['Franz Beckenbauer', 'Bayern Munich > New York Cosmos', 'Germany', 'Short Number: 5', 'World Cup winner as both player and coach'],
['George Best', 'Manchester United > Los Angeles Aztecs', 'Northern Ireland', 'Short Number: 7', 'Widely regarded as one of the greatest dribblers in history'],
['Paolo Maldini', 'AC Milan', 'Italy', 'Short Number: 3', 'Legendary Italian defender and one-club man'],
['Lev Yashin', 'Dynamo Moscow', 'Soviet Union', 'Short Number: 1', 'The only goalkeeper to win the Ballon d\'Or'],
    ['Bobby Charlton', 'Manchester United', 'England', 'Short Number: 9', 'Scored a record number of goals for Manchester United'],
    ['Ferenc Puskás', 'Budapest Honvéd > Real Madrid', 'Hungary', 'Short Number: 10', 'Prolific goal scorer and member of the Mighty Magyars'],
    ['Ronaldo Nazário', 'PSV Eindhoven > Barcelona > Inter Milan > Real Madrid', 'Brazil', 'Short Number: 9', 'Two-time FIFA World Player of the Year'],
    ['Zinedine Zidane', 'AS Cannes > Girondins de Bordeaux > Juventus > Real Madrid', 'France', 'Short Number: 5', 'Scored twice in the 1998 World Cup final'],
    ['Ronaldinho', 'Gremio > PSG > Barcelona > AC Milan', 'Brazil', 'Short Number: 10', 'Known for his mesmerizing skills and creativity'],
    ['Thierry Henry', 'AS Monaco > Juventus > Arsenal > Barcelona > New York Red Bulls', 'France', 'Short Number: 14', 'Arsenal\'s all-time leading goal scorer'],
    ['Roberto Baggio', 'Vicenza > Fiorentina > Juventus > Inter Milan', 'Italy', 'Short Number: 10', 'Known for his dribbling and free-kick abilities'],
    ['Samuel Eto\'o', 'Real Madrid > Mallorca > Barcelona > Inter Milan > Chelsea', 'Cameroon', 'Short Number: 9', 'Won back-to-back trebles with Barcelona and Inter Milan'],
    ['Xavi Hernandez', 'Barcelona > Al Sadd', 'Spain', 'Short Number: 6', 'Key figure in Barcelona\'s tiki-taka era'],
    ['Gianluigi Buffon', 'Parma > Juventus > PSG', 'Italy', 'Short Number: 1', 'One of the greatest goalkeepers of all time'],
    ['Fabio Cannavaro', 'Parma > Inter Milan > Juventus > Real Madrid', 'Italy', 'Short Number: 5', 'Captained Italy to the 2006 World Cup victory'],
    ['Gheorghe Hagi', 'Farul Constanța > Steaua Bucharest > Real Madrid > Barcelona', 'Romania', 'Short Number: 10', 'Nicknamed "The Maradona of the Carpathians"'],
    ['David Beckham', 'Manchester United > Real Madrid > LA Galaxy > Paris Saint-Germain', 'England', 'Short Number: 7', 'Known for his precise free-kicks and crossing'],
    ['George Weah', 'Monaco > Paris Saint-Germain > AC Milan', 'Liberia', 'Short Number: 9', 'The only African player to win the FIFA World Player of the Year'],
    ['Fernando Torres', 'Atletico Madrid > Liverpool > Chelsea', 'Spain', 'Short Number: 9', 'Scored the winning goal in the 2008 Euro final'],
    ['Michael Ballack', 'Kaiserslautern > Bayer Leverkusen > Bayern Munich > Chelsea', 'Germany', 'Short Number: 13', 'One of Germany\'s finest midfielders'],
    ['Rivaldo', 'Deportivo La Coruña > Barcelona > AC Milan', 'Brazil', 'Short Number: 11', 'Won the FIFA World Player of the Year in 1999'],
    ['Johan Cruyff', 'Ajax > Barcelona > Los Angeles Aztecs', 'Netherlands', 'Short Number: 14', 'Pioneer of Total Football'],
    ['Alfredo Di Stefano', 'River Plate > Real Madrid > Espanyol', 'Argentina', 'Short Number: 9', 'Five-time Ballon d\'Or winner'],
    ['Franco Baresi', 'AC Milan', 'Italy', 'Short Number: 6', 'Legendary Italian defender and captain'],
    ['George Best', 'Manchester United > Los Angeles Aztecs', 'Northern Ireland', 'Short Number: 7', 'Widely regarded as one of the greatest dribblers in history'],
    ['Jack Grealish', 'Aston Villa > Manchester City', 'England', 'Short Number: 10', 'A fact about the player: He is 26 years old', 'A fact about the player: He won the champions league 2023'],
    ['Jorginho', 'Hellas Verona > Napoli > Chelsea > Arsenal', 'Italy', 'Short Number: 8', 'A fact about the player: He is 29 years old', 'A fact about the player: He won the champions league 2021'],
    ['Declan Rice', 'West Ham United > Arsenal', 'England', 'Short Number: 4', 'A fact about the player: He is 22 years old'],
     ['Serge Gnabry', 'Arsenal > Werder Bremen > Bayern Munich', 'Germany', 'Short Number: 22', 'Known for his speed and goal-scoring ability'],
    ['Kieran Trippier', 'Manchester City > Burnley > Tottenham Hotspur > Atletico Madrid', 'England', 'Short Number: 23', 'A versatile full-back known for his crossing'],
    ['Dayot Upamecano', 'RB Leipzig > Bayern Munich', 'France', 'Short Number: 5', 'A young and promising central defender'],
    ['Wojciech Szczęsny', 'Legia Warsaw > Arsenal > Juventus', 'Poland', 'Short Number: 1', 'Poland\'s national team goalkeeper'],
    ['Sergej Milinković-Savić', 'KRC Genk > Lazio', 'Serbia', 'Short Number: 21', 'A tall and powerful midfielder'],
    ['Dani Carvajal', 'Real Madrid', 'Spain', 'Short Number: 2', 'An attacking right-back with defensive skills'],
    ['Ferran Torres', 'Valencia > Manchester City', 'Spain', 'Short Number: 21', 'A young winger with immense potential'],
    ['Luis Alberto', 'Sevilla > Lazio', 'Spain', 'Short Number: 10', 'A creative midfielder known for his passing'],
    ['Tammy Abraham', 'Chelsea', 'England', 'Short Number: 9', 'A tall and agile striker'],
    ['Raphaël Varane', 'Lens > Real Madrid > Manchester United', 'France', 'Short Number: 19', 'Known for his defensive prowess'],
    ['Achraf Hakimi', 'Real Madrid > Borussia Dortmund > Inter Milan > Paris Saint-Germain', 'Morocco', 'Short Number: 2', 'A fast and attacking right-back'],
    ['Federico Valverde', 'Peñarol > Real Madrid', 'Uruguay', 'Short Number: 15', 'A dynamic and versatile midfielder'],
    ['Ciro Immobile', 'Juventus > Torino > Sevilla > Lazio', 'Italy', 'Short Number: 17', 'A prolific goal scorer in Serie A'],
    ['Emiliano Martínez', 'Independiente > Arsenal > Aston Villa', 'Argentina', 'Short Number: 26', 'Argentina\'s national team goalkeeper'],
    ['Nicolo Zaniolo', 'Inter Milan > Roma', 'Italy', 'Short Number: 22', 'A young and talented midfielder'],
    ['Youri Tielemans', 'Anderlecht > AS Monaco > Leicester City', 'Belgium', 'Short Number: 8', 'Known for his long-range goals'],
    ['Isak Belfodil', 'Lyon > Bologna > Parma > Inter Milan > Hoffenheim', 'Algeria', 'Short Number: 19', 'A tall and skillful forward'],
    ['Sergi Roberto', 'Barcelona', 'Spain', 'Short Number: 20', 'Versatile player who can play in multiple positions'],
    ['Ferland Mendy', 'Lyon > Real Madrid', 'France', 'Short Number: 23', 'Attacking left-back with pace'],
    ['Kalvin Phillips', 'Leeds United > Man city', 'England', 'Short Number: 23', 'A dynamic midfielder known for his work rate'],
    ['Andreas Christensen', 'Brondby > Chelsea > Barcelona', 'Denmark', 'Short Number: 4', 'A composed central defender'],
      ['Leon Goretzka', 'Bochum > Schalke 04 > Bayern Munich', 'Germany', 'Short Number: 18', 'Dynamic midfielder for Bayern Munich and Germany'],
    ['Donyell Malen', 'Jong PSV > PSV Eindhoven > Borussia Dortmund', 'Netherlands', 'Short Number: 9', 'Young Dutch striker with great potential'],
    ['Dominik Szoboszlai', 'Red Bull Salzburg > RB Leipzig', 'Hungary', 'Short Number: 17', 'Talented midfielder known for his free-kick ability'],
    ['Lucas Paquetá', 'Flamengo > AC Milan > Lyon', 'Brazil', 'Short Number: 10', 'Creative midfielder representing Brazil'],
    ['Nicolas Pepe', 'Lille > Arsenal', 'Ivory Coast', 'Short Number: 19', 'Pacey winger for Arsenal and Ivory Coast'],
    ['Chris Wood', 'Leeds United > Burnley', 'New Zealand', 'Short Number: 9', 'New Zealand\'s leading goal scorer'],
    ['Eduardo Camavinga', 'Rennes > Paris Saint-Germain', 'France', 'Short Number: 10', 'Highly touted young midfielder'],
    ['Sander Berge', 'Genk > Sheffield United', 'Norway', 'Short Number: 32', 'Norwegian midfielder'],
    ['Ozan Kabak', 'Schalke 04 > Liverpool', 'Turkey', 'Short Number: 19', 'Defender known for his composure'],
    ['Amad Diallo', 'Atalanta > Manchester United', 'Ivory Coast', 'Short Number: 16', 'Young winger with great potential'],
    ['Darwin Nunez', 'Almería > Benfica', 'Uruguay', 'Short Number: 9', 'Uruguayan striker with an eye for goal'],
    ['Mikel Oyarzabal', 'Real Sociedad', 'Spain', 'Short Number: 10', 'Talented winger for Real Sociedad'],
    ['Breel Embolo', 'FC Basel > Borussia Mönchengladbach > Borussia Dortmund', 'Switzerland', 'Short Number: 36', 'Versatile forward'],
    ['Sergio Reguilón', 'Real Madrid > Tottenham Hotspur', 'Spain', 'Short Number: 3', 'Attacking left-back'],
    ['Sandro Tonali', 'Brescia > AC Milan', 'Italy', 'Short Number: 8', 'Young Italian midfielder with great passing ability'],
    ['Houssem Aouar', 'Lyon', 'France', 'Short Number: 8', 'Creative midfielder for Lyon'],
    ['Patson Daka', 'Red Bull Salzburg > Leicester City', 'Zambia', 'Short Number: 23', 'Zambian striker with a clinical finish'],
    ['Marcelo Brozović', 'Dinamo Zagreb > Inter Milan', 'Croatia', 'Short Number: 77', 'Croatian midfielder for Inter Milan'],
    ['Denis Zakaria', 'Young Boys > Borussia Mönchengladbach', 'Switzerland', 'Short Number: 6', 'Defensive midfielder'],
    ['Joaquin Correa', 'Estudiantes > Sevilla > Lazio', 'Argentina', 'Short Number: 11', 'Argentinian forward'],
    ['Matteo Guendouzi', 'Lorient > Arsenal > Marseille', 'France', 'Short Number: 4', 'Young French midfielder'],
    ['Emerson Palmieri', 'AS Roma > Chelsea', 'Italy', 'Short Number: 33', 'Defender who plays for Italy'],
    ['Diego Lainez', 'Club América > Real Betis', 'Mexico', 'Short Number: 25', 'Mexican winger with flair'],
     ['Gareth Bale', 'Southampton > Tottenham Hotspur > Real Madrid > Tottenham Hotspur', 'Wales', 'Short Number: 9', 'Wales international known for his speed and skills'],
    ['Mesut Özil', 'Schalke 04 > Werder Bremen > Real Madrid > Arsenal > Fenerbahçe', 'Germany', 'Short Number: 67', 'German playmaker'],
    ['Franshisco Isco', 'Valencia > Malaga > Real Madrid', 'Spain', 'Short Number: 22', 'Spanish midfielder known for his dribbling'],
    ['Giovani Lo Celso', 'Rosario Central > Paris Saint-Germain > Real Betis > Tottenham Hotspur', 'Argentina', 'Short Number: 18', 'Argentinian midfielder'],
    ['Lucas Moura', 'São Paulo > Paris Saint-Germain > Tottenham Hotspur', 'Brazil', 'Short Number: 27', 'Brazilian winger known for his pace'],
    ['Wissam Ben Yedder', 'Toulouse > Sevilla > AS Monaco', 'France', 'Short Number: 9', 'French striker with a clinical finish'],
    ['Memphis Depay', 'PSV Eindhoven > Manchester United > Lyon > Barcelona > Olympique Lyonnais', 'Netherlands', 'Short Number: 10', 'Dutch forward with flair'],
    ['Edin Džeko', 'Željezničar > Teplice > Željezničar > FK Teplice > Wolfsburg > Manchester City > AS Roma > Inter Milan', 'Bosnia and Herzegovina', 'Short Number: 9', 'Bosnian striker known for his strength'],
    ['Pierre-Emerick Aubameyang', 'AC Milan > Dijon > Lille > AS Saint-Étienne > Borussia Dortmund > Arsenal', 'Gabon', 'Short Number: 14', 'Gabonese striker with pace'],
    ['Erling Haaland', 'Bryne > Molde > Red Bull Salzburg > Borussia Dortmund > Manchester City', 'Norway', 'Short Number: 9', 'Norwegian sensation known for his goal-scoring ability'],
    ['Timo Werner', 'Stuttgart > RB Leipzig > Chelsea', 'Germany', 'Short Number: 11', 'German forward with speed'],
    ['Jules Koundé', 'Girondins de Bordeaux > Sevilla', 'France', 'Short Number: 12', 'French defender with great potential'],
    ['Lorenzo Insigne', 'Napoli', 'Italy', 'Short Number: 24', 'Italian forward with excellent dribbling skills'],
    ['Raphaël Varane', 'Lens > Real Madrid > Manchester United', 'France', 'Short Number: 4', 'French defender known for his composure'],
    ['Kai Havertz', 'Bayer Leverkusen > Chelsea', 'Germany', 'Short Number: 29', 'Young German midfielder with versatility'],
    ['Ferran Torres', 'Valencia > Manchester City', 'Spain', 'Short Number: 21', 'Spanish winger with great potential'],
    ['Dani Ceballos', 'Real Betis > Real Madrid > Arsenal', 'Spain', 'Short Number: 8', 'Spanish midfielder'],
    ['Andrea Belotti', 'Palermo > Torino', 'Italy', 'Short Number: 9', 'Italian striker known for his work rate'],
    ['James Rodríguez', 'Porto > AS Monaco > Real Madrid > Bayern Munich > Everton', 'Colombia', 'Short Number: 19', 'Colombian playmaker'],
       ['Dayot Upamecano', 'RB Salzburg > RB Leipzig > Bayern Munich', 'France', 'Short Number: 5', 'French defender with great potential'],
        ['Gerard Moreno', 'Villarreal > Espanyol > Villarreal', 'Spain', 'Short Number: 7', 'Spanish striker known for his clinical finishing'],
    ['Yannick Carrasco', 'Monaco > Atlético Madrid > Dalian Professional > Atlético Madrid', 'Belgium', 'Short Number: 21', 'Belgian winger with pace'],
    ['Hakim Ziyech', 'Heerenveen > Twente > Ajax > Chelsea', 'Morocco', 'Short Number: 22', 'Moroccan midfielder with creative flair'],
    ['Riyad Mahrez', 'Le Havre > Leicester City > Manchester City', 'Algeria', 'Short Number: 26', 'Algerian winger known for his dribbling skills'],
    ['Kalidou Koulibaly', 'Metz > Genk > Napoli', 'Senegal', 'Short Number: 26', 'Senegalese defender known for his strength'],
    ['Lucas Paquetá', 'Flamengo > AC Milan > Olympique Lyonnais', 'Brazil', 'Short Number: 39', 'Brazilian midfielder with flair'],
    ['João Cancelo', 'Benfica > Valencia > Inter Milan > Manchester City > Bayern > Barcelona', 'Portugal', 'Short Number: 27', 'Portuguese right-back with attacking prowess'],
    ['Sergej Milinković-Savić', 'Genk > Lazio', 'Serbia', 'Short Number: 21', 'Serbian midfielder known for his versatility'],
    ['Ismaïla Sarr', 'Metz > Rennes > Watford', 'Senegal', 'Short Number: 23', 'Senegalese winger with speed'],
    ['Youssef En-Nesyri', 'Malaga > Leganés > Sevilla', 'Morocco', 'Short Number: 15', 'Moroccan striker known for his aerial ability'],
    ['Rui Patrício', 'Sporting CP > Wolverhampton Wanderers > AS Roma', 'Portugal', 'Short Number: 11', 'Portuguese goalkeeper'],
    ['Nicolo Barella', 'Cagliari > Inter Milan', 'Italy', 'Short Number: 23', 'Italian midfielder with great work rate'],
    ['Serge Aurier', 'Lens > Toulouse > Paris Saint-Germain > Tottenham Hotspur', 'Ivory Coast', 'Short Number: 24', 'Ivorian right-back with attacking capabilities'],
    ['Rafinha Alcântara', 'Barcelona > Paris Saint-Germain', 'Spain', 'Short Number: 12', 'Spanish midfielder with technical skills'],
    ['Rúben Dias', 'Benfica > Manchester City', 'Portugal', 'Short Number: 3', 'Portuguese defender known for his composure'],
    ['Nikola Vlašić', 'Hajduk Split > Everton > CSKA Moscow', 'Croatia', 'Short Number: 8', 'Croatian midfielder with versatility'],
    ['Donyell Malen', 'Jong PSV > PSV Eindhoven > Borussia Dortmund', 'Netherlands', 'Short Number: 9', 'Dutch striker with goal-scoring ability'],
    ['Emiliano Martínez', 'Independiente > Arsenal > Aston Villa', 'Argentina', 'Short Number: 26', 'Argentinian goalkeeper'],
    ['Matteo Guendouzi', 'Lorient > Arsenal > Hertha BSC', 'France', 'Short Number: 8', 'French midfielder known for his tenacity'],
    ['David Neres', 'São Paulo > Ajax', 'Brazil', 'Short Number: 7', 'Brazilian winger with flair'],
    ['Douglas Luiz', 'Vasco da Gama > Manchester City > Aston Villa', 'Brazil', 'Short Number: 6', 'Brazilian midfielder with defensive qualities'],
    ['Sergi Roberto', 'Barcelona', 'Spain', 'Short Number: 20', 'Versatile Spanish midfielder'],
    ['Kieran Tierney', 'Celtic > Arsenal', 'Scotland', 'Short Number: 3', 'Scottish left-back known for his crossing'],
     ['Christian Pulisic', 'Borussia Dortmund > Chelsea', 'United States', 'Short Number: 10', 'Talented American winger'],
    ['Federico Valverde', 'Penarol > Real Madrid', 'Uruguay', 'Short Number: 15', 'Uruguayan midfielder with great potential'],
    ['Dominik Szoboszlai', 'Salzburg > RB Leipzig', 'Hungary', 'Short Number: 17', 'Hungarian midfielder known for his set pieces'],
    ['Jules Koundé', 'Bordeaux > Sevilla', 'France', 'Short Number: 12', 'French defender with immense potential'],
    ['Lucas Ocampos', 'Monaco > Marseille > Sevilla', 'Argentina', 'Short Number: 5', 'Argentinian winger with versatility'],
    ['Giovanni Reyna', 'New York City FC > Borussia Dortmund', 'United States', 'Short Number: 32', 'Young American talent'],
    ['Eduardo Camavinga', 'Rennes > Real Madrid', 'France', 'Short Number: 23', 'French midfielder with a bright future'],
    ['Jadon Sancho', 'Manchester City > Borussia Dortmund > Manchester United', 'England', 'Short Number: 7', 'English winger with creativity'],
    ['Houssem Aouar', 'Lyon', 'France', 'Short Number: 8', 'French midfielder with dribbling skills'],
    ['Kai Havertz', 'Bayer Leverkusen > Chelsea', 'Germany', 'Short Number: 29', 'German attacking midfielder with versatility'],
    ['Sander Berge', 'Genk > Sheffield United > Arsenal', 'Norway', 'Short Number: 32', 'Norwegian midfielder with physicality'],
    ['Ben White', 'Brighton & Hove Albion > Arsenal', 'England', 'Short Number: 4', 'English defender known for his composure'],
    ['Ferran Torres', 'Valencia > Manchester City', 'Spain', 'Short Number: 21', 'Spanish winger with pace and flair'],
    ['Nuno Mendes', 'Sporting CP > Paris Saint-Germain', 'Portugal', 'Short Number: 25', 'Portuguese left-back with potential'],
    ['Odsonne Édouard', 'Celtic > Crystal Palace', 'France', 'Short Number: 22', 'French striker with goal-scoring ability'],
    ['Renato Sanches', 'Benfica > Bayern Munich > Lille', 'Portugal', 'Short Number: 18', 'Portuguese midfielder with drive'],
    ['Weston McKennie', 'Schalke 04 > Juventus', 'United States', 'Short Number: 14', 'American midfielder with versatility'],
    ['Dwight McNeil', 'Burnley', 'England', 'Short Number: 11', 'English winger known for his crossing'],
    ['Maxence Lacroix', 'Sochaux > Wolfsburg', 'France', 'Short Number: 4', 'French defender with potential'],
    ]

def Quiz():
    #pick a ramdom player
    player = random.choice(M.Players)
    print('Welcome to the Quiz!')
    PlayerName = (player[0])
    PlayerN = PlayerName.split()
    Playername = PlayerN[0]
    PlayerLN = PlayerN[1]
    Hint1 = (player[1])
    Hint2 = (player[random.randint(2, len(player)-1)])
    while Hint1 == Hint2:
        Hint2 = (player[random.randint(2, len(player)-1)])
    print(f'First hint: {Hint1}')
    print(f'Second hint: {Hint2}')
    Answer = input('Who is this player? ')

    def similarity_score(a, b):
        return difflib.SequenceMatcher(None, a, b).ratio()





    def check_answer(Answer, PlayerName):
        similarity = similarity_score(Answer.lower(), PlayerName.lower())
        if similarity >= 0.7:
            print("Correct! Its " + PlayerName + "!") 
            M.score = M.score + 3
            M.tries = M.tries + 1
            print(f'Your score is {M.score} in {M.tries} tries')
            print('=====================')
            return Quiz()

        else:
            if Answer == 'Help' or Answer == 'help':
                print(f' Player name: {Playername}')
                SAnswer = input('Enter Player Last Name: ')
                def CA(SAnswer, PlayerName):
                    similarity = similarity_score(SAnswer.lower(), PlayerName.lower())
                    if similarity >= 0.7:
                        print("Correct! Its " + PlayerName + "!")
                        M.score = M.score + 2
                        M.tries = M.tries + 1
                        print(f'Your score is {M.score} in {M.tries} tries')
                        print('=====================')
                        return Quiz()
                        
                    else:
                        if SAnswer == 'Hint' or SAnswer == 'hint':
                            Hint3 = (player[random.randint(2, len(player)-1)])
                            while Hint3 == Hint1 or Hint3 == Hint2:
                                Hint3 = (player[random.randint(2, len(player)-1)])
                            print(f'Third hint: {Hint3}')
                            answer = input('Enter Player Name: ')
                            def ff(answer, PlayerName):
                                similarity = similarity_score(answer.lower(), PlayerName.lower())
                                if similarity >= 0.7:
                                    print("Correct! Its " + PlayerName + "!")
                                    M.score = M.score + 1
                                    M.tries = M.tries + 1
                                    print(f'Your score is {M.score} in {M.tries} tries')
                                    print('=====================')
                                    return Quiz()   
                                else:
                                        print("Incorrect. The correct answer is: " + PlayerName)
                                        M.tries = M.tries + 1
                                        print(f'Your score is {M.score} in {M.tries} tries')
                                        print('=====================')
                                        return Quiz()
                            ff(SAnswer, PlayerName)

                        print("Incorrect. The correct answer is: " + PlayerName)
                        M.tries = M.tries + 1
                        print(f'Your score is {M.score} in {M.tries} tries')
                        print('=====================')
                        return Quiz()
                CA(SAnswer, PlayerLN)
            if Answer == 'Hint' or Answer == 'hint':
                Hint3 = (player[random.randint(2, len(player)-1)])
                while Hint3 == Hint1 or Hint3 == Hint2:
                    Hint3 = (player[random.randint(2, len(player)-1)])
                print(f'Third hint: {Hint3}')
                answer = input('Enter Player Name: ')
                def checkanswer(answer, PlayerName):
                    similarity = similarity_score(answer.lower(), PlayerName.lower())
                    if similarity >= 0.7:
                        print("Correct! Its " + PlayerName + "!")
                        M.score = M.score + 2
                        M.tries = M.tries + 1
                        print(f'Your score is {M.score} in {M.tries} tries')
                        print('=====================')
                        return Quiz()   
                    else:
                        if answer == 'Help' or answer == 'help':
                            print(f' Player name: {Playername}')
                            HH = input('Enter Player Last Name: ')
                            def eee(HH, PlayerName):
                                similarity = similarity_score(HH.lower(), HH.lower())
                                if similarity >= 0.7:
                                    print("Correct! Its " + PlayerName + "!")
                                    M.score = M.score + 1
                                    M.tries = M.tries + 1
                                    print(f'Your score is {M.score} in {M.tries} tries')
                                    print('=====================')
                                    return Quiz()
                                else:
                                    print("Incorrect. The correct answer is: " + PlayerName)
                                    M.tries = M.tries + 1
                                    print(f'Your score is {M.score} in {M.tries} tries')
                                    print('=====================')
                                    return Quiz()
                            eee(SAnswer, PlayerLN)

                            print("Incorrect. The correct answer is: " + PlayerName)
                            M.tries = M.tries + 1
                            print(f'Your score is {M.score} in {M.tries} tries')
                            print('=====================')
                            return Quiz()
                checkanswer(answer, PlayerName)

            print("Incorrect. The correct answer is: " + PlayerName)
            M.tries = M.tries + 1
            print(f'Your score is {M.score} in {M.tries} tries')
            print('=====================')
            return Quiz()
            
    
    check_answer(Answer, PlayerName)





Quiz()
