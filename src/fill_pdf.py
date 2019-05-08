from reportlab.pdfgen import canvas



def init_canvas():
    c = canvas.Canvas("build/hello.pdf")
    c.setPageSize((595, 841))
    c.getAvailableFonts()
    c.setFont('Helvetica', 10)
    return c


def field_to_xy(field_locations, field):
    return field_locations[field][0], 842 - field_locations[field][1]


def write_fields_to_temp_pdf(user_input, field_locations):

    canvas_tmp = init_canvas()

    canvas_tmp.drawString(*field_to_xy(field_locations,'team_a_info'),
                          text=user_input['team_a'])
    canvas_tmp.drawString(*field_to_xy(field_locations, 'team_b_info'),
                          text=user_input['team_b'])
    canvas_tmp.drawString(*field_to_xy(field_locations, 'competition'),
                          text=user_input['competition'])
    canvas_tmp.drawString(*field_to_xy(field_locations, 'venue'),
                          text=user_input['venue'])
    canvas_tmp.drawString(*field_to_xy(field_locations, 'date'),
                          text=user_input['date'])
    canvas_tmp.drawString(*field_to_xy(field_locations, 'time'),
                          text=user_input['time'])





    canvas_tmp.save()
