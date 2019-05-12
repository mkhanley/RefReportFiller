import run


def create_user_input():
    user_input = {}
    user_input['report_type'] = '2'
    user_input['team_a'] = 'TeamA'
    user_input['team_b'] = 'TeamB'
    user_input['competition'] = 'Competition'
    user_input['venue'] = 'Venue'
    user_input['date'] = '01-01-1970'
    user_input['time'] = '00:00'
    user_input['team_a_goals'] = '1'
    user_input['team_a_points'] = '2'
    user_input['team_b_goals'] = '3'
    user_input['team_b_points'] = '4'
    user_input['team_a_field_time'] = '12:34'
    user_input['team_b_field_time'] = '56:78'
    user_input['match_start_time'] = '00:00'

    user_input['team_a_subs'] = [{'player_off': 'Player', 'player_on': 'Swap'}]
    user_input['team_b_subs'] = [
        {'player_off': 'Player', 'player_on': '1'},
        {'player_off': 'Player', 'player_on': '2'},
        {'player_off': 'Player', 'player_on': '3'},
        {'player_off': 'Player', 'player_on': '4'},
        {'player_off': 'Player', 'player_on': '5'},
        {'player_off': 'Player', 'player_on': '6'}
    ]

    user_input['injuries'] = [
        "Player - Club - Injury 1",
        "Player - Club - Injury 2",
        "Player - Club - Injury 3",
        "Player - Club - Injury 4",
        "Player - Club - Injury 5",
        "Player - Club - Injury 6",
    ]

    user_input['red_cards'] = [
        {'player': 'Name1', 'club': 'Club', 'infraction': 'Punch'},
        {'player': 'Name2', 'club': 'Club', 'infraction': 'Punch'},
        {'player': 'Name3', 'club': 'Club', 'infraction': 'Punch'},
        {'player': 'Name4', 'club': 'Club', 'infraction': 'Punch'},
        {'player': 'Name5', 'club': 'Club', 'infraction': 'Punch'},
        {'player': 'Name6', 'club': 'Club', 'infraction': 'Punch'}
    ]
    user_input['double_cards'] = user_input['red_cards']
    user_input['black_cards'] = user_input['red_cards']
    user_input['yellow_cards'] = user_input['red_cards']

    user_input['team_a_teamsheet'] = 'test/test_image.jpg'
    user_input['team_b_teamsheet'] = 'test/test_image.jpg'

    user_input['comment'] = ''
    return user_input


run.main(create_user_input())
