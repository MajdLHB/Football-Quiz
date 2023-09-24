import random
import difflib

class M:
    Bool = False
    score = 0
    tries = 0
    Players = [[ 'Lionel Messi', 'Fc Barcelona > PSG > Inter Miami', 'Argentina', 'Short Number: 10', 'Age:36', 'La polga', 'He won The world cup', 'He wonts 47 titels'],
[ 'Cristiano Ronaldo', 'Sporting > Manchester United > Fc Real Madrid > Juventus > Manchester United > Al nasr', 'Portugal', 'Short Number: 7', 'Age:38', 'The' 'He won The Uero', 'He wonts 36 titels'],
[ 'Neymar Jr', 'Santos > Fc Barcelona > PSG > Al Hilal', 'Brazil', 'Short Number: 10', 'Age:29', 'He plays with Messi',],
[ 'Robert Lewandowski', 'Znicz Pruszków > Lech Poznań > Borussia Dortmund > Bayern Munich > FC Barcelona', 'Poland', 'Short Number: 9', 'One of the best strikers in the world'],
[ 'Kylian Mbappé', 'Monaco > PSG', 'France', 'Short Number: 7', 'Age:24', 'The Tuetle'],
[ 'Kevin De-Bruyne', 'Genk > Chelsea > Werder Bremen > Wolfsburg > Manchester City', 'Belgium', 'Short Number: 17',  'He won the Uero', 'He wonts 17 titels'],
[ 'Harry Kane', 'Tottenham Hotspur', 'England', 'Short Number: 10', 'Age:28', 'He plays with Son', 'He wonts 0 titels'],
[ 'Erling Haaland', 'Bryne > Molde > Red Bull Salzburg > Borussia Dortmund > Man City', 'Norway', 'Short Number: 9',  'He plays with Marco Reus', 'He is the top scorer in Primier League 2023'],
[ 'Romelu Lukaku', 'Anderlecht > Chelsea > West Bromwich Albion > Everton > Manchester United > Inter Milan', 'Belgium', 'Short Number: 9', 'He plays with Lautaro Martinez'],
[ 'Mohamed Salah', 'El Mokawloon > Basel > Chelsea > Fiorentina > Roma > Liverpool', 'Egypt', 'Short Number: 11' 'He plays with Sadio Mane',],
[ 'Karim Benzema', 'Lyon > Real Madrid > Al Itihad', 'France', 'Short Number: 9', 'Age:33', 'He won the ballon dor 2022'],
[ 'Sadio Mané', 'Metz > Red Bull Salzburg > Southampton > Liverpool > Al Nasr', 'Senegal', 'Short Number: 10', 'He won the African Golden Ball '],
[ 'Luis Suárez', 'Nacional > Groningen > Ajax > Liverpool > Barcelona > Atlético Madrid', 'Uruguay', 'Short Number: 9'],
[ 'Raheem Sterling', 'Queens Park Rangers > Liverpool > Manchester City > Chelsea', 'England', 'Short Number: 7'],
[ 'Eden Hazard', 'Lille > Chelsea > Real Madrid', 'Belgium', 'Short Number: 7', 'He plays with Karim Benzema'],
[ 'Antoine Griezmann', 'Real Sociedad > Atlético Madrid > Barcelona > Atlético Madrid', 'France', 'Short Number: 7', 'He plays 11 seasons in Laliga without winning the league'],
[ 'Paul Pogba', 'Le Havre > Manchester United > Juventus > Manchester United > Juventos', 'France', 'Short Number: 6', 'He is fined'],
[ 'Luka Modrić', 'Dinamo Zagreb > Zrinjski Mostar > Inter Zaprešić > Dinamo Zagreb > Tottenham Hotspur > Real Madrid', 'Croatia', 'Short Number: 10', 'He plays with Karim Benzema'],
[ 'Bruno Fernandes', 'Boavista > Novara > Udinese > Sampdoria > Sporting CP > Manchester United', 'Portugal', 'Short Number: 18', 'Famous Medfielder'],
[ 'Toni Kroos', 'Bayern Munich > Bayer Leverkusen > Bayern Munich > Real Madrid', 'Germany', 'Short Number: 8', 'He won the champions league 5 times'],
[ 'Sergio Ramos', 'Sevilla > Real Madrid > Paris Saint-Germain > Sevelia', 'Spain', 'Short Number: 4', 'We won The world cup', 'He plays with Lionel Messi and Cristiono Ronaldo'],
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
[ 'Jadon Sancho', 'Manchester City > Borussia Dortmund > Manchester United', 'England', 'Short Number: 7', 'He plays with Erling Haaland'],
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
[ 'Hakim Ziyech', 'Heerenveen > Twente > Ajax > Chelsea', 'Morocco', 'Short Number: 22', 'He plays with N\'Golo Kanté'],
[ 'Paulo Dybala', 'Instituto > Palermo > Juventus', 'Argentina', 'Short Number: 10', 'He is playing right now'],
[ 'Christian Eriksen', 'Ajax > Tottenham Hotspur > Internazionale > Brentfors > Man Utd', 'Denmark', 'Short Number: 24', 'He retired because of a heart attack and back to football'],
[ 'Memphis Depay', 'Transfer History: PSV Eindhoven > Manchester United > Lyon > Barcelona > Atlético Madrid', 'Netherlands', 'Short Number: 10', 'A fact about the player: He plays with Lionel Messi', 'A fact about the player: He plays with Antoine Griezmann'],
[ 'Lautaro Martínez', 'Racing Club > Inter Milan', 'Argentina', 'Short Number: 10', 'A fact about the player: He plays with Romelu Lukaku', 'A fact about the player: He won the Copa America 2021'],
[ 'Nicolò Barella', 'Inter Milan', 'Italy', 'Short Number: 23', 'A fact about the player: He plays with Romelu Lukaku', 'A fact about the player: He won the Euro 2021'],
[ 'Jude Bellingham', 'Birmingham City > Borussia Dortmund > Real Madrid', 'England', 'Short Number: 22', 'A fact about the player: He is 20 years old', 'A fact about the player: He is the youngest player in the Euro 2021'],
[ 'Phil Foden', 'Manchester City', 'England', 'Short Number: 47'],
[ 'Pedri Gonzalez', 'Las Palmas > Barcelona', 'Spain', 'Short Number: 16', 'A fact about the player: He is 20 years old', 'A fact about the player: He is the youngest Spain player in the Euro 2021'],
[ 'Federico Chiesa', 'Fiorentina > Juventus', 'Italy', 'Short Number: 22' ],
[ 'Mason Mount', 'Chelsea > Man utd', 'England', 'Short Number: 19', 'A fact about the player: He is 24 years old' ],
[ 'Kai Havertz', 'Bayer Leverkusen > Chelsea > Arsenal', 'Germany', 'Short Number: 29', 'A fact about the player: He is 24 years old', 'A fact about the player: He won the champions league 2021']]

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
                        if answer == 'Help' or answer == 'Help':
                            print(f' Player name: {Playername}')
                            HH = input('Enter Player Last Name: ')
                            def eee(HH, PlayerLN):
                                similarity = similarity_score(HH.lower(), PlayerLN.lower())
                                if similarity >= 0.7:
                                    print("Correct! Its " + PlayerLN + "!")
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
                            eee(HH, PlayerLN)

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
