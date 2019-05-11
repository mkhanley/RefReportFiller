import json
from src.handle_pdf import write_fields_to_temp_pdf, merge_pdf, open_report_template, init_canvas, save_pdf, add_comment


def create_user_input():
    user_input = {}
    user_input['report_type_input'] = '2'
    user_input['team_a'] = 'TeamA'
    user_input['team_b'] = 'TeamB'
    user_input['competition'] = 'Competition'
    user_input['venue'] = 'Venue'
    user_input['date'] = '01/01/1970'
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
    return user_input


with open("pdf_fields/ccc2_fields.json") as f:
    field_points = json.load(f)

tmp_pdf_filename = 'build/tmp.pdf'

report_template = open_report_template('templates/CCC2_Referees_Report.pdf')
canvas_tmp = init_canvas(tmp_pdf_filename, report_template.getPage(0).mediaBox)


write_fields_to_temp_pdf(canvas_tmp, create_user_input(), field_points)
add_comment(canvas_tmp, "The quick brown fox jumps over the lazy dog")
canvas_tmp.save()
merged = merge_pdf(report_template, tmp_pdf_filename)
save_pdf(merged, 'build/test_output.pdf')