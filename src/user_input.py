def handle_input():
    user_input = {}
    user_input['report_type'] = input("CCC[2]/[A]dult/[C]amogie: ")
    user_input['team_a'] = input("Team A: ")
    user_input['team_b'] = input("Team B: ")
    user_input['competition'] = input("Competition: ")
    user_input['venue'] = input("Venue: ")
    user_input['date'] = input("Date: ")
    user_input['time'] = input("Time: ")
    user_input['team_a_goals'] = input("Team A Goals: ")
    user_input['team_a_points'] = input("Team A Points: ")
    user_input['team_b_goals'] = input("Team B Goals: ")
    user_input['team_b_points'] = input("Team B Points: ")
    user_input['team_a_field_time'] = input("Team A Field Time: ")
    user_input['team_b_field_time'] = input("Team B Field Time: ")
    user_input['match_start_time'] = input("Match Start Time: ")

    subs = input("Subs [Y/N]: ")
    if subs.upper() == 'Y':
        user_input['team_a_subs'], user_input['team_b_subs'] = handle_subs()

    injury = input("Injuries [Y/N]: ")
    if injury.upper() == 'Y':
        user_input['injuries'] = handle_injuries()
    else:
        user_input['injuries'] = []

    cards = input("Any Cards [Y/N]: ")
    if cards.upper() == 'Y':
        reds = input("Red Cards [Y/N]: ")
        if reds.upper() == 'Y':
            user_input['red_cards'] = handle_cards()

        doubles = input("Double Cards (2xY / 1xY + 1xB) [Y/N]: ")
        if doubles.upper() == 'Y':
            user_input['double_cards'] = handle_cards()

        blacks = input("Black Cards [Y/N]: ")
        if blacks.upper() == 'Y':
            user_input['black_cards'] = handle_cards()

        yellows = input("Yellow Cards [Y/N]: ")
        if yellows.upper() == 'Y':
            user_input['yellows_cards'] = handle_cards()

    else:
        user_input['red_cards'] = []
        user_input['double_cards'] = []
        user_input['black_cards'] = []
        user_input['yellow_cards'] = []

    user_input['team_a_teamsheet'] = input("Team A Teamsheet: ")
    user_input['team_b_teamsheet'] = input("Team B Teamsheet: ")

    comment_in = input("Comments to report [Y/N]: ")
    if comment_in.upper() == 'Y':
        user_input['comment'] = input("Comment: ")
    else:
        user_input['comment'] = ""
    return user_input


def handle_subs():
    team_a_subs = []
    team_b_subs = []
    team_a_sub_present = input("Team A Subs [Y/N]: ")
    if team_a_sub_present.upper() == 'Y':
        team_a_subs = handle_subs_for_team()

    team_a_sub_present = input("Team B Subs [Y/N]: ")
    if team_a_sub_present.upper() == 'Y':
        team_b_subs = handle_subs_for_team()

    return team_a_subs, team_b_subs


def handle_subs_for_team():
    num_subs = int(input("Number of Subs: "))
    subs = []
    for i in range(num_subs):
        player_on = input("Player on: ")
        player_off = input("Player off: ")
        subs.append({
            'player_off': player_off,
            'player_on': player_on
        })
    return subs


def handle_injuries():
    num_injuries = int(input("Number of Injuries: "))
    injuries = []
    for i in range(num_injuries):
        player = input("Player: ")
        club = input("Club: ")
        injury = input("Injury: ")
        injuries.append("{}  -  {}  -  {}".format(player, club, injury))
    return injuries


def handle_cards():
    num_cards = int(input("Number of Cards: "))
    cards = []
    for i in range(num_cards):
        player = input("Player: ")
        club = input("Club: ")
        infraction = input("Infraction: ")
        cards.append({
            'player': player,
            'club': club,
            'infraction': infraction
        })
    return cards
