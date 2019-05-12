import json
from src.user_input import handle_input
from src.handle_pdf import *


def load_template_fields(report_type):
    report_filepath = ''
    if report_type is '2':
        report_filepath = 'pdf_fields/ccc2_fields.json'
    if report_type is 'A':
        report_filepath = ''  # TODO assign adult points
    if report_type is 'C':
        report_filepath = ''  # TODO assign camogie points

    with open(report_filepath) as f:
        return json.load(f)


def load_template_path(report_type):
    if report_type is '2':
        return 'templates/ccc2.pdf'
    if report_type is 'A':
        return ''  # TODO assign adult template
    if report_type is 'C':
        return ''  # TODO assign camogie template


def cleanup(tmp_pdf, tmp_img):
    from os import remove
    remove(tmp_pdf)


def create_build_dir():
    from os import mkdir, path
    if not path.exists('build'):
        mkdir('build')


def main(user_input):
    create_build_dir()
    field_points = load_template_fields(user_input['report_type'])

    tmp_pdf_filename = 'build/tmp.pdf'

    report_template = open_report_template(load_template_path(user_input['report_type']))
    canvas_tmp = init_canvas(tmp_pdf_filename, report_template.getPage(0).mediaBox)

    write_fields_to_temp_pdf(canvas_tmp, user_input, field_points)

    if user_input['comment']:
        add_comment(canvas_tmp, user_input['comment'])

    add_image(canvas_tmp, user_input['team_a_teamsheet'], user_input['team_a'])
    add_image(canvas_tmp, user_input['team_b_teamsheet'], user_input['team_b'])

    canvas_tmp.save()
    merged = merge_pdf(report_template, tmp_pdf_filename)
    save_pdf(merged, 'build/{} v {} {}.pdf'.format(user_input['team_a'],
                                                   user_input['team_b'], user_input['date']))
    cleanup(tmp_pdf_filename, 'build/tmp_image.jpg')


if __name__ == '__main__':
    user_input = handle_input()
    main(user_input)
