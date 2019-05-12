from reportlab.pdfgen import canvas
from PyPDF2 import PdfFileWriter, PdfFileReader, filters
from datetime import date

CANVAS_HEIGHT = 0


def init_canvas(tmp_pdf_filename, canvas_size):
    c = canvas.Canvas(tmp_pdf_filename, canvas_size, pageCompression=1)
    c.setPageSize(canvas_size)
    c.setFont('Helvetica', 10)
    global CANVAS_HEIGHT
    CANVAS_HEIGHT = int(canvas_size[3])
    return c


def open_report_template(report_path):
    return PdfFileReader(open(report_path, "rb"))


def field_to_xy(field_locations, field):
    return field_locations[field][0], CANVAS_HEIGHT - field_locations[field][1]


def write_cards(canvas_tmp, field_locations, cards, card_type):
    i = 1
    for card in cards:
        player = card['player']
        club = card['club']
        infraction = card['infraction']

        field_player = "{}_card_player_{}".format(card_type, i)
        field_club = "{}_card_club_{}".format(card_type, i)
        field_infraction = "{}_card_infraction_{}".format(card_type, i)

        canvas_tmp.drawString(*field_to_xy(field_locations, field_player),
                              text=player)
        canvas_tmp.drawString(*field_to_xy(field_locations, field_club),
                              text=club)
        canvas_tmp.drawString(*field_to_xy(field_locations, field_infraction),
                              text=infraction)
        i += 1


def write_subs(canvas_tmp, field_locations, subs, team_letter, club):
    i = 1
    for sub in subs:
        on = sub['player_on']
        off = sub['player_off']

        field_on = "team_{}_player_on_{}".format(team_letter, i)
        field_off = "team_{}_player_off_{}".format(team_letter, i)
        field_club = "team_{}_club_{}".format(team_letter, i)

        canvas_tmp.drawString(*field_to_xy(field_locations, field_on),
                              text=on)
        canvas_tmp.drawString(*field_to_xy(field_locations, field_off),
                              text=off)
        canvas_tmp.drawString(*field_to_xy(field_locations, field_club),
                              text=club)
        i += 1


def write_fields_to_temp_pdf(canvas_tmp, user_input, field_locations):

    canvas_tmp.drawString(*field_to_xy(field_locations, 'team_a_info'),
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
    canvas_tmp.drawString(*field_to_xy(field_locations, 'team_a_score_name'),
                          text=user_input['team_a'])
    canvas_tmp.drawString(*field_to_xy(field_locations, 'team_b_score_name'),
                          text=user_input['team_b'])
    canvas_tmp.drawString(*field_to_xy(field_locations, 'team_a_goals'),
                          text=user_input['team_a_goals'])
    canvas_tmp.drawString(*field_to_xy(field_locations, 'team_b_goals'),
                          text=user_input['team_b_goals'])
    canvas_tmp.drawString(*field_to_xy(field_locations, 'team_a_points'),
                          text=user_input['team_a_points'])
    canvas_tmp.drawString(*field_to_xy(field_locations, 'team_b_points'),
                          text=user_input['team_b_points'])
    canvas_tmp.drawString(*field_to_xy(field_locations, 'team_a_field_time'),
                          text=user_input['team_a_field_time'])
    canvas_tmp.drawString(*field_to_xy(field_locations, 'team_b_field_time'),
                          text=user_input['team_b_field_time'])
    canvas_tmp.drawString(*field_to_xy(field_locations, 'match_start_time'),
                          text=user_input['match_start_time'])

    write_subs(canvas_tmp, field_locations, user_input['team_a_subs'],
               'a', user_input['team_a'])

    write_subs(canvas_tmp, field_locations, user_input['team_b_subs'],
               'b', user_input['team_b'])

    move_to_next_canvas_page(canvas_tmp)

    i = 1
    for injury in user_input['injuries']:
        field = "injury_{}".format(i)
        canvas_tmp.drawString(*field_to_xy(field_locations, field),
                              text=injury)
        i += 1

    write_cards(canvas_tmp, field_locations, user_input['red_cards'], 'red')
    write_cards(canvas_tmp, field_locations, user_input['double_cards'], 'double')
    write_cards(canvas_tmp, field_locations, user_input['yellow_cards'], 'yellow')
    write_cards(canvas_tmp, field_locations, user_input['black_cards'], 'black')

    canvas_tmp.drawString(*field_to_xy(field_locations, "sig_date"),
                          text=str(date.today()))


def move_to_next_canvas_page(canvas_tmp):
    canvas_tmp.showPage()


def add_comment(canvas_tmp, comment):
    move_to_next_canvas_page(canvas_tmp)
    canvas_tmp.drawString(35, CANVAS_HEIGHT - 100, text=comment)


def add_image(canvas_tmp, image_path):
    move_to_next_canvas_page(canvas_tmp)
    fill_page_with_image(image_path, canvas_tmp)


def fill_page_with_image(path, canvas_tmp):
    # https://gist.github.com/bradleyayers/1480017
    """
    Given the path to an image and a reportlab canvas, fill the current page
    with the image.

    This function takes into consideration EXIF orientation information (making
    it compatible with photos taken from iOS devices).

    This function makes use of ``canvas.setPageRotation()`` and
    ``canvas.setPageSize()`` which will affect subsequent pages, so be sure to
    reset them to appropriate values after calling this function.

    :param   path: filesystem path to an image
    :param canvas_tmp: ``reportlab.canvas.Canvas`` object
    """
    from PIL import Image

    page_width_f, page_height_f = canvas_tmp._pagesize.upperRight
    page_width = int(page_width_f)
    page_height = int(page_height_f)

    image = Image.open(path)
    image_width, image_height = image.size
    if hasattr(image, '_getexif'):
        try:
            orientation = image._getexif().get(274, 1)  # 274 = Orientation
        except AttributeError:
            orientation = 1
    else:
        orientation = 1

    # These are the possible values for the Orientation EXIF attribute:
    ORIENTATIONS = {
        1: "Horizontal (normal)",
        2: "Mirrored horizontal",
        3: "Rotated 180",
        4: "Mirrored vertical",
        5: "Mirrored horizontal then rotated 90 CCW",
        6: "Rotated 90 CW",
        7: "Mirrored horizontal then rotated 90 CW",
        8: "Rotated 90 CCW",
    }
    draw_width, draw_height = page_width, page_height
    if orientation == 1:
        canvas_tmp.setPageRotation(0)
    elif orientation == 3:
        canvas_tmp.setPageRotation(180)
    elif orientation == 6:
        image_width, image_height = image_height, image_width
        draw_width, draw_height = page_height, page_width
        canvas_tmp.setPageRotation(90)
    elif orientation == 8:
        image_width, image_height = image_height, image_width
        draw_width, draw_height = page_height, page_width
        canvas_tmp.setPageRotation(270)
    else:
        raise ValueError("Unsupported image orientation '%s'."
                         % ORIENTATIONS[orientation])

    if image_width > image_height:
        page_width, page_height = page_height, page_width  # flip width/height
        draw_width, draw_height = draw_height, draw_width
        canvas_tmp.setPageSize((page_width, page_height))

    image.save('build/tmp_image.jpg', quality=50)

    canvas_tmp.drawImage('build/tmp_image.jpg', 0, 0, width=draw_width, height=draw_height,
                         preserveAspectRatio=True)


def merge_pdf(report_template, tmp_pdf_filename):
    merged = PdfFileWriter()

    watermark = PdfFileReader(open(tmp_pdf_filename, "rb"))

    template_pages = report_template.getNumPages()
    watermark_pages = watermark.getNumPages()

    for i in range(max(template_pages, watermark_pages)):
        if i < template_pages:
            page = report_template.getPage(i)
            page.mergePage(watermark.getPage(i))
            merged.addPage(page)

        else:
            merged.addPage(watermark.getPage(i))
    return merged


def save_pdf(output, output_pdf_filename):
    output_stream = open(output_pdf_filename, "wb")


    output.write(output_stream)
